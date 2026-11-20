from __future__ import annotations

import json
from pathlib import Path

from automation.browser import browser_session, open_juice_shop
from automation.executor import execute
from automation.observer import observe
from config.settings import settings
from reporting.evidence import Evidence, capture, save_json, timestamp
from reporting.report import save_execution, save_report


def load_scenarios(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))["scenarios"]


async def run_scenario(scenario: dict) -> dict:
    execution = {
        "scenario_id": scenario["id"],
        "status": "ERROR",
        "steps": [],
        "final_result": "",
        "messages": "",
    }

    async with browser_session() as (_, _, page):
        await open_juice_shop(page)

        previous_action = None
        repeated = 0

        for number, action in enumerate(scenario.get("actions", []), start=1):
            if number > settings.max_steps:
                execution["final_result"] = "Execução interrompida pelo limite máximo de passos."
                break

            fingerprint = json.dumps(action, sort_keys=True, ensure_ascii=False)
            if fingerprint == previous_action:
                repeated += 1
            else:
                repeated = 0
            previous_action = fingerprint

            if repeated >= 2:
                execution["final_result"] = "Execução interrompida por repetição da mesma ação sem progresso."
                break

            result = await execute(page, action)
            screenshot = await capture(
                page,
                settings.screenshot_dir,
                scenario["id"],
                number,
            )

            evidence = Evidence(
                step=number,
                action=result.action,
                data=result.data,
                url_before=result.url_before,
                url_after=result.url_after,
                observed_result=result.observed_result,
                changed=result.changed,
                success=result.success,
                screenshot=screenshot,
                error=result.error,
                timestamp=timestamp(),
            )
            execution["steps"].append(evidence.__dict__)

            if result.error:
                execution["final_result"] = result.error
                break

        final_state = await observe(page)
        execution["final_url"] = final_state.url
        execution["final_visible_text"] = final_state.visible_text
        execution["status"] = "PASSED" if execution["steps"] and all(
            item["success"] for item in execution["steps"]
        ) else "FAILED"

        if not execution["final_result"]:
            execution["final_result"] = final_state.visible_text[:2000]

    out = settings.report_dir / scenario["id"]
    save_execution(out.with_suffix(".json"), execution)
    save_report(out.with_suffix(".md"), scenario, execution)
    return execution


async def run_selected(ids: set[str] | None = None) -> list[dict]:
    scenarios = load_scenarios(Path(__file__).resolve().parents[1] / "scenarios" / "scenarios.json")
    selected = [s for s in scenarios if ids is None or s["id"] in ids]

    if ids:
        missing = ids - {s["id"] for s in selected}
        if missing:
            raise ValueError(f"Cenários não encontrados: {', '.join(sorted(missing))}")

    results = []
    for scenario in selected:
        results.append(await run_scenario(scenario))
    return results
