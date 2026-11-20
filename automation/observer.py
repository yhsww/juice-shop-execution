from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from playwright.async_api import Page


@dataclass(frozen=True)
class UIState:
    url: str
    title: str
    visible_text: str
    body_hash: str


async def observe(page: Page) -> UIState:
    text = (await page.locator("body").inner_text(timeout=5000)).strip()
    normalized = " ".join(text.split())
    return UIState(
        url=page.url,
        title=await page.title(),
        visible_text=normalized[:12000],
        body_hash=sha256(normalized.encode("utf-8")).hexdigest(),
    )


def meaningful_change(before: UIState, after: UIState) -> bool:
    return (
        before.url != after.url
        or before.body_hash != after.body_hash
        or before.title != after.title
    )
