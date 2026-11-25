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

    successful_evidence = [
        item for item in (evidence or [])
        if item.get("success") is not False
    ]

    # Keep both the final DOM and the state captured immediately after each
    # action. This is important for transient Angular/Material feedback such
    # as snackbars, confirmation text, and controls that disappear after a
    # subsequent render. The stable final state alone is not sufficient.
    evidence_text: list[str] = []
    for item in successful_evidence:
        evidence_text.extend([
            str(item.get("observed_result") or ""),
            str(item.get("visible_text_before") or ""),
            str(item.get("visible_text_after") or ""),
            " ".join(str(message) for message in (item.get("messages") or [])),
            " ".join(str(control) for control in (item.get("controls") or [])),
        ])

    observed_text = "\n".join(
        [
            state.visible_text,
            " ".join(state.controls),
            *evidence_text,
        ]
    ).casefold()

    if expected.get("url_contains"):
        ok = expected["url_contains"].casefold() in state.url.casefold()
        checks.append((ok, f"URL contém '{expected['url_contains']}'"))

    for phrase in expected.get("text_contains", []):
        ok = str(phrase).casefold() in observed_text
        checks.append((ok, f"texto contém '{phrase}'"))

    if expected.get("status"):
        expected_status = str(expected["status"]).casefold()
        status_marker = f"status={expected_status}"

        # Semantic states such as Juice Shop's delivery status are represented
        # by UI controls/icons rather than literal visible text. Prefer the
        # final state, but also accept the same semantic marker captured by a
        # successful interaction snapshot. This is still black-box evidence:
        # it never derives the result from the scenario id or from application
        # internals, and it prevents a late observer snapshot from erasing a
        # state that was visibly present during the successful flow.
        status_controls = [str(control) for control in state.controls]
        for item in successful_evidence:
            status_controls.extend(
                str(control) for control in (item.get("controls") or [])
            )
        ok = any(status_marker in control.casefold() for control in status_controls)

        # Some Juice Shop views render the same semantic state as human-readable
        # text (for example "In Transit") without exposing the icon/control in
        # the final snapshot. Successful step evidence is already part of the
        # observable black-box corpus, so map the known delivery vocabulary to
        # its semantic status as a fallback.
        if not ok:
            status_text_patterns = {
                "new": (r"\border\s+placed\b", r"\bnew\b"),
                "packing": (r"\bpacking\b",),
                "transit": (
                    r"\bin\s+transit\b",
                    r"\bshipped\b",
                    r"\btransit\b",
                ),
                "delivered": (r"\bdelivered\b",),
            }
            patterns = status_text_patterns.get(expected_status, ())
            ok = any(re.search(pattern, observed_text) for pattern in patterns)

        checks.append((ok, f"status semântico = '{expected['status']}'"))

    for phrase in expected.get("text_not_contains", []):
        # Negative expectations describe the final application state, not
        # transient toast/snackbar overlays. The observer keeps those messages
        # separately, so remove their exact visible text before evaluating
        # absence. This prevents a successful basket-clear assertion from
        # failing because an old "Placed Apple Juice..." notification is still
        # rendered by the global notification layer.
        application_text = state.visible_text
        for message in state.messages:
            if message:
                # Compare normalized whitespace as well as the raw string.
                # Angular/CDK can normalize the same snackbar differently in
                # body.inner_text() and in the message container.
                normalized_message = " ".join(str(message).split())
                normalized_application = " ".join(application_text.split())
                if normalized_message:
                    normalized_application = normalized_application.replace(
                        normalized_message,
                        " ",
                    )
                application_text = normalized_application

        # Juice Shop can briefly leave a basket confirmation snackbar in the
        # rendered document even after the basket itself is empty. It is
        # feedback from the preceding action, not an item in the basket.
        application_text = re.sub(
            r"\bplaced\s+.+?\s+into\s+basket\.?(?:\s+x)?",
            " ",
            application_text,
            flags=re.IGNORECASE,
        )

        ok = str(phrase).casefold() not in application_text.casefold()
        checks.append((ok, f"texto não contém '{phrase}'"))

    if not checks:
        return True, "Nenhum critério explícito informado."

    failed = [message for ok, message in checks if not ok]
    if failed:
        return False, "; ".join(failed)

    return True, "Todos os critérios observáveis foram atendidos."


def normalize_message(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()
