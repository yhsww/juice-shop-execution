from __future__ import annotations

import re

from automation.observer import UIState


def validate(state: UIState, expected: dict, execution: dict | None = None) -> tuple[bool, str]:
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

    for step_number in expected.get("step_changed", []):
        if not execution:
            checks.append((False, f"passo {step_number} não disponível para validação"))
            continue
        steps = execution.get("steps", [])
        index = int(step_number) - 1
        changed = (
            0 <= index < len(steps)
            and bool(steps[index].get("changed"))
            and bool(steps[index].get("success"))
        )
        checks.append((changed, f"passo {step_number} produziu mudança observável"))

    # Some UI feedback is intentionally transient (for example the invalid
    # coupon snackbar). Validate the evidence produced by the relevant action
    # instead of requiring the message to survive until the final page state.
    for item in expected.get("step_text_contains", []):
        if not execution:
            checks.append((False, f"passo {item.get('step')} não disponível para validação"))
            continue
        step_number = int(item.get("step", 0))
        phrase = str(item.get("text", ""))
        index = step_number - 1
        steps = execution.get("steps", [])
        visible = ""
        if 0 <= index < len(steps):
            after = steps[index].get("state_after") or {}
            visible = str(after.get("visible_text", ""))
            if not visible:
                observed = str(steps[index].get("observed_result") or "")
                visible = observed
        ok = bool(phrase) and phrase.casefold() in visible.casefold()
        checks.append((ok, f"passo {step_number} contém texto '{phrase}'"))

    if not checks:
        return True, "Nenhum critério explícito informado."

    failed = [message for ok, message in checks if not ok]
    if failed:
        return False, "; ".join(failed)

    return True, "Todos os critérios observáveis foram atendidos."


def normalize_message(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()
