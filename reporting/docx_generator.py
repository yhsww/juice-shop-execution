from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

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


def set_cell_shading(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def set_repeat_table_header(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    tr_pr.append(el)


def add_table(doc: Document, headers: list[str], rows: list[list[str]]) -> None:
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"
    header = table.rows[0]
    set_repeat_table_header(header)
    for index, value in enumerate(headers):
        cell = header.cells[index]
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        paragraph = cell.paragraphs[0]
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = paragraph.add_run(normalize(value))
        run.bold = True
        set_cell_shading(cell, "D9EAF7")
    for row in rows:
        cells = table.add_row().cells
        for index, value in enumerate(row):
            cells[index].text = normalize(value)
            cells[index].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
    doc.add_paragraph()
    return table


def add_text(doc: Document, label: str, value: Any) -> None:
    paragraph = doc.add_paragraph()
    run = paragraph.add_run(f"{label}: ")
    run.bold = True
    paragraph.add_run(normalize(value) or "Não registrado.")


def action_description(action: dict[str, Any]) -> str:
    typ = str(action.get("type", "")).upper()
    target = action.get("target") or {}
    parts = []
    for key in ("role", "name", "label", "text"):
        if target.get(key) is not None:
            parts.append(f'{key}="{target[key]}"')
    target_text = ", ".join(parts) or "alvo não especificado"
    if target.get("exact") is not None:
        target_text += f', correspondência={"exata" if target["exact"] else "parcial"}'

    if typ == "NAVIGATE":
        return f'Navegar para a rota "{action.get("route", "")}".'
    if typ == "FILL":
        return f'Preencher {target_text} com o valor definido pelo cenário.'
    if typ == "CLICK":
        return f'Acionar {target_text}.'
    if typ == "WAIT":
        return f'Aguardar {action.get("milliseconds", 0)} ms para estabilização da interface.'
    if typ == "PRESS":
        return f'Pressionar "{action.get("key", "")}" em {target_text}.'
    if typ == "SELECT":
        return f'Selecionar "{action.get("value", "")}" em {target_text}.'
    if typ == "CLICK_ALL":
        return f'Acionar os elementos {target_text}, respeitando o limite de {action.get("max_clicks", "não informado")} interações.'
    return f'Executar a ação "{typ}" com os parâmetros definidos no catálogo.'


def expected_description(expected: dict[str, Any]) -> str:
    parts = []
    if expected.get("url_contains"):
        parts.append(f'a URL contenha "{expected["url_contains"]}"')
    if expected.get("text_contains"):
        values = ", ".join(f'"{x}"' for x in expected["text_contains"])
        parts.append(f'o texto observado contenha {values}')
    if expected.get("text_not_contains"):
        values = ", ".join(f'"{x}"' for x in expected["text_not_contains"])
        parts.append(f'o texto observado não contenha {values}')
    if expected.get("status"):
        parts.append(f'o status observado seja "{expected["status"]}"')
    if expected.get("state"):
        parts.append(f'o estado observado seja "{expected["state"]}"')
    return " e ".join(parts) or "o critério de aceite definido no catálogo seja atendido."


def load_scenarios(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("scenarios", payload if isinstance(payload, list) else [])


def load_executions(directory: Path) -> dict[str, dict[str, Any]]:
    executions: dict[str, dict[str, Any]] = {}
    if not directory.exists():
        return executions
    for path in sorted(directory.glob("*.json")):
        if path.name.startswith("_"):
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        scenario_id = str(payload.get("scenario_id") or path.stem)
        executions[scenario_id] = payload
    return executions


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
    styles["Heading 2"].font.name = "Aptos Display"
    styles["Heading 2"].font.size = Pt(13)
    styles["Heading 3"].font.name = "Aptos Display"
    styles["Heading 3"].font.size = Pt(11)


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


def add_environment_sheet(doc: Document, env: dict[str, str]) -> None:
    doc.add_heading("Ficha de Ambiente", level=1)
    add_table(doc, ["Item", "Configuração"], [[k, v] for k, v in env.items()])
    doc.add_paragraph(
        "Os dados desta ficha representam o contexto técnico disponível para a execução. "
        "Campos ausentes nos artefatos permanecem como não registrados; não são criados valores "
        "de evidência pelo gerador."
    )


def status_label(execution: dict[str, Any] | None) -> str:
    if not execution:
        return "NÃO EXECUTADO"
    return str(execution.get("status") or "NÃO INFORMADO").upper()


def status_is_passed(execution: dict[str, Any] | None) -> bool:
    return bool(execution and str(execution.get("status", "")).upper() == "PASSED")


def add_execution_summary(doc: Document, execution: dict[str, Any] | None) -> None:
    if not execution:
        doc.add_heading("Evidência de execução", level=3)
        doc.add_paragraph(
            "Não foi localizado JSON de execução para este cenário. "
            "O gerador documenta o catálogo, mas não transforma a ausência de evidência em aprovação."
        )
        return

    validation = execution.get("validation") or {}
    doc.add_heading("Resumo da execução real", level=3)
    add_table(
        doc,
        ["Campo", "Valor observado"],
        [
            ["Status", status_label(execution)],
            ["URL final", execution.get("final_url") or "Não registrado."],
            ["Resultado final", execution.get("final_result") or "Não registrado."],
            ["Validação", validation.get("message") or "Não registrada."],
            ["Validação aprovada", "Sim" if validation.get("passed") else "Não"],
            ["Mensagens", " | ".join(execution.get("messages") or []) or "Nenhuma registrada."],
            ["Resumo de rede", execution.get("network_summary") or "Não registrado."],
        ],
    )

    final_text = normalize(execution.get("final_visible_text"), 5000)
    if final_text:
        doc.add_heading("Texto visível no estado final", level=3)
        doc.add_paragraph(final_text)


def add_step_evidence(doc: Document, step: dict[str, Any]) -> None:
    step_no = step.get("step", "?")
    action = step.get("action", step.get("user_action", ""))
    user_action = step.get("user_action", "")
    data = step.get("data", "")
    before_url = step.get("url_before", "")
    after_url = step.get("url_after", "")
    before_text = normalize(step.get("visible_text_before"), 2500)
    after_text = normalize(step.get("visible_text_after"), 2500)
    observed = step.get("observed_result", "")
    error = step.get("error", "")
    changed = step.get("changed")
    success = step.get("success")
    screenshot = step.get("screenshot")
    network = step.get("network_summary", "")
    controls = step.get("controls") or []
    messages = step.get("messages") or []

    doc.add_heading(f"Passo {step_no} — {normalize(user_action or action)}", level=3)

    add_table(
        doc,
        ["Evidência", "Registro"],
        [
            ["Ação técnica", action],
            ["Ação do usuário", user_action],
            ["Dados", data],
            ["URL antes", before_url],
            ["URL depois", after_url],
            ["Mudança detectada", "Sim" if changed else "Não"],
            ["Execução do passo", "Sucesso" if success else "Falha"],
            ["Resultado observado", observed],
            ["Erro", error or "Nenhum erro registrado."],
            ["Mensagens", " | ".join(str(x) for x in messages) or "Nenhuma."],
            ["Resumo de rede", network or "Não registrado."],
        ],
    )

    if before_text:
        doc.add_heading("Estado visível antes da ação", level=4)
        doc.add_paragraph(before_text)
    if after_text:
        doc.add_heading("Estado visível depois da ação", level=4)
        doc.add_paragraph(after_text)

    if controls:
        compact_controls = []
        for control in controls[:40]:
            if isinstance(control, dict):
                compact_controls.append(
                    " | ".join(
                        f"{key}={normalize(control.get(key))}"
                        for key in ("role", "name", "value", "checked")
                        if control.get(key) not in (None, "")
                    )
                )
            else:
                compact_controls.append(normalize(control))
        doc.add_heading("Controles semânticos capturados", level=4)
        doc.add_paragraph("\n".join(x for x in compact_controls if x) or "Nenhum controle registrado.")

    if screenshot:
        screenshot_path = Path(str(screenshot))
        if not screenshot_path.is_absolute():
            screenshot_path = ROOT / screenshot_path
        if screenshot_path.exists():
            doc.add_heading("Evidência visual", level=4)
            try:
                doc.add_picture(str(screenshot_path), width=Inches(6.4))
            except Exception as exc:
                doc.add_paragraph(f"Screenshot registrado em {screenshot_path}, mas não pôde ser incorporado: {exc}")
        else:
            doc.add_paragraph(f"Evidência visual registrada no artefato, mas o arquivo não está disponível: {screenshot}")


def add_scenario(doc: Document, scenario: dict[str, Any], execution: dict[str, Any] | None) -> None:
    sid = scenario["id"]
    status = status_label(execution)
    doc.add_heading(f"{sid} — {scenario['name']}", level=2)

    add_table(
        doc,
        ["Campo", "Descrição"],
        [
            ["Domínio", f"{scenario.get('domain', '')} — {DOMAINS.get(scenario.get('domain', ''), scenario.get('domain', ''))}"],
            ["Ator", scenario.get("actor", "")],
            ["Status da execução", status],
            ["Fluxo", scenario.get("flow", "")],
            ["Objetivo / requisito", scenario.get("requirement", "")],
            ["Pré-condição", scenario.get("precondition", "")],
            ["Dados de teste", scenario.get("data", "")],
            ["Justificativa", scenario.get("justification", "")],
            ["Coerência", scenario.get("coherent", "")],
            ["Critério de aceite", expected_description(scenario.get("expected", {}))],
        ],
    )

    doc.add_heading("Descrição funcional", level=3)
    doc.add_paragraph(
        f"O cenário verifica se o sistema permite que o ator '{scenario.get('actor', 'não informado')}' "
        f"execute o fluxo '{scenario.get('flow', '')}'. A finalidade funcional é atender ao requisito: "
        f"{scenario.get('requirement', '')}"
    )

    doc.add_heading("Procedimento previsto no catálogo", level=3)
    for index, action in enumerate(scenario.get("actions", []), start=1):
        doc.add_paragraph(f"{index}. {action_description(action)}")

    add_execution_summary(doc, execution)

    if execution:
        doc.add_heading("Evidência passo a passo", level=3)
        steps = execution.get("steps") or []
        if steps:
            for step in steps:
                add_step_evidence(doc, step)
        else:
            doc.add_paragraph("O JSON de execução não contém passos registrados.")

        doc.add_heading("Conclusão do cenário", level=3)
        if status == "PASSED":
            doc.add_paragraph(
                "O cenário foi aprovado pelo executor e pelo validador configurado. "
                "A conclusão é sustentada pelo status da execução e pela evidência registrada nos passos."
            )
        elif status in {"FAILED", "AUTOMATION_ERROR", "TIMEOUT"}:
            doc.add_paragraph(
                "O cenário não foi aprovado. A causa deve ser analisada a partir do status, "
                "da validação e dos passos/evidências registrados acima."
            )
        else:
            doc.add_paragraph("Não foi possível classificar a conclusão com base nos artefatos disponíveis.")


def create_domain_doc(
    scenarios: list[dict[str, Any]],
    domain: str,
    env: dict[str, str],
    executions: dict[str, dict[str, Any]],
    out: Path,
) -> None:
    selected = [s for s in scenarios if s.get("domain") == domain]
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
            ["Não aprovados", str(sum(
                bool(executions.get(s["id"])) and not status_is_passed(executions.get(s["id"]))
                for s in selected
            ))],
        ],
    )

    add_environment_sheet(doc, env)

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
    not_passed = sum(
        bool(executions.get(s["id"])) and not status_is_passed(executions.get(s["id"]))
        for s in scenarios
    )

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

    add_environment_sheet(doc, env)

    doc.add_heading("2. Resultado por domínio", level=1)
    rows = []
    for code, name in DOMAINS.items():
        selected = [s for s in scenarios if s.get("domain") == code]
        if not selected:
            continue
        executed_domain = sum(s["id"] in executions for s in selected)
        passed_domain = sum(status_is_passed(executions.get(s["id"])) for s in selected)
        rows.append([
            code,
            name,
            str(len(selected)),
            str(executed_domain),
            f"{passed_domain}/{len(selected)}",
        ])
    add_table(doc, ["Código", "Domínio", "Catálogo", "Executados", "Aprovados"], rows)

    doc.add_heading("3. Integridade documental", level=1)
    doc.add_paragraph(
        "Este relatório separa o que foi definido no catálogo do que foi realmente observado durante a execução. "
        "O campo expected é documentado como critério de aceite, mas não é usado como evidência. "
        "Quando um cenário não possui JSON de execução, ele permanece como NÃO EXECUTADO."
    )

    doc.add_heading("4. Detalhamento por domínio", level=1)
    for code, name in DOMAINS.items():
        selected = [s for s in scenarios if s.get("domain") == code]
        if not selected:
            continue
        doc.add_heading(f"{code} — {name}", level=2)
        for scenario in selected:
            add_scenario(doc, scenario, executions.get(scenario["id"]))

    doc.save(out / "AMBOLS_JUICE_SHOP_RELATORIO_GERAL.docx")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Gera DOCX por domínio e relatório geral a partir do catálogo e das evidências reais."
    )
    parser.add_argument("--scenarios", type=Path, default=DEFAULT_SCENARIOS)
    parser.add_argument(
        "--executions",
        type=Path,
        default=DEFAULT_EXECUTIONS,
        help="Diretório com reports/executions/*.json gerados pelo runner.",
    )
    parser.add_argument(
        "--results",
        type=Path,
        default=None,
        help="JSON adicional de resultados; usado somente para complementar a execução quando necessário.",
    )
    parser.add_argument("--environment", type=Path, default=DEFAULT_ENV)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    scenarios = load_scenarios(args.scenarios)
    executions = load_executions(args.executions)

    if args.results and args.results.exists():
        try:
            payload = json.loads(args.results.read_text(encoding="utf-8"))
            items = payload.get("results", payload) if isinstance(payload, dict) else payload
            if isinstance(items, list):
                for item in items:
                    sid = str(item.get("scenario_id") or item.get("id") or "")
                    if sid and sid not in executions:
                        executions[sid] = item
        except (OSError, json.JSONDecodeError):
            pass

    env = load_environment(args.environment)
    args.output.mkdir(parents=True, exist_ok=True)

    domains = sorted({str(s.get("domain")) for s in scenarios if s.get("domain")})
    for domain in domains:
        create_domain_doc(scenarios, domain, env, executions, args.output)
    create_general_doc(scenarios, env, executions, args.output)

    print(
        f"[DOCX] {len(domains)} relatórios por domínio + 1 relatório geral "
        f"gerados em {args.output}"
    )
    print(
        f"[DOCX] evidências encontradas: {len(executions)}/{len(scenarios)} cenários"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
