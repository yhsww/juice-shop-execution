from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from automation.observer import UIState


@dataclass(frozen=True)
class BehaviorEvent:
    """Machine-readable observation of one user action.

    This is intentionally independent from PASS/FAIL. The event describes what
    the application actually exposed before and after the action, which is the
    primary evidence used by AMBOLS for reverse engineering.
    """
    scenario_id: str
    step: int
    action: str
    user_action: str
    target: dict[str, Any]
    data: str
    behavior_type: str
    observed: str
    changed: bool
    success: bool
    url_before: str
    url_after: str
    messages: list[str]
    controls_before: list[str]
    controls_after: list[str]
    visible_text_before: str
    visible_text_after: str
    screenshot: str | None
    error: str | None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def classify_behavior(action: str, before: UIState | None, after: UIState | None,
                       success: bool, observed: str) -> str:
    if not success:
        return "automation_error"
    if before is None or after is None:
        return "action_completed"
    if before.url != after.url:
        return "navigation"
    if after.messages and after.messages != before.messages:
        return "feedback"
    if before.controls != after.controls:
        return "control_state_change"
    if before.body_hash != after.body_hash:
        return "content_change"
    if before.visible_text != after.visible_text:
        return "visible_text_change"
    if observed and "Nenhuma mudança" not in observed:
        return "observable_change"
    return "no_visible_change"


def build_behavior_event(scenario_id: str, step: int, result, target: dict[str, Any]) -> BehaviorEvent:
    before = result.state_before
    after = result.state_after
    return BehaviorEvent(
        scenario_id=scenario_id,
        step=step,
        action=result.action,
        user_action=result.user_action,
        target=target or {},
        data=result.data,
        behavior_type=classify_behavior(
            result.action, before, after, result.success, result.observed_result
        ),
        observed=result.observed_result,
        changed=result.changed,
        success=result.success,
        url_before=result.url_before,
        url_after=result.url_after,
        messages=list(result.messages),
        controls_before=list(before.controls if before else ()),
        controls_after=list(after.controls if after else ()),
        visible_text_before=(before.visible_text if before else ""),
        visible_text_after=(after.visible_text if after else ""),
        screenshot=None,
        error=result.error,
    )
