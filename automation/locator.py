from __future__ import annotations

from playwright.async_api import Locator, Page


async def first_visible(candidates: list[Locator]) -> Locator | None:
    for candidate in candidates:
        try:
            if await candidate.count() and await candidate.first.is_visible():
                return candidate.first
        except Exception:
            continue
    return None


async def resolve(page: Page, target: dict) -> Locator | None:
    role = target.get("role")
    name = target.get("name")
    label = target.get("label")
    text = target.get("text")
    css = target.get("css")

    candidates: list[Locator] = []

    if role and name:
        candidates.append(page.get_by_role(role, name=name, exact=target.get("exact", True)))
    if label:
        candidates.append(page.get_by_label(label, exact=target.get("exact", True)))
    if text:
        candidates.append(page.get_by_text(text, exact=target.get("exact", True)))
    if css:
        candidates.append(page.locator(css))

    return await first_visible(candidates)
