from __future__ import annotations

import base64
import json
import os
import re
import time
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")


from reporting.llm.prompt import HUMANIZER_SCHEMA, HUMANIZER_SYSTEM_PROMPT


# Cenários longos (ex.: CHK-28, 15 passos) estouravam 2400 tokens e o JSON
# vinha truncado. O valor é teto, não custo: paga-se só o que é gerado.
MAX_OUTPUT_TOKENS = int(os.getenv("REPORTING_LLM_MAX_TOKENS", "8000"))


class LLMHumanizerError(RuntimeError):
    """Erro controlado ao gerar documentação com LLM."""


def _config() -> tuple[str, str, str, str]:
    provider = os.getenv("REPORTING_LLM_PROVIDER", "gemini").strip().lower()

    configs = {
        "groq": (
            os.getenv("GROQ_API_KEY", "").strip(),
            os.getenv("GROQ_API_BASE_URL", "https://api.groq.com/openai/v1").strip(),
            os.getenv("GROQ_LLM_MODEL", "openai/gpt-oss-120b").strip(),
            "GROQ_API_KEY",
        ),
        "openai": (
            os.getenv("OPENAI_API_KEY", "").strip(),
            os.getenv("OPENAI_API_BASE_URL", "https://api.openai.com/v1").strip(),
            os.getenv("OPENAI_LLM_MODEL", "gpt-6.2-sol").strip(),
            "OPENAI_API_KEY",
        ),
        "kimi": (
            os.getenv("KIMI_API_KEY", "").strip(),
            os.getenv("KIMI_API_BASE_URL", "https://api.moonshot.ai/v1").strip(),
            os.getenv("KIMI_LLM_MODEL", "kimi-k3.1-pro").strip(),
            "KIMI_API_KEY",
        ),
        "gemini": (
            os.getenv("GEMINI_API_KEY", "").strip(),
            os.getenv(
                "GEMINI_API_BASE_URL",
                "https://generativelanguage.googleapis.com/v1beta/openai/",
            ).strip(),
            os.getenv(
                "GEMINI_LLM_MODEL",
                "gemini-3.5-flash-lite",
            ).strip(),
            "GEMINI_API_KEY",
        ),
        "claude": (
            os.getenv("ANTHROPIC_API_KEY", "").strip(),
            os.getenv(
                "ANTHROPIC_API_BASE_URL",
                "https://api.anthropic.com",
            ).strip(),
            os.getenv(
                "CLAUDE_LLM_MODEL",
                "claude-sonnet-5",
            ).strip(),
            "ANTHROPIC_API_KEY",
        ),
    }

    if provider not in configs:
        raise LLMHumanizerError(
            f"REPORTING_LLM_PROVIDER inválido: {provider}. "
            "Use 'groq', 'openai', 'kimi', 'gemini' ou 'claude'."
        )

    api_key, base_url, model, env_name = configs[provider]

    if not api_key:
        raise LLMHumanizerError(f"{env_name} não configurada.")

    return provider, api_key, base_url, model


def humanize(payload: dict[str, Any]) -> dict[str, Any]:
    provider, api_key, base_url, model = _config()

    try:
        if provider == "claude":
            # Claude usa a Messages API nativa e Structured Outputs. A API
            # restringe a saída ao schema; o SDK ainda entrega o JSON
            # estruturado como texto no bloco de conteúdo, então a conversão
            # para dict é feita dentro de _humanize_claude.
            return _humanize_claude(payload, api_key, base_url, model)
        return _humanize_openai_compatible(
            payload, provider, api_key, base_url, model
        )
    except LLMHumanizerError:
        raise
    except Exception as exc:
        raise LLMHumanizerError(
            f"Falha ao consultar a LLM ({provider}, modelo {model}): {exc}"
        ) from exc


def _humanize_openai_compatible(
    payload: dict[str, Any],
    provider: str,
    api_key: str,
    base_url: str,
    model: str,
) -> str:
    return _request_openai_compatible(
        payload=payload,
        provider=provider,
        api_key=api_key,
        base_url=base_url,
        model=model,
        use_schema=True,
        user_content=_build_input(payload),
    )


