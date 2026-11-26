from __future__ import annotations

import json
import os
from typing import Any

from openai import OpenAI

from reporting.llm.prompt import HUMANIZER_SCHEMA, HUMANIZER_SYSTEM_PROMPT


class LLMHumanizerError(RuntimeError):
    """Erro controlado ao gerar documentação com LLM."""


def humanize(payload: dict[str, Any]) -> dict[str, Any]:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise LLMHumanizerError("OPENAI_API_KEY não configurada.")

    model = os.getenv("REPORTING_LLM_MODEL", "gpt-6.2-sol").strip()
    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": HUMANIZER_SYSTEM_PROMPT},
            {"role": "user", "content": _build_input(payload)},
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "qa_humanized_scenario",
                "strict": True,
                "schema": HUMANIZER_SCHEMA,
            }
        },
        max_output_tokens=2400,
    )

    raw = response.output_text.strip()
    if not raw:
        raise LLMHumanizerError("A LLM retornou uma resposta vazia.")

    try:
        result = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise LLMHumanizerError("A LLM retornou JSON inválido.") from exc

    _validate(result)
    return result


def _build_input(payload: dict[str, Any]) -> str:
    return "\n".join(
        [
            "Transforme as evidências abaixo em documentação funcional.",
            "",
            "CATÁLOGO DO CENÁRIO:",
            json.dumps(payload["catalog"], ensure_ascii=False, indent=2),
            "",
            "EVIDÊNCIAS DA EXECUÇÃO:",
            json.dumps(payload["execution"], ensure_ascii=False, indent=2),
        ]
    )


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
