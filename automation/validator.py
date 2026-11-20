from __future__ import annotations

import re

from automation.observer import UIState


def validate(state: UIState, expected: dict) -> tuple[bool, str]:
    checks: list[tuple[bool, str]] = []

    if expected.get("url_contains"):
        ok = expected["url_contains"] in state.url
        checks.append((ok, f"URL contém '{expected['url_contains']}'"))

    for phrase in expected.get("text_contains", []):
        ok = phrase.lower() in state.visible_text.lower()
        checks.append((ok, f"texto contém '{phrase}'"))

    for phrase in expected.get("text_not_contains", []):
        ok = phrase.lower() not in state.visible_text.lower()
        checks.append((ok, f"texto não contém '{phrase}'"))

    if not checks:
        return True, "Nenhum critério explícito informado."

    failed = [message for ok, message in checks if not ok]
    if failed:
        return False, "; ".join(failed)

    return True, "Todos os critérios observáveis foram atendidos."


def normalize_message(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()
