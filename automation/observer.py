from __future__ import annotations

from dataclasses import dataclass
import asyncio
from hashlib import sha256
import re

from playwright.async_api import Page


@dataclass(frozen=True)
class UIState:
    url: str
    title: str
    visible_text: str
    body_hash: str
    messages: tuple[str, ...] = ()
    headings: tuple[str, ...] = ()
    controls: tuple[str, ...] = ()


MESSAGE_SELECTORS = (
    '[role="alert"]:visible',
    '[aria-live]:visible',
    '[role="status"]:visible',
    '.mat-mdc-snack-bar-label:visible',
    '.mat-snack-bar-container:visible',
    '.mat-mdc-form-field-error:visible',
    'mat-error:visible',
    '.mat-error:visible',
    '.cdk-overlay-container [role="status"]:visible',
    '.cdk-overlay-container [role="alert"]:visible',
    '[class*="snack"]:visible',
    '[class*="toast"]:visible',
    '[class*="notification"]:visible',
)

HEADING_SELECTORS = "h1,h2,h3,h4,[role='heading']"

CONTROL_SELECTORS = (
    "button", "a", "input", "textarea", "select", "mat-select",
    "mat-radio-button", "mat-checkbox", "[role='button']",
    "[role='link']", "[role='radio']", "[role='checkbox']",
    "[role='option']", "[role='tab']",
)


async def _texts(page: Page, selector: str) -> list[str]:
    """Read visible text in one DOM round-trip.

    The observer is called before and after every action. Iterating through
    Playwright locators one node at a time can spend the whole action budget
    waiting for nodes that Angular is replacing. A single DOM evaluation keeps
    observation bounded and makes it diagnostic rather than a source of
    automation failures.
    """
    try:
        values = await page.locator(selector).evaluate_all(
            """nodes => nodes
                .filter(node => {
                    const style = window.getComputedStyle(node);
                    return style.display !== 'none' &&
                           style.visibility !== 'hidden' &&
                           !!(node.offsetWidth || node.offsetHeight ||
                              node.getClientRects().length);
                })
                .map(node => (node.innerText || node.textContent || '')
                    .replace(/\\s+/g, ' ').trim())
                .filter(Boolean)""",
            timeout=500,
        )
        return [str(value) for value in values if str(value).strip()]
    except Exception:
        return []


