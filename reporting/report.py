from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from reporting.templates import DOMAIN_SHEET, SCENARIO_SHEET


def _safe(value: object) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


def _unique(items: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for item in items:
        normalized = " ".join(str(item or "").split()).strip()
        if not normalized:
            continue
        key = normalized.casefold()
        if key not in seen:
            seen.add(key)
            result.append(normalized)
    return result


def _successful_steps(execution: dict) -> list[dict]:
    return [
        step for step in execution.get("steps", [])
        if step.get("success") is True
    ]


def _observed_behavior(execution: dict) -> str:
    """Build a conservative scenario-level observation from execution evidence.

    This is intentionally evidence-first: it never upgrades the declared
    expectation into an observed fact. The report describes only successful
    steps, their UI responses, and the final observable state.
    """
    steps = _successful_steps(execution)
    observations = _unique([
        str(step.get("observed_result") or "")
        for step in steps
        if step.get("observed_result")
        and "Nenhuma mudança visual relevante detectada." not in str(step.get("observed_result"))
    ])

    if not observations:
        final_url = str(execution.get("final_url") or "").strip()
        final_text = " ".join(str(execution.get("final_visible_text") or "").split()).strip()
        if final_url:
            return f"A execução foi concluída na URL observada: {final_url}."
        if final_text:
            return f"A execução foi concluída com o estado visível observado na interface: {final_text[:700]}."
        return "A execução foi concluída sem mudança de estado adicional capturada pela observação."

    if len(observations) == 1:
        return observations[0][:1600]

    lines = ["Durante a execução, foram observadas as seguintes mudanças na interface:"]
    for index, item in enumerate(observations[:8], start=1):
        lines.append(f"{index}. {item}")
    return "\n".join(lines)[:2600]


def _observed_messages(execution: dict) -> list[str]:
    messages = list(execution.get("messages") or [])
    for step in execution.get("steps", []):
        messages.extend(step.get("messages") or [])
    return _unique([str(item) for item in messages])[:20]


def _observed_data(execution: dict, scenario: dict) -> str:
    values = []
    declared = str(scenario.get("data") or "").strip()
    if declared:
        values.append(f"Dados declarados no cenário: {declared}")

    for step in execution.get("steps", []):
        value = str(step.get("data") or "").strip()
        if value:
            values.append(
                f"Passo {step.get('step')}: {value}"
            )

    return "\n".join(_unique(values))[:2200] or "Nenhum dado de entrada relevante registrado."


def _scenario_description(scenario: dict, execution: dict) -> str:
    """Describe the scenario without introducing a new REQ/END/COMP artifact."""
    name = str(scenario.get("name") or "").strip()
    flow = str(scenario.get("flow") or "").strip()
    actor = str(scenario.get("actor") or "").strip()
    if name and flow and actor:
        return (
            f"{actor} executa o fluxo '{flow}'. "
            f"A descrição corresponde ao cenário '{name}' e deve ser interpretada "
            "em conjunto com as evidências registradas nos passos."
        )
    return flow or name or "Cenário sem descrição textual."


def build_report(scenario: dict, execution: dict) -> str:
    step_rows = []
    for item in execution.get("steps", []):
        response = str(item.get("observed_result") or "").strip()
        if item.get("error"):
            response = f"Falha de automação: {item.get('error')}"
        step_rows.append(
            f"| {item['step']} | {_safe(item.get('user_action', item.get('action')))} "
            f"| {_safe(item.get('data'))} | {_safe(response)[:900]} |"
        )

    messages = _observed_messages(execution)
    message_text = "\n".join(f"- {item}" for item in messages) or "Nenhuma mensagem transitória relevante capturada."

    return SCENARIO_SHEET.format(
        id=scenario["id"],
        domain=scenario["domain"],
        name=scenario["name"],
        actor=scenario.get("actor", ""),
        flow=scenario.get("flow", ""),
        precondition=scenario.get("precondition", ""),
        result=_observed_behavior(execution),
        description=_scenario_description(scenario, execution),
        messages=message_text,
        data=_observed_data(execution, scenario),
        coherent=scenario.get("coherent", ""),
        justification=scenario.get("justification", ""),
        requirement=scenario.get("requirement", ""),
        steps="\n".join(step_rows) or "| — | — | — | Nenhum passo registrado. |",
    )


def save_report(path: Path, scenario: dict, execution: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_report(scenario, execution), encoding="utf-8")


def save_execution(path: Path, execution: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(execution, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def build_domain_report(domain: str, executions: list[dict]) -> str:
    passed = [item for item in executions if item.get("status") == "PASSED"]
    lines = [
        f"# Relatório do domínio {domain}",
        "",
        f"**Cenários executados:** {len(executions)}",
        f"**Cenários aprovados:** {len(passed)}",
        f"**Status do conjunto:** {'PASSED' if len(passed) == len(executions) else 'NÃO CONSOLIDADO'}",
        "",
        "## Cenários",
        "",
        "| ID | Cenário | Status | Comportamento observado |",
        "|---|---|---|---|",
    ]

    for execution in executions:
        scenario = execution.get("_scenario", {})
        observation = _observed_behavior(execution).replace("\n", " ")
        lines.append(
            f"| {scenario.get('id', execution.get('scenario_id', ''))} | "
            f"{_safe(scenario.get('name', ''))} | {execution.get('status', '')} | "
            f"{_safe(observation)[:1000]} |"
        )

    lines.extend(["", "## Mensagens observadas", ""])
    all_messages: list[str] = []
    for execution in executions:
        all_messages.extend(_observed_messages(execution))
    for message in _unique(all_messages):
        lines.append(f"- {message}")

    lines.extend(["", "## Rastreabilidade", ""])
    lines.append(
        "Cada descrição acima é derivada dos passos e evidências da execução do "
        "respectivo cenário; nenhum comportamento é inferido a partir de END, COMP ou REQ."
    )
    return "\n".join(lines) + "\n"


def save_domain_reports(
    output_dir: Path,
    scenarios: list[dict],
    executions: list[dict],
) -> None:
    """Persist domain consolidations only for a complete successful run."""
    if not executions or any(item.get("status") != "PASSED" for item in executions):
        return

    scenario_by_id = {item["id"]: item for item in scenarios}
    grouped: dict[str, list[dict]] = defaultdict(list)
    for execution in executions:
        enriched = dict(execution)
        enriched["_scenario"] = scenario_by_id.get(execution.get("scenario_id"), {})
        domain = str(enriched["_scenario"].get("domain") or "").upper()
        if domain:
            grouped[domain].append(enriched)

    domains_dir = output_dir / "domains"
    domains_dir.mkdir(parents=True, exist_ok=True)

    for domain, items in sorted(grouped.items()):
        items.sort(key=lambda item: str(item.get("scenario_id", "")))
        (domains_dir / f"{domain}.md").write_text(
            build_domain_report(domain, items),
            encoding="utf-8",
        )
        payload = {
            "stage": "ETAPA_1",
            "domain": domain,
            "scenario_count": len(items),
            "status": "PASSED",
            "scenarios": [
                {
                    "id": item.get("scenario_id"),
                    "name": item.get("_scenario", {}).get("name"),
                    "status": item.get("status"),
                    "observed_behavior": _observed_behavior(item),
                    "steps": item.get("steps", []),
                }
                for item in items
            ],
        }
        (domains_dir / f"{domain}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
