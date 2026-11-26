from __future__ import annotations

import asyncio
from dataclasses import dataclass
from time import monotonic

from playwright.async_api import Page, TimeoutError as PlaywrightTimeoutError

from automation.locator import first_visible, resolve
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
    deadline = monotonic() + 1.8
    while monotonic() < deadline:
        try:
            return await observe(page)
        except Exception:
            await page.wait_for_timeout(80)
    return fallback


def _norm_text(value: object) -> str:
    return " ".join(str(value or "").split()).strip().casefold()


async def _install_mutation_observer(page: Page) -> None:
    """Install a short-lived, page-generic mutation recorder.

    The collector is deliberately framework-agnostic. It records visible text
    from changed nodes and their nearby visible ancestors so feedback rendered
    by Angular Material/CDK is captured even when the message is inserted into
    an existing overlay container instead of arriving as a new top-level node.
    """
    try:
        await page.evaluate("""
            () => {
                if (window.__ambolsMutationObserver) {
                    try { window.__ambolsMutationObserver.disconnect(); } catch (_) {}
                }

                window.__ambolsMutationBuffer = [];
                const normalize = (value) =>
                    String(value || '').replace(/\\s+/g, ' ').trim();

                const visible = (el) => {
                    if (!el || el.nodeType !== Node.ELEMENT_NODE) return '';
                    try {
                        const style = window.getComputedStyle(el);
                        if (
                            style.display === 'none' ||
                            style.visibility === 'hidden' ||
                            style.opacity === '0'
                        ) {
                            return '';
                        }
                        const rect = el.getBoundingClientRect();
                        if (rect.width === 0 || rect.height === 0) return '';
                    } catch (_) {}
                    return normalize(el.innerText || el.textContent);
                };

                const push = (value) => {
                    const text = normalize(value);
                    if (!text || text.length > 1600) return;
                    if (!window.__ambolsMutationBuffer.includes(text)) {
                        window.__ambolsMutationBuffer.push(text);
                    }
                    if (window.__ambolsMutationBuffer.length > 120) {
                        window.__ambolsMutationBuffer.shift();
                    }
                };

                const captureContext = (node) => {
                    let current =
                        node && node.nodeType === Node.ELEMENT_NODE
                            ? node
                            : node && node.parentElement;

                    let depth = 0;
                    while (current && depth < 5) {
                        const text = visible(current);
                        if (text) push(text);

                        const role = String(current.getAttribute?.('role') || '').toLowerCase();
                        const ariaLive = String(current.getAttribute?.('aria-live') || '').toLowerCase();
                        const className = String(current.className || '').toLowerCase();

                        if (
                            role === 'alert' ||
                            role === 'status' ||
                            ariaLive === 'assertive' ||
                            ariaLive === 'polite' ||
                            /snack|toast|notification|alert|error/.test(className)
                        ) {
                            break;
                        }

                        current = current.parentElement;
                        depth += 1;
                    }
                };

                const observer = new MutationObserver((records) => {
                    for (const record of records) {
                        captureContext(record.target);

                        // Some Angular Material feedback is revealed by a class
                        // or style transition on an already-mounted overlay node.
                        // Capture the current visible document text as a bounded
                        // supplemental signal whenever the DOM changes.
                        if (document.body) {
                            push(document.body.innerText || document.body.textContent);
                        }

                        for (const node of record.addedNodes) {
                            captureContext(node);
                        }

                        if (record.type === 'characterData') {
                            captureContext(record.target);
                        }
                    }
                });

                observer.observe(document.documentElement, {
                    subtree: true,
                    childList: true,
                    characterData: true,
                    attributes: true,
                    attributeFilter: ['class', 'style', 'aria-live', 'role'],
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
    """Click a control with bounded actionability recovery.

    A click must not consume the entire global action budget merely waiting
    for Playwright actionability. The executor already has a scenario-level
    timeout, so this primitive uses a short retry budget and then applies a
    generic force-click fallback only when no functional dialog is blocking.
    """
    page = locator.page
    await _scroll_into_view(locator)

    # Keep click actionability bounded. A blocked target is recoverable through
    # overlay dismissal or a fresh semantic resolution; it should not consume
    # the whole 20s action budget before those recovery paths run.
    click_timeout = min(
        3000,
        max(800, int(settings.action_timeout_ms)),
    )

    await _dismiss_blocking_overlay(page)

    first_error = None
    try:
        await locator.click(timeout=click_timeout)
    except Exception as exc:
        first_error = exc
        # Some Angular components expose the user interaction on the host
        # element while Playwright's actionability check is blocked by a
        # transparent/animated layer. Deliver one native DOM click before
        # retrying expensive actionability paths. This is generic and preserves
        # the component's real event handlers.
        try:
            await locator.evaluate("(el) => el.click()")
            return
        except Exception:
            pass
        if await _dismiss_blocking_overlay(page):
            await page.wait_for_timeout(120)
        try:
            await locator.click(timeout=click_timeout)
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

async def _read_control_value(locator) -> str | None:
    """Read the current value of a text-like control without assuming its DOM type."""
    try:
        tag_name = (await locator.evaluate("(el) => el.tagName")).upper()
    except Exception:
        return None

    if tag_name in {"INPUT", "TEXTAREA", "SELECT"}:
        try:
            return str(await locator.input_value())
        except Exception:
            return None

    try:
        value = await locator.get_attribute("value")
        return str(value) if value is not None else None
    except Exception:
        return None


async def _fill(locator, value: str) -> None:
    """Fill native text controls and verify the value actually reached the control.

    Angular Material forms can re-render a control during change detection.
    A successful Playwright fill call therefore is not, by itself, sufficient
    evidence that the intended value survived in the live DOM. The primitive
    verifies the resulting value and retries through a generic focus/type path
    when the framework replaced or reset the control.

    Scenario definitions remain semantic; no page- or scenario-specific
    selector is introduced here.
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

    async def verified(stable: bool = False) -> bool:
        current = await _read_control_value(locator)
        if current != value:
            return False

        # Angular can accept the DOM mutation and then recreate the control
        # during change detection. A single immediate read is therefore not
        # enough evidence that the value survived. For a stable check, sample
        # the live locator again after a short framework-settling interval.
        if stable:
            await locator.page.wait_for_timeout(120)
            current = await _read_control_value(locator)

        return current == value

    try:
        await locator.fill(value, timeout=settings.action_timeout_ms)
        if await verified(stable=True):
            return
    except Exception:
        pass

    # The first fill may have targeted a control instance that Angular replaced
    # immediately after the input event. Recover with a real keyboard sequence
    # against the live locator so Angular receives the same input/change events
    # a user would generate.
    try:
        await _click(locator)
        await locator.press("ControlOrMeta+A", timeout=1500)
        await locator.press("Backspace", timeout=1500)
        # Prefer Playwright's user-like sequential keyboard path for
        # controls that attach custom Angular input handlers.
        await locator.press_sequentially(
            value,
            timeout=settings.action_timeout_ms,
        )

        # Some Angular controls replace the native node during change
        # detection. If the keyboard path still does not survive, update the
        # live DOM property through its native setter and emit the normal input
        # lifecycle. This remains generic and is only a recovery path.
        try:
            await locator.evaluate(
                """(el, nextValue) => {
                    const proto = Object.getPrototypeOf(el);
                    const descriptor =
                        Object.getOwnPropertyDescriptor(proto, 'value') ||
                        Object.getOwnPropertyDescriptor(
                            Object.getPrototypeOf(proto),
                            'value'
                        );
                    if (descriptor && descriptor.set) {
                        descriptor.set.call(el, nextValue);
                    } else {
                        el.value = nextValue;
                    }
                    el.dispatchEvent(new Event('input', { bubbles: true }));
                    el.dispatchEvent(new Event('change', { bubbles: true }));
                    el.dispatchEvent(new Event('blur', { bubbles: true }));
                }""",
                value,
            )
        except Exception:
            pass

        if await verified(stable=True):
            return
    except Exception:
        pass

    current = await _read_control_value(locator)
    raise RuntimeError(
        f"O campo não reteve o valor informado. "
        f"Esperado={value!r}; atual={current!r}."
    )



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


async def _click_visible_menuitem_host(page: Page, value: str) -> bool:
    """Click the live Angular Material menu-item host without locator races.

    Angular Material/CDK can replace an overlay item between Locator resolution
    and Playwright actionability checks. A Locator.evaluate() call can then wait
    for a detached element until the full timeout. For menu items, resolve the
    current visible host directly inside the page and invoke its native click
    in the same DOM turn. This remains generic: the scenario supplies only the
    semantic menu-item name.
    """
    wanted = _norm_text(value)
    if not wanted:
        return False

    try:
        clicked = await page.evaluate(
            """
            (wanted) => {
                const normalize = (value) =>
                    String(value || '').replace(/\\s+/g, ' ').trim().toLowerCase();

                const tokenSet = (value) =>
                    new Set(
                        normalize(value)
                            .replace(/[^\\p{L}\\p{N}]+/gu, ' ')
                            .split(' ')
                            .filter(Boolean)
                    );

                const matches = (actual) => {
                    const a = normalize(actual);
                    if (!a) return false;
                    if (a === wanted || a.includes(wanted) || wanted.includes(a)) {
                        return true;
                    }

                    const wantedTokens = tokenSet(wanted);
                    const actualTokens = tokenSet(a);
                    if (!wantedTokens.size) return false;

                    for (const token of wantedTokens) {
                        if (!actualTokens.has(token)) return false;
                    }
                    return true;
                };

                const visible = (el) => {
                    if (!el) return false;
                    const style = window.getComputedStyle(el);
                    if (
                        style.display === 'none' ||
                        style.visibility === 'hidden' ||
                        style.pointerEvents === 'none'
                    ) {
                        return false;
                    }
                    const rect = el.getBoundingClientRect();
                    return rect.width > 0 && rect.height > 0;
                };

                const selectors = [
                    "[role='menu']:not([aria-hidden='true']) button[mat-menu-item]",
                    "[role='menu']:not([aria-hidden='true']) a[mat-menu-item]",
                    ".mat-mdc-menu-panel button[mat-menu-item]",
                    ".mat-mdc-menu-panel a[mat-menu-item]",
                    ".mat-menu-panel button[mat-menu-item]",
                    ".mat-menu-panel a[mat-menu-item]",
                    "button[mat-menu-item]",
                    "a[mat-menu-item]",
                    "[mat-menu-item][role='menuitem']",
                    "[role='menuitem']"
                ];

                const seen = new Set();

                for (const selector of selectors) {
                    for (const el of document.querySelectorAll(selector)) {
                        if (seen.has(el) || !visible(el)) continue;
                        seen.add(el);

                        const values = [
                            el.innerText,
                            el.getAttribute('aria-label'),
                            el.getAttribute('title')
                        ];

                        if (values.some(matches)) {
                            el.click();
                            return true;
                        }
                    }
                }

                return false;
            }
            """,
            wanted,
        )
        return bool(clicked)
    except Exception:
        return False


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
        # Angular Material menu items are transient overlay hosts, and some
        # scenario definitions describe them only by visible text instead of
        # role=menuitem. When a menu is visibly open, use the same semantic
        # live-host path for any click target that supplies a text/name value.
        # This keeps the recovery generic while avoiding a hard-coded scenario
        # selector or scenario ID.
        menu_value = str(
            target.get("name") or target.get("text") or target.get("label") or ""
        ).strip()
        if menu_value:
            try:
                visible_menu = page.locator(
                    "[role='menu']:visible, "
                    ".mat-mdc-menu-panel:visible, "
                    ".mat-menu-panel:visible"
                )
                if await visible_menu.count():
                    if await _click_visible_menuitem_host(page, menu_value):
                        return
            except Exception:
                pass

        locator = await resolve(page, target)
        if locator is None:
            await page.wait_for_timeout(150)
            continue

        try:
            if requested_role == "menuitem":
                try:
                    tag = (await locator.evaluate("(el) => el.tagName")).lower()
                except Exception:
                    tag = ""
                if tag not in {"mat-menu-item"}:
                    ancestor = locator.locator(
                        "xpath=ancestor-or-self::*["
                        "self::mat-menu-item or @role='menuitem' or @mat-menu-item"
                        "][1]"
                    )
                    if await ancestor.count() and await ancestor.first.is_visible():
                        locator = ancestor.first

            if requested_role in {"button", "link", "menuitem"}:
                try:
                    tag = (await locator.evaluate("(el) => el.tagName")).lower()
                except Exception:
                    tag = ""

                allowed_tags = {
                    "button",
                    "a",
                    "mat-menu-item",
                }
                if tag not in allowed_tags:
                    ancestor = locator.locator(
                        "xpath=ancestor-or-self::*["
                        "self::button or self::a or self::mat-menu-item "
                        "or @role='button' or @role='link' or @role='menuitem'"
                        "][1]"
                    )
                    if await ancestor.count() and await ancestor.first.is_visible():
                        locator = ancestor.first

            # A row target is itself an interaction target in Juice Shop
            # checkout tables: the application attaches the selection handler
            # to the mat-row/tr. Descending into the radio is unsafe because the
            # radio click also bubbles to the row and can toggle the same
            # SelectionModel twice. Keep the semantic row as the click target.

            # Radio actions are selection intents, not toggle intents.
            # Text-only scenario targets such as "0002" or "Standard Delivery"
            # can legitimately resolve directly to a mat-radio-button even
            # when no role was declared. Treat the real resolved control as a
            # radio so its Angular selection lifecycle is handled consistently.
            try:
                resolved_tag = (await locator.evaluate("(el) => el.tagName")).lower()
                resolved_role = (await locator.get_attribute("role") or "").casefold()
            except Exception:
                resolved_tag = ""
                resolved_role = ""
            effective_radio = (
                requested_role == "radio"
                or resolved_tag == "mat-radio-button"
                or resolved_role == "radio"
            )

            # When possible, use the native radio input so Angular Material's
            # selection lifecycle receives the same event as a user choice.
            if effective_radio:
                try:
                    selected = (await locator.get_attribute("aria-checked") or "").casefold()
                except Exception:
                    selected = ""
                # A selected radio can still require a click to notify its
                # parent component. Native radios do not toggle off when clicked
                # while selected, so always deliver one host click and verify the
                # resulting component state.

                # Material radios are not native inputs from the scenario's
                # point of view. Playwright.check() may update the nested input
                # without delivering the host component's (click) handler,
                # which is exactly how Juice Shop emits payment selection.
                # Prefer the host click, then verify the component state.
                await page.wait_for_timeout(60)
                await _click(locator)
                await page.wait_for_timeout(100)

                def _selected_semantically() -> bool:
                    return False

                try:
                    selected = (await locator.get_attribute("aria-checked") or "").casefold()
                except Exception:
                    selected = ""

                if selected == "true":
                    return

                try:
                    classes = (await locator.get_attribute("class") or "").casefold()
                    if "mat-radio-checked" in classes:
                        return
                except Exception:
                    pass

                native_radio = locator.locator("input[type='radio']")
                if await native_radio.count():
                    try:
                        if await native_radio.first.is_checked():
                            return
                    except Exception:
                        pass

                if await native_radio.count() and await native_radio.first.is_visible():
                    try:
                        await native_radio.first.check(timeout=1500)
                        await page.wait_for_timeout(100)
                    except Exception:
                        pass

                try:
                    selected = (await locator.get_attribute("aria-checked") or "").casefold()
                except Exception:
                    selected = ""

                if selected == "true":
                    return

                try:
                    classes = (await locator.get_attribute("class") or "").casefold()
                    if "mat-radio-checked" in classes:
                        return
                except Exception:
                    pass

                if await native_radio.count():
                    try:
                        if await native_radio.first.is_checked():
                            return
                    except Exception:
                        pass

                raise RuntimeError(
                    "O radio foi acionado, mas o estado selecionado não foi refletido no componente."
                )

            # Give Angular one render turn before interacting. The target is
            # resolved again on every retry, so this is not a scenario wait.
            await page.wait_for_timeout(80)
            await _click(locator)

            if requested_role == "row":
                # Checkout rows own the Angular selection handler. If a ripple
                # or translated wrapper swallowed the row event, recover only
                # when the row's own radio is still unselected.
                try:
                    radios = locator.locator(
                        "mat-radio-button, [role='radio'], input[type='radio']"
                    )
                    if await radios.count():
                        radio = radios.first
                        if await radio.is_visible():
                            checked = (
                                await radio.get_attribute("aria-checked") or ""
                            ).casefold()
                            if checked != "true":
                                try:
                                    native_checked = await radio.is_checked()
                                except Exception:
                                    native_checked = False
                                if not native_checked:
                                    await _click(radio)
                                    await page.wait_for_timeout(100)
                except Exception:
                    pass

            return
        except Exception as exc:
            last_error = exc

            # Angular Material/CDK overlays can make Playwright's native
            # actionability check fail even though the live component is
            # present and clickable. For semantic menu items and radios, the
            # component's own DOM click is a generic event-delivery fallback.
            if requested_role in {"menuitem", "radio", "row", "button"}:
                try:
                    fresh = await resolve(page, target)
                    if fresh is not None and await fresh.is_visible():
                        await fresh.evaluate("(el) => el.click()")
                        if requested_role == "radio":
                            await page.wait_for_timeout(120)
                            selected = (
                                await fresh.get_attribute("aria-checked") or ""
                            ).casefold()
                            if selected == "true":
                                return
                            classes = (
                                await fresh.get_attribute("class") or ""
                            ).casefold()
                            if "mat-radio-checked" in classes:
                                return
                            native = fresh.locator("input[type='radio']")
                            if await native.count():
                                try:
                                    if await native.first.is_checked():
                                        return
                                except Exception:
                                    pass
                        else:
                            return
                except Exception:
                    pass

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


async def _post_action_settle(page: Page, kind: str) -> None:
    """Apply only the synchronization appropriate to the completed action.

    Scenario WAIT actions are already explicit synchronization points and must
    not be followed by another load/readiness wait. For navigation-like
    actions, allow a short DOM-ready window; for ordinary interactions, one
    render turn is enough. This keeps observation from consuming the action's
    timeout budget.
    """
    if kind == "WAIT":
        return

    if kind == "NAVIGATE":
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=700)
        except PlaywrightTimeoutError:
            pass
        await page.wait_for_timeout(60)
        return

    if kind == "CLICK":
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=700)
        except PlaywrightTimeoutError:
            pass

    await page.wait_for_timeout(60)

