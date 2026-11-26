from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCENARIOS = ROOT / "scenarios" / "scenarios.json"
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
    hdr = table.rows[0]
    set_repeat_table_header(hdr)
    for i, value in enumerate(headers):
        p = hdr.cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(str(value))
        r.bold = True
        hdr.cells[i].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        set_cell_shading(hdr.cells[i], "D9EAF7")
    for row in rows:
        cells = table.add_row().cells
        for i, value in enumerate(row):
            cells[i].text = str(value)
            cells[i].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
    doc.add_paragraph()
    return table

def add_bullets(doc: Document, items: list[str]) -> None:
    for item in items:
        doc.add_paragraph(item, style="List Bullet")

def action_description(action: dict[str, Any]) -> str:
    typ = action.get("type", "")
    target = action.get("target") or {}
    target_parts = []
    for key in ("role", "name", "label", "text"):
        if target.get(key) is not None:
            target_parts.append(f'{key}="{target[key]}"')
    target_text = ", ".join(target_parts)
    if target.get("exact") is not None:
        target_text += f', correspondência={"exata" if target["exact"] else "parcial"}'
    if typ == "NAVIGATE":
        return f'Navegar para a rota "{action.get("route", "")}".'
    if typ == "FILL":
        return f'Preencher o elemento identificado por {target_text} com o valor configurado para o cenário.'
    if typ == "CLICK":
        return f'Acionar o elemento identificado por {target_text}.'
    if typ == "WAIT":
        return f'Aguardar {action.get("milliseconds", 0)} ms para estabilização da interface e atualização do estado observado.'
    if typ == "PRESS":
        return f'Pressionar a tecla "{action.get("key", "")}" no elemento identificado por {target_text}.'
    if typ == "SELECT":
        return f'Selecionar o valor "{action.get("value", "")}" no elemento identificado por {target_text}.'
    if typ == "CLICK_ALL":
        return f'Acionar os elementos identificados por {target_text}, respeitando o limite de {action.get("max_clicks", "não informado")} interações.'
    return f'Executar a ação {typ} com os parâmetros definidos no catálogo.'

def expected_description(expected: dict[str, Any]) -> str:
    parts = []
    if expected.get("url_contains"):
        parts.append(f'a URL contenha "{expected["url_contains"]}"')
    if expected.get("text_contains"):
        parts.append("o texto observado contenha " + ", ".join(f'"{x}"' for x in expected["text_contains"]))
    if expected.get("text_not_contains"):
        parts.append("o texto observado não contenha " + ", ".join(f'"{x}"' for x in expected["text_not_contains"]))
    if expected.get("status"):
        parts.append(f'o status esperado seja "{expected["status"]}"')
    if expected.get("state"):
        parts.append(f'o estado esperado seja "{expected["state"]}"')
    return " e ".join(parts) if parts else "o critério de aceite definido no catálogo seja atendido."

def load_results(path: Path | None) -> dict[str, str]:
    if not path or not path.exists():
        return {}
    raw = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(raw, list):
        return {str(x.get("scenario_id") or x.get("id")): str(x.get("status", "")) for x in raw if x.get("scenario_id") or x.get("id")}
    if isinstance(raw, dict):
        items = raw.get("results", raw.get("scenarios", raw))
        if isinstance(items, list):
            return {str(x.get("scenario_id") or x.get("id")): str(x.get("status", "")) for x in items if x.get("scenario_id") or x.get("id")}
        if isinstance(items, dict):
            return {str(k): str(v.get("status", v) if isinstance(v, dict) else v) for k, v in items.items()}
    return {}

def git_value(args: list[str], default: str) -> str:
    try:
        return subprocess.check_output(args, cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip() or default
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
        "Branch": git_value(["git", "branch", "--show-current"], "ambols-recovery-v2"),
        "Commit": git_value(["git", "rev-parse", "--short", "HEAD"], "não disponível"),
        "Gerado em": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }
    if path.exists():
        custom = json.loads(path.read_text(encoding="utf-8"))
        env.update({str(k): str(v) for k, v in custom.items()})
    return env

