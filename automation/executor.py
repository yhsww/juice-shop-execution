from __future__ import annotations

import asyncio
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


async def _install_mutation_observer(page: Page) -> None:
    """Install a short-lived, page-generic mutation recorder.

    This is black-box evidence collection: it does not target a scenario,
    component or framework. It records visible text introduced/changed while
    an action is executing, including transient Angular/Material feedback
    that may disappear before the final stable snapshot.
    """
    try:
        await page.evaluate("""
            () => {
                if (window.__ambolsMutationObserver) {
                    try { window.__ambolsMutationObserver.disconnect(); } catch (_) {}
                }
                window.__ambolsMutationBuffer = [];
                const visibleText = (node) => {
                    if (!node || node.nodeType !== Node.ELEMENT_NODE) return '';
                    const el = node;
                    const style = window.getComputedStyle(el);
                    if (style.display === 'none' || style.visibility === 'hidden') return '';
                    return String(el.innerText || el.textContent || '').replace(/\\s+/g, ' ').trim();
                };
                const push = (text) => {
                    if (!text) return;
                    const item = text.slice(0, 1200);
                    if (!window.__ambolsMutationBuffer.includes(item)) {
                        window.__ambolsMutationBuffer.push(item);
                    }
                    if (window.__ambolsMutationBuffer.length > 80) {
                        window.__ambolsMutationBuffer.shift();
                    }
                };
                const observer = new MutationObserver((records) => {
                    for (const record of records) {
                        if (record.type === 'characterData') {
                            push(visibleText(record.target.parentElement));
                        }
                        for (const node of record.addedNodes) {
                            push(visibleText(node));
                        }
                    }
                });
                observer.observe(document.documentElement, {
                    subtree: true,
                    childList: true,
                    characterData: true,
                });
                window.__ambolsMutationObserver = observer;
            }
        """)
    except Exception:
        pass


async def _collect_mutation_text(page: Page) -> list[str]:
    try:
        values = await page.evaluate("""
            () => {
                const values = Array.isArray(window.__ambolsMutationBuffer)
                    ? window.__ambolsMutationBuffer.slice()
                    : [];
                try { window.__ambolsMutationObserver?.disconnect(); } catch (_) {}
                window.__ambolsMutationObserver = null;
                window.__ambolsMutationBuffer = [];
                return values;
            }
        """)
        return [str(v).strip() for v in values if str(v).strip()]
    except Exception:
        return []


async def _scroll_into_view(locator) -> None:
    try:
        await locator.scroll_into_view_if_needed(timeout=1500)
    except Exception:
        pass