async def _controls(page: Page) -> tuple[str, ...]:
    """Capture a compact semantic fingerprint of visible interactive controls.

    Use one DOM evaluation per selector instead of multiple Playwright calls
    per control. This is critical because observation runs around every
    interaction and must remain cheaper than the action it is observing.
    """
    values: list[str] = []
    for selector in CONTROL_SELECTORS:
        try:
            items = await page.locator(selector).evaluate_all(
                """nodes => nodes.map(node => {
                    const style = window.getComputedStyle(node);
                    const visible = style.display !== 'none' &&
                                    style.visibility !== 'hidden' &&
                                    !!(node.offsetWidth || node.offsetHeight ||
                                       node.getClientRects().length);
                    if (!visible) return null;

                    const text = (node.innerText || node.textContent || '')
                        .replace(/\\s+/g, ' ').trim();
                    const aria = (node.getAttribute('aria-label') || '')
                        .replace(/\\s+/g, ' ').trim();
                    const title = (node.getAttribute('title') || '')
                        .replace(/\\s+/g, ' ').trim();
                    const attrValue = (node.getAttribute('value') || '')
                        .replace(/\\s+/g, ' ').trim();

                    let liveValue = attrValue;
                    if (!liveValue && ('value' in node)) {
                        liveValue = String(node.value || '').replace(/\\s+/g, ' ').trim();
                    }

                    const checked = node.getAttribute('aria-checked');
                    const disabled = node.getAttribute('disabled');
                    const label = text || aria || title || attrValue ||
                                  node.getAttribute('id') || '';
                    if (!label) return null;

                    const state = [];
                    if (liveValue && liveValue.toLowerCase() !== label.toLowerCase()) {
                        state.push('value=' + liveValue.toLowerCase());
                    }
                    if (checked !== null) state.push('checked=' + checked);
                    if (disabled !== null) state.push('disabled');

                    return selector + ':' + label.toLowerCase() + ':' + state.join('|');
                }).filter(Boolean)""",
                timeout=500,
            )
            values.extend(str(item) for item in items)
        except Exception:
            continue

    # Capture semantic delivery status when the page exposes the Juice Shop
    # tracking state through its confirmation icon. The primary selector follows
    # the component structure; the class-based fallback tolerates harmless DOM
    # restructuring while remaining a black-box observation of the rendered UI.
    status_selectors = (
        ".delivery-status .confirmation",
        ".delivery-status [class*='fa-truck-loading'], "
        ".delivery-status [class*='fa-truck'], "
        ".delivery-status [class*='fa-warehouse'], "
        ".delivery-status [class*='fa-home']",
        "[class*='fa-truck-loading']:visible, "
        "[class*='fa-truck']:visible, "
        "[class*='fa-warehouse']:visible, "
        "[class*='fa-home']:visible",
    )
    try:
        status = []
        for selector in status_selectors:
            items = await page.locator(selector).evaluate_all(
                """nodes => nodes.map(node => {
                    const classes = String(node.className || '').toLowerCase();
                    if (classes.includes('fa-truck-loading')) return 'status=packing';
                    if (classes.includes('fa-truck')) return 'status=transit';
                    if (classes.includes('fa-warehouse')) return 'status=new';
                    if (classes.includes('fa-home')) return 'status=delivered';
                    return null;
                }).filter(Boolean)""",
                timeout=500,
            )
            status.extend(str(item) for item in items)
            if status:
                break

        # The current Juice Shop track-result template puts the state on the
        # rendered confirmation icon itself. Keep a DOM-level fallback that
        # inspects every visible element inside the delivery-status component,
        # including nested <span>/<i> pairs and SVG/icon wrappers. This remains
        # framework-agnostic and does not depend on scenario IDs or literal UI
        # text.
        if not status:
            items = await page.locator(".delivery-status:visible").evaluate_all(
                """nodes => nodes.flatMap(root => Array.from(
                    root.querySelectorAll("*")
                ).map(node => {
                    const classes = String(node.className || '').toLowerCase();
                    if (classes.includes('fa-truck-loading')) return 'status=packing';
                    if (classes.includes('fa-truck')) return 'status=transit';
                    if (classes.includes('fa-warehouse')) return 'status=new';
                    if (classes.includes('fa-home')) return 'status=delivered';
                    return null;
                }).filter(Boolean))""",
                timeout=500,
            )
            status.extend(str(item) for item in items)

        if status:
            values.extend(status)
    except Exception:
        pass

    return tuple(sorted(set(values))[:200])


async def _read_body_text(page: Page, timeout_ms: int = 500) -> str:
    """Read the current document without letting a transient navigation crash observation.

    Angular can replace the document/body while Playwright is resolving a
    locator. The observer is diagnostic infrastructure, so it retries the
    read instead of treating that transient condition as an automation crash.
    """
    body = page.locator("body")
    try:
        return (await body.inner_text(timeout=timeout_ms)).strip()
    except Exception:
        # A DOM-backed locator can lose its document during SPA navigation.
        # Reading the current document through the page context gives the
        # observer a second, framework-independent path.
        try:
            value = await page.evaluate(
                "() => document.body ? document.body.innerText : ''"
            )
            return str(value or "").strip()
        except Exception:
            raise


async def _read_page_title(page: Page) -> str:
    """Read the page title without using an unsupported Playwright timeout argument."""
    try:
        return await page.title()
    except Exception:
        try:
            value = await page.evaluate("() => document.title || ''")
            return str(value or "")
        except Exception:
            return ""


async def observe(page: Page) -> UIState:
    last_error: Exception | None = None
    text = ""
    for _ in range(4):
        try:
            text = await _read_body_text(page)
            # An empty body is usually a transient navigation/rendering state.
            # Give Angular one render turn before accepting it as the snapshot.
            if text or page.url:
                break
        except Exception as exc:
            last_error = exc
            try:
                await page.wait_for_timeout(80)
            except Exception:
                break

    if last_error is not None and not text:
        raise RuntimeError(
            f"Não foi possível observar a página de forma estável: {last_error}"
        ) from last_error

    normalized = " ".join(text.split())
    messages: list[str] = []
    for selector in MESSAGE_SELECTORS:
        messages.extend(await _texts(page, selector))
    # Angular Material/CDK feedback can be mounted in an overlay outside the
    # page's normal content tree. Keep a small, semantic message corpus instead
    # of depending on one concrete snackbar implementation.
    messages = list(dict.fromkeys(messages))
    headings = list(dict.fromkeys(await _texts(page, HEADING_SELECTORS)))
    return UIState(
        url=page.url,
        title=await _read_page_title(page),
        visible_text=normalized[:12000],
        body_hash=sha256(normalized.encode("utf-8")).hexdigest(),
        messages=tuple(messages[:20]),
        headings=tuple(headings[:20]),
        controls=await _controls(page),
    )