def _request_openai_compatible(
    *,
    payload: dict[str, Any],
    provider: str,
    api_key: str,
    base_url: str,
    model: str,
    use_schema: bool,
    user_content: str,
) -> str:
    client = OpenAI(api_key=api_key, base_url=base_url)

    kwargs: dict[str, Any] = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": HUMANIZER_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": (
                    _build_multimodal_content(payload, user_content)
                    if provider == "gemini"
                    else user_content
                ),
            },
        ],
        "max_tokens": MAX_OUTPUT_TOKENS,
    }

    if use_schema:
        kwargs["response_format"] = {
            "type": "json_schema",
            "json_schema": {
                "name": "qa_humanized_scenario",
                "strict": True,
                "schema": HUMANIZER_SCHEMA,
            },
        }

    response = None
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            response = client.chat.completions.create(**kwargs)
            break
        except Exception as exc:
            last_error = exc
            if "429" not in str(exc) or attempt == 2:
                break
            # Rate limit temporário: aguarda antes de repetir a mesma requisição.
            time.sleep(5 * (2 ** attempt))

    if response is None:
        if last_error is not None:
            raise _format_provider_error(
                provider=provider,
                model=model,
                exc=last_error,
            ) from last_error
        if not use_schema:
            raise RuntimeError("Falha desconhecida ao consultar a LLM.")
        kwargs.pop("response_format", None)
        try:
            response = client.chat.completions.create(**kwargs)
        except Exception as exc:
            raise _format_provider_error(
                provider=provider,
                model=model,
                exc=exc,
            ) from exc

    content = response.choices[0].message.content
    return (content or "").strip()


def _format_provider_error(
    *,
    provider: str,
    model: str,
    exc: Exception,
) -> LLMHumanizerError:
    status_code = getattr(exc, "status_code", None)
    body = getattr(exc, "body", None)
    response = getattr(exc, "response", None)
    if status_code is None and response is not None:
        status_code = getattr(response, "status_code", None)

    details: list[str] = []
    if status_code is not None:
        details.append(f"HTTP {status_code}")

    if isinstance(body, dict):
        error = body.get("error")
        if isinstance(error, dict):
            for key in ("status", "code", "message"):
                value = error.get(key)
                if value:
                    details.append(f"{key}={value}")
        elif error:
            details.append(f"error={error}")
    elif body:
        details.append(f"body={str(body)[:1200]}")

    if not details:
        details.append(str(exc))

    return LLMHumanizerError(
        f"Falha ao consultar a LLM ({provider}, modelo {model}): "
        + " | ".join(details)
    )


def _humanize_claude(
    payload: dict[str, Any],
    api_key: str,
    base_url: str,
    model: str,
    retry_prompt: str | None = None,
) -> str:
    try:
        from anthropic import Anthropic
    except ImportError as exc:
        raise LLMHumanizerError(
            "O suporte a Claude requer o pacote 'anthropic'. "
            "Execute: pip install -r requirements.txt"
        ) from exc

    # max_retries: o SDK repete sozinho em erro de conexão, 429 e 5xx,
    # com espera exponencial (antes ficava no padrão de 2 tentativas).
    client = Anthropic(
        api_key=api_key,
        base_url=base_url,
        max_retries=6,
        timeout=180,
    )

    user_content = retry_prompt or (
        _build_input(payload)
        + "\n\nRETORNE SOMENTE JSON VÁLIDO. "
        "NÃO use Markdown, comentários ou texto fora do JSON."
    )

    response = client.messages.create(
        model=model,
        max_tokens=MAX_OUTPUT_TOKENS,
        system=HUMANIZER_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": user_content,
            }
        ],
        output_config={
            "format": {
                "type": "json_schema",
                "schema": HUMANIZER_SCHEMA,
            }
        },
    )

    parts = [
        block.text
        for block in response.content
        if getattr(block, "type", None) == "text"
    ]

    raw = "\n".join(parts).strip()
    if not raw:
        raise LLMHumanizerError(
            f"Claude ({model}) retornou conteúdo vazio."
        )

    try:
        result = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise LLMHumanizerError(
            f"Claude ({model}) retornou Structured Output que não pôde ser "
            f"decodificado como JSON: {exc}"
        ) from exc

    try:
        _validate(result)
    except LLMHumanizerError as exc:
        raise LLMHumanizerError(
            f"Claude ({model}) retornou JSON fora do schema esperado: {exc}"
        ) from exc

    return result


