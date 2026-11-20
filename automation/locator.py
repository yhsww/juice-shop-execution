from __future__ import annotations

from playwright.async_api import Locator, Page


async def first_visible(candidates: list[Locator]) -> Locator | None:
    for candidate in candidates:
        try:
            count = await candidate.count()
            for index in range(count):
                item = candidate.nth(index)
                if await item.is_visible():
                    return item
        except Exception:
            continue
    return None


async def resolve(page: Page, target: dict) -> Locator | None:
    role = target.get("role")
    name = target.get("name")
    label = target.get("label")
    text = target.get("text")
    css = target.get("css")
    placeholder = target.get("placeholder")
    exact = target.get("exact", True)

    candidates: list[Locator] = []

    if role and name:
        candidates.append(page.get_by_role(role, name=name, exact=exact))
        if exact:
            candidates.append(page.get_by_role(role, name=name, exact=False))

    if label:
        candidates.append(page.get_by_label(label, exact=exact))
        if exact:
            candidates.append(page.get_by_label(label, exact=False))

    if placeholder:
        candidates.append(page.get_by_placeholder(placeholder, exact=exact))
        if exact:
            candidates.append(page.get_by_placeholder(placeholder, exact=False))

    if text:
        candidates.append(page.get_by_text(text, exact=exact))
        if exact:
            candidates.append(page.get_by_text(text, exact=False))

    if css:
        try:
            candidates.append(page.locator(css))
        except Exception:
            # Invalid CSS must not crash scenario execution.
            pass

    # Common Angular Material fallbacks. These remain generic and are useful
    # when translations change the visible label slightly.
    if role == "button" and name:
        candidates.extend([
            page.locator("button").filter(has_text=name),
            page.locator("[role='button']").filter(has_text=name),
        ])

    return await first_visible(candidates)
