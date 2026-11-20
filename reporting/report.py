from __future__ import annotations

import json
from pathlib import Path

from reporting.templates import SCENARIO_SHEET


def _safe(value: object) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


def build_report(scenario: dict, execution: dict) -> str:
    step_rows = []
    for item in execution.get("steps", []):
        step_rows.append(
            f"| {item['step']} | {_safe(item.get('user_action', item.get('action')))} "
            f"| {_safe(item.get('data'))} | {_safe(item.get('observed_result'))[:500]} |"
        )

    messages = execution.get("messages") or []
    message_text = "\n".join(f"- {item}" for item in messages[:10])

    return SCENARIO_SHEET.format(
        id=scenario["id"],
        domain=scenario["domain"],
        name=scenario["name"],
        actor=scenario.get("actor", ""),
        flow=scenario.get("flow", ""),
        precondition=scenario.get("precondition", ""),
        result=execution.get("final_result", ""),
        messages=message_text,
        data=scenario.get("data", ""),
        coherent=scenario.get("coherent", ""),
        justification=scenario.get("justification", ""),
        requirement=scenario.get("requirement", ""),
        steps="\n".join(step_rows),
    )


def save_report(path: Path, scenario: dict, execution: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_report(scenario, execution), encoding="utf-8")


def save_execution(path: Path, execution: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(execution, ensure_ascii=False, indent=2), encoding="utf-8")
