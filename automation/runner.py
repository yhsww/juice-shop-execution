from __future__ import annotations

import asyncio
import json
import time
from pathlib import Path
from uuid import uuid4

from automation.browser import browser_session, open_juice_shop
from automation.executor import execute
from automation.observer import observe
from automation.validator import validate
from automation.preconditions import (
    prepare_precondition,
    scenario_email,
    scenario_password,
)
from config.settings import settings
from reporting.evidence import Evidence, capture, save_execution, timestamp
from reporting.report import save_report


def load_scenarios(path: Path) -> list[dict]:
    scenarios = []
    for file in sorted(path.glob("*.json")):
        if file.name.startswith("_"):
            continue
        payload = json.loads(file.read_text(encoding="utf-8"))
        scenarios.extend(payload.get("scenarios", []))

    ids = [item["id"] for item in scenarios]
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        raise ValueError(f"IDs de cenário duplicados: {', '.join(duplicates)}")
    return scenarios



def _materialize_action(action: dict, scenario: dict) -> dict:
    """Resolve scenario data placeholders at execution time."""
    runtime = scenario.setdefault("_runtime_data", {})
    if "unique_email" not in runtime:
        runtime["unique_email"] = f"cen-{scenario['id'].lower()}-{uuid4().hex[:10]}@example.com"

    replacements = {
        "${SCENARIO_EMAIL}": scenario_email(scenario),
        "${SCENARIO_PASSWORD}": scenario_password(scenario),
        "${BASE_TEST_EMAIL}": "teste@example.com",
        "${UNIQUE_EMAIL}": runtime["unique_email"],
    }

    def replace(value):
        if isinstance(value, str):
            for source, target in replacements.items():
                value = value.replace(source, target)
            return value
        if isinstance(value, list):
            return [replace(item) for item in value]
        if isinstance(value, dict):
            return {key: replace(item) for key, item in value.items()}
        return value

    return replace(action)


