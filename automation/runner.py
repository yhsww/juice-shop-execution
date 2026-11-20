from __future__ import annotations

import json
from pathlib import Path

from automation.browser import browser_session, open_juice_shop
from automation.executor import execute
from automation.locator import resolve
from automation.observer import observe
from automation.validator import validate
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


def _requires_authentication(scenario: dict) -> bool:
    precondition = str(scenario.get("precondition", "")).lower()
    actor = str(scenario.get("actor", "")).lower()
    return "autenticad" in precondition or "administrador" in actor


def _is_admin(scenario: dict) -> bool:
    return str(scenario.get("actor", "")).lower().startswith("administrador")


async def _login(page, scenario: dict) -> str | None:
    if not _requires_authentication(scenario):
        return None

    email = settings.admin_email if _is_admin(scenario) else settings.user_email
    password = settings.admin_password if _is_admin(scenario) else settings.user_password

    await page.goto(f"{settings.base_url}/#/login", wait_until="domcontentloaded")
    email_field = await resolve(page, {"label": "Email", "exact": False})
    password_field = await resolve(page, {"label": "Password", "exact": False})

    if email_field is None or password_field is None:
        return "Não foi possível localizar os campos de autenticação."

    await email_field.fill(email, timeout=settings.action_timeout_ms)
    await password_field.fill(password, timeout=settings.action_timeout_ms)

    login_button = await resolve(page, {"role": "button", "name": "Login", "exact": False})
    if login_button is None:
        return "Botão de login não encontrado."

    await login_button.click(timeout=settings.action_timeout_ms)
    await page.wait_for_timeout(700)

    if "/#/login" in page.url:
        return "A autenticação não foi concluída; a aplicação permaneceu na tela de login."

    return None


async def run_scenario(scenario: dict) -> dict:
    execution = {
        "scenario_id": scenario["id"],
        "status": "ERROR",
        "steps": [],
        "final_result": "",
        "messages": [],
    }

    async with browser_session() as (_, _, page):
        await open_juice_shop(page)

        auth_error = await _login(page, scenario)
        if auth_error:
            execution["final_result"] = auth_error
            execution["status"] = "FAILED"
            out = settings.report_dir / scenario["id"]
            save_execution(out.with_suffix(".json"), execution)
            save_report(out.with_suffix(".md"), scenario, execution)
            return execution

        previous_action = None
        repeated = 0

        for number, action in enumerate(scenario.get("actions", []), start=1):
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
            )
            execution["steps"].append(evidence.__dict__)

            for message in result.messages:
                if message not in execution["messages"]:
                    execution["messages"].append(message)

            if result.error:
                execution["final_result"] = result.observed_result or result.error

                print(
                    f"[ERROR] {scenario['id']} | passo {number} | "
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
                if result.screenshot:
                    print(f"[ERROR] Evidência: {result.screenshot}")

                break

        final_state = await observe(page)
        execution["final_url"] = final_state.url
        execution["final_visible_text"] = final_state.visible_text

        valid, validation_message = validate(final_state, scenario.get("expected", {}))
        execution["validation"] = {
            "passed": valid,
            "message": validation_message,
        }

        execution["status"] = (
            "PASSED"
            if execution["steps"]
            and all(item["success"] for item in execution["steps"])
            and valid
            else "FAILED"
        )

        if not execution["final_result"]:
            execution["final_result"] = (
                execution["steps"][-1]["observed_result"]
                if execution["steps"]
                else validation_message
            )

    out = settings.report_dir / scenario["id"]
    save_execution(out.with_suffix(".json"), execution)
    save_report(out.with_suffix(".md"), scenario, execution)
    return execution


async def run_selected(ids: set[str] | None = None) -> list[dict]:
    scenarios = load_scenarios(
        Path(__file__).resolve().parents[1] / "scenarios"
    )
    selected = [s for s in scenarios if ids is None or s["id"] in ids]

    if ids:
        missing = ids - {s["id"] for s in selected}
        if missing:
            raise ValueError(
                f"Cenários não encontrados: {', '.join(sorted(missing))}"
            )

    results = []
    for scenario in selected:
        results.append(await run_scenario(scenario))
    return results
