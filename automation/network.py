"""Coleta do tráfego HTTP do frontend durante a execução dos cenários (Etapa 2).

Cada requisição de API feita pela interface é registrada com método, caminho,
parâmetros, status e corpos (resumidos) e associada ao passo do cenário que a
originou. O resultado é salvo por cenário em formato HAR 1.2 (``CEN-xx.har``),
com o campo extra ``_step``, além de um resumo por passo na evidência JSON.

Finalidade documental: nada aqui envia requisições próprias à aplicação, só
observa as que a interface já faz. Credenciais (senhas, respostas de segurança,
tokens, cookies) são mascaradas antes de gravar, e números de cartão ficam
reduzidos aos 4 últimos dígitos.
"""
from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlsplit

MASK = "***"
BODY_LIMIT = 2000

# Chaves cujo valor nunca deve ser gravado (comparação sem caixa e sem _/-).
SECRET_KEYS = {
    "password", "passwordrepeat", "repeatpassword", "currentpassword",
    "newpassword", "repeatnewpassword", "current", "new", "repeat",
    "securityanswer", "answer", "token", "authentication", "authorization",
    "cookie", "setcookie", "totpsecret", "totptoken", "cvv", "captcha",
}
CARD_KEYS = {"cardnum", "cardnumber"}
API_PREFIXES = ("/api/", "/rest/", "/b2b/", "/file-upload", "/profile", "/dataerasure")
SKIP_RESOURCE_TYPES = {"image", "font", "stylesheet", "media", "script", "manifest", "websocket"}


def enabled() -> bool:
    return os.getenv("JUICE_SHOP_CAPTURE_NETWORK", "true").strip().casefold() not in {"0", "false", "no"}


def _norm(key: str) -> str:
    return str(key).casefold().replace("_", "").replace("-", "")


def _mask_card(value: Any) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    return f"****{digits[-4:]}" if len(digits) >= 4 else MASK


def redact(value: Any) -> Any:
    """Mascara recursivamente credenciais e números de cartão em JSON."""
    if isinstance(value, dict):
        out = {}
        for key, item in value.items():
            k = _norm(key)
            if k in SECRET_KEYS:
                out[key] = MASK
            elif k in CARD_KEYS:
                out[key] = _mask_card(item)
            else:
                out[key] = redact(item)
        return out
    if isinstance(value, list):
        return [redact(item) for item in value]
    return value


def redact_text(text: str | None) -> str:
    """Mascara um corpo textual: JSON é tratado campo a campo; o resto é truncado."""
    if not text:
        return ""
    try:
        parsed = json.loads(text)
    except (ValueError, TypeError):
        return text[:BODY_LIMIT]
    return json.dumps(redact(parsed), ensure_ascii=False)[:BODY_LIMIT]


def redact_query(url: str) -> tuple[str, list[dict[str, str]]]:
    """Separa caminho e parâmetros, mascarando os sensíveis (ex.: change-password)."""
    parts = urlsplit(url)
    params = []
    for name, value in parse_qsl(parts.query, keep_blank_values=True):
        k = _norm(name)
        if k in SECRET_KEYS:
            value = MASK
        elif k in CARD_KEYS:
            value = _mask_card(value)
        params.append({"name": name, "value": value})
    return parts.path, params


def is_api_call(url: str, resource_type: str, base_url: str) -> bool:
    if resource_type in SKIP_RESOURCE_TYPES or not url.startswith(base_url):
        return False
    path = urlsplit(url).path
    return any(path.startswith(prefix) for prefix in API_PREFIXES)


def assign_step(started: float, windows: list[tuple[int, float, float]]) -> int:
    """Passo cujo intervalo contém o instante; 0 = pré-condição (antes do 1º passo).

    Requisições disparadas depois do fim de um passo e antes do próximo
    (respostas assíncronas) ficam com o passo anterior.
    """
    step = 0
    for number, begin, _end in windows:
        if started >= begin:
            step = number
        else:
            break
    return step


@dataclass
class NetworkRecorder:
    base_url: str
    entries: list[dict[str, Any]] = field(default_factory=list)
    windows: list[tuple[int, float, float]] = field(default_factory=list)

    def attach(self, context) -> None:
        context.on("requestfinished", self._on_finished)
        context.on("requestfailed", self._on_failed)

    def mark_step(self, number: int, begin: float, end: float) -> None:
        self.windows.append((number, begin, end))

    async def _on_finished(self, request) -> None:
        try:
            response = await request.response()
            body = ""
            if response is not None:
                ctype = (response.headers or {}).get("content-type", "")
                if "json" in ctype or "text" in ctype:
                    try:
                        body = await response.text()
                    except Exception:
                        body = ""
            self._record(request, response, body, failure=None)
        except Exception:
            pass

    def _on_failed(self, request) -> None:
        try:
            self._record(request, None, "", failure=request.failure or "failed")
        except Exception:
            pass

    def _record(self, request, response, body: str, failure: str | None) -> None:
        if not is_api_call(request.url, request.resource_type, self.base_url):
            return
        path, query = redact_query(request.url)
        timing = getattr(request, "timing", None) or {}
        started = time.time()
        if isinstance(timing, dict) and timing.get("startTime", -1) > 0:
            started = timing["startTime"] / 1000
        req_headers = request.headers or {}
        res_headers = (response.headers if response is not None else {}) or {}
        self.entries.append({
            "_started": started,
            "_failure": failure,
            "request": {
                "method": request.method,
                "url": f"{self.base_url}{path}",
                "path": path,
                "queryString": query,
                "headers": [
                    {"name": k, "value": MASK if _norm(k) in SECRET_KEYS else v}
                    for k, v in req_headers.items()
                    if _norm(k) in {"contenttype", "accept", "authorization", "cookie"}
                ],
                "postData": {
                    "mimeType": req_headers.get("content-type", ""),
                    "text": redact_text(request.post_data),
                } if request.post_data else None,
            },
            "response": {
                "status": response.status if response is not None else 0,
                "statusText": response.status_text if response is not None else (failure or ""),
                "content": {
                    "mimeType": res_headers.get("content-type", ""),
                    "text": redact_text(body),
                },
            },
        })

    def build(self) -> tuple[dict[str, Any], dict[int, list[str]]]:
        """Monta o HAR (com ``_step``) e o resumo legível por passo."""
        entries, per_step = [], {}
        for raw in sorted(self.entries, key=lambda e: e["_started"]):
            step = assign_step(raw["_started"], self.windows)
            req, res = raw["request"], raw["response"]
            entry = {
                "_step": step,
                "startedDateTime": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(raw["_started"])) + "Z",
                "request": {k: v for k, v in req.items() if k != "path" and v is not None},
                "response": res,
            }
            if raw["_failure"]:
                entry["_failure"] = raw["_failure"]
            entries.append(entry)
            per_step.setdefault(step, []).append(f'{req["method"]} {req["path"]} -> {res["status"]}')
        har = {"log": {"version": "1.2", "creator": {"name": "juice-shop-execution", "version": "1"}, "entries": entries}}
        return har, per_step

    def save(self, path: Path) -> dict[int, list[str]]:
        har, per_step = self.build()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(har, ensure_ascii=False, indent=2), encoding="utf-8")
        return per_step
