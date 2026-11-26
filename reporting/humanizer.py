from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any

from reporting.llm.client import LLMHumanizerError, humanize

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCENARIOS = ROOT / "scenarios" / "scenarios.json"
DEFAULT_EXECUTIONS = ROOT / "reports" / "executions"
DEFAULT_OUTPUT = ROOT / "reports" / "humanized"
PROMPT_VERSION = "4"

MAX_REPORT_CHARS = 30000


def collect_artifacts(scenario_id: str, executions_dir: Path) -> dict[str, Any]:
    """Coleta todos os relatórios textuais e screenshots do cenário."""
    reports = []
    for path in sorted(executions_dir.glob(f"{scenario_id}*")):
        if path.is_file() and path.suffix.lower() in {".json", ".md", ".txt"}:
            try:
                content = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            reports.append({"name": path.name, "content": content[:MAX_REPORT_CHARS]})
    screenshots = [
        str(path.resolve())
        for path in sorted(executions_dir.glob(f"{scenario_id}*.png"))
        if path.is_file()
    ]
    return {"reports": reports, "screenshots": screenshots}


def normalize(value: Any, limit: int = 1200) -> str:
    text = " ".join(str(value or "").split()).strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"


def safe_text(value: Any, limit: int = 1200) -> str:
    text = normalize(value, limit)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"(?<!\w)/#/[A-Za-z0-9_./?=&%-]+", "", text)
    text = re.sub(r"\s{2,}", " ", text).strip()
    return normalize(text, limit)


def is_sensitive(target: Any) -> bool:
    raw = json.dumps(target, ensure_ascii=False).casefold()
    return any(
        token in raw
        for token in (
            "password",
            "senha",
            "token",
            "authorization",
            "api_key",
            "secret",
        )
    )


def target_description(target: dict[str, Any]) -> str:
    parts = []
    for key in ("label", "name", "text", "role"):
        value = safe_text(target.get(key), 300)
        if value and value not in parts:
            parts.append(value)

    if target.get("exact") is False:
        parts.append("correspondência parcial")

    return " — ".join(parts)


def prepare_step(step: dict[str, Any]) -> dict[str, Any]:
    action = step.get("action") if isinstance(step.get("action"), dict) else {}
    target = action.get("target") if isinstance(action.get("target"), dict) else {}

    data = step.get("data")
    if is_sensitive(target) or is_sensitive(data):
        data = "[dado sensível omitido]"

    return {
        "number": step.get("step"),
        "user_action": safe_text(step.get("user_action"), 900),
        "action_type": safe_text(action.get("type"), 200),
        "target": target_description(target),
        "target_text": safe_text(
            target.get("text") or target.get("name") or target.get("label"),
            500,
        ),
        "data": safe_text(data, 700),
        "observed_result": safe_text(step.get("observed_result"), 1100),
        "success": step.get("success") is True,
    }


def prepare_execution(execution: dict[str, Any]) -> dict[str, Any]:
    steps = [prepare_step(step) for step in execution.get("steps", [])]
    messages = [
        safe_text(message, 700)
        for message in execution.get("messages", [])
        if safe_text(message, 700)
    ]

    return {
        "scenario_id": safe_text(execution.get("scenario_id"), 100),
        "status": safe_text(execution.get("status"), 50),
        "steps": steps,
        "messages": messages[:12],
        "final_visible_text": safe_text(execution.get("final_visible_text"), 2000),
    }


def prepare_catalog(scenario: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": safe_text(scenario.get("id"), 100),
        "domain": safe_text(scenario.get("domain"), 100),
        "name": safe_text(scenario.get("name"), 300),
        "actor": safe_text(scenario.get("actor"), 200),
        "flow": safe_text(scenario.get("flow"), 1200),
        "precondition": safe_text(scenario.get("precondition"), 1200),
        "data": safe_text(scenario.get("data"), 1200),
    }


def fingerprint(catalog: dict[str, Any], execution: dict[str, Any], model: str) -> str:
    payload = {
        "prompt_version": PROMPT_VERSION,
        "model": model,
        "catalog": catalog,
        "execution": execution,
    }
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def humanize_scenario(
    scenario: dict[str, Any],
    execution: dict[str, Any],
    output_dir: Path,
    force: bool = False,
    executions_dir: Path | None = None,
) -> dict[str, Any]:
    model = os.environ.get("REPORTING_LLM_MODEL", "gemini-3.5-flash-lite")
    catalog = prepare_catalog(scenario)
    evidence = prepare_execution(execution)
    evidence["artifacts"] = collect_artifacts(
        str(scenario["id"]),
        executions_dir or DEFAULT_EXECUTIONS,
    )
    path = output_dir / f"{scenario['id']}.json"
    fp = fingerprint(catalog, evidence, model)

    if path.exists() and not force:
        try:
            cached = json.loads(path.read_text(encoding="utf-8"))
            if cached.get("fingerprint") == fp:
                return cached["content"]
        except (OSError, json.JSONDecodeError, KeyError):
            pass

    content = humanize({"catalog": catalog, "execution": evidence})
    sanitized = sanitize_output(content)

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "scenario_id": scenario["id"],
                "fingerprint": fp,
                "content": sanitized,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    return sanitized


def sanitize_output(content: dict[str, Any]) -> dict[str, Any]:
    cleaned = {
        "flow": safe_text(content.get("flow"), 1600),
        "precondition": safe_text(content.get("precondition"), 1400),
        "observed_result": safe_text(content.get("observed_result"), 2000),
        "messages": [
            safe_text(item, 700)
            for item in content.get("messages", [])
        ][:12],
        "data": safe_text(content.get("data"), 1800),
        "steps": [],
    }

    for step in content.get("steps", []):
        cleaned["steps"].append(
            {
                "number": step.get("number"),
                "action": safe_text(step.get("action"), 700),
                "data": safe_text(step.get("data"), 700),
                "response": safe_text(step.get("response"), 900),
            }
        )

    return cleaned


def load_catalog(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("scenarios", payload if isinstance(payload, list) else [])


def load_execution(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Humaniza evidências de cenários usando uma LLM."
    )
    parser.add_argument("--scenario", action="append")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--scenarios", type=Path, default=DEFAULT_SCENARIOS)
    parser.add_argument("--executions", type=Path, default=DEFAULT_EXECUTIONS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    catalog = load_catalog(args.scenarios)
    selected_ids = set(args.scenario or [])
    if not args.all and not selected_ids:
        parser.error("Informe --scenario ID ou --all.")

    selected = [
        item
        for item in catalog
        if args.all or str(item.get("id")) in selected_ids
    ]

    generated = 0
    skipped = 0
    failed = 0
    for scenario in selected:
        scenario_id = str(scenario.get("id") or "")
        execution_path = args.executions / f"{scenario_id}.json"
        if not execution_path.exists():
            print(f"[LLM] {scenario_id}: execução não encontrada; ignorado.")
            skipped += 1
            continue

        try:
            humanize_scenario(
                scenario,
                load_execution(execution_path),
                args.output,
                force=args.force,
                executions_dir=args.executions,
            )
            generated += 1
            print(f"[LLM] {scenario_id}: documentação humanizada pronta.")
        except LLMHumanizerError as exc:
            failed += 1
            print(f"[LLM] {scenario_id}: erro controlado: {exc}")
            continue

    print(
        f"[LLM] {generated} humanizados; {skipped} ignorados; {failed} com erro."
    )
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
