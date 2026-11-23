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
    '[role="alert"]',
    '[aria-live]:visible',
    '[role="status"]',
    '.mat-mdc-snack-bar-label',
    '.mat-snack-bar-container',
    '.mat-mdc-form-field-error',
    'mat-error',
    '.mat-error',
    '.cdk-overlay-container [role="status"]',
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
        return [
            " ".join(value.split())
            for value in await page.locator(selector).all_inner_texts()
            if " ".join(value.split())
        ]
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


async def observe(page: Page) -> UIState:
    body = page.locator("body")
    text = (await body.inner_text(timeout=1200)).strip()
    normalized = " ".join(text.split())
    messages: list[str] = []
    for selector in MESSAGE_SELECTORS:
        messages.extend(await _texts(page, selector))
    messages = list(dict.fromkeys(messages))
    headings = list(dict.fromkeys(await _texts(page, HEADING_SELECTORS)))
    return UIState(
        url=page.url,
        title=await page.title(),
        visible_text=normalized[:12000],
        body_hash=sha256(normalized.encode("utf-8")).hexdigest(),
        messages=tuple(messages[:20]),
        headings=tuple(headings[:20]),
        controls=await _controls(page),
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