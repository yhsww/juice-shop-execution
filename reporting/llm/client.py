from __future__ import annotations

import base64
import json
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from openai import OpenAI

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")

from reporting.llm.prompt import HUMANIZER_SCHEMA, HUMANIZER_SYSTEM_PROMPT


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
            os.getenv("GEMINI_LLM_MODEL", "gemini-3.5-flash-lite").strip(),
            "GEMINI_API_KEY",
        ),
        "claude": (
            os.getenv("ANTHROPIC_API_KEY", "").strip(),
            os.getenv("ANTHROPIC_API_BASE_URL", "https://api.anthropic.com").strip(),
            os.getenv("CLAUDE_LLM_MODEL", "claude-sonnet-5").strip(),
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
            raw = _humanize_claude(payload, api_key, base_url, model)
        else:
            raw = _humanize_openai_compatible(
                payload, provider, api_key, base_url, model
            )
    except LLMHumanizerError:
        raise
    except Exception as exc:
        raise LLMHumanizerError(
            f"Falha ao consultar a LLM ({provider}, modelo {model}): {exc}"
        ) from exc

    if not raw:
        raise LLMHumanizerError(f"A LLM ({provider}) retornou uma resposta vazia.")

    result = _parse_json_response(raw)
    _validate(result)
    return result


def _parse_json_response(raw: str) -> dict[str, Any]:
    text = (raw or "").strip()
    candidates = [text]

    fenced = re.search(
        r"\`\`\`(?:json)?\\s*(.*?)\\s*\`\`\`",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if fenced:
        candidates.insert(0, fenced.group(1).strip())

    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        candidates.append(text[start : end + 1])

    for candidate in candidates:
        try:
            value = json.loads(candidate)
            if isinstance(value, dict):
                return value
        except json.JSONDecodeError:
            continue

    raise LLMHumanizerError("A LLM retornou JSON inválido.")


def _humanize_openai_compatible(
    payload: dict[str, Any],
    provider: str,
    api_key: str,
    base_url: str,
    model: str,
) -> str:
    client = OpenAI(api_key=api_key, base_url=base_url)

    # Gemini usa o endpoint Chat Completions compatível com OpenAI.
    # Responses API não é usada aqui porque a compatibilidade oficial do Gemini
    # não cobre Responses da mesma forma.
    messages = [
        {"role": "system", "content": HUMANIZER_SYSTEM_PROMPT},
        {"role": "user", "content": _build_multimodal_content(payload)},
    ]

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "qa_humanized_scenario",
                    "strict": True,
                    "schema": HUMANIZER_SCHEMA,
                },
            },
            max_tokens=2400,
        )
        content = response.choices[0].message.content
        if content and content.strip():
            return content.strip()
    except Exception:
        pass

    fallback_messages = [
        {
            "role": "system",
            "content": (
                HUMANIZER_SYSTEM_PROMPT
                + "\n\nIMPORTANTE: responda SOMENTE com um objeto JSON válido. "
                "Não use Markdown, cercas de código, comentários ou texto antes/depois do JSON."
            ),
        },
        {"role": "user", "content": _build_multimodal_content(payload)},
    ]
    response = client.chat.completions.create(
        model=model,
        messages=fallback_messages,
        max_tokens=2400,
    )
    return (response.choices[0].message.content or "").strip()


def _humanize_claude(
    payload: dict[str, Any],
    api_key: str,
    base_url: str,
    model: str,
) -> str:
    try:
        from anthropic import Anthropic
    except ImportError as exc:
        raise LLMHumanizerError(
            "O suporte a Claude requer o pacote 'anthropic'. "
            "Execute: pip install -r requirements.txt"
        ) from exc

    client = Anthropic(api_key=api_key, base_url=base_url)
    response = client.messages.create(
        model=model,
        max_tokens=2400,
        system=HUMANIZER_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": (
                    _build_input(payload)
                    + "\n\nRETORNE SOMENTE JSON VÁLIDO. "
                    "NÃO use Markdown, comentários ou texto fora do JSON."
                ),
            }
        ],
    )

    parts = [
        block.text
        for block in response.content
        if getattr(block, "type", None) == "text"
    ]
    return "\n".join(parts).strip()


def _build_input(payload: dict[str, Any]) -> str:
    execution = payload["execution"].copy()
    artifacts = execution.pop("artifacts", {})
    reports = artifacts.get("reports", [])
    report_text = "\n\n".join(
        f"--- {item.get('name', 'report')} ---\n{item.get('content', '')}"
        for item in reports
    )
    return "\n".join(
        [
            "Transforme as evidências abaixo em documentação funcional.",
            "",
            "CATÁLOGO DO CENÁRIO:",
            json.dumps(payload["catalog"], ensure_ascii=False, indent=2),
            "",
            "RELATÓRIOS TEXTUAIS DO CENÁRIO:",
            report_text or "Nenhum relatório textual adicional encontrado.",
            "",
            "EVIDÊNCIA ESTRUTURADA DA EXECUÇÃO:",
            json.dumps(execution, ensure_ascii=False, indent=2),
            "",
            "As capturas de tela deste cenário serão anexadas à mesma mensagem. Use-as para confirmar visualmente textos, rótulos, campos, produtos, quantidades, mensagens, menus, estados e mudanças de interface. Não invente elementos que não estejam visíveis ou registrados.",
        ]
    )


def _build_multimodal_content(payload: dict[str, Any]) -> list[dict[str, Any]]:
    content: list[dict[str, Any]] = [
        {"type": "text", "text": _build_input(payload)}
    ]
    screenshots = payload.get("execution", {}).get("artifacts", {}).get("screenshots", [])
    for path in screenshots:
        try:
            raw = Path(path).read_bytes()
            encoded = base64.b64encode(raw).decode("ascii")
            content.append(
                {
                    "type": "text",
                    "text": f"CAPTURA DE TELA: {Path(path).name}",
                }
            )
            content.append(
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{encoded}",
                    },
                }
            )
        except OSError:
            continue
    return content


def _validate(result: dict[str, Any]) -> None:
    required = {
        "flow",
        "precondition",
        "observed_result",
        "messages",
        "data",
        "steps",
    }
    if not isinstance(result, dict) or set(required) - set(result):
        raise LLMHumanizerError("Resposta estruturada incompleta.")

    if not isinstance(result["messages"], list) or not isinstance(result["steps"], list):
        raise LLMHumanizerError("Resposta estruturada com tipos inválidos.")

    for step in result["steps"]:
        if not isinstance(step, dict):
            raise LLMHumanizerError("Passo humanizado inválido.")
        if not {"number", "action", "data", "response"} <= set(step):
            raise LLMHumanizerError("Passo humanizado incompleto.")
