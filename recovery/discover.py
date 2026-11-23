from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from config.settings import settings
from recovery.artifacts import evidence_index, write_json
from recovery.explorer import explore_scenarios
from recovery.report import save_stage1_report
from recovery.zap import ensure_zap, load_config, stop_zap


@dataclass(frozen=True)
class DiscoveryConfig:
    max_pages: int = 0
    max_depth: int = 0
    timeout_seconds: int = 180
    max_events: int = 2000
    zap: bool = False
    domains: tuple[str, ...] = ()
    scenario_ids: tuple[str, ...] = ()
    max_steps_per_scenario: int = 30
    max_variants_per_input: int = 6


def _load_scenarios() -> list[dict[str, Any]]:
    path = Path(__file__).resolve().parents[1] / "scenarios" / "scenarios.json"
    return list(json.loads(path.read_text(encoding="utf-8")).get("scenarios", []))


async def discover(config: DiscoveryConfig | None = None) -> dict:
    config = config or DiscoveryConfig(
        timeout_seconds=settings.recovery_timeout_seconds,
        max_steps_per_scenario=settings.recovery_max_steps_per_scenario,
        max_variants_per_input=settings.recovery_max_variants_per_input,
    )
    scenarios = _load_scenarios()
    domains = {d.upper() for d in config.domains}
    ids = set(config.scenario_ids)
    selected = [s for s in scenarios
                if (not domains or str(s.get("domain", "")).upper() in domains)
                and (not ids or s.get("id") in ids)]
    zap_config = load_config(config.zap)
    proxy = None
    if config.zap:
        proxy = ensure_zap(zap_config)
        if proxy:
            import os
            os.environ["AMBOLS_PROXY_SERVER"] = proxy
    try:
        result = await explore_scenarios(
            selected,
            output_dir=Path(settings.recovery_output_dir) / "evidence",
            max_steps=config.max_steps_per_scenario,
            max_seconds=config.timeout_seconds,
            max_variants=config.max_variants_per_input,
        )
    finally:
        stop_zap(zap_config)

    result.update({
        "method": "scenario-guided-behavioral-exploration",
        "target": settings.base_url,
        "selected_domains": sorted(domains),
        "selected_scenario_ids": sorted(ids),
        "zap_enabled": config.zap,
        "zap_proxy_active": bool(proxy),
    })
    output = Path(settings.recovery_output_dir)
    output.mkdir(parents=True, exist_ok=True)
    write_json(output / "discovery-summary.json", result)
    write_json(output / "behaviors.json", {"behaviors": result["behaviors"]})
    write_json(output / "discovered-scenarios.json", {"scenarios": result["discovered_scenarios"]})
    write_json(output / "stage1-scenarios.json", result)
    write_json(output / "evidence-index.json",
               evidence_index(states=[], transitions=[], behaviors=result["behaviors"], network=[]))
    save_stage1_report(output, result)
    return result
