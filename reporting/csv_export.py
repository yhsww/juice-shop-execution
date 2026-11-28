"""Exporta o catálogo executado para CSV (uma visão tabular dos mesmos dados dos DOCX).

Gera em reports/csv/:
- cenarios.csv: uma linha por cenário (catálogo + resultado + texto humanizado);
- passos.csv: uma linha por passo executado (ação, dados, resposta, API, captura).

Formato: separador ";" e UTF-8 com BOM, para abrir direto no Excel em português.
Não executa cenários nem chama a LLM: só lê o que já foi gerado.

Uso: python -m reporting.csv_export
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

from reporting.docx_generator import load_scenarios, scenario_order

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCENARIOS = ROOT / "scenarios"
DEFAULT_EXECUTIONS = ROOT / "reports" / "executions"
DEFAULT_HUMANIZED = ROOT / "reports" / "humanized"
DEFAULT_OUTPUT = ROOT / "reports" / "csv"

SCENARIO_COLUMNS = [
    "id", "dominio", "nome", "ator", "tipo_fluxo", "cenario_base", "acesso",
    "status", "executado_em", "passos", "requisicoes_api",
    "precondicao", "fluxo", "dados", "resultado_observado", "mensagens",
    "evidencia_json", "evidencia_har",
]
STEP_COLUMNS = [
    "id_cenario", "passo", "tipo_acao", "acao", "dados", "resposta",
    "sucesso", "requisicoes_api", "captura",
]


def _read_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def _one_line(value: Any) -> str:
    if isinstance(value, list):
        value = " | ".join(str(item) for item in value if str(item).strip())
    return " ".join(str(value or "").split())


def build_rows(
    scenarios: list[dict[str, Any]],
    executions_dir: Path,
    humanized_dir: Path,
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    scenario_rows, step_rows = [], []
    for scenario in sorted(scenarios, key=scenario_order):
        sid = str(scenario.get("id") or "")
        execution = _read_json(executions_dir / f"{sid}.json")
        text = _read_json(humanized_dir / f"{sid}.json").get("content") or {}
        steps = execution.get("steps") or []
        text_steps = {str(item.get("number")): item for item in text.get("steps") or []}
        api_calls = sum(len(step.get("network") or []) for step in steps)
        har = executions_dir / f"{sid}.har"

        scenario_rows.append({
            "id": sid,
            "dominio": str(scenario.get("domain") or ""),
            "nome": _one_line(scenario.get("name")),
            "ator": _one_line(scenario.get("actor")),
            "tipo_fluxo": _one_line(scenario.get("flow_type") or "Fluxo principal (catálogo-base)"),
            "cenario_base": _one_line(scenario.get("base_scenario")),
            "acesso": _one_line(scenario.get("auth")),
            "status": _one_line(execution.get("status") or "NÃO EXECUTADO"),
            "executado_em": _one_line(steps[0].get("timestamp") if steps else ""),
            "passos": str(len(steps)),
            "requisicoes_api": str(api_calls),
            "precondicao": _one_line(text.get("precondition") or scenario.get("precondition")),
            "fluxo": _one_line(text.get("flow") or scenario.get("flow")),
            "dados": _one_line(text.get("data") or scenario.get("data")),
            "resultado_observado": _one_line(text.get("observed_result") or execution.get("final_result")),
            "mensagens": _one_line(text.get("messages")),
            "evidencia_json": f"{sid}.json" if execution else "",
            "evidencia_har": har.name if har.exists() else "",
        })

        for step in steps:
            number = str(step.get("step") or "")
            described = text_steps.get(number, {})
            screenshot = Path(str(step.get("screenshot") or "")).name
            step_rows.append({
                "id_cenario": sid,
                "passo": number,
                "tipo_acao": _one_line(step.get("action")),
                "acao": _one_line(described.get("action") or step.get("user_action")),
                "dados": _one_line(described.get("data") or step.get("data")),
                "resposta": _one_line(described.get("response") or step.get("observed_result")),
                "sucesso": "sim" if step.get("success") else "não",
                "requisicoes_api": _one_line(step.get("network")),
                "captura": screenshot,
            })
    return scenario_rows, step_rows


def write_csv(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Exporta cenários e passos para CSV.")
    parser.add_argument("--scenarios", type=Path, default=DEFAULT_SCENARIOS)
    parser.add_argument("--executions", type=Path, default=DEFAULT_EXECUTIONS)
    parser.add_argument("--humanized", type=Path, default=DEFAULT_HUMANIZED)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    scenario_rows, step_rows = build_rows(
        load_scenarios(args.scenarios), args.executions, args.humanized
    )
    write_csv(args.output / "cenarios.csv", SCENARIO_COLUMNS, scenario_rows)
    write_csv(args.output / "passos.csv", STEP_COLUMNS, step_rows)
    print(
        f"[CSV] {len(scenario_rows)} cenários e {len(step_rows)} passos "
        f"exportados em {args.output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
