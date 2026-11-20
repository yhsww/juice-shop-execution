from __future__ import annotations

import re

from playwright.async_api import Locator, Page


# Playwright/ARIA roles that are safe to pass to get_by_role().
_VALID_ROLES = {
    "alert", "alertdialog", "application", "article", "banner", "blockquote",
    "button", "caption", "cell", "checkbox", "code", "columnheader", "combobox",
    "complementary", "contentinfo", "definition", "deletion", "dialog", "directory",
    "document", "feed", "figure", "form", "generic", "grid", "gridcell",
    "group", "heading", "img", "insertion", "link", "list", "listbox", "listitem",
    "log", "main", "marquee", "math", "meter", "menu", "menubar", "menuitem",
    "menuitemcheckbox", "menuitemradio", "navigation", "none", "option", "paragraph",
    "presentation", "progressbar", "radio", "radiogroup", "region", "row",
    "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator",
    "slider", "spinbutton", "status", "strong", "subscript", "superscript",
    "switch", "tab", "table", "tablist", "tabpanel", "term", "textbox",
    "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"
}


def _norm(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip().casefold()


async def first_visible(candidates: list[Locator]) -> Locator | None:
    seen: set[str] = set()

    for candidate in candidates:
        try:
            count = await candidate.count()
            for index in range(count):
                item = candidate.nth(index)

                if not await item.is_visible():
                    continue

                # Avoid repeatedly returning the same DOM node when multiple
                # semantic strategies resolve to it.
                try:
                    key = await item.evaluate(
                        "(el) => el.outerHTML.slice(0, 500)"
                    )
                except Exception:
                    key = f"{id(candidate)}:{index}"

                if key in seen:
                    continue

                seen.add(key)
                return item

        except Exception:
            continue

    return None


def _safe_role_candidate(
    page: Page,
    role: str | None,
    name: str | None,
    exact: bool,
) -> list[Locator]:
    if not role or not name:
        return []

    role_normalized = role.lower().strip()

    # Do not call get_by_role() with scenario roles that are not valid ARIA
    # roles (e.g. "text"). Fall back to visible text below instead.
    if role_normalized not in _VALID_ROLES:
        return []

    candidates = [
        page.get_by_role(role_normalized, name=name, exact=exact)
    ]

    if exact:
        candidates.append(
            page.get_by_role(role_normalized, name=name, exact=False)
        )

    return candidates


async def _angular_material_field(page: Page, label: str) -> Locator | None:
    wanted = _norm(label)
    if not wanted:
        return None

    fields = page.locator("mat-form-field")

    try:
        count = await fields.count()
    except Exception:
        return None

    for index in range(count):
        field = fields.nth(index)

        try:
            if not await field.is_visible():
                continue

            text = _norm(await field.inner_text())
            aria = _norm(await field.get_attribute("aria-label"))

            if wanted not in text and wanted not in aria:
                continue

            controls = field.locator(
                "input, textarea, select, mat-select, "
                "[contenteditable='true'], [role='combobox'], "
                "[role='textbox']"
            )

            control_count = await controls.count()
            for control_index in range(control_count):
                control = controls.nth(control_index)
                if await control.is_visible():
                    return control

        except Exception:
            continue

    return None


async def _associated_field(page: Page, label: str) -> Locator | None:
    wanted = _norm(label)
    if not wanted:
        return None

    # Native <label>.
    labels = page.locator("label")
    try:
        count = await labels.count()
    except Exception:
        count = 0

    for index in range(count):
        current = labels.nth(index)

        try:
            if not await current.is_visible():
                continue

            text = _norm(await current.inner_text())
            aria = _norm(await current.get_attribute("aria-label"))

            if wanted not in text and wanted not in aria:
                continue

            target_id = await current.get_attribute("for")
            if target_id:
                control = page.locator(f"#{target_id}")
                if await control.is_visible():
                    return control

            nested = current.locator(
                "input, textarea, select, mat-select, "
                "[contenteditable='true'], [role='combobox'], "
                "[role='textbox']"
            )
            nested_count = await nested.count()
            for nested_index in range(nested_count):
                control = nested.nth(nested_index)
                if await control.is_visible():
                    return control

        except Exception:
            continue

    # Angular Material fields may expose the label through a mat-label.
    labels = page.locator("mat-label")
    try:
        count = await labels.count()
    except Exception:
        count = 0

    for index in range(count):
        current = labels.nth(index)
        try:
            if not await current.is_visible():
                continue
            if wanted not in _norm(await current.inner_text()):
                continue

            parent = current.locator("xpath=ancestor::mat-form-field[1]")
            controls = parent.locator(
                "input, textarea, mat-select, "
                "[role='combobox'], [role='textbox']"
            )

            for control_index in range(await controls.count()):
                control = controls.nth(control_index)
                if await control.is_visible():
                    return control
        except Exception:
            continue

    return None


async def resolve(page: Page, target: dict) -> Locator | None:
    """
    Resolve a scenario target against the real Juice Shop DOM.

    The resolver deliberately prefers semantic Playwright locators but has
    generic fallbacks for Angular Material, translated labels, ARIA labels,
    title attributes and controls whose accessible name differs slightly
    from the scenario text.

    This is shared by all 78 scenarios; it must not contain scenario-specific
    selectors.
    """
    role = target.get("role")
    name = target.get("name")
    label = target.get("label")
    text = target.get("text")
    css = target.get("css")
    placeholder = target.get("placeholder")
    exact = bool(target.get("exact", True))

    candidates: list[Locator] = []

    # 1. Semantic ARIA role.
    candidates.extend(_safe_role_candidate(page, role, name, exact))

    # 2. Label-based controls.
    if label:
        candidates.append(page.get_by_label(label, exact=exact))
        if exact:
            candidates.append(page.get_by_label(label, exact=False))

    # 3. Placeholder.
    if placeholder:
        candidates.append(
            page.get_by_placeholder(placeholder, exact=exact)
        )
        if exact:
            candidates.append(
                page.get_by_placeholder(placeholder, exact=False)
            )

    # 4. Visible text. This is also the fallback for invalid pseudo-roles
    # such as "text" used by some scenario definitions.
    if text or (role and role.lower() not in _VALID_ROLES and name):
        wanted_text = text or name
        candidates.append(page.get_by_text(wanted_text, exact=exact))
        if exact:
            candidates.append(page.get_by_text(wanted_text, exact=False))

    # 5. Explicit CSS.
    if css:
        try:
            candidates.append(page.locator(css))
        except Exception:
            pass

    # 6. Common native/Angular Material semantic fallbacks.
    if name:
        # Buttons and links often have a visible label but no stable accessible
        # name because of nested icons.
        candidates.extend([
            page.locator("button").filter(has_text=name),
            page.locator("[role='button']").filter(has_text=name),
            page.locator("a").filter(has_text=name),
            page.locator("[role='link']").filter(has_text=name),
        ])

        # aria-label/title are more stable than generated CSS classes.
        candidates.extend([
            page.locator(f"[aria-label='{name}']"),
            page.locator(f"[title='{name}']"),
        ])

    if label:
        angular = await _angular_material_field(page, label)
        if angular is not None:
            candidates.append(angular)

        associated = await _associated_field(page, label)
        if associated is not None:
            candidates.append(associated)

    # 7. Useful generic attributes for generated Angular controls.
    for value in (name, label, text):
        if not value:
            continue
        normalized = _norm(value)
        if not normalized:
            continue

        # CSS attribute selectors are intentionally broad here; they are
        # only fallbacks after semantic strategies have failed.
        candidates.extend([
            page.locator("[aria-label]").filter(
                has_text=value
            ),
            page.locator("[title]").filter(
                has_text=value
            ),
        ])

    return await first_visible(candidates)
