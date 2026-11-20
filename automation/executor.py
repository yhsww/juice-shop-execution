from __future__ import annotations

from dataclasses import dataclass
from time import monotonic

from playwright.async_api import Page, TimeoutError as PlaywrightTimeoutError

from automation.locator import resolve
from automation.observer import UIState, describe_change, meaningful_change, observe
from config.settings import settings


@dataclass
class ActionResult:
    action: str
    user_action: str
    data: str
    url_before: str
    url_after: str
    observed_result: str
    changed: bool
    success: bool
    error: str | None = None


def _user_action(action: dict) -> str:
    explicit = action.get("user_action")
    if explicit:
        return explicit

    kind = action["type"].upper()
    target = action.get("target", {})
    name = target.get("name") or target.get("label") or target.get("text") or ""
    if kind == "NAVIGATE":
        return f"Abrir a rota {action.get('route', '')}".strip()
    if kind == "CLICK":
        return f'Clicar em "{name}"' if name else "Clicar no elemento"
    if kind == "FILL":
        return f'Preencher "{name}"'
    if kind == "SELECT":
        return f'Selecionar "{name}"'
    if kind == "PRESS":
        return f'Pressionar {action.get("key", "Enter")}'
    if kind == "CHECK":
        return f'Marcar "{name}"'
    if kind == "UNCHECK":
        return f'Desmarcar "{name}"'
    if kind == "WAIT":
        return "Aguardar a atualização da interface"
    return kind


def _action_data(action: dict) -> str:
    if "data" in action:
        return str(action["data"])
    if action["type"].upper() == "FILL":
        return str(action.get("value", ""))
    if action["type"].upper() == "SELECT":
        return str(action.get("value", ""))
    if action["type"].upper() == "NAVIGATE":
        return str(action.get("route", ""))
    return ""


async def _safe_observe(page: Page, fallback: UIState) -> UIState:
    deadline = monotonic() + 5
    while monotonic() < deadline:
        try:
            return await observe(page)
        except Exception:
            await page.wait_for_timeout(150)
    return fallback


async def execute(page: Page, action: dict) -> ActionResult:
    before = await observe(page)
    kind = action["type"].upper()
    data = _action_data(action)
    error: str | None = None

    try:
        if kind == "NAVIGATE":
            await page.goto(
                f"{settings.base_url}{action['route']}",
                wait_until="domcontentloaded",
                timeout=settings.navigation_timeout_ms,
            )
        elif kind == "CLICK":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Elemento alvo não encontrado ou não visível.")
            await locator.click(timeout=settings.action_timeout_ms)
        elif kind == "FILL":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Campo alvo não encontrado ou não visível.")
            await locator.fill(str(action["value"]), timeout=settings.action_timeout_ms)
        elif kind == "SELECT":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Select alvo não encontrado ou não visível.")
            await locator.select_option(str(action["value"]), timeout=settings.action_timeout_ms)
        elif kind == "CHECK":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Controle alvo não encontrado ou não visível.")
            await locator.check(timeout=settings.action_timeout_ms)
        elif kind == "UNCHECK":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Controle alvo não encontrado ou não visível.")
            await locator.uncheck(timeout=settings.action_timeout_ms)
        elif kind == "PRESS":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Elemento alvo não encontrado ou não visível.")
            await locator.press(action.get("key", "Enter"), timeout=settings.action_timeout_ms)
        elif kind == "WAIT":
            await page.wait_for_timeout(int(action.get("milliseconds", 500)))
        else:
            raise ValueError(f"Tipo de ação não suportado: {kind}")

        try:
            await page.wait_for_load_state(
                "domcontentloaded",
                timeout=min(1500, settings.navigation_timeout_ms),
            )
        except PlaywrightTimeoutError:
            pass

    except Exception as exc:
        error = str(exc)

    after = await _safe_observe(page, before)

    return ActionResult(
        action=kind,
        user_action=_user_action(action),
        data=data,
        url_before=before.url,
        url_after=after.url,
        observed_result=describe_change(before, after),
        changed=meaningful_change(before, after),
        success=error is None,
        error=error,
    )
