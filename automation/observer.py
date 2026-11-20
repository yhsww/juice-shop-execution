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


MESSAGE_SELECTORS = (
    '[role="alert"]',
    '.mat-mdc-snack-bar-label',
    '.mat-snack-bar-container',
    '.cdk-overlay-container [role="status"]',
)

HEADING_SELECTORS = "h1,h2,h3,h4,[role='heading']"


async def _texts(page: Page, selector: str) -> list[str]:
    try:
        return [
            " ".join(value.split())
            for value in await page.locator(selector).all_inner_texts()
            if " ".join(value.split())
        ]
    except Exception:
        return []


async def observe(page: Page) -> UIState:
    body = page.locator("body")
    text = (await body.inner_text(timeout=5000)).strip()
    normalized = " ".join(text.split())

    messages: list[str] = []
    for selector in MESSAGE_SELECTORS:
        messages.extend(await _texts(page, selector))

    # Keep order while removing duplicates.
    messages = list(dict.fromkeys(messages))

    headings = list(dict.fromkeys(await _texts(page, HEADING_SELECTORS)))

    return UIState(
        url=page.url,
        title=await page.title(),
        visible_text=normalized[:12000],
        body_hash=sha256(normalized.encode("utf-8")).hexdigest(),
        messages=tuple(messages[:20]),
        headings=tuple(headings[:20]),
    )


def meaningful_change(before: UIState, after: UIState) -> bool:
    return (
        before.url != after.url
        or before.body_hash != after.body_hash
        or before.title != after.title
        or before.messages != after.messages
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


def describe_change(before: UIState, after: UIState) -> str:
    parts: list[str] = []

    if before.url != after.url:
        parts.append(f"URL: {before.url} → {after.url}")

    new_messages = [m for m in after.messages if m not in before.messages]
    if new_messages:
        parts.append("Mensagem: " + " | ".join(new_messages[:3]))

    new_text = _new_text(before.visible_text, after.visible_text)
    if new_text:
        parts.append("Texto visível: " + new_text)

    if not parts:
        if before.body_hash != after.body_hash:
            parts.append("Conteúdo visível da página foi alterado.")
        else:
            parts.append("Nenhuma mudança visual relevante detectada.")

    return " ".join(parts)[:1200]
