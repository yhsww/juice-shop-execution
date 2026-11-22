from __future__ import annotations

import asyncio
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin

from playwright.async_api import Page

from automation.browser import browser_session, open_juice_shop
from automation.observer import UIState, observe, meaningful_change, wait_for_stable_ui, describe_change
from config.settings import settings
from recovery.artifacts import route_key, state_record, write_json


@dataclass(frozen=True)
class DiscoveryConfig:
    max_pages: int = 30
    max_depth: int = 2
    timeout_seconds: int = 120


async def _internal_links(page: Page) -> list[str]:
    links: list[str] = []
    anchors = page.locator("a[href]")
    for i in range(await anchors.count()):
        a = anchors.nth(i)
        try:
            if not await a.is_visible():
                continue
            href = await a.get_attribute("href") or ""
            if href.startswith("/#/"):
                links.append(href)
            elif href.startswith("http") and href.startswith(settings.base_url):
                links.append(href)
        except Exception:
            continue
    return list(dict.fromkeys(links))


def _candidate_requirements(states: list[dict], transitions: list[dict]) -> list[dict]:
    requirements: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for state in states:
        route = route_key(state["url"])
        for control in state.get("controls", []):
            key = (route, control)
            if key in seen:
                continue
            seen.add(key)
            requirements.append({
                "id": f"REC-{len(requirements)+1:04d}",
                "source": "ui-observation",
                "type": "availability",
                "route": route,
                "behavior": f"A interface deve disponibilizar o controle observado: {control}.",
                "evidence": {"url": state["url"], "control": control},
                "confidence": "medium",
            })
    for transition in transitions:
        requirements.append({
            "id": f"REC-{len(requirements)+1:04d}",
            "source": "ui-transition",
            "type": "navigation",
            "route": transition["from_route"],
            "behavior": f"A aplicação deve permitir acessar {transition['to_route']} a partir da interface observada.",
            "evidence": transition,
            "confidence": "high" if transition.get("changed") else "low",
        })
    return requirements


async def discover(config: DiscoveryConfig | None = None) -> dict:
    config = config or DiscoveryConfig()
    started = asyncio.get_running_loop().time()
    states: list[dict] = []
    transitions: list[dict] = []
    queue: list[tuple[str, int]] = [("/#/", 0)]
    visited: set[str] = set()

    async with browser_session() as (_, _, page):
        await open_juice_shop(page)
        while queue and len(states) < config.max_pages:
            if asyncio.get_running_loop().time() - started >= config.timeout_seconds:
                break
            route, depth = queue.pop(0)
            absolute = route if route.startswith("http") else f"{settings.base_url}{route}"
            key = route_key(absolute)
            if key in visited or depth > config.max_depth:
                continue
            visited.add(key)
            try:
                await page.goto(absolute, wait_until="domcontentloaded", timeout=settings.navigation_timeout_ms)
                state = await wait_for_stable_ui(page, timeout_ms=1600)
            except Exception as exc:
                states.append({"url": absolute, "error": f"{type(exc).__name__}: {exc}"})
                continue

            record = state_record(state)
            record["depth"] = depth
            states.append(record)

            for href in await _internal_links(page):
                target = route_key(href if href.startswith("http") else urljoin(settings.base_url, href))
                if target not in visited and all(item[0] != target for item in queue):
                    queue.append((target, depth + 1))
                    before = state
                    try:
                        await page.goto(href if href.startswith("http") else f"{settings.base_url}{href}", wait_until="domcontentloaded", timeout=settings.navigation_timeout_ms)
                        after = await wait_for_stable_ui(page, timeout_ms=1000)
                        transitions.append({
                            "from_route": route_key(before.url),
                            "to_route": route_key(after.url),
                            "link": href,
                            "changed": meaningful_change(before, after),
                            "description": describe_change(before, after),
                        })
                    except Exception:
                        continue
                    await page.goto(absolute, wait_until="domcontentloaded", timeout=settings.navigation_timeout_ms)
                    await wait_for_stable_ui(page, timeout_ms=800)

    result = {
        "method": "deterministic-ui-discovery",
        "target": settings.base_url,
        "pages_observed": len(states),
        "transitions_observed": len(transitions),
        "states": states,
        "transitions": transitions,
        "candidate_requirements": _candidate_requirements(states, transitions),
    }
    out = Path(settings.report_dir).parent / "recovery"
    write_json(out / "ui-states.json", {"target": settings.base_url, "states": states})
    write_json(out / "behaviors.json", {"transitions": transitions})
    write_json(out / "candidate-requirements.json", {"requirements": result["candidate_requirements"]})
    write_json(out / "discovery-summary.json", result)
    return result
