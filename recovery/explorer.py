from __future__ import annotations

import asyncio
import json
import time
from pathlib import Path
from typing import Any

from playwright.async_api import Page

from automation.browser import browser_session, open_juice_shop
from automation.executor import ActionResult, execute
from automation.observer import wait_for_stable_ui
from config.settings import settings
from recovery.change_detector import diff, fingerprint
from recovery.data_generator import variants_for
from recovery.control_discovery import discover_controls
from recovery.network import NetworkCollector


class BehavioralExplorer:
    def __init__(self, page: Page, network: NetworkCollector, scenario: dict[str, Any],
                 output_dir: Path, max_steps: int, max_seconds: int, max_variants: int):
        self.page = page
        self.network = network
        self.scenario = scenario
        self.output_dir = output_dir
        self.max_steps = max_steps
        self.max_seconds = max_seconds
        self.max_variants = max_variants
        self.started = time.monotonic()
        self.step_counter = 0
        self.observations: list[dict[str, Any]] = []
        self.discovered: list[dict[str, Any]] = []
        self.seen: set[str] = set()
        self.baseline_url: str = ""
        self.baseline_storage: dict[str, Any] | None = None

    async def run(self) -> dict[str, Any]:
        await open_juice_shop(self.page)
        for index, action in enumerate(self.scenario.get("actions", []), 1):
            if self.exhausted():
                break
            await self._planned(index, action)
            if self.exhausted():
                break
        if not self.exhausted():
            self.baseline_url = self.page.url
            self.baseline_storage = await self.page.context.storage_state()
            await self._explore_state()
        return {
            "scenario_id": self.scenario["id"], "domain": self.scenario.get("domain"),
            "name": self.scenario.get("name"), "planned_flow": self.scenario.get("flow"),
            "observations": self.observations, "discovered_scenarios": self.discovered,
            "steps_executed": self.step_counter,
        }

    async def _planned(self, index: int, action: dict[str, Any]) -> None:
        before = await self.snapshot()
        action_id = f"{self.scenario['id']}-P{index:02d}"
        self.network.set_action(action_id)
        started = time.time()
        result = await self.perform(action)
        after = await self.snapshot()
        network = self.network.correlate_window(started, time.time(), action_id)
        change = diff(before, after)
        self.step_counter += 1
        self.record(action_id, "planned", action, before, after, change, network, result.success, result.error or "")

    async def _explore_state(self) -> None:
        controls = await discover_controls(self.page)
        for control in controls:
            if self.exhausted() or control.get("disabled") or control.get("readonly"):
                continue
            signature = f"{fingerprint({'interactive_fingerprint': control.get('key')})}|{control.get('value')}"
            if signature in self.seen:
                continue
            self.seen.add(signature)
            tag = control.get("tag")
            if tag in {"input", "textarea"}:
                for variant in variants_for(control, self.max_variants):
                    if self.exhausted():
                        return
                    await self._variant(control, variant)
            elif tag == "select":
                await self._select(control)
            elif tag in {"button", "a"} or control.get("role") in {"button", "link", "checkbox", "radio", "tab"}:
                if self._skip(control):
                    continue
                await self._click(control)

    async def _variant(self, control: dict[str, Any], variant: Any) -> None:
        await self._restore_baseline()
        before = await self.snapshot()
        action = {"type": "FILL", "control": control, "value": variant.value, "variant": variant.label}
        action_id = self.next_id("ALT")
        self.network.set_action(action_id)
        started = time.time()
        result = await execute(self.page, {"type": "FILL", "target": self._action_target(control), "value": variant.value})
        await self.settle()
        after = await self.snapshot()
        network = self.network.correlate_window(started, time.time(), action_id)
        change = diff(before, after)
        self.step_counter += 1
        self.record(action_id, "alternative", action, before, after, change, network, result.success, result.error or "")
        if result.success and change["changed"]:
            self.register_alternative(action, before, after, change)

    async def _select(self, control: dict[str, Any]) -> None:
        await self._restore_baseline()
        before = await self.snapshot()
        action = {"type": "SELECT", "control": control}
        action_id = self.next_id("ALT")
        self.network.set_action(action_id)
        started = time.time()
        options = control.get("options") or []
        if not options:
            return
        option = options[0]
        result = await execute(self.page, {"type": "SELECT", "target": self._action_target(control), "value": option.get("value") or option.get("label") or ""})
        await self.settle()
        after = await self.snapshot()
        network = self.network.correlate_window(started, time.time(), action_id)
        change = diff(before, after)
        self.step_counter += 1
        self.record(action_id, "alternative", action, before, after, change, network, result.success, result.error or "")
        if result.success and change["changed"]:
            self.register_alternative(action, before, after, change)

    async def _click(self, control: dict[str, Any]) -> None:
        await self._restore_baseline()
        before = await self.snapshot()
        action = {"type": "CLICK", "control": control}
        action_id = self.next_id("ALT")
        self.network.set_action(action_id)
        started = time.time()
        result = await execute(self.page, {"type": "CLICK", "target": self._action_target(control)})
        await self.settle()
        after = await self.snapshot()
        network = self.network.correlate_window(started, time.time(), action_id)
        change = diff(before, after)
        self.step_counter += 1
        self.record(action_id, "alternative", action, before, after, change, network, result.success, result.error or "")
        if result.success and change["changed"]:
            self.register_alternative(action, before, after, change)

    async def _restore_baseline(self) -> None:
        if not self.baseline_storage or not self.baseline_url:
            return

        old_context = self.page.context
        browser = old_context.browser
        if browser is None:
            return

        try:
            await old_context.close()
        except Exception:
            pass

        context = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            ignore_https_errors=True,
            storage_state=self.baseline_storage,
        )
        page = await context.new_page()
        page.set_default_timeout(0)
        page.set_default_navigation_timeout(0)
        await page.goto(
            self.baseline_url,
            wait_until="domcontentloaded",
            timeout=0,
        )
        await self.settle()

        self.page = page
        self.network = NetworkCollector(settings.recovery_max_events)
        self.network.attach(page)

    async def perform(self, action: dict[str, Any]) -> ActionResult:
        """Use the same UI interaction engine as deterministic scenario execution."""
        return await execute(self.page, action)

    @staticmethod
    def _action_target(control: dict[str, Any]) -> dict[str, Any]:
        """Convert observed DOM metadata into a semantic execution target."""
        target: dict[str, Any] = {}
        for key in ("role", "label", "name", "text", "placeholder", "id"):
            value = control.get(key)
            if value:
                target[key] = value
        if target.get("role") in {"input", "textarea", "select"}:
            target.pop("role", None)
        return target

    async def snapshot(self) -> dict[str, Any]:
        state = await wait_for_stable_ui(self.page, timeout_ms=1200)
        controls = await discover_controls(self.page)
        visual = await self.page.evaluate("""() => [...document.querySelectorAll('body *')].slice(0,500).map(el => {
          const s=getComputedStyle(el); return [el.tagName,el.className,s.display,s.visibility,s.opacity,s.backgroundColor,s.color].join('|')
        }).join('\\n')""")
        path = self.output_dir / self.scenario["id"] / f"{self.step_counter + 1:03d}.png"
        path.parent.mkdir(parents=True, exist_ok=True)
        screenshot_path = ""
        try:
            await self.page.screenshot(path=str(path), full_page=True)
            screenshot_path = str(path) if path.exists() else ""
        except Exception:
            screenshot_path = ""
        return {"url": state.url, "title": state.title, "visible_text": state.visible_text,
                "messages": list(state.messages), "controls": controls,
                "interactive_fingerprint": "|".join(sorted(
                    f"{c.get('key')}:{c.get('disabled')}:{c.get('required')}:{c.get('checked')}:{c.get('selected')}:{c.get('value')}"
                    for c in controls)),
                "visual_fingerprint": fingerprint({"visual_fingerprint": visual}),
                "screenshot": screenshot_path}

    async def settle(self) -> None:
        try:
            await self.page.wait_for_load_state("domcontentloaded", timeout=800)
        except Exception:
            pass
        await self.page.wait_for_timeout(150)

    def record(self, action_id: str, kind: str, action: dict[str, Any], before: dict[str, Any],
               after: dict[str, Any], change: dict[str, Any], network: list[dict[str, Any]],
               success: bool, error: str) -> None:
        desc = str(action.get("type", "INTERACTION")).upper() + ": "
        desc += "; ".join(change.get("changes", [])) if change.get("changes") else "nenhuma mudança observável detectada."
        self.observations.append({
            "action_id": action_id, "kind": kind, "action": action,
            "data": action.get("value") or action.get("variant") or action.get("control", {}),
            "success": success, "error": error,
            "state_before": {k:v for k,v in before.items() if k != "screenshot"},
            "state_after": {k:v for k,v in after.items() if k != "screenshot"},
            "screenshot_before": before.get("screenshot"), "screenshot_after": after.get("screenshot"),
            "change": change, "network": network, "observed_behavior": desc})

    def register_alternative(self, action: dict[str, Any], before: dict[str, Any],
                             after: dict[str, Any], change: dict[str, Any]) -> None:
        key = json.dumps([action.get("type"), action.get("control", {}).get("key"),
                          action.get("value"), change.get("changes")], sort_keys=True, ensure_ascii=False)
        if any(x.get("_key") == key for x in self.discovered):
            return
        self.discovered.append({
            "scenario_id": f"{self.scenario['id']}-ALT-{len(self.discovered)+1:03d}",
            "domain": self.scenario.get("domain"), "source_scenario": self.scenario["id"],
            "trigger": action, "description": self.observations[-1]["observed_behavior"],
            "observed_change": change,
            "evidence": {"before": before, "after": after}, "_key": key})

    def next_id(self, kind: str) -> str:
        return f"{self.scenario['id']}-{kind}-{self.step_counter + 1:03d}"

    def _skip(self, control: dict[str, Any]) -> bool:
        label = str(control.get("label") or "").lower()
        return any(x in label for x in ("github", "twitter", "facebook", "linkedin"))

    def exhausted(self) -> bool:
        # Zero means unlimited. Exploration ends only when there is no more
        # interaction work to execute (all discovered controls/variants have
        # already been attempted) or when an explicit safety cap is configured.
        return self.max_steps > 0 and self.step_counter >= self.max_steps


