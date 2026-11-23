from __future__ import annotations

import asyncio
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin

from playwright.async_api import Page

from automation.browser import browser_session, open_juice_shop
from automation.observer import wait_for_stable_ui
from config.settings import settings
from recovery.artifacts import evidence_index, route_key, write_json, write_jsonl
from recovery.behavior import extract_behaviors
from recovery.network import NetworkCollector, summarize_network
from recovery.state_model import state_record, transition
from recovery.zap import ensure_zap, load_config, stop_zap

@dataclass(frozen=True)
class DiscoveryConfig:
    max_pages: int = 30
    max_depth: int = 2
    timeout_seconds: int = 120
    max_events: int = 2000
    zap: bool = False

async def _internal_links(page: Page) -> list[str]:
    links: list[str] = []
    anchors = page.locator('a[href]')
    for i in range(await anchors.count()):
        a = anchors.nth(i)
        try:
            if not await a.is_visible():
                continue
            href = await a.get_attribute('href') or ''
            if href.startswith('/#/' ) or (href.startswith('http') and href.startswith(settings.base_url)):
                links.append(href)
        except Exception:
            continue
    return list(dict.fromkeys(links))

def _candidate_requirements(states: list[dict], transitions: list[dict]) -> list[dict]:
    requirements = []
    seen = set()
    for state in states:
        route = route_key(state['url'])
        for control in state.get('controls', []):
            key = (route, control)
            if key in seen:
                continue
            seen.add(key)
            requirements.append({
                'id': f'REC-{len(requirements)+1:04d}',
                'source': 'ui-observation',
                'type': 'availability',
                'route': route,
                'behavior': f'A interface disponibilizou o controle observado: {control}.',
                'evidence': {'url': state['url'], 'control': control},
                'confidence': 'medium',
            })
    return requirements

async def discover(config: DiscoveryConfig | None = None) -> dict:
    config = config or DiscoveryConfig(settings.recovery_max_pages, settings.recovery_max_depth, settings.recovery_timeout_seconds, settings.recovery_max_events, False)
    started = asyncio.get_running_loop().time()
    states, transitions, actions = [], [], []
    visited: set[str] = set()
    queue: list[tuple[str, int]] = [('/#/', 0)]
    zap_config = load_config(config.zap)
    proxy = ensure_zap(zap_config)
    if proxy:
        import os
        os.environ['AMBOLS_PROXY_SERVER'] = proxy
    try:
        async with browser_session() as (_, _, page):
            network = NetworkCollector(config.max_events)
            network.attach(page)
            await open_juice_shop(page)
            while queue and len(states) < config.max_pages:
                if asyncio.get_running_loop().time() - started >= config.timeout_seconds:
                    break
                route, depth = queue.pop(0)
                absolute = route if route.startswith('http') else f'{settings.base_url}{route}'
                key = route_key(absolute)
                if key in visited or depth > config.max_depth:
                    continue
                visited.add(key)
                try:
                    await page.goto(absolute, wait_until='domcontentloaded', timeout=settings.navigation_timeout_ms)
                    current = await wait_for_stable_ui(page, timeout_ms=1600)
                except Exception as exc:
                    states.append({'url': absolute, 'error': f'{type(exc).__name__}: {exc}', 'depth': depth})
                    continue
                states.append(state_record(current))
                for href in await _internal_links(page):
                    target_url = href if href.startswith('http') else urljoin(settings.base_url, href)
                    target = route_key(target_url)
                    if target in visited or any(item[0] == target for item in queue):
                        continue
                    queue.append((target, depth + 1))
                    action_id = f'A-{len(actions)+1:04d}'
                    network.set_action(action_id)
                    before = current
                    action_started = asyncio.get_running_loop().time()
                    try:
                        await page.goto(target_url, wait_until='domcontentloaded', timeout=settings.navigation_timeout_ms)
                        after = await wait_for_stable_ui(page, timeout_ms=1000)
                        action_ended = asyncio.get_running_loop().time()
                        tr = transition(before, after, action_id=action_id, action='NAVIGATE', evidence={'link': href, 'network': network.correlate_window(action_started, action_ended, action_id)})
                        transitions.append(tr.to_dict())
                        actions.append({'action_id': action_id, 'action': 'NAVIGATE', 'url_before': before.url, 'url_after': after.url, 'observed_result': tr.description, 'network': network.correlate_window(action_started, action_ended, action_id)})
                    except Exception as exc:
                        actions.append({'action_id': action_id, 'action': 'NAVIGATE', 'url_before': before.url, 'url_after': '', 'observed_result': '', 'error': f'{type(exc).__name__}: {exc}', 'network': network.events_for_action(action_id)})
                    try:
                        await page.goto(absolute, wait_until='domcontentloaded', timeout=settings.navigation_timeout_ms)
                        current = await wait_for_stable_ui(page, timeout_ms=800)
                    except Exception:
                        break
            behavior_list = extract_behaviors(states=states, transitions=transitions, actions=actions)
            network_events = network.snapshot()
    finally:
        stop_zap(zap_config)
    output = Path(settings.recovery_output_dir)
    index = evidence_index(states=states, transitions=transitions, behaviors=behavior_list, network=network_events)
    result = {'method': 'evidence-driven-ui-discovery', 'target': settings.base_url, 'pages_observed': len(states), 'transitions_observed': len(transitions), 'behaviors_observed': len(behavior_list), 'network_events': len(network_events), 'zap_enabled': config.zap, 'zap_proxy_active': bool(proxy), 'states': states, 'transitions': transitions, 'actions': actions, 'behaviors': behavior_list, 'network_summary': summarize_network(network_events), 'evidence_index': index}
    write_json(output / 'discovery-summary.json', result)
    write_json(output / 'ui-states.json', {'target': settings.base_url, 'states': states})
    write_json(output / 'behaviors.json', {'behaviors': behavior_list})
    write_json(output / 'state-transitions.json', {'transitions': transitions})
    write_jsonl(output / 'network.jsonl', network_events)
    write_json(output / 'evidence-index.json', index)
    return result