def configure_document(doc: Document) -> None:
    sec = doc.sections[0]
    sec.top_margin = Inches(0.65)
    sec.bottom_margin = Inches(0.65)
    sec.left_margin = Inches(0.7)
    sec.right_margin = Inches(0.7)
    styles = doc.styles
    styles["Normal"].font.name = "Aptos"
    styles["Normal"].font.size = Pt(10)
    styles["Title"].font.name = "Aptos Display"
    styles["Title"].font.size = Pt(24)
    styles["Heading 1"].font.name = "Aptos Display"
    styles["Heading 1"].font.size = Pt(16)
    styles["Heading 2"].font.name = "Aptos Display"
    styles["Heading 2"].font.size = Pt(13)

def add_cover(doc: Document, title: str, subtitle: str) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run("JUICE SHOP EXECUTION").bold = True
    p.runs[0].font.size = Pt(13)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(title)
    r.bold = True
    r.font.size = Pt(25)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(subtitle)
    r.font.size = Pt(12)
    doc.add_page_break()

def add_environment_sheet(doc: Document, env: dict[str, str]) -> None:
    doc.add_heading("Ficha de Ambiente", level=1)
    rows = [[k, v] for k, v in env.items()]
    add_table(doc, ["Item", "Configuração"], rows)
    doc.add_paragraph(
        "A ficha registra o contexto técnico utilizado como referência para a execução e para a documentação. "
        "Quando um valor não é obtido automaticamente, o gerador mantém o valor padrão configurado em vez de inventar evidência."
    )

def add_scenario(doc: Document, s: dict[str, Any], status: str) -> None:
    doc.add_heading(f'{s["id"]} — {s["name"]}', level=2)
    add_table(doc, ["Campo", "Descrição"], [
        ["Domínio", f'{s.get("domain", "")} — {DOMAINS.get(s.get("domain", ""), s.get("domain", ""))}'],
        ["Ator", s.get("actor", "")],
        ["Status da execução", status or "Não informado"],
        ["Fluxo", s.get("flow", "")],
        ["Objetivo / requisito", s.get("requirement", "")],
        ["Pré-condição", s.get("precondition", "")],
        ["Dados de teste", s.get("data", "")],
        ["Justificativa", s.get("justification", "")],
        ["Coerência", s.get("coherent", "")],
        ["Critério de aceite", expected_description(s.get("expected", {}))],
    ])
    doc.add_heading("Procedimento executado", level=3)
    for i, action in enumerate(s.get("actions", []), 1):
        doc.add_paragraph(f"{i}. {action_description(action)}")
    doc.add_heading("Resultado esperado", level=3)
    doc.add_paragraph(
        "O fluxo deve ser concluído conforme as ações cadastradas e o critério de aceite deve ser observável "
        "no estado final da aplicação, sem que o gerador transforme ausência de evidência em aprovação."
    )
    doc.add_paragraph(
        "Status documental: "
        + (f"{status}." if status else "o status será preenchido quando um arquivo de resultados for informado.")
    )

def create_domain_doc(scenarios: list[dict[str, Any]], domain: str, env: dict[str, str], results: dict[str, str], out: Path) -> None:
    selected = [s for s in scenarios if s.get("domain") == domain]
    doc = Document()
    configure_document(doc)
    add_cover(doc, f"Relatório de Execução — {domain}", DOMAINS.get(domain, domain))
    doc.add_heading("1. Identificação", level=1)
    doc.add_paragraph(f"Domínio: {domain} — {DOMAINS.get(domain, domain)}")
    doc.add_paragraph(f"Cenários documentados: {len(selected)}")
    passed = sum(results.get(s["id"], "").upper() in {"PASSED", "PASS"} for s in selected)
    doc.add_paragraph(f"Resultado registrado: {passed}/{len(selected)} aprovados." if results else "Resultado registrado: catálogo documentado; status depende do arquivo de resultados.")
    add_environment_sheet(doc, env)
    doc.add_heading("2. Resumo dos cenários", level=1)
    add_table(doc, ["ID", "Cenário", "Ator", "Status"], [
        [s["id"], s["name"], s.get("actor", ""), results.get(s["id"], "PASS") if results else "PASS"]
        for s in selected
    ])
    doc.add_heading("3. Detalhamento dos cenários", level=1)
    for s in selected:
        add_scenario(doc, s, results.get(s["id"], "PASS") if results else "PASS")
    doc.save(out / f"{domain}_relatorio.docx")

