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
    "CAR": "Carrinho",
    "CAT": "Catálogo",
    "CHK": "Checkout",
    "IDT": "Identidade e Conta",
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

    for index, value in enumerate(headers):
        cell = table.rows[0].cells[index]
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(normalize(value))
        run.bold = True
        shade(cell)

    for row in rows:
        cells = table.add_row().cells
        for index, value in enumerate(row):
            cells[index].text = normalize(value)
            cells[index].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP

    if widths:
        for row in table.rows:
            for index, width in enumerate(widths):
                row.cells[index].width = Inches(width)

    doc.add_paragraph()


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
        return f'Navegar para "{action.get("route", "")}".'
    if typ == "FILL":
        return f'Preencher "{target_name}" com o valor definido pelo cenário.'
    if typ == "CLICK":
        return f'Acionar "{target_name}".'
    if typ == "SELECT":
        return f'Selecionar "{action.get("value", "")}" em "{target_name}".'
    if typ == "PRESS":
        return f'Pressionar "{action.get("key", "Enter")}" em "{target_name}".'
    if typ == "CHECK":
        return f'Marcar "{target_name}".'
    if typ == "UNCHECK":
        return f'Desmarcar "{target_name}".'
    if typ == "WAIT":
        return f'Aguardar {action.get("milliseconds", 0)} ms para estabilização.'
    if typ == "ASSERT_ENABLED":
        return f'Verificar se "{target_name}" está habilitado.'
    if typ == "ASSERT_DISABLED":
        return f'Verificar se "{target_name}" está desabilitado.'
    if typ == "ASSERT_SELECTED":
        return f'Verificar se "{target_name}" está selecionado.'
    return f'Executar a ação "{typ}".'


def expected_description(expected: dict[str, Any]) -> str:
    parts = []
    if expected.get("url_contains"):
        parts.append(f'a URL contenha "{expected["url_contains"]}"')
    if expected.get("text_contains"):
        values = ", ".join(f'"{item}"' for item in expected["text_contains"])
        parts.append(f'o texto observado contenha {values}')
    if expected.get("text_not_contains"):
        values = ", ".join(f'"{item}"' for item in expected["text_not_contains"])
        parts.append(f'o texto observado não contenha {values}')
    if expected.get("status"):
        parts.append(f'o status observado seja "{expected["status"]}"')
    if expected.get("state"):
        parts.append(f'o estado observado seja "{expected["state"]}"')
    return " e ".join(parts) or "o critério de aceite definido no catálogo seja atendido."


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
            args, cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
        return value or default
    except Exception:
        return default


def load_environment(path: Path) -> dict[str, str]:
    env = {
        "Projeto": "Juice Shop Execution",
        "Aplicação": "OWASP Juice Shop",
        "Versão da imagem": "bkimminich/juice-shop:v20.3.0",
        "URL base": "http://127.0.0.1:3000",
        "Executor": "Playwright / Chromium",
        "Python": "3.10+ (recomendado 3.12)",
        "Docker": "Docker Desktop / Docker Engine + Compose v2",
        "Branch": git_value(["git", "branch", "--show-current"], "não disponível"),
        "Commit": git_value(["git", "rev-parse", "--short", "HEAD"], "não disponível"),
        "Gerado em": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }
    if path.exists():
        try:
            custom = json.loads(path.read_text(encoding="utf-8"))
            env.update({str(k): str(v) for k, v in custom.items()})
        except (OSError, json.JSONDecodeError):
            pass
    return env


def configure_document(doc: Document) -> None:
    section = doc.sections[0]
    section.top_margin = Inches(0.65)
    section.bottom_margin = Inches(0.65)
    section.left_margin = Inches(0.65)
    section.right_margin = Inches(0.65)

    styles = doc.styles
    styles["Normal"].font.name = "Aptos"
    styles["Normal"].font.size = Pt(10)
    styles["Title"].font.name = "Aptos Display"
    styles["Title"].font.size = Pt(24)
    styles["Heading 1"].font.name = "Aptos Display"
    styles["Heading 1"].font.size = Pt(16)
    styles["Heading 1"].font.bold = True
    styles["Heading 2"].font.name = "Aptos Display"
    styles["Heading 2"].font.size = Pt(13)
    styles["Heading 2"].font.bold = True
    styles["Heading 3"].font.name = "Aptos Display"
    styles["Heading 3"].font.size = Pt(11)
    styles["Heading 3"].font.bold = True


