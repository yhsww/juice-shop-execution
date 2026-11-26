from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

from reporting.report import _observed_behavior, _observed_data, _observed_messages

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCENARIOS = ROOT / "scenarios" / "scenarios.json"
DEFAULT_EXECUTIONS = ROOT / "reports" / "executions"
DEFAULT_OUT = ROOT / "reports" / "docx"
DEFAULT_ENV = ROOT / ".report-environment.json"

DOMAINS = {
    "ADM": "Administração",
    "CAR": "Carrinho de Compras",
    "CAT": "Catálogo",
    "CHK": "Checkout e Pedidos",
    "IDT": "Gestão de Identidade e Usuários",
    "PER": "Perfil",
}


def normalize(value: Any, limit: int | None = None) -> str:
    text = " ".join(str(value or "").split()).strip()
    if limit and len(text) > limit:
        return text[: limit - 1] + "…"
    return text


def shade(cell, fill: str = "D9EAF7") -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def repeat_header(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    tr_pr.append(el)


def add_table(
    doc: Document,
    headers: list[str],
    rows: list[list[str]],
    widths: list[float] | None = None,
) -> None:
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    repeat_header(table.rows[0])

    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(normalize(header))
        run.bold = True
        shade(cell)

    for row in rows:
        cells = table.add_row().cells
        for i, value in enumerate(row):
            cells[i].text = normalize(value)
            cells[i].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP

    if widths:
        for row in table.rows:
            for i, width in enumerate(widths):
                row.cells[i].width = Inches(width)

    doc.add_paragraph()


def configure_document(doc: Document) -> None:
    section = doc.sections[0]
    section.top_margin = Inches(0.65)
    section.bottom_margin = Inches(0.65)
    section.left_margin = Inches(0.65)
    section.right_margin = Inches(0.65)

    styles = doc.styles
    styles["Normal"].font.name = "Aptos"
    styles["Normal"].font.size = Pt(10)
    for name, size in (("Heading 1", 15), ("Heading 2", 13), ("Heading 3", 11)):
        styles[name].font.name = "Aptos Display"
        styles[name].font.size = Pt(size)
        styles[name].font.bold = True


def load_scenarios(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("scenarios", payload if isinstance(payload, list) else [])


def load_executions(
    directory: Path,
    valid_ids: set[str],
) -> tuple[dict[str, dict[str, Any]], list[str]]:
    executions: dict[str, dict[str, Any]] = {}
    extras: list[str] = []

    if not directory.exists():
        return executions, extras

    for path in sorted(directory.glob("*.json")):
        if path.name.startswith("_"):
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue

        scenario_id = str(payload.get("scenario_id") or path.stem)
        if scenario_id not in valid_ids:
            extras.append(scenario_id)
            continue

        executions[scenario_id] = payload

    return executions, sorted(set(extras))


def git_value(args: list[str], default: str) -> str:
    try:
        value = subprocess.check_output(
            args,
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        return value or default
    except Exception:
        return default


def load_environment(path: Path) -> dict[str, str]:
    # Estrutura intencionalmente igual à Ficha de Ambiente do modelo fornecido.
    env = {
        "Avaliador e data": datetime.now().strftime("%d/%m/%Y"),
        "Versão do Juice Shop": "v20.3.0",
        "Sistema operacional": "Windows",
    }

    if path.exists():
        try:
            custom = json.loads(path.read_text(encoding="utf-8"))
            if custom.get("Avaliador e data"):
                env["Avaliador e data"] = str(custom["Avaliador e data"])
            if custom.get("Versão do Juice Shop"):
                env["Versão do Juice Shop"] = str(custom["Versão do Juice Shop"])
            if custom.get("Sistema operacional"):
                env["Sistema operacional"] = str(custom["Sistema operacional"])
        except (OSError, json.JSONDecodeError):
            pass

    return env


def action_description(action: dict[str, Any]) -> str:
    typ = str(action.get("type", "")).upper()
    target = action.get("target") or {}
    target_name = (
        target.get("name")
        or target.get("label")
        or target.get("text")
        or target.get("role")
        or "elemento"
    )

    if typ == "NAVIGATE":
        return f'Navegar para "{action.get("route", "")}"'
    if typ == "FILL":
        return f'Preencher "{target_name}"'
    if typ == "CLICK":
        return f'Clicar em "{target_name}"'
    if typ == "SELECT":
        return f'Selecionar "{action.get("value", "")}" em "{target_name}"'
    if typ == "PRESS":
        return f'Pressionar "{action.get("key", "Enter")}" em "{target_name}"'
    if typ == "CHECK":
        return f'Marcar "{target_name}"'
    if typ == "UNCHECK":
        return f'Desmarcar "{target_name}"'
    if typ == "WAIT":
        return f'Aguardar a estabilização da interface'
    if typ == "ASSERT_ENABLED":
        return f'Verificar se "{target_name}" está habilitado'
    if typ == "ASSERT_DISABLED":
        return f'Verificar se "{target_name}" está desabilitado'
    if typ == "ASSERT_SELECTED":
        return f'Verificar se "{target_name}" está selecionado'
    return f'Executar a ação "{typ}"'


def observed_result(execution: dict[str, Any] | None) -> str:
    if not execution:
        return "Execução não localizada."

    value = normalize(_observed_behavior(execution), 3200)
    return value or "Nenhum resultado observável foi registrado."


def observed_messages(execution: dict[str, Any] | None) -> str:
    if not execution:
        return "Não registrado."

    messages = _observed_messages(execution)
    return " ".join(messages[:10]) if messages else "Nenhuma mensagem relevante registrada."


def observed_data(scenario: dict[str, Any], execution: dict[str, Any] | None) -> str:
    if not execution:
        return "Não registrado."

    # Prioriza os dados realmente registrados durante a execução.
    runtime_values: list[str] = []
    for step in execution.get("steps", []):
        value = normalize(step.get("data"))
        if value:
            runtime_values.append(value)

    if runtime_values:
        unique: list[str] = []
        seen: set[str] = set()
        for value in runtime_values:
            key = value.casefold()
            if key not in seen:
                seen.add(key)
                unique.append(value)
        return " ".join(unique)[:2600]

    return normalize(scenario.get("data")) or "Nenhum dado informado."


def add_environment(doc: Document, env: dict[str, str]) -> None:
    doc.add_heading("Ficha de Ambiente", level=1)
    add_table(
        doc,
        ["Campo", "Informação"],
        [
            ["Avaliador e data", env["Avaliador e data"]],
            ["Versão do Juice Shop", env["Versão do Juice Shop"]],
            ["Sistema operacional", env["Sistema operacional"]],
        ],
        widths=[2.6, 4.7],
    )


def add_domain_header(doc: Document, domain: str) -> None:
    doc.add_heading(
        f"Guia de Domínio: {domain} — {DOMAINS.get(domain, domain)}",
        level=1,
    )


def add_scenario(doc: Document, scenario: dict[str, Any], execution: dict[str, Any] | None) -> None:
    # Estrutura mantida na mesma ordem e com os mesmos campos do modelo fornecido.
    doc.add_heading("Ficha de Cenário", level=2)

    domain = str(scenario.get("domain") or "")
    rows = [
        ["ID do cenário", scenario.get("id", "")],
        ["Domínio", f"{domain} — {DOMAINS.get(domain, '')}".strip(" —")],
        ["Nome do cenário", scenario.get("name", "")],
        ["Ator", scenario.get("actor", "")],
        ["Fluxo", scenario.get("flow", "")],
        ["Pré-condição (estado inicial)", scenario.get("precondition", "")],
        ["Resultado observado (mudança de estado)", observed_result(execution)],
        ["Mensagens exibidas ao usuário", observed_messages(execution)],
        ["Dados manipulados", observed_data(scenario, execution)],
        ["Coerente com loja de sucos?", scenario.get("coherent", "") or "Sim"],
        ["Justificativa", scenario.get("justification", "")],
        ["Requisito candidato (opcional)", scenario.get("requirement", "")],
    ]

    add_table(
        doc,
        ["Campo", "Informação"],
        rows,
        widths=[2.6, 4.7],
    )

    # Exatamente como no modelo: tabela imediatamente vinculada à ficha.
    doc.add_heading("Passos Executados (Tabela anexa à ficha de cenário)", level=2)

    step_rows: list[list[str]] = []
    if execution:
        for step in execution.get("steps", []):
            response = normalize(step.get("observed_result"))
            if not response or "Nenhuma mudança visual relevante detectada." in response:
                response = "Nenhuma resposta adicional registrada."

            if step.get("error"):
                response = f"Falha durante a execução: {normalize(step.get('error'))}"

            step_rows.append(
                [
                    str(step.get("step", "")),
                    normalize(step.get("user_action") or step.get("action")),
                    normalize(step.get("data")) or "—",
                    response,
                ]
            )

    if not step_rows:
        # Não inventa uma execução quando o artefato não existe.
        step_rows.append(
            ["—", "Nenhum passo executado registrado.", "—", "Evidência não registrada."]
        )

    add_table(
        doc,
        ["#", "Ação do usuário", "Dados informados", "Resposta da interface"],
        step_rows,
        widths=[0.35, 2.55, 1.55, 2.85],
    )

    # As capturas continuam sendo preservadas, mas sem criar uma nova seção
    # ou alterar a estrutura textual do modelo.
    if execution:
        for step in execution.get("steps", []):
            screenshot = step.get("screenshot")
            if not screenshot:
                continue
            path = Path(str(screenshot))
            if not path.is_absolute():
                path = ROOT / path
            if path.exists():
                try:
                    p = doc.add_paragraph()
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p.add_run().add_picture(str(path), width=Inches(6.5))
                except Exception:
                    pass


def create_document(
    scenarios: list[dict[str, Any]],
    env: dict[str, str],
    executions: dict[str, dict[str, Any]],
    out: Path,
    domains: list[str],
    filename: str,
) -> None:
    doc = Document()
    configure_document(doc)

    add_environment(doc, env)

    for index, domain in enumerate(domains):
        if index:
            doc.add_page_break()

        add_domain_header(doc, domain)

        selected = [
            scenario
            for scenario in scenarios
            if str(scenario.get("domain", "")).upper() == domain
        ]

        for scenario_index, scenario in enumerate(selected):
            if scenario_index:
                doc.add_page_break()
            add_scenario(doc, scenario, executions.get(str(scenario.get("id"))))

    doc.save(out / filename)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Gera DOCX seguindo estritamente a estrutura da Etapa 1."
    )
    parser.add_argument("--scenarios", type=Path, default=DEFAULT_SCENARIOS)
    parser.add_argument("--executions", type=Path, default=DEFAULT_EXECUTIONS)
    parser.add_argument("--results", type=Path, default=None)
    parser.add_argument("--environment", type=Path, default=DEFAULT_ENV)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    scenarios = load_scenarios(args.scenarios)
    valid_ids = {str(item.get("id")) for item in scenarios if item.get("id")}
    executions, extras = load_executions(args.executions, valid_ids)

    # Compatibilidade com --results, sem substituir evidência já registrada.
    if args.results and args.results.exists():
        try:
            payload = json.loads(args.results.read_text(encoding="utf-8"))
            items = payload.get("results", payload) if isinstance(payload, dict) else payload
            if isinstance(items, list):
                for item in items:
                    sid = str(item.get("scenario_id") or item.get("id") or "")
                    if sid in valid_ids and sid not in executions:
                        executions[sid] = item
                    elif sid and sid not in valid_ids:
                        extras.append(sid)
        except (OSError, json.JSONDecodeError):
            pass

    env = load_environment(args.environment)
    args.output.mkdir(parents=True, exist_ok=True)

    domains = sorted(
        {str(item.get("domain")).upper() for item in scenarios if item.get("domain")}
    )

    # Um documento por domínio, mantendo a mesma ficha/estrutura do modelo.
    for domain in domains:
        create_document(
            scenarios,
            env,
            executions,
            args.output,
            [domain],
            f"{domain}_relatorio.docx",
        )

    # Documento geral: mesma estrutura, apenas reunindo os domínios.
    create_document(
        scenarios,
        env,
        executions,
        args.output,
        domains,
        "JUICE_SHOP_RELATORIO_GERAL.docx",
    )

    print(
        f"[DOCX] {len(domains)} relatórios por domínio + 1 relatório geral gerados em {args.output}"
    )
    print(
        f"[DOCX] evidências válidas encontradas: {len(executions)}/{len(scenarios)} cenários"
    )

    extras = sorted(set(extras))
    if extras:
        print(
            f"[DOCX] artefatos extras ignorados: {len(extras)} ({', '.join(extras)})"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
