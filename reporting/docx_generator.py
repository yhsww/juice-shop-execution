from __future__ import annotations

import argparse
import json
from datetime import datetime
import platform
import re
from pathlib import Path
from typing import Any

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

from reporting.humanizer import humanize_scenario
from reporting.report import _observed_behavior, _observed_messages

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCENARIOS = ROOT / "scenarios"
DEFAULT_EXECUTIONS = ROOT / "reports" / "executions"
DEFAULT_OUT = ROOT / "reports" / "docx"
DEFAULT_ENV = ROOT / ".report-environment.json"
DEFAULT_HUMANIZED = ROOT / "reports" / "humanized"
DEFAULT_COMPOSE = ROOT / "juice-shop" / "docker-compose.yml"

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


def humanize_text(value: Any, limit: int = 1200) -> str:
    """Converte evidência textual em texto funcional, limpo e legível."""
    text = normalize(value, limit)
    if not text:
        return ""

    # URLs, rotas e detalhes técnicos pertencem aos artefatos de execução,
    # não à narrativa funcional do DOCX.
    import re
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"(?<!\w)/#/[A-Za-z0-9_./?=&%-]+", "", text)
    text = re.sub(r"\s{2,}", " ", text).strip()
    text = text.replace("Falha de automação:", "A aplicação não concluiu a ação esperada: ")
    text = text.replace("Nenhuma mudança visual relevante detectada.", "")
    return normalize(text, limit)


def humanize_observation(execution: dict[str, Any] | None) -> str:
    """Retorna uma conclusão curta baseada apenas no que foi observado."""
    if not execution:
        return "Execução não localizada."

    raw = _observed_behavior(execution)
    text = humanize_text(raw, 1600)

    # O helper de evidência pode cair em URL quando não há observação textual.
    # Nesse caso, não levamos a URL para o documento.
    if not text or text.lower().startswith("a execução foi concluída na url observada"):
        final_text = humanize_text(execution.get("final_visible_text"), 900)
        if final_text:
            return f"A execução foi concluída com o estado visível registrado na interface: {final_text}."
        return "A execução foi concluída sem mudança de estado adicional registrada."

    return text


def humanize_messages(execution: dict[str, Any] | None) -> str:
    if not execution:
        return "Não registrado."

    messages = []
    for item in _observed_messages(execution):
        text = humanize_text(item, 500)
        if text:
            messages.append(text)

    return " ".join(messages[:8]) if messages else "Nenhuma mensagem relevante registrada."


def humanize_data(scenario: dict[str, Any], execution: dict[str, Any] | None) -> str:
    if not execution:
        return humanize_text(scenario.get("data")) or "Não registrado."

    values: list[str] = []
    for step in execution.get("steps", []):
        value = humanize_text(step.get("data"), 500)
        if value:
            values.append(value)

    if not values:
        value = humanize_text(scenario.get("data"), 1200)
        return value or "Nenhum dado informado."

    unique: list[str] = []
    seen: set[str] = set()
    for value in values:
        key = value.casefold()
        if key not in seen:
            seen.add(key)
            unique.append(value)

    return "; ".join(unique)[:1800]


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
    """Load one catalog file or every ``*.json`` catalog in a directory.

    A directory is read in name order and files starting with ``_`` are
    skipped, matching ``automation.runner.load_scenarios``; this keeps the
    reports aligned with the scenarios the runner actually executes.
    """
    files = (
        [item for item in sorted(path.glob("*.json")) if not item.name.startswith("_")]
        if path.is_dir()
        else [path]
    )
    scenarios: list[dict[str, Any]] = []
    for file in files:
        payload = json.loads(file.read_text(encoding="utf-8"))
        scenarios.extend(
            payload.get("scenarios", []) if isinstance(payload, dict)
            else payload if isinstance(payload, list) else []
        )
    return scenarios


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



def _juice_shop_version(compose_path: Path) -> str:
    """Obtém a versão do Juice Shop a partir da imagem configurada no Compose."""
    try:
        content = compose_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "Não identificada"

    match = re.search(r"bkimminich/juice-shop:([^\\s]+)", content)
    return match.group(1) if match else "Não identificada"