async def execute(page: Page, action: dict) -> ActionResult:
    before = await observe(page)
    await _install_mutation_observer(page)
    kind = action["type"].upper()
    data = _action_data(action)
    error: str | None = None

    try:
        if kind == "NAVIGATE":
            route = str(action["route"])
            target_url = f"{settings.base_url}{route}"

            # Juice Shop is an Angular SPA. For hash routes, avoid a full
            # document navigation: network activity is not the navigation
            # condition and can cause false Playwright timeouts.
            app_origin = settings.base_url.rstrip("/")
            current_origin = page.url.split("#", 1)[0].rstrip("/")
            if route.startswith("/#") and current_origin == app_origin:
                target_hash = "#" + route.split("#", 1)[1]
                await page.evaluate(
                    "(hash) => { if (window.location.hash !== hash) window.location.hash = hash; }",
                    target_hash,
                )
                await page.wait_for_timeout(180)
            else:
                await page.goto(
                    target_url,
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
            # Repeated UI mutation (for example, removing every basket item).
            # Resolve the live control directly so Angular re-renders cannot
            # make a previously resolved Locator stale or consume the action
            # timeout while searching a large semantic candidate set.
            max_clicks = max(1, min(int(action.get("max_clicks", 20)), 100))
            target = action.get("target", {})
            wanted = str(
                target.get("name")
                or target.get("label")
                or target.get("text")
                or ""
            ).strip().casefold()
            clicked = 0

            if not wanted:
                raise RuntimeError(
                    "A ação CLICK_ALL não possui um alvo semântico."
                )

            async def _click_live_match() -> bool:
                try:
                    return bool(
                        await page.evaluate(
                            """
                            (wanted) => {
                                const normalize = value =>
                                    String(value || "")
                                        .replace(/\\s+/g, " ")
                                        .trim()
                                        .toLowerCase();

                                const visible = el => {
                                    if (!el) return false;
                                    const style = getComputedStyle(el);
                                    if (
                                        style.display === "none" ||
                                        style.visibility === "hidden" ||
                                        style.opacity === "0"
                                    ) return false;
                                    const rect = el.getBoundingClientRect();
                                    return rect.width > 0 && rect.height > 0;
                                };

                                const semantic = el => normalize([
                                    el.getAttribute?.("aria-label"),
                                    el.getAttribute?.("title"),
                                    el.getAttribute?.("mattooltip"),
                                    el.innerText,
                                    el.textContent
                                ].filter(Boolean).join(" "));

                                // Inspect both interactive hosts and descendants
                                // such as mat-icon. When the label is exposed by
                                // a child icon, click its nearest real control.
                                const nodes = Array.from(
                                    document.querySelectorAll(
                                        "button,a,[role='button'],[role='link'],"
                                        + "mat-icon,[aria-label],[title],[mat-icon-button]"
                                    )
                                );

                                for (const node of nodes) {
                                    if (!visible(node)) continue;

                                    const value = semantic(node);
                                    if (!value.includes(wanted)) continue;

                                    let control = node;
                                    if (!/^(BUTTON|A|MAT-ICON-BUTTON)$/.test(control.tagName)
                                        && control.getAttribute("role") !== "button") {
                                        control = node.closest(
                                            "button,a,[role='button'],[mat-icon-button]"
                                        ) || node;
                                    }

                                    if (!visible(control)) continue;

                                    control.scrollIntoView({
                                        block: "center",
                                        inline: "nearest"
                                    });
                                    control.click();
                                    return true;
                                }

                                return false;
                            }
                            """,
                            wanted,
                        )
                    )
                except Exception:
                    return False

            for _ in range(max_clicks):
                before = await observe(page)

                if not await _click_live_match():
                    break

                clicked += 1
                await page.wait_for_timeout(180)

                after = await _safe_observe(page, before)
                if not meaningful_change(before, after):
                    break

                await page.wait_for_timeout(120)

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

            fill_error: Exception | None = None
            for attempt in range(3):
                try:
                    await _fill(locator, str(action["value"]))
                    fill_error = None
                    break
                except Exception as exc:
                    fill_error = exc
                    # Angular can replace a form control during change detection.
                    # Re-resolve the same semantic target before retrying instead
                    # of keeping a stale Locator instance.
                    if attempt < 2:
                        await page.wait_for_timeout(120)
                        fresh = await resolve(
                            page,
                            action.get("target", {}),
                        )
                        if fresh is not None:
                            locator = fresh

            if fill_error is not None:
                raise fill_error
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
            deadline = monotonic() + 2500 / 1000
            while monotonic() < deadline:
                try:
                    if await locator.is_enabled():
                        break
                except Exception:
                    pass
                await page.wait_for_timeout(100)
                fresh = await resolve(page, action.get("target", {}))
                if fresh is not None:
                    locator = fresh
            else:
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

                # Angular Material radios may expose the selected state on
                # the host class or on the hidden native input instead of
                # aria-checked. Read all semantic representations before
                # declaring the control unselected.
                if not checked:
                    try:
                        classes = (
                            await locator.get_attribute("class") or ""
                        ).casefold()
                        checked = "mat-radio-checked" in classes
                    except Exception:
                        checked = False

                if not checked:
                    try:
                        native = locator.locator(
                            "input[type='radio'], input[type='checkbox']"
                        ).first
                        if await native.count():
                            checked = await native.is_checked()
                    except Exception:
                        checked = False

                if not checked:
                    raise AssertionError("O controle deveria estar selecionado.")
        elif kind == "WAIT":
            await page.wait_for_timeout(int(action.get("milliseconds", 500)))
        else:
            raise ValueError(f"Tipo de ação não suportado: {kind}")

        await _post_action_settle(page, kind)

    except Exception as exc:
        error = str(exc)

    # Capture transient evidence before stability can erase it. In addition
    # to semantic UI snapshots, a short-lived MutationObserver records text
    # that appeared and disappeared between snapshots.
    immediate_states: list[UIState] = []
    first_after = await _safe_observe(page, before)
    immediate_states.append(first_after)

    # WAIT is already a deliberate synchronization point. Keep evidence
    # collection lightweight for it; other actions retain the short transient
    # capture window needed for snackbars/toasts and Angular feedback.
    # Capture a little longer for interaction actions because Angular/Material
    # feedback can be rendered asynchronously after the click event. WAIT is
    # already an explicit synchronization primitive, so it remains lightweight.
    # This is intentionally generic: no scenario or message text is special-cased.
    # Keep the evidence window bounded, but long enough to cover asynchronous
    # Angular/Material feedback that is rendered after the initiating click.
    # This is an observation budget, not an action timeout.
    transient_window = 0.08 if kind == "WAIT" else 1.5
    transient_deadline = monotonic() + transient_window
    while monotonic() < transient_deadline:
        await page.wait_for_timeout(60)
        snapshot = await _safe_observe(page, before)
        immediate_states.append(snapshot)
        if snapshot.messages:
            break

    mutation_text = await _collect_mutation_text(page)

    after = await wait_for_stable_ui(
        page,
        initial=immediate_states[-1],
        timeout_ms=180 if kind == "WAIT" else 320,
        sample_interval_ms=80,
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
