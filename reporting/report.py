from __future__ import annotations

import json
from pathlib import Path

from reporting.templates import SCENARIO_SHEET


def build_report(scenario: dict, execution: dict) -> str:
    step_rows = []
    for item in execution["steps"]:
        response = item["observed_result"].replace("|", "\\|").replace("\n", " ")
        step_rows.append(
            f"| {item['step']} | {item['action']} | {item['data']} | {response[:500]} |"
        )

    return SCENARIO_SHEET.format(
        id=scenario["id"],
        domain=scenario["domain"],
        name=scenario["name"],
        actor=scenario.get("actor", ""),
        flow=scenario.get("flow", ""),
        precondition=scenario.get("precondition", ""),
        result=execution.get("final_result", ""),
        messages=execution.get("messages", ""),
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