def load_environment(path: Path) -> dict[str, str]:
    # Estrutura intencionalmente igual à Ficha de Ambiente do modelo fornecido.
    env = {
        "Avaliador e data": datetime.now().strftime("%d/%m/%Y"),
        "Versão do Juice Shop": _juice_shop_version(DEFAULT_COMPOSE),
        "Sistema operacional": platform.system(),
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
    """Converte uma ação técnica do catálogo em ação funcional curta."""
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
        return "Acessar a área correspondente da aplicação"
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
        return 'Aguardar a estabilização da interface'
    if typ == "ASSERT_ENABLED":
        return f'Verificar se "{target_name}" está habilitado'
    if typ == "ASSERT_DISABLED":
        return f'Verificar se "{target_name}" está desabilitado'
    if typ == "ASSERT_SELECTED":
        return f'Verificar se "{target_name}" está selecionado'
    return f'Executar a ação "{typ}"'


def detailed_flow(
    scenario: dict[str, Any],
    execution: dict[str, Any] | None,
) -> str:
    """Produz uma descrição funcional curta e humanizada.

    O fluxo do catálogo é a fonte principal. A execução só complementa a
    descrição quando houver evidência funcional útil; URLs, waits e detalhes
    de automação nunca entram na narrativa.
    """
    base = humanize_text(scenario.get("flow"), 1000)
    if base:
        return base

    name = humanize_text(scenario.get("name"), 500)
    actor = humanize_text(scenario.get("actor"), 200)
    if name:
        return f"{actor + ' ' if actor else ''}realiza o cenário {name.lower()}."

    return "Executar o cenário conforme definido."



def observed_result(execution: dict[str, Any] | None) -> str:
    return humanize_observation(execution)



def observed_messages(execution: dict[str, Any] | None) -> str:
    return humanize_messages(execution)



def observed_data(scenario: dict[str, Any], execution: dict[str, Any] | None) -> str:
    return humanize_data(scenario, execution)



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


def add_scenario(
    doc: Document,
    scenario: dict[str, Any],
    execution: dict[str, Any] | None,
    humanized: dict[str, Any] | None = None,
) -> None:
    # Estrutura mantida na mesma ordem e com os mesmos campos do modelo fornecido.
    doc.add_heading("Ficha de Cenário", level=2)

    domain = str(scenario.get("domain") or "")
    flow_text = humanized.get("flow") if humanized else detailed_flow(scenario, execution)
    # Catálogos com "flow_type" (Principal/Alternativo/Incoerente) mostram o tipo
    # de fluxo exigido pelo template AMBOLS antes da descrição.
    if scenario.get("flow_type"):
        flow_text = f'{scenario["flow_type"]}. {flow_text}'
    rows = [
        ["ID do cenário", scenario.get("id", "")],
        ["Domínio", f"{domain} — {DOMAINS.get(domain, '')}".strip(" —")],
        ["Nome do cenário", scenario.get("name", "")],
        ["Ator", scenario.get("actor", "")],
        ["Fluxo", flow_text],
        ["Pré-condição (estado inicial)", humanized.get("precondition") if humanized else scenario.get("precondition", "")],
        ["Resultado observado (mudança de estado)", humanized.get("observed_result") if humanized else observed_result(execution)],
        ["Mensagens exibidas ao usuário", "\n".join(humanized.get("messages", [])) if humanized else observed_messages(execution)],
        ["Dados manipulados", humanized.get("data") if humanized else observed_data(scenario, execution)],
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
                # Não inventa uma resposta: mantém somente a ausência de
                # evidência adicional registrada pelo executor.
                response = "Nenhuma resposta adicional registrada."

            if step.get("error"):
                response = f"Falha durante a execução: {normalize(step.get('error'))}"

            humanized_steps = (
                humanized.get("steps", [])
                if isinstance(humanized, dict)
                else []
            )
            if not isinstance(humanized_steps, list):
                humanized_steps = []

            humanized_step = next(
                (
                    item
                    for item in humanized_steps
                    if isinstance(item, dict)
                    and str(item.get("number")) == str(step.get("step"))
                ),
                None,
            )

            if humanized_step:
                user_action = normalize(humanized_step.get("action"))
                step_data = normalize(humanized_step.get("data")) or "—"
                response = normalize(humanized_step.get("response")) or response
            else:
                raw_action = step.get("user_action")
                if raw_action:
                    user_action = normalize(raw_action)
                elif isinstance(step.get("action"), dict):
                    user_action = action_description(step["action"])
                else:
                    user_action = normalize(step.get("action")) or "Ação não registrada."
                step_data = normalize(step.get("data")) or "—"

            step_rows.append(
                [
                    str(step.get("step", "")),
                    user_action,
                    step_data,
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


def scenario_order(scenario: dict[str, Any]) -> tuple[str, int, str]:
    """Chave de ordenação: domínio e número do cenário (CEN-CHK-07 -> CHK, 7)."""
    scenario_id = str(scenario.get("id") or "")
    match = re.search(r"([A-Z]+)-(\d+)$", scenario_id)
    if not match:
        return (scenario_id, 0, scenario_id)
    return (match.group(1), int(match.group(2)), scenario_id)


def create_document(
    scenarios: list[dict[str, Any]],
    env: dict[str, str],
    executions: dict[str, dict[str, Any]],
    humanized: dict[str, dict[str, Any]],
    out: Path,
    domains: list[str],
    filename: str,
) -> None:
    doc = Document()
    configure_document(doc)
    doc.core_properties.title = filename.rsplit(".", 1)[0]
    doc.core_properties.subject = "Relatório funcional do OWASP Juice Shop"
    doc.core_properties.author = "Juice Shop Execution"

    add_environment(doc, env)

    for index, domain in enumerate(domains):
        if index:
            doc.add_page_break()

        add_domain_header(doc, domain)

        # Ordem numérica dentro do domínio (CHK-01, CHK-02, ... CHK-44),
        # independente da ordem em que os cenários aparecem nos catálogos.
        selected = sorted(
            (
                scenario
                for scenario in scenarios
                if str(scenario.get("domain", "")).upper() == domain
            ),
            key=scenario_order,
        )

        for scenario_index, scenario in enumerate(selected):
            if scenario_index:
                doc.add_page_break()
            add_scenario(doc, scenario, executions.get(str(scenario.get("id"))), humanized.get(str(scenario.get("id"))))

    doc.save(out / filename)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Gera DOCX seguindo estritamente a estrutura da Etapa 1."
    )
    parser.add_argument("--scenarios", type=Path, default=DEFAULT_SCENARIOS)
    parser.add_argument(
        "--scenario",
        help="Processa somente o cenário informado pelo ID.",
    )
    parser.add_argument("--executions", type=Path, default=DEFAULT_EXECUTIONS)
    parser.add_argument("--results", type=Path, default=None)
    parser.add_argument("--environment", type=Path, default=DEFAULT_ENV)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--humanize",
        choices=["auto", "llm", "deterministic"],
        default="auto",
        help="Humanização das descrições: LLM, determinística ou automática.",
    )
    parser.add_argument("--humanized", type=Path, default=DEFAULT_HUMANIZED)
    parser.add_argument("--force-humanize", action="store_true")
    args = parser.parse_args()

    scenarios = load_scenarios(args.scenarios)
    if args.scenario:
        scenarios = [
            item for item in scenarios
            if str(item.get("id") or "") == args.scenario
        ]
        if not scenarios:
            raise SystemExit(
                f"Cenário não encontrado no catálogo: {args.scenario}"
            )

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

    humanized: dict[str, dict[str, Any]] = {}
    if args.humanize in {"auto", "llm"}:
        for scenario in scenarios:
            sid = str(scenario.get("id") or "")
            execution = executions.get(sid)
            if not execution:
                continue
            try:
                humanized[sid] = humanize_scenario(
                    scenario,
                    execution,
                    args.humanized,
                    force=args.force_humanize,
                )
            except Exception as exc:
                if args.humanize == "llm":
                    raise SystemExit(
                        f"Falha na humanização LLM de {sid}: {exc}"
                    ) from exc
                print(
                    f"[DOCX] LLM indisponível para {sid}; "
                    f"usando descrição determinística: {exc}"
                )

    domains = sorted(
        {str(item.get("domain")).upper() for item in scenarios if item.get("domain")}
    )

    # Um documento por domínio, mantendo a mesma ficha/estrutura do modelo.
    for domain in domains:
        create_document(
            scenarios,
            env,
            executions,
            humanized,
            args.output,
            [domain],
            f"{domain}_relatorio.docx",
        )

    # Documento geral: mesma estrutura, apenas reunindo os domínios.
    create_document(
        scenarios,
        env,
        executions,
        humanized,
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
