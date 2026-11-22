from __future__ import annotations

import re

from automation.observer import UIState


def validate(
    state: UIState,
    expected: dict,
    evidence: list[dict] | None = None,
) -> tuple[bool, str]:
    """Validate declared expectations against the complete observable evidence.

    A UI requirement may be satisfied by transient feedback that is no longer
    present in the final DOM (for example a snackbar such as "Invalid coupon").
    The final UI state remains the authoritative source for final-state
    expectations, while successful step observations provide additional
    evidence for transient text.

    Automation errors are deliberately excluded from the evidence corpus so
    an assertion cannot pass merely because a failed interaction happened to
    mention the expected phrase.
    """
    checks: list[tuple[bool, str]] = []

    successful_observations = [
        str(item.get("observed_result") or "")
        for item in (evidence or [])
        if item.get("success") is not False
    ]
    observed_text = "\n".join(
        [state.visible_text, *successful_observations]
    ).casefold()

    if expected.get("url_contains"):
        ok = expected["url_contains"].casefold() in state.url.casefold()
        checks.append((ok, f"URL contém '{expected['url_contains']}'"))

    for phrase in expected.get("text_contains", []):
        ok = str(phrase).casefold() in observed_text
        checks.append((ok, f"texto contém '{phrase}'"))

    for phrase in expected.get("text_not_contains", []):
        # Negative expectations must describe the final visible application
        # state; transient evidence from earlier steps must not make a final
        # absence assertion fail.
        ok = str(phrase).casefold() not in state.visible_text.casefold()
        checks.append((ok, f"texto não contém '{phrase}'"))

    if not checks:
        return True, "Nenhum critério explícito informado."

    failed = [message for ok, message in checks if not ok]
    if failed:
        return False, "; ".join(failed)

    return True, "Todos os critérios observáveis foram atendidos."


def normalize_message(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()
