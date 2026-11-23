from __future__ import annotations

import json
from pathlib import Path


def build_stage1_report(result: dict) -> str:
    lines = [
        "# Engenharia reversa — Etapa 1", "",
        "**Método:** exploração guiada por cenários, com execução real da UI e registro de comportamento observável.",
        "", "## Resumo", "",
        f"- Cenários executados: {result.get('counts', {}).get('scenarios', 0)}",
        f"- Comportamentos observados: {result.get('counts', {}).get('behaviors', 0)}",
        f"- Cenários alternativos descobertos: {result.get('counts', {}).get('alternatives', 0)}",
        "", "## Comportamentos observados", "",
        "| ID | Cenário | Tipo | Comportamento observado |",
        "|---|---|---|---|"
    ]
    for item in result.get("behaviors", []):
        desc = " ".join(str(item.get("description") or "").split()).replace("|", "\|")
        lines.append(f"| {item.get('behavior_id','')} | {item.get('scenario_id','')} | {item.get('kind','')} | {desc[:1200]} |")
    lines += [
        "", "## Cenários alternativos descobertos", "",
        "| ID | Origem | Domínio | Comportamento que originou o caminho |",
        "|---|---|---|---|"
    ]
    for item in result.get("discovered_scenarios", []):
        desc = " ".join(str(item.get("description") or "").split()).replace("|", "\|")
        lines.append(f"| {item.get('scenario_id','')} | {item.get('source_scenario','')} | {item.get('domain','')} | {desc[:1200]} |")
    lines += ["", "## Evidência por cenário", ""]
    for scenario in result.get("scenarios", []):
        lines += [
            f"### {scenario.get('scenario_id','')} — {scenario.get('name','')}", "",
            f"**Fluxo planejado:** {scenario.get('planned_flow','')}", "",
            f"**Passos executados:** {scenario.get('steps_executed', 0)}", ""
        ]
        for obs in scenario.get("observations", []):
            lines += [
                f"#### {obs.get('action_id','')}", "",
                f"**Ação:** {obs.get('action', {}).get('type','')}",
                f"**Dados:** {str(obs.get('data',''))[:500]}",
                f"**Resultado observado:** {obs.get('observed_behavior','')}",
                f"**Screenshot antes:** {obs.get('screenshot_before','')}",
                f"**Screenshot depois:** {obs.get('screenshot_after','')}", ""
            ]
    lines += [
        "## Integridade metodológica", "",
        "O comportamento é derivado da execução observável da interface. Dados esperados do cenário não são tratados como evidência. Network/ZAP são evidências complementares. Esta etapa não produz END, COMP ou REQ.", ""
    ]
    return "\n".join(lines)


def save_stage1_report(output_dir: Path, result: dict) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "ETAPA_1.md").write_text(build_stage1_report(result), encoding="utf-8")
    (output_dir / "ETAPA_1.json").write_text(
        json.dumps({
            "stage": "ETAPA_1",
            "counts": result.get("counts", {}),
            "scenarios": result.get("scenarios", []),
            "behaviors": result.get("behaviors", []),
            "discovered_scenarios": result.get("discovered_scenarios", []),
        }, ensure_ascii=False, indent=2), encoding="utf-8")
