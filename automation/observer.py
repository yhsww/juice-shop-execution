from __future__ import annotations

from dataclasses import dataclass
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
    try:
        values: list[str] = []
        nodes = page.locator(selector)
        count = await nodes.count()
        for index in range(count):
            node = nodes.nth(index)
            try:
                if not await node.is_visible():
                    continue
                value = " ".join((await node.inner_text()).split())
                if value:
                    values.append(value)
            except Exception:
                continue
        return values
    except Exception:
        return []


async def _controls(page: Page) -> tuple[str, ...]:
    """Capture a compact semantic fingerprint of visible interactive controls."""
    values: list[str] = []
    for selector in CONTROL_SELECTORS:
        try:
            nodes = page.locator(selector)
            count = await nodes.count()
        except Exception:
            continue
        for index in range(count):
            node = nodes.nth(index)
            try:
                if not await node.is_visible():
                    continue
                text = " ".join((await node.inner_text()).split())
                aria = " ".join((await node.get_attribute("aria-label") or "").split())
                title = " ".join((await node.get_attribute("title") or "").split())
                value = " ".join((await node.get_attribute("value") or "").split())
                # Form controls often expose important behavior only through
                # their current value; input.value is not part of body.inner_text().
                # Include it in the black-box control fingerprint so assertions
                # can validate entered data without page-specific DOM hacks.
                text_value = value
                if not text_value:
                    try:
                        text_value = " ".join((await node.input_value()).split())
                    except Exception:
                        pass
                checked = await node.get_attribute("aria-checked")
                disabled = await node.get_attribute("disabled")
                label = text or aria or title or value
                if not label:
                    label = await node.get_attribute("id") or ""
                if not label:
                    continue
                state = []
                if text_value and text_value.casefold() != label.casefold():
                    state.append(f"value={text_value.casefold()}")
                if checked is not None:
                    state.append(f"checked={checked}")
                if disabled is not None:
                    state.append("disabled")
                values.append(f"{selector}:{label.casefold()}:{'|'.join(state)}")
            except Exception:
                continue
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
            current = await observe(page)
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