def _build_input(payload: dict[str, Any]) -> str:
    execution = payload["execution"]
    return "\n".join(
        [
            "Transforme as evidências abaixo em documentação funcional.",
            "",
            "CATÁLOGO DO CENÁRIO:",
            json.dumps(payload["catalog"], ensure_ascii=False, indent=2),
            "",
            "EVIDÊNCIAS DA EXECUÇÃO:",
            json.dumps(execution, ensure_ascii=False, indent=2),
            "",
            "IMPORTANTE:",
            "Os relatórios textuais e as imagens anexadas fazem parte das evidências.",
            "Use as imagens somente para identificar elementos visíveis e confirmar mudanças de estado.",
            "A execução estruturada continua sendo a fonte da verdade.",
        ]
    )


def _build_multimodal_content(
    payload: dict[str, Any],
    text_content: str,
) -> list[dict[str, Any]]:
    content: list[dict[str, Any]] = [{"type": "text", "text": text_content}]

    artifacts = payload.get("execution", {}).get("artifacts", {})
    screenshots = (
        artifacts.get("screenshots", [])
        if isinstance(artifacts, dict)
        else []
    )

    for screenshot in screenshots:
        path = Path(str(screenshot))
        if not path.is_file():
            continue

        try:
            encoded = base64.b64encode(path.read_bytes()).decode("ascii")
        except OSError:
            continue

        content.append(
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{encoded}",
                },
            }
        )

    return content


def _parse_and_validate(raw: str) -> dict[str, Any] | None:
    if not raw:
        return None

    candidates = [raw.strip()]

    fenced = re.findall(
        r"\u0060\u0060\u0060(?:json)?\s*(.*?)\s*\u0060\u0060\u0060",
        raw,
        flags=re.IGNORECASE | re.DOTALL,
    )
    candidates.extend(item.strip() for item in fenced if item.strip())

    for candidate in list(candidates):
        extracted = _extract_json_object(candidate)
        if extracted:
            candidates.append(extracted)

    seen: set[str] = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)

        try:
            result = json.loads(candidate)
        except json.JSONDecodeError:
            continue

        if not isinstance(result, dict):
            continue

        try:
            _validate(result)
        except LLMHumanizerError:
            continue

        return result

    return None


def _extract_json_object(text: str) -> str | None:
    start = text.find("{")
    if start < 0:
        return None

    depth = 0
    in_string = False
    escaped = False

    for index in range(start, len(text)):
        char = text[index]

        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue

        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start : index + 1]

    return None


def _validate(result: Any) -> None:
    if not isinstance(result, dict):
        raise LLMHumanizerError(
            "Resposta estruturada não é um objeto JSON."
        )

    required = {
        "flow",
        "precondition",
        "observed_result",
        "messages",
        "data",
        "steps",
    }

    missing = required - set(result)
    if missing:
        raise LLMHumanizerError(
            f"Resposta estruturada incompleta. Campos ausentes: {', '.join(sorted(missing))}."
        )

    if (
        not isinstance(result["flow"], str)
        or not isinstance(result["precondition"], str)
        or not isinstance(result["observed_result"], str)
        or not isinstance(result["data"], str)
        or not isinstance(result["messages"], list)
        or not isinstance(result["steps"], list)
    ):
        raise LLMHumanizerError(
            "Resposta estruturada com tipos inválidos."
        )

    if not all(isinstance(item, str) for item in result["messages"]):
        raise LLMHumanizerError(
            "Resposta estruturada com mensagens inválidas."
        )

    for step in result["steps"]:
        if not isinstance(step, dict):
            raise LLMHumanizerError(
                "Passo humanizado inválido."
            )

        required_step = {"number", "action", "data", "response"}
        missing_step = required_step - set(step)
        if missing_step:
            raise LLMHumanizerError(
                "Passo humanizado incompleto."
            )

        if (
            not isinstance(step["number"], int)
            or not isinstance(step["action"], str)
            or not isinstance(step["data"], str)
            or not isinstance(step["response"], str)
        ):
            raise LLMHumanizerError(
                "Passo humanizado com tipos inválidos."
            )
