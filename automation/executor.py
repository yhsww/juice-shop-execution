from __future__ import annotations

from dataclasses import dataclass
from time import monotonic

from playwright.async_api import Page

from automation.locator import resolve
from automation.observer import UIState, meaningful_change, observe
from config.settings import settings


@dataclass
class ActionResult:
    action: str
    data: str
    url_before: str
    url_after: str
    observed_result: str
    changed: bool
    success: bool
    error: str | None = None


async def execute(page: Page, action: dict) -> ActionResult:
    before = await observe(page)
    kind = action["type"].upper()
    data = action.get("data", "")
    target = action.get("target", {})

    try:
        if kind == "NAVIGATE":
            route = action["route"]
            await page.goto(f"{settings.base_url}{route}", wait_until="domcontentloaded")
        elif kind == "CLICK":
            locator = await resolve(page, target)
            if locator is None:
                raise RuntimeError("Elemento alvo não encontrado ou não visível.")
            await locator.click()
        elif kind == "FILL":
            locator = await resolve(page, target)
            if locator is None:
                raise RuntimeError("Campo alvo não encontrado ou não visível.")
            await locator.fill(action["value"])
        elif kind == "SELECT":
            locator = await resolve(page, target)
            if locator is None:
                raise RuntimeError("Select alvo não encontrado ou não visível.")
            await locator.select_option(action["value"])
        elif kind == "CHECK":
            locator = await resolve(page, target)
            if locator is None:
                raise RuntimeError("Controle alvo não encontrado ou não visível.")
            await locator.check()
        elif kind == "UNCHECK":
            locator = await resolve(page, target)
            if locator is None:
                raise RuntimeError("Controle alvo não encontrado ou não visível.")
            await locator.uncheck()
        elif kind == "PRESS":
            locator = await resolve(page, target)
            if locator is None:
                raise RuntimeError("Elemento alvo não encontrado ou não visível.")
            await locator.press(action.get("key", "Enter"))
        elif kind == "WAIT":
            await page.wait_for_timeout(int(action.get("milliseconds", 500)))
        else:
            raise ValueError(f"Tipo de ação não suportado: {kind}")

        await page.wait_for_load_state("domcontentloaded", timeout=3000)
    except Exception as exc:
        # A ação pode ter disparado navegação; a observação abaixo deve acontecer
        # mesmo quando o wait de navegação não for aplicável.
        error = str(exc)
    else:
        error = None

    deadline = monotonic() + 5
    after = before
    while monotonic() < deadline:
        try:
            after = await observe(page)
            break
        except Exception:
            await page.wait_for_timeout(150)

    changed = meaningful_change(before, after)
    success = error is None

    return ActionResult(
        action=kind,
        data=data,
        url_before=before.url,
        url_after=after.url,
        observed_result=after.visible_text,
        changed=changed,
        success=success,
        error=error,
    )