async def explore_scenarios(scenarios: list[dict[str, Any]], *, output_dir: Path,
                            max_steps: int, max_seconds: int, max_variants: int) -> dict[str, Any]:
    results = []

    # Each scenario receives a fresh BrowserContext. This prevents authentication,
    # cart, form and navigation state from leaking between independent scenarios.
    async with browser_session() as (browser, base_context, _):
        try:
            await base_context.close()
        except Exception:
            pass

        for scenario in scenarios:
            if not scenario.get("actions"):
                continue

            context = await browser.new_context(
                viewport={"width": 1440, "height": 900},
                ignore_https_errors=True,
            )
            page = await context.new_page()
            # Recovery is an exhaustion-driven exploration. Playwright itself
            # must not introduce the old 10s/15s action/navigation ceilings.
            # A zero timeout means no artificial Playwright timeout.
            page.set_default_timeout(0)
            page.set_default_navigation_timeout(0)

            network = NetworkCollector(settings.recovery_max_events)
            network.attach(page)
            explorer = BehavioralExplorer(
                page, network, scenario, output_dir,
                max_steps, max_seconds, max_variants,
            )
            try:
                results.append(await explorer.run())
            except Exception as exc:
                results.append({
                    "scenario_id": scenario["id"],
                    "domain": scenario.get("domain"),
                    "name": scenario.get("name"),
                    "status": "AUTOMATION_ERROR",
                    "error": f"{type(exc).__name__}: {exc}",
                    "observations": [],
                    "discovered_scenarios": [],
                    "steps_executed": explorer.step_counter,
                })
            finally:
                try:
                    await asyncio.wait_for(context.close(), timeout=5)
                except Exception:
                    pass

    behaviors = []
    alternatives = []
    for result in results:
        for obs in result.get("observations", []):
            behaviors.append({
                "behavior_id": f"BE-{len(behaviors) + 1:05d}",
                "scenario_id": result["scenario_id"],
                "domain": result.get("domain"),
                "kind": obs.get("kind"),
                "description": obs.get("observed_behavior"),
                "evidence": obs,
            })
        alternatives.extend(result.get("discovered_scenarios", []))

    for alt in alternatives:
        alt.pop("_key", None)

    return {
        "scenarios": results,
        "behaviors": behaviors,
        "discovered_scenarios": alternatives,
        "counts": {
            "scenarios": len(results),
            "behaviors": len(behaviors),
            "alternatives": len(alternatives),
        },
    }