def add_cover(doc: Document, title: str, subtitle: str) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("JUICE SHOP EXECUTION")
    run.bold = True
    run.font.size = Pt(13)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(title)
    run.bold = True
    run.font.size = Pt(25)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run(subtitle).font.size = Pt(12)
    doc.add_page_break()


def add_environment(doc: Document, env: dict[str, str]) -> None:
    doc.add_heading("Ficha de Ambiente", level=1)
    add_table(doc, ["Item", "Configuração"], [[key, value] for key, value in env.items()])
    doc.add_paragraph(
        "Os dados desta ficha representam o contexto técnico disponível para a execução. "
        "Campos ausentes nos artefatos permanecem como não registrados."
    )


def status_label(execution: dict[str, Any] | None) -> str:
    return str((execution or {}).get("status") or "NÃO EXECUTADO").upper()


def status_is_passed(execution: dict[str, Any] | None) -> bool:
    return bool(execution and status_label(execution) == "PASSED")


def observed_result(execution: dict[str, Any]) -> str:
    return normalize(_observed_behavior(execution), 2600)


def observed_messages(execution: dict[str, Any]) -> str:
    messages = _observed_messages(execution)
    return " | ".join(messages[:10]) if messages else "Nenhuma mensagem transitória relevante capturada."


def observed_data(scenario: dict[str, Any], execution: dict[str, Any]) -> str:
    return normalize(_observed_data(execution, scenario), 2200)


def add_execution_summary(doc: Document, scenario: dict[str, Any], execution: dict[str, Any] | None) -> None:
    doc.add_heading("Resumo da execução real", level=3)

    if not execution:
        doc.add_paragraph(
            "Não foi localizado JSON de execução para este cenário. "
            "A ausência de evidência não é convertida em aprovação."
        )
        return

    validation = execution.get("validation") or {}
    add_table(
        doc,
        ["Campo", "Valor observado"],
        [
            ["Status", status_label(execution)],
            ["URL final", execution.get("final_url") or "Não registrada."],
            ["Resultado observado", observed_result(execution)],
            ["Validação", validation.get("message") or "Não registrada."],
            ["Validação aprovada", "Sim" if validation.get("passed") else "Não"],
            ["Mensagens exibidas", observed_messages(execution)],
            ["Dados observados", observed_data(scenario, execution)],
        ],
    )


def add_execution_steps(doc: Document, execution: dict[str, Any]) -> None:
    steps = execution.get("steps") or []
    doc.add_heading("Passos Executados", level=3)

    if not steps:
        doc.add_paragraph("O JSON de execução não contém passos registrados.")
        return

    rows = []
    for step in steps:
        response = normalize(step.get("observed_result") or "")
        if step.get("error"):
            response = f"Falha de automação: {normalize(step.get('error'))}"

        rows.append([
            str(step.get("step", "")),
            normalize(step.get("user_action") or step.get("action")),
            normalize(step.get("data") or "—", 500),
            response or "Nenhuma resposta observável registrada.",
        ])

    add_table(
        doc,
        ["#", "Ação do usuário", "Dados informados", "Resposta da interface"],
        rows,
        widths=[0.35, 2.05, 1.45, 3.25],
    )


def add_step_evidence(doc: Document, step: dict[str, Any]) -> None:
    step_no = step.get("step", "?")
    doc.add_heading(
        f"Passo {step_no} — {normalize(step.get('user_action') or step.get('action'))}",
        level=4,
    )

    before_url = normalize(step.get("url_before"))
    after_url = normalize(step.get("url_after"))
    before_text = normalize(step.get("visible_text_before"), 1800)
    after_text = normalize(step.get("visible_text_after"), 1800)
    messages = step.get("messages") or []
    controls = step.get("controls") or []

    add_table(
        doc,
        ["Evidência", "Registro"],
        [
            ["Ação técnica", step.get("action", "")],
            ["URL antes", before_url or "Não registrada."],
            ["URL depois", after_url or "Não registrada."],
            ["Mudança detectada", "Sim" if step.get("changed") else "Não"],
            ["Execução do passo", "Sucesso" if step.get("success") else "Falha"],
            ["Resultado observado", step.get("observed_result") or "Não registrado."],
            ["Mensagens", " | ".join(map(str, messages)) or "Nenhuma."],
            ["Erro", step.get("error") or "Nenhum erro registrado."],
        ],
    )

    if before_text:
        doc.add_paragraph(f"Estado antes: {before_text}")
    if after_text:
        doc.add_paragraph(f"Estado depois: {after_text}")

    if controls:
        doc.add_paragraph(
            "Controles semânticos: "
            + " | ".join(normalize(item) for item in controls[:30])
        )

    screenshot = step.get("screenshot")
    if screenshot:
        path = Path(str(screenshot))
        if not path.is_absolute():
            path = ROOT / path
        if path.exists():
            try:
                doc.add_picture(str(path), width=Inches(6.4))
            except Exception as exc:
                doc.add_paragraph(f"Evidência visual registrada, mas não incorporada: {exc}")
        else:
            doc.add_paragraph(
                f"Evidência visual registrada no JSON, mas o arquivo não está disponível: {screenshot}"
            )


def add_scenario(doc: Document, scenario: dict[str, Any], execution: dict[str, Any] | None) -> None:
    doc.add_heading(f"{scenario['id']} — {scenario['name']}", level=2)

    add_table(
        doc,
        ["Campo", "Descrição"],
        [
            ["Domínio", f"{scenario.get('domain', '')} — {DOMAINS.get(scenario.get('domain', ''), '')}"],
            ["Ator", scenario.get("actor", "")],
            ["Status da execução", status_label(execution)],
            ["Fluxo", scenario.get("flow", "")],
            ["Pré-condição", scenario.get("precondition", "")],
            ["Resultado observado", observed_result(execution) if execution else "Não registrado."],
            ["Mensagens exibidas", observed_messages(execution) if execution else "Não registradas."],
            ["Dados manipulados", observed_data(scenario, execution) if execution else scenario.get("data", "")],
            ["Coerente com a aplicação", scenario.get("coherent", "")],
            ["Justificativa", scenario.get("justification", "")],
            ["Requisito candidato", scenario.get("requirement", "")],
        ],
    )

    doc.add_heading("Descrição funcional", level=3)
    if execution:
        doc.add_paragraph(
            f"O cenário foi executado pelo ator '{scenario.get('actor', 'não informado')}'. "
            f"A descrição abaixo é baseada no comportamento efetivamente observado: "
            f"{observed_result(execution)}"
        )
    else:
        doc.add_paragraph(
            f"O cenário verifica o fluxo '{scenario.get('flow', '')}' definido no catálogo. "
            "Não há evidência de execução disponível para complementar a descrição."
        )

    doc.add_heading("Critério de aceite", level=3)
    doc.add_paragraph(expected_description(scenario.get("expected", {})))

    doc.add_heading("Procedimento previsto no catálogo", level=3)
    for index, action in enumerate(scenario.get("actions", []), start=1):
        doc.add_paragraph(f"{index}. {action_description(action)}")

    if execution:
        add_execution_summary(doc, scenario, execution)
        add_execution_steps(doc, execution)

        doc.add_heading("Evidências detalhadas", level=3)
        for step in execution.get("steps") or []:
            add_step_evidence(doc, step)

        doc.add_heading("Conclusão do cenário", level=3)
        if status_is_passed(execution):
            doc.add_paragraph(
                "Cenário aprovado. O status PASSED foi sustentado pela execução e pela validação "
                "dos estados observáveis registrados nos artefatos."
            )
        else:
            doc.add_paragraph(
                "Cenário não aprovado. O status e as evidências acima representam o resultado efetivamente registrado."
            )