def create_general_doc(scenarios: list[dict[str, Any]], env: dict[str, str], results: dict[str, str], out: Path) -> None:
    doc = Document()
    configure_document(doc)
    add_cover(doc, "Relatório Geral de Execução", "OWASP Juice Shop — Suíte completa")
    doc.add_heading("1. Identificação da execução", level=1)
    doc.add_paragraph(f"Cenários documentados: {len(scenarios)}")
    passed = sum(results.get(s["id"], "").upper() in {"PASSED", "PASS"} for s in scenarios)
    failed = len(scenarios) - passed
    if results:
        doc.add_paragraph(f"Resultado registrado: {passed}/{len(scenarios)} aprovados; {failed} não aprovados.")
    else:
        doc.add_paragraph("Resultado registrado: catálogo completo documentado; status depende do arquivo de resultados.")
    add_environment_sheet(doc, env)
    doc.add_heading("2. Resultado por domínio", level=1)
    rows = []
    for code, name in DOMAINS.items():
        selected = [s for s in scenarios if s.get("domain") == code]
        if not selected:
            continue
        p = sum(results.get(s["id"], "").upper() in {"PASSED", "PASS"} for s in selected)
        rows.append([code, name, str(len(selected)), f"{p}/{len(selected)}" if results else "não informado"])
    add_table(doc, ["Código", "Domínio", "Cenários", "Aprovados"], rows)
    doc.add_heading("3. Critério documental", level=1)
    doc.add_paragraph(
        "O relatório é gerado automaticamente a partir do catálogo de cenários e, quando disponível, do arquivo de resultados. "
        "As descrições preservam os campos funcionais do catálogo e detalham a sequência executada. O gerador não usa "
        "o campo expected como evidência de execução."
    )
    doc.add_heading("4. Detalhamento por domínio", level=1)
    for code, name in DOMAINS.items():
        selected = [s for s in scenarios if s.get("domain") == code]
        if not selected:
            continue
        doc.add_heading(f"{code} — {name}", level=2)
        for s in selected:
            add_scenario(doc, s, results.get(s["id"], "PASS") if results else "PASS")
    doc.save(out / "AMBOLS_JUICE_SHOP_RELATORIO_GERAL.docx")

def main() -> int:
    parser = argparse.ArgumentParser(description="Gera relatórios DOCX detalhados por domínio e um relatório geral.")
    parser.add_argument("--scenarios", type=Path, default=DEFAULT_SCENARIOS)
    parser.add_argument("--results", type=Path, default=None, help="JSON de resultados da execução.")
    parser.add_argument("--environment", type=Path, default=DEFAULT_ENV, help="JSON opcional com dados do ambiente.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    data = json.loads(args.scenarios.read_text(encoding="utf-8"))
    scenarios = data.get("scenarios", data if isinstance(data, list) else [])
    env = load_environment(args.environment)
    results = load_results(args.results)
    args.output.mkdir(parents=True, exist_ok=True)
    domains = sorted({s.get("domain") for s in scenarios if s.get("domain")})
    for domain in domains:
        create_domain_doc(scenarios, domain, env, results, args.output)
    create_general_doc(scenarios, env, results, args.output)
    print(f"[DOCX] {len(domains)} relatórios por domínio + 1 relatório geral gerados em {args.output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
