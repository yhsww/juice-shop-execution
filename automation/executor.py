from __future__ import annotations

from dataclasses import dataclass
from time import monotonic

from playwright.async_api import Page, TimeoutError as PlaywrightTimeoutError

from automation.locator import resolve
from automation.observer import UIState, describe_change, meaningful_change, observe, wait_for_stable_ui
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
    state_before: UIState | None = None
    state_after: UIState | None = None


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


async def _dismiss_blocking_overlay(page) -> bool:
    """Dismiss only a clearly blocking, dismissible overlay."""
    candidates = page.locator(
        "[role='dialog']:visible, .cdk-overlay-pane:visible, "
        ".mat-mdc-dialog-container:visible"
    )
    try:
        count = await candidates.count()
    except Exception:
        return False

    for index in range(count):
        dialog = candidates.nth(index)
        try:
            if not await dialog.is_visible():
                continue

            close = dialog.get_by_role("button", name="Dismiss", exact=True)
            if not await close.count():
                close = dialog.get_by_role("button", name="Close", exact=True)
            if not await close.count():
                close = dialog.locator(
                    "[aria-label='Dismiss'], [aria-label='Close']"
                )

            if await close.count() and await close.first.is_visible():
                await close.first.click(timeout=1200)
                await page.wait_for_timeout(120)
                return True
        except Exception:
            continue

    # Cookie banner is a non-modal overlay.
    cookie = page.locator(
        "#cookieconsent, .cc-window, [class*='cookieconsent'], "
        "[class*='cc-window']"
    )
    try:
        for index in range(await cookie.count()):
            banner = cookie.nth(index)
            if not await banner.is_visible():
                continue

            button = banner.get_by_role(
                "button",
                name="Me want it!",
                exact=False,
            )
            if not await button.count():
                button = banner.locator(
                    "button, [role='button']"
                ).filter(has_text="Me want it")

            if await button.count() and await button.first.is_visible():
                await button.first.click(timeout=1200)
                await page.wait_for_timeout(150)
                return True
    except Exception:
        pass

    return False

async def _click(locator) -> None:
    """Click a control with generic overlay and Angular Material recovery."""
    await _scroll_into_view(locator)
    first_error = None
    try:
        await locator.click(timeout=settings.action_timeout_ms)
    except Exception as exc:
        first_error = exc
        if await _dismiss_blocking_overlay(locator.page):
            await locator.page.wait_for_timeout(120)
        try:
            await locator.click(timeout=settings.action_timeout_ms)
        except Exception:
            try:
                visible_dialog = locator.page.locator("[role='dialog']:visible, .cdk-overlay-pane:visible, .mat-mdc-dialog-container:visible")
                if await visible_dialog.count() == 0:
                    await locator.click(timeout=1500, force=True)
                else:
                    raise first_error
            except Exception:
                raise first_error
    # Radio components must be clicked only once. Angular Material may also
    # emit a row click handler, but clicking the containing row after the radio
    # can toggle the same SelectionModel a second time and leave Continue
    # disabled. The resolver/precondition layer is responsible for locating
    # the semantic radio; do not add a second interaction here.