async def _dismiss_blocking_overlay(page) -> bool:
    """Dismiss only known, clearly non-functional overlays that block input."""
    cookie_containers = page.locator(
        "[aria-label='cookieconsent']:visible, "
        ".cc-window:visible, .cc-floating:visible, .cc-banner:visible"
    )
    try:
        cookie_count = await cookie_containers.count()
    except Exception:
        cookie_count = 0

    # CookieConsent labels are configurable/localized. Prefer the component's
    # own compliance button rather than guessing its text.
    for index in range(cookie_count):
        container = cookie_containers.nth(index)
        try:
            if not await container.is_visible():
                continue
            buttons = container.locator(
                ".cc-btn.cc-allow, .cc-btn.cc-dismiss, "
                ".cc-btn, .cc-compliance button, button, [role='button']"
            )
            for button_index in range(await buttons.count()):
                button = buttons.nth(button_index)
                if await button.is_visible():
                    try:
                        await button.click(timeout=1200)
                    except Exception:
                        await button.click(timeout=1200, force=True)
                    await page.wait_for_timeout(120)
                    return True
        except Exception:
            continue

    # Application dialogs are handled only when an explicit dismiss/close
    # affordance exists. Never click an arbitrary business-action button.
    candidates = page.locator(
        "[role='dialog']:visible, [role='alertdialog']:visible, "
        ".cdk-overlay-pane:visible, .mat-mdc-dialog-container:visible"
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
    return False

async def _click(locator) -> None:
    """Click a control with generic overlay and Angular Material recovery."""
    page = locator.page
    await _scroll_into_view(locator)

    # Avoid spending the full action timeout on a consent/welcome layer that
    # is known to be outside the behavior under test.
    await _dismiss_blocking_overlay(page)

    first_error = None
    try:
        await locator.click(timeout=settings.action_timeout_ms)
    except Exception as exc:
        first_error = exc
        if await _dismiss_blocking_overlay(page):
            await page.wait_for_timeout(120)
        try:
            await locator.click(timeout=settings.action_timeout_ms)
        except Exception:
            # CookieConsent is infrastructure UI, not application behavior.
            # If it remains visible after the semantic dismissal attempt,
            # force-click only the original user target instead of letting a
            # fixed consent layer turn a valid UI action into an automation
            # error. Functional dialogs still block the action.
            cookie_visible = False
            try:
                cookie_visible = await page.locator(
                    "[aria-label='cookieconsent']:visible, "
                    ".cc-window:visible, .cc-floating:visible, .cc-banner:visible"
                ).count() > 0
            except Exception:
                pass

            if cookie_visible:
                try:
                    await locator.click(timeout=1500, force=True)
                    return
                except Exception:
                    pass

            try:
                visible_dialog = page.locator(
                    "[role='dialog']:visible, [role='alertdialog']:visible, "
                    ".cdk-overlay-pane:visible, .mat-mdc-dialog-container:visible"
                )
                if await visible_dialog.count() == 0:
                    await locator.click(timeout=1500, force=True)
                else:
                    raise first_error
            except Exception:
                raise first_error

    # Radio components must be clicked only once. The resolver/precondition
    # layer is responsible for locating the semantic radio; do not add a
    # second row interaction that can toggle the same SelectionModel.

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


async def _click_target(page: Page, target: dict, attempts: int = 5) -> None:
    """Resolve and click a semantic target, recovering from SPA re-rendering.

    A semantic resolver can legitimately return a nested label/span when the
    framework has not finished exposing the final ARIA tree. Before clicking,
    normalize such a result to its nearest interactive ancestor. This is
    framework-generic and avoids selectors tied to individual scenarios.
    """
    last_error: Exception | None = None
    requested_role = str(target.get("role") or "").casefold()

    for _ in range(max(1, attempts)):
        locator = await resolve(page, target)
        if locator is None:
            await page.wait_for_timeout(150)
            continue

        try:
            if requested_role in {"button", "link"}:
                try:
                    tag = (await locator.evaluate("(el) => el.tagName")).lower()
                except Exception:
                    tag = ""

                if tag not in {"button", "a"}:
                    ancestor = locator.locator(
                        "xpath=ancestor-or-self::*[self::button or self::a "
                        "or @role='button' or @role='link'][1]"
                    )
                    if await ancestor.count() and await ancestor.first.is_visible():
                        locator = ancestor.first

            # Give Angular one render turn before interacting. The target is
            # resolved again on every retry, so this is not a scenario wait.
            await page.wait_for_timeout(80)
            await _click(locator)
            return
        except Exception as exc:
            last_error = exc

            # Angular Material/CDK menus can replace the menu item between
            # Playwright's actionability check and the native click. Re-resolve
            # the semantic target and, only for a detached-node failure, use the
            # DOM click handler as a last-resort event delivery mechanism.
            if "detached from the DOM" in str(exc).casefold():
                try:
                    fresh = await resolve(page, target)
                    if fresh is not None:
                        await fresh.evaluate("(el) => el.click()")
                        return
                except Exception:
                    pass

            await page.wait_for_timeout(180)

    if last_error is not None:
        raise last_error
    raise RuntimeError("Elemento alvo não encontrado ou não visível.")

async def execute(page: Page, action: dict) -> ActionResult:
    before = await observe(page)
    await _install_mutation_observer(page)
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
            target = action.get("target", {})

            if action.get("expect_new_page"):
                # "External outcome" is deliberately broader than "new tab":
                # browser actions may yield a popup, a download, or a current
                # page navigation. Observe all three without changing the UI
                # action itself.
                original_url = page.url
                pages_before = set(page.context.pages)
                downloads: list = []
                pdf_responses: list = []

                def on_download(download):
                    downloads.append(download)

                async def inspect_pdf_response(response):
                    try:
                        content_type = (response.headers.get("content-type") or "").casefold()
                        url = response.url.casefold()
                        if ".pdf" in url or "application/pdf" in content_type:
                            pdf_responses.append(response)
                    except Exception:
                        pass

                page.on("download", on_download)
                page.on("response", inspect_pdf_response)
                try:
                    await _click_target(page, target)
                    await page.wait_for_timeout(1200)

                    if pdf_responses:
                        action["_new_page_url"] = pdf_responses[-1].url

                    new_pages = [
                        candidate for candidate in page.context.pages
                        if candidate not in pages_before
                    ]
                    if pdf_responses:
                        # Prefer an observed PDF response over unrelated popups
                        # (for example a help/tutorial tab opened by the UI).
                        action["_new_page_url"] = pdf_responses[-1].url
                    elif new_pages:
                        new_page = new_pages[-1]
                        try:
                            await new_page.wait_for_load_state(
                                "domcontentloaded",
                                timeout=settings.navigation_timeout_ms,
                            )
                        except Exception:
                            pass
                        await new_page.wait_for_timeout(150)
                        action["_new_page_url"] = new_page.url
                    elif downloads:
                        # Download URLs are real browser-observable outcomes
                        # and are valid evidence even when Chromium never opens
                        # a PDF in a separate tab.
                        action["_new_page_url"] = downloads[-1].url
                        action["_download_filename"] = downloads[-1].suggested_filename
                    elif page.url != original_url:
                        action["_new_page_url"] = page.url
                    else:
                        # Do not manufacture a navigation. Keep the click
                        # successful and let the scenario validator decide
                        # whether its declared observable outcome was actually
                        # satisfied.
                        action["_external_outcome_observed"] = False
                finally:
                    try:
                        page.remove_listener("download", on_download)
                    except Exception:
                        pass
                    try:
                        page.remove_listener("response", inspect_pdf_response)
                    except Exception:
                        pass
            else:
                await _click_target(page, target)

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
            target = action.get("target", {})
            locator = await resolve(page, target)

            if locator is None and target.get("role") == "radio":
                name = str(target.get("name") or target.get("text") or "").strip()
                if name:
                    rows = page.locator(
                        "mat-row, tr, [role='row'], "
                        ".mat-mdc-list-item, .mat-mdc-radio-button"
                    )
                    for index in range(await rows.count()):
                        row = rows.nth(index)
                        try:
                            if not await row.is_visible():
                                continue
                            row_text = " ".join((await row.inner_text()).split())
                            if name.casefold() not in row_text.casefold():
                                continue
                            radio = row.locator(
                                "[role='radio'], input[type='radio'], mat-radio-button"
                            )
                            if await radio.count():
                                locator = radio.first
                                break
                        except Exception:
                            continue

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

    # Capture transient evidence before stability can erase it. In addition
    # to semantic UI snapshots, a short-lived MutationObserver records text
    # that appeared and disappeared between snapshots.
    immediate_states: list[UIState] = []
    first_after = await _safe_observe(page, before)
    immediate_states.append(first_after)

    transient_deadline = monotonic() + 1.5
    while monotonic() < transient_deadline:
        await page.wait_for_timeout(120)
        snapshot = await _safe_observe(page, before)
        immediate_states.append(snapshot)
        if snapshot.messages:
            break

    mutation_text = await _collect_mutation_text(page)

    after = await wait_for_stable_ui(
        page,
        initial=immediate_states[-1],
        timeout_ms=900,
        sample_interval_ms=120,
    )

    transient_messages: list[str] = []
    transient_text: list[str] = []
    for snapshot in immediate_states:
        for message in snapshot.messages:
            if message and message not in transient_messages:
                transient_messages.append(message)
        if snapshot.visible_text and snapshot.visible_text not in transient_text:
            transient_text.append(snapshot.visible_text)

    observed = describe_change(before, after)
    if mutation_text:
        observed = (
            observed + " "
            + "Texto transitório capturado: "
            + " | ".join(mutation_text[-5:])[:1200]
        )
        for item in mutation_text:
            if item not in transient_messages:
                transient_messages.append(item)
    if transient_messages:
        observed = (
            observed + " "
            + "Mensagem transitória: "
            + " | ".join(transient_messages[:5])
        )
    elif transient_text:
        # Keep a compact transient-text signal for feedback rendered outside
        # the standard alert/snackbar selectors.
        observed = (
            observed + " "
            + "Texto observado durante a ação: "
            + " | ".join(transient_text[-2:])[:900]
        )

    url_after = str(action.get("_new_page_url") or after.url)

    return ActionResult(
        action=kind,
        user_action=_user_action(action),
        data=data,
        url_before=before.url,
        url_after=url_after,
        observed_result=observed,
        changed=meaningful_change(before, after),
        success=error is None,
        error=error,
        messages=tuple(transient_messages[:20]),
        state_before=before,
        state_after=after,
    )