async def _run_scenario(scenario: dict) -> dict:
    scenario_started = time.monotonic()
    scenario_timeout = max(1, settings.scenario_timeout_seconds)

    execution = {
        "scenario_id": scenario["id"],
        "status": "ERROR",
        "steps": [],
        "final_result": "",
        "messages": [],
    }

    async with browser_session() as (_, _, page):
        await open_juice_shop(page)

        # Preconditions are part of the scenario budget. A stalled browser
        # request or Angular wait must not block the whole domain run.
        remaining = max(0.5, scenario_timeout - (time.monotonic() - scenario_started))
        try:
            prepared, preparation_error = await asyncio.wait_for(
                prepare_precondition(page, scenario),
                timeout=remaining,
            )
        except asyncio.TimeoutError:
            prepared = False
            preparation_error = (
                f"Tempo limite de pré-condição atingido ({scenario_timeout}s)."
            )
        except Exception as exc:
            # A fixture/precondition failure is an automation problem, not a
            # crash of the whole domain run. Keep the scenario isolated so a
            # bad fixture cannot prevent the remaining scenarios from running.
            prepared = False
            preparation_error = (
                f"Erro ao preparar pré-condição: {type(exc).__name__}: {exc}"
            )

        if not prepared:
            execution["final_result"] = preparation_error
            execution["status"] = "AUTOMATION_ERROR"
            print(f"[AUTOMATION_ERROR] {scenario['id']} | pré-condição | {preparation_error}")
            out = settings.report_dir / scenario["id"]
            save_execution(out.with_suffix(".json"), execution)
            save_report(out.with_suffix(".md"), scenario, execution)
            return execution

        previous_action = None
        repeated = 0
        timed_out = False

        print(f"[START] {scenario['id']} | limite: {scenario_timeout}s")

        if time.monotonic() - scenario_started >= scenario_timeout:
            execution["status"] = "TIMEOUT"
            execution["final_result"] = (
                f"Tempo limite do cenário atingido ({scenario_timeout}s) durante a pré-condição."
            )
            print(f"[TIMEOUT] {scenario['id']} | pré-condição excedeu {scenario_timeout}s.")
            out = settings.report_dir / scenario["id"]
            save_execution(out.with_suffix(".json"), execution)
            save_report(out.with_suffix(".md"), scenario, execution)
            return execution

        for number, raw_action in enumerate(scenario.get("actions", []), start=1):
            elapsed = time.monotonic() - scenario_started
            if elapsed >= scenario_timeout:
                timed_out = True
                execution["final_result"] = (
                    f"Tempo limite do cenário atingido ({scenario_timeout}s)."
                )
                print(
                    f"[TIMEOUT] {scenario['id']} | "
                    f"{scenario_timeout}s atingidos antes do passo {number}."
                )
                break
            action = _materialize_action(raw_action, scenario)
            if number > settings.max_steps:
                execution["final_result"] = "Execução interrompida pelo limite máximo de passos."
                print(
                    f"[ERROR] {scenario['id']} | limite máximo de passos "
                    f"({settings.max_steps}) atingido."
                )
                break

            fingerprint = json.dumps(action, sort_keys=True, ensure_ascii=False)
            repeated = repeated + 1 if fingerprint == previous_action else 0
            previous_action = fingerprint

            if repeated >= 2:
                execution["final_result"] = "Execução interrompida por repetição da mesma ação sem progresso."
                print(
                    f"[ERROR] {scenario['id']} | passo {number} | "
                    "repetição da mesma ação sem progresso."
                )
                break

            result = await execute(page, action)

            if time.monotonic() - scenario_started >= scenario_timeout:
                timed_out = True

            screenshot = await capture(
                page,
                settings.screenshot_dir,
                scenario["id"],
                number,
            )

            evidence = Evidence(
                step=number,
                action=result.action,
                user_action=result.user_action,
                data=result.data,
                url_before=result.url_before,
                url_after=result.url_after,
                observed_result=result.observed_result,
                changed=result.changed,
                success=result.success,
                screenshot=screenshot,
                error=result.error,
                timestamp=timestamp(),
                visible_text_before=(result.state_before.visible_text if result.state_before else ""),
                visible_text_after=(result.state_after.visible_text if result.state_after else ""),
                messages=result.messages,
            )
            execution["steps"].append(evidence.__dict__)

            for message in result.messages:
                if message not in execution["messages"]:
                    execution["messages"].append(message)

            if result.error:
                # A locator/action failure means the scenario could not be
                # exercised. It must not be reported as a functional failure
                # of the Juice Shop application.
                execution["final_result"] = result.observed_result or result.error
                execution["status"] = "AUTOMATION_ERROR"

                print(
                    f"[AUTOMATION_ERROR] {scenario['id']} | passo {number} | "
                    f"{result.user_action}"
                )
                print(f"[ERROR] {result.error}")
                print(f"[ERROR] URL antes: {result.url_before}")
                print(f"[ERROR] URL depois: {result.url_after}")
                if result.observed_result:
                    print(
                        f"[ERROR] Resultado observado: "
                        f"{result.observed_result}"
                    )
                if screenshot:
                    print(f"[ERROR] Evidência: {screenshot}")

                break

        final_state = await observe(page)
        execution["final_url"] = final_state.url
        execution["final_visible_text"] = final_state.visible_text

        expected = scenario.get("expected", {})
        valid, validation_message = validate(
            final_state,
            expected,
            evidence=execution["steps"],
        )

        # Some Juice Shop actions intentionally open a new browser page (for
        # example the donation/merchandise links and printable confirmation).
        # The original page remains on the checkout screen, so validate the
        # captured popup URL as part of the same generic scenario contract.
        external_expected = expected.get("external_url_contains")
        if valid and external_expected:
            observed_urls = [step.get("url_after", "") for step in execution["steps"]]
            if not any(external_expected.casefold() in str(url).casefold() for url in observed_urls):
                valid = False
                validation_message = (
                    f"Nenhuma nova página/aba observada com URL contendo "
                    f"'{external_expected}'. URLs observadas: {observed_urls}"
                )

        execution["validation"] = {
            "passed": valid,
            "message": validation_message,
        }

        if not valid:
            print(
                f"[VALIDATION] {scenario['id']} | "
                f"{validation_message}"
            )
            print(f"[VALIDATION] URL final: {final_state.url}")

        if timed_out:
            execution["status"] = "TIMEOUT"
        elif any(not item["success"] for item in execution["steps"]):
            # The UI action itself could not be executed. Keep this distinct
            # from a functional assertion failure.
            execution["status"] = "AUTOMATION_ERROR"
        elif not valid:
            # Actions completed, but the observed application state did not
            # satisfy the scenario expectation.
            execution["status"] = "FAILED"
        else:
            execution["status"] = "PASSED"

        if timed_out and not execution["final_result"]:
            execution["final_result"] = (
                f"Tempo limite do cenário atingido ({scenario_timeout}s)."
            )
        elif not execution["final_result"]:
            execution["final_result"] = (
                execution["steps"][-1]["observed_result"]
                if execution["steps"]
                else validation_message
            )

    out = settings.report_dir / scenario["id"]
    save_execution(out.with_suffix(".json"), execution)
    save_report(out.with_suffix(".md"), scenario, execution)
    return execution


async def run_scenario(scenario: dict) -> dict:
    """Execute one scenario with a cancellation-safe, soft time budget."""
    return await _run_scenario(scenario)


async def run_selected(ids: set[str] | None = None, domains: set[str] | None = None) -> list[dict]:
    scenarios = load_scenarios(
        Path(__file__).resolve().parents[1] / "scenarios"
    )
    normalized_domains = {domain.upper() for domain in domains} if domains else None
    available_domains = {s.get("domain", s["id"].split("-")[1]).upper() for s in scenarios}
    if normalized_domains:
        unknown_domains = normalized_domains - available_domains
        if unknown_domains:
            raise ValueError(
                f"Domínios não encontrados: {', '.join(sorted(unknown_domains))}. "
                f"Disponíveis: {', '.join(sorted(available_domains))}"
            )

    selected = [
        s for s in scenarios
        if (ids is None or s["id"] in ids)
        and (normalized_domains is None or s.get("domain", s["id"].split("-")[1]).upper() in normalized_domains)
    ]

    if ids:
        missing = ids - {s["id"] for s in scenarios}
        if missing:
            raise ValueError(
                f"Cenários não encontrados: {', '.join(sorted(missing))}"
            )

    results = []
    for scenario in selected:
        results.append(await run_scenario(scenario))
    return results