async def _fill(locator, value: str) -> None:
    """Fill native text controls while transparently handling native selects.

    Scenario data sometimes models a form field semantically as FILL even when
    a Juice Shop version renders that field as an Angular Material select.
    Keep the scenario language stable and adapt the interaction to the real
    control type instead of adding page-specific selectors.
    """
    await _scroll_into_view(locator)

    try:
        tag_name = (await locator.evaluate("(el) => el.tagName")).upper()
    except Exception:
        tag_name = ""

    if tag_name == "MAT-SELECT":
        await _select_option(locator, value)
        return

    if tag_name == "SELECT":
        try:
            await locator.select_option(value, timeout=settings.action_timeout_ms)
        except Exception:
            await locator.select_option(label=value, timeout=settings.action_timeout_ms)
        return

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
        options = locator.page.locator(
            "[role='option'], .mat-mdc-option"
        )
        wanted = " ".join(str(value).split()).strip().casefold()

        async def find_visible_option():
            try:
                count = await options.count()
            except Exception:
                return None

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
                        return option
                except Exception:
                    continue

            return None

        # Angular Material renders mat-select options in a CDK overlay. If
        # another overlay is already open, clicking the trigger again is
        # incorrect: the backdrop intercepts the click. Reuse an already
        # visible matching option first, then open the select only when needed.
        option = await find_visible_option()

        if option is None:
            try:
                await locator.click(timeout=settings.action_timeout_ms)
            except Exception as first_error:
                # A stale/open overlay can make the trigger unclickable. Give
                # Angular a brief chance to settle and inspect the overlay again
                # before failing the whole action.
                await locator.page.wait_for_timeout(150)
                option = await find_visible_option()
                if option is None:
                    try:
                        await locator.press("Escape", timeout=1000)
                    except Exception:
                        pass
                    await locator.page.wait_for_timeout(100)
                    await locator.click(timeout=settings.action_timeout_ms)
                else:
                    pass

        if option is None:
            deadline = monotonic() + settings.action_timeout_ms / 1000
            while monotonic() < deadline:
                option = await find_visible_option()
                if option is not None:
                    break
                await locator.page.wait_for_timeout(100)

        if option is None:
            raise RuntimeError(
                f"Opção de seleção não encontrada: {value!r}"
            )

        await _scroll_into_view(option)

        # The option lives inside the CDK overlay, not inside the mat-select
        # element. Clicking the option is therefore the correct interaction
        # point and also closes the overlay through Angular Material's normal
        # selection lifecycle.
        await option.click(timeout=settings.action_timeout_ms)
        return

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
            locator = None
            # Angular/Material controls can exist only after the route settles.
            for _ in range(40):
                locator = await resolve(page, action.get("target", {}))
                if locator is not None:
                    break
                await page.wait_for_timeout(250)

            if locator is None:
                raise RuntimeError("Elemento alvo não encontrado ou não visível.")

            if action.get("expect_new_page"):
                before_url = page.url
                try:
                    async with page.context.expect_page(timeout=2500) as page_info:
                        await _click(locator)
                    new_page = await page_info.value
                    try:
                        await new_page.wait_for_load_state(
                            "domcontentloaded",
                            timeout=settings.navigation_timeout_ms,
                        )
                    except Exception:
                        pass
                    await new_page.wait_for_timeout(150)
                    action["_new_page_url"] = new_page.url
                except PlaywrightTimeoutError:
                    await page.wait_for_timeout(300)
                    after_url = page.url
                    if after_url != before_url:
                        action["_new_page_url"] = after_url
                    else:
                        raise RuntimeError(
                            "A ação esperava abrir uma nova página/aba, mas não houve nova página nem navegação na aba atual."
                        )
                except Exception as exc:
                    await page.wait_for_timeout(200)
                    after_url = page.url
                    if after_url != before_url:
                        action["_new_page_url"] = after_url
                    else:
                        raise RuntimeError(
                            f"A ação esperava abrir uma nova página/aba, mas isso não ocorreu: {exc}"
                        )
            else:
                await _click(locator)

        elif kind == "CLICK_ALL":
            # Generic repeated-click primitive for actions whose semantics are
            # explicitly plural (for example, clearing a basket). The target
            # is resolved afresh after every click because Angular re-renders
            # the table after mutations.
            max_clicks = max(1, min(int(action.get("max_clicks", 20)), 100))
            clicked = 0

            for _ in range(max_clicks):
                locator = await resolve(page, action.get("target", {}))
                if locator is None:
                    break
                await _click(locator)
                clicked += 1
                await page.wait_for_timeout(
                    min(250, max(50, settings.action_timeout_ms // 40))
                )

            if clicked == 0:
                raise RuntimeError(
                    "Nenhum elemento correspondente à ação repetitiva foi encontrado."
                )
        elif kind == "FILL":
            locator = None

            # Angular pages can expose the route before the form controls have
            # finished rendering. Resolve generically with a short retry window
            # instead of baking page/scenario-specific waits into the scenarios.
            for attempt in range(40):
                locator = await resolve(page, action.get("target", {}))
                if locator is not None:
                    break
                await page.wait_for_timeout(250)

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
        elif kind == "ASSERT_ENABLED":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Elemento alvo não encontrado para ASSERT_ENABLED.")
            if not await locator.is_enabled():
                raise AssertionError("O controle deveria estar habilitado, mas está desabilitado.")
        elif kind == "ASSERT_DISABLED":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Elemento alvo não encontrado para ASSERT_DISABLED.")
            if await locator.is_enabled():
                raise AssertionError("O controle deveria estar desabilitado, mas está habilitado.")
        elif kind == "ASSERT_SELECTED":
            locator = await resolve(page, action.get("target", {}))
            if locator is None:
                raise RuntimeError("Elemento alvo não encontrado para ASSERT_SELECTED.")
            selected = (await locator.get_attribute("aria-checked") or "").casefold()
            if selected != "true":
                try:
                    checked = await locator.is_checked()
                except Exception:
                    checked = False
                if not checked:
                    raise AssertionError("O controle deveria estar selecionado.")
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

    # Angular/Material can finish rendering after the action returns. Wait for
    # a generic settled UI state before recording the observation.
    after = await _safe_observe(page, before)

    # Preserve the first post-action observation before waiting for Angular to
    # settle. This matters for transient UI feedback such as snackbar/toast
    # messages: they are valid evidence of the action even when they disappear
    # before the final stable snapshot.
    immediate_observation = describe_change(before, after)

    after = await wait_for_stable_ui(
        page,
        initial=after,
        timeout_ms=1200,
        sample_interval_ms=120,
    )

    stable_observation = describe_change(before, after)
    observed_result = stable_observation
    if immediate_observation != stable_observation:
        observed_result = (
            f"{immediate_observation} | Estado estável: {stable_observation}"
        )[:1200]

    url_after = str(action.get("_new_page_url") or after.url)

    return ActionResult(
        action=kind,
        user_action=_user_action(action),
        data=data,
        url_before=before.url,
        url_after=url_after,
        observed_result=describe_change(before, after),
        changed=meaningful_change(before, after),
        success=error is None,
        error=error,
        state_before=before,
        state_after=after,
    )
