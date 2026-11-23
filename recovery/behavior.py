from __future__ import annotations

from collections import defaultdict
from typing import Any


def extract_behaviors(*, states: list[dict[str, Any]], transitions: list[dict[str, Any]],
                      actions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Extract observed behavior from evidence, never from declared expectations."""
    result = []
    seen = set()
    for item in transitions:
        if not item.get("changed"):
            continue
        key = (str(item.get("from_state", item.get("from_route", ""))),
               str(item.get("to_state", item.get("to_route", ""))),
               str(item.get("action_id", "")))
        if key in seen:
            continue
        seen.add(key)
        result.append({
            "behavior_id": f"BEH-{len(result)+1:04d}", "type": "state-transition",
            "action_id": item.get("action_id"), "description": item.get("description"),
            "evidence": {
                "from_state": item.get("from_state", item.get("from_route")),
                "to_state": item.get("to_state", item.get("to_route")),
                "action": item.get("action"), "network": item.get("network", []),
            },
        })
    for action in actions:
        observed = str(action.get("observed_result") or "").strip()
        messages = list(action.get("messages") or [])
        if not observed and not messages:
            continue
        key = (str(action.get("action_id", "")), observed, "|".join(map(str, messages)))
        if key in seen:
            continue
        seen.add(key)
        result.append({
            "behavior_id": f"BEH-{len(result)+1:04d}", "type": "ui-observation",
            "action_id": action.get("action_id"),
            "description": observed or "A interface exibiu uma mensagem observada.",
            "evidence": {
                "url_before": action.get("url_before"), "url_after": action.get("url_after"),
                "messages": messages, "network": action.get("network", []),
            },
        })
    return result


def consolidate_by_domain(behaviors: list[dict[str, Any]],
                          domain_map: dict[str, str]) -> dict[str, list[dict[str, Any]]]:
    grouped = defaultdict(list)
    for behavior in behaviors:
        grouped[domain_map.get(str(behavior.get("scenario_id") or ""), "UNSPECIFIED")].append(behavior)
    return dict(grouped)