def create_domain_doc(
    scenarios: list[dict[str, Any]],
    domain: str,
    env: dict[str, str],
    executions: dict[str, dict[str, Any]],
    out: Path,
) -> None:
    selected = [scenario for scenario in scenarios if scenario.get("domain") == domain]
    doc = Document()
    configure_document(doc)
    add_cover(doc, f"Relatório de Execução — {domain}", DOMAINS.get(domain, domain))

    doc.add_heading("1. Identificação", level=1)
    add_table(
        doc,
        ["Item", "Valor"],
        [
            ["Domínio", f"{domain} — {DOMAINS.get(domain, domain)}"],
            ["Cenários no catálogo", str(len(selected))],
            ["Cenários com execução", str(sum(s["id"] in executions for s in selected))],
            ["Aprovados", str(sum(status_is_passed(executions.get(s["id"])) for s in selected))],
            ["Não aprovados", str(sum(bool(executions.get(s["id"])) and not status_is_passed(executions.get(s["id"])) for s in selected))],
        ],
    )

    add_environment(doc, env)

    doc.add_heading("2. Resumo dos cenários", level=1)
    rows = []
    for scenario in selected:
        execution = executions.get(scenario["id"])
        rows.append([
            scenario["id"],
            scenario["name"],
            scenario.get("actor", ""),
            status_label(execution),
            execution.get("final_url", "") if execution else "Não executado.",
        ])
    add_table(doc, ["ID", "Cenário", "Ator", "Status", "URL final observada"], rows)

    doc.add_heading("3. Detalhamento dos cenários", level=1)
    for scenario in selected:
        add_scenario(doc, scenario, executions.get(scenario["id"]))

    doc.save(out / f"{domain}_relatorio.docx")


def create_general_doc(
    scenarios: list[dict[str, Any]],
    env: dict[str, str],
    executions: dict[str, dict[str, Any]],
    out: Path,
) -> None:
    doc = Document()
    configure_document(doc)
    add_cover(doc, "Relatório Geral de Execução", "OWASP Juice Shop — Suíte completa")

    passed = sum(status_is_passed(executions.get(s["id"])) for s in scenarios)
    executed = sum(s["id"] in executions for s in scenarios)
    not_passed = sum(bool(executions.get(s["id"])) and not status_is_passed(executions.get(s["id"])) for s in scenarios)

    doc.add_heading("1. Identificação da execução", level=1)
    add_table(
        doc,
        ["Indicador", "Resultado"],
        [
            ["Cenários no catálogo", str(len(scenarios))],
            ["Cenários executados", str(executed)],
            ["Aprovados", str(passed)],
            ["Não aprovados", str(not_passed)],
            ["Sem artefato de execução", str(len(scenarios) - executed)],
        ],
    )

    add_environment(doc, env)

    doc.add_heading("2. Resultado por domínio", level=1)
    rows = []
    for code, name in DOMAINS.items():
        selected = [s for s in scenarios if s.get("domain") == code]
        if not selected:
            continue
        executed_domain = sum(s["id"] in executions for s in selected)
        passed_domain = sum(status_is_passed(executions.get(s["id"])) for s in selected)
        rows.append([code, name, str(len(selected)), str(executed_domain), f"{passed_domain}/{len(selected)}"])
    add_table(doc, ["Código", "Domínio", "Catálogo", "Executados", "Aprovados"], rows)

    doc.add_heading("3. Integridade documental", level=1)
    doc.add_paragraph(
        "Os dados de catálogo descrevem intenção, fluxo e critério de aceite. "
        "Os campos de resultado, mensagens, dados observados, URLs e respostas da interface "
        "são derivados dos artefatos reais de execução. A ausência de evidência não é convertida em aprovação."
    )

    doc.add_heading("4. Detalhamento por domínio", level=1)
    for code, name in DOMAINS.items():
        selected = [s for s in scenarios if s.get("domain") == code]
        if not selected:
            continue
        doc.add_heading(f"{code} — {name}", level=2)
        for scenario in selected:
            add_scenario(doc, scenario, executions.get(scenario["id"]))

    doc.save(out / "JUICE_SHOP_RELATORIO_GERAL.docx")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Gera DOCX por domínio e relatório geral a partir do catálogo e das evidências reais."
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

    extras = sorted(set(extras))
    env = load_environment(args.environment)
    args.output.mkdir(parents=True, exist_ok=True)

    domains = sorted({str(item.get("domain")) for item in scenarios if item.get("domain")})
    for domain in domains:
        create_domain_doc(scenarios, domain, env, executions, args.output)
    create_general_doc(scenarios, env, executions, args.output)

    print(
        f"[DOCX] {len(domains)} relatórios por domínio + 1 relatório geral gerados em {args.output}"
    )
    print(f"[DOCX] evidências válidas encontradas: {len(executions)}/{len(scenarios)} cenários")
    if extras:
        print(f"[DOCX] artefatos extras ignorados: {len(extras)} ({', '.join(extras)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