async def safe_observe(
    page: Page,
    fallback: UIState | None = None,
    timeout_ms: int = 1800,
) -> UIState:
    """Best-effort observation boundary used by timeout/error recovery paths.

    Observation must never turn an already-classified action timeout into a
    process-level crash. When the page is temporarily unavailable, return the
    last known state so the runner can preserve diagnostic evidence.
    """
    deadline = __import__("time").monotonic() + timeout_ms / 1000
    last_error: Exception | None = None
    while __import__("time").monotonic() < deadline:
        try:
            return await observe(page)
        except Exception as exc:
            last_error = exc
            try:
                await page.wait_for_timeout(80)
            except Exception:
                break
    if fallback is not None:
        return fallback

    # No prior snapshot exists (for example, a scenario failed during its
    # first action). Return an explicitly empty diagnostic snapshot rather than
    # allowing observation infrastructure to terminate the entire suite.
    try:
        url = page.url
    except Exception:
        url = ""
    return UIState(
        url=url,
        title="",
        visible_text="",
        body_hash="",
    )


async def wait_for_stable_ui(page: Page, initial: UIState | None = None, timeout_ms: int = 1200, sample_interval_ms: int = 120) -> UIState:
    """Wait until two consecutive UI snapshots are identical."""
    deadline = __import__("time").monotonic() + timeout_ms / 1000
    previous = initial or await observe(page)
    stable_samples = 0
    while __import__("time").monotonic() < deadline:
        await page.wait_for_timeout(sample_interval_ms)
        try:
            current = await asyncio.wait_for(observe(page), timeout=1.5)
        except Exception:
            continue
        if current == previous:
            stable_samples += 1
            if stable_samples >= 2:
                return current
        else:
            stable_samples = 0
            previous = current
    return previous


def meaningful_change(before: UIState, after: UIState) -> bool:
    return (
        before.url != after.url
        or before.body_hash != after.body_hash
        or before.title != after.title
        or before.messages != after.messages
        or before.headings != after.headings
        or before.controls != after.controls
    )


def _new_text(before: str, after: str, limit: int = 700) -> str:
    if not after:
        return ""
    if not before:
        return after[:limit]
    before_tokens = set(re.findall(r"\S+", before))
    chunks = []
    for sentence in re.split(r"(?<=[.!?])\s+|\s{2,}", after):
        tokens = set(re.findall(r"\S+", sentence))
        if sentence and tokens and len(tokens - before_tokens) >= max(1, min(4, len(tokens) // 3)):
            chunks.append(sentence.strip())
    return " | ".join(chunks)[:limit]


def _changed_controls(before: UIState, after: UIState, limit: int = 8) -> str:
    added = sorted(set(after.controls) - set(before.controls))
    removed = sorted(set(before.controls) - set(after.controls))
    parts: list[str] = []
    if added:
        parts.append("adicionados: " + " | ".join(added[:limit]))
    if removed:
        parts.append("removidos/ocultados: " + " | ".join(removed[:limit]))
    return " ".join(parts)[:900]


def describe_change(before: UIState, after: UIState) -> str:
    parts: list[str] = []
    if before.url != after.url:
        parts.append(f"URL: {before.url} → {after.url}")
    new_messages = [m for m in after.messages if m not in before.messages]
    if new_messages:
        parts.append("Mensagem: " + " | ".join(new_messages[:3]))
    control_change = _changed_controls(before, after)
    if control_change:
        parts.append("Controles: " + control_change)
    new_text = _new_text(before.visible_text, after.visible_text)
    if new_text:
        parts.append("Texto visível: " + new_text)
    if not parts:
        if before.body_hash != after.body_hash or before.headings != after.headings or before.controls != after.controls:
            parts.append("Conteúdo/estrutura visível da página foi alterado.")
        else:
            parts.append("Nenhuma mudança visual relevante detectada.")
    return " ".join(parts)[:1200]