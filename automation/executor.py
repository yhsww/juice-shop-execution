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
    messages: tuple[str, ...] = ()
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


def _norm_text(value: object) -> str:
    return " ".join(str(value or "").split()).strip().casefold()


async def _scroll_into_view(locator) -> None:
    try:
        await locator.scroll_into_view_if_needed(timeout=1500)
    except Exception:
        pass


async def _click(locator) -> None:
    await _scroll_into_view(locator)
    try:
        await locator.click(timeout=settings.action_timeout_ms)
        return
    except Exception as first_error:
        await locator.page.wait_for_timeout(150)
        try:
            await locator.click(timeout=settings.action_timeout_ms)
            return
        except Exception:
            try:
                await locator.click(timeout=1500, force=True)
                return
            except Exception:
                raise first_error


async def _fill(locator, value: str) -> None:
    await _scroll_into_view(locator)
    try:
        await locator.fill(value, timeout=settings.action_timeout_ms)
        return
    except Exception as first_error:
        try:
            await _click(locator)
            await locator.press("ControlOrMeta+A", timeout=1500)
            await locator.press("Backspace", timeout=1500)
            await locator.type(value, timeout=settings.action_timeout_ms)
            return
        except Exception:
            raise first_error


async def _select_option(locator, value: str) -> None:
    """
    Seleciona uma opção de forma compatível com:
    - <select> nativo;
    - Angular Material mat-select / role=combobox.

    Para controles customizados, o valor aceito pelo cenário pode ser
    tanto o value/ID quanto o texto visível da opção.
    """
    tag_name = ""
    role = ""

    try:
        tag_name = (await locator.evaluate("(el) => el.tagName")).upper()
        role = (await locator.get_attribute("role") or "").lower()
    except Exception:
        pass

    if tag_name == "SELECT":
        try:
            await locator.select_option(
                value,
                timeout=settings.action_timeout_ms,
            )
            return
        except Exception as first_error:
            try:
                await locator.select_option(
                    label=value,
                    timeout=settings.action_timeout_ms,
                )
                return
            except Exception:
                raise first_error

    if tag_name == "MAT-SELECT" or role == "combobox":
        await locator.click(timeout=settings.action_timeout_ms)

        options = locator.page.locator(
            "[role='option'], .mat-mdc-option"
        )
        wanted = " ".join(str(value).split()).strip().casefold()

        deadline = monotonic() + settings.action_timeout_ms / 1000
        while monotonic() < deadline:
            count = await options.count()

            for index in range(count):
                option = options.nth(index)

                try:
                    if not await option.is_visible():
                        continue

                    text = " ".join(
                        (await option.inner_text()).split()
                    ).strip()

                    data_value = await option.get_attribute("data-value")
                    aria_label = await option.get_attribute("aria-label")

                    candidates = {
                        _norm_text(text),
                        _norm_text(data_value),
                        _norm_text(aria_label),
                    }

                    if wanted in candidates or any(
                        wanted and (wanted in candidate or candidate in wanted)
                        for candidate in candidates
                        if candidate
                    ):
                        await _scroll_into_view(option)
                        await option.click(
                            timeout=settings.action_timeout_ms
                        )
                        return

                except Exception:
                    continue

            await locator.page.wait_for_timeout(100)

        raise RuntimeError(
            f"Opção de seleção não encontrada: {value!r}"
        )

    raise RuntimeError(
        f"Controle não suporta SELECT de forma semântica: "
        f"tag={tag_name!r}, role={role!r}"
    )


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
            await _click(locator)
        elif kind == "FILL":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Campo alvo não encontrado ou não visível.")
            await _fill(locator, str(action["value"]))
        elif kind == "SELECT":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Select alvo não encontrado ou não visível.")
            await _select_option(locator, str(action["value"]))
        elif kind == "CHECK":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Controle alvo não encontrado ou não visível.")
            await _scroll_into_view(locator)
            await locator.check(timeout=settings.action_timeout_ms)
        elif kind == "UNCHECK":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Controle alvo não encontrado ou não visível.")
            await _scroll_into_view(locator)
            await locator.uncheck(timeout=settings.action_timeout_ms)
        elif kind == "PRESS":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Elemento alvo não encontrado ou não visível.")
            await _scroll_into_view(locator)
            try:
                await locator.press(
                    action.get("key", "Enter"),
                    timeout=settings.action_timeout_ms,
                )
            except Exception:
                await _click(locator)
                await locator.press(
                    action.get("key", "Enter"),
                    timeout=settings.action_timeout_ms,
                )
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

        # Angular can finish rendering a control after DOMContentLoaded.
        # A short generic settle prevents interacting with an intermediate
        # state without replacing scenario-defined WAITs.
        try:
            await page.wait_for_function(
                "() => document.readyState === 'complete'",
                timeout=1200,
            )
        except Exception:
            pass
        await page.wait_for_timeout(120)

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
