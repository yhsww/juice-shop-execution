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


def _tokens(value: str | None) -> set[str]:
    # Ignore short English UI articles/prepositions so semantic labels such as
    # "Add New Address" can resolve controls exposed as "Add a new address".
    stop_words = {"a", "an", "the", "to", "of", "for", "in", "on"}
    return {
        token
        for token in re.findall(r"[\wÀ-ÿ]+", _norm(value))
        if token not in stop_words
    }


def _semantic_text_match(wanted: str | None, actual: str | None) -> bool:
    wanted_norm = _norm(wanted)
    actual_norm = _norm(actual)
    if not wanted_norm or not actual_norm:
        return False

    if wanted_norm == actual_norm:
        return True

    if wanted_norm in actual_norm or actual_norm in wanted_norm:
        return True

    wanted_tokens = _tokens(wanted_norm)
    actual_tokens = _tokens(actual_norm)

    return bool(wanted_tokens) and wanted_tokens.issubset(actual_tokens)


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


async def _semantic_control_candidates(page: Page, value: str) -> list[Locator]:
    """
    Generic fallback for Angular Material/native controls whose accessible
    name is generated from a visible label or icon.
    """
    wanted = _norm(value)
    if not wanted:
        return []

    candidates: list[Locator] = []
    controls = page.locator(
        "input, textarea, select, mat-select, "
        "[role='textbox'], [role='combobox'], "
        "[role='radio'], [role='checkbox']"
    )

    try:
        count = await controls.count()
    except Exception:
        count = 0

    for index in range(count):
        control = controls.nth(index)
        try:
            if not await control.is_visible():
                continue

            attrs = [
                await control.get_attribute("aria-label"),
                await control.get_attribute("placeholder"),
                await control.get_attribute("title"),
                await control.get_attribute("name"),
                await control.get_attribute("id"),
            ]

            if any(
                _semantic_text_match(wanted, attr)
                for attr in attrs
                if attr
            ):
                candidates.append(control)
                continue

            parent = control.locator("xpath=ancestor::mat-form-field[1]")
            if await parent.count() and wanted in _norm(await parent.inner_text()):
                candidates.append(control)
                continue

            # Generic legacy/native form relationship. Some Juice Shop pages
            # use a visible <label> plus a sibling input inside a form-field
            # container instead of Angular Material's mat-form-field.
            try:
                context_text = await control.evaluate(
                    """(el) => {
                        const labels = Array.from(document.querySelectorAll("label"));
                        const directLabel = el.id
                            ? labels.find(label => label.htmlFor === el.id)
                            : null;
                        const container = el.closest(
                            "form, .form-container, .profile-field, [class*='field'], [class*='form']"
                        );
                        return [
                            directLabel?.textContent || "",
                            container?.textContent || ""
                        ].join(" ");
                    }"""
                )
                if _semantic_text_match(wanted, context_text):
                    candidates.append(control)
                    continue
            except Exception:
                pass

            control_id = await control.get_attribute("id")
            if control_id:
                label = page.locator(f"label[for='{control_id}']")
                if await label.count() and await label.first.is_visible():
                    if wanted in _norm(await label.first.inner_text()):
                        candidates.append(control)
        except Exception:
            continue

    return candidates


async def _visible_text_control(page: Page, value: str) -> list[Locator]:
    """
    Resolve controls represented by visible text, including Angular Material
    radio/checkbox components and icon buttons.
    """
    wanted = _norm(value)
    if not wanted:
        return []

    candidates: list[Locator] = []

    for selector in (
        "mat-radio-button",
        "mat-checkbox",
        "label",
        "[role='radio']",
        "[role='checkbox']",
        "button",
        "a",
        "[role='button']",
        "[role='link']",
    ):
        nodes = page.locator(selector)
        try:
            count = await nodes.count()
        except Exception:
            continue

        for index in range(count):
            node = nodes.nth(index)
            try:
                if not await node.is_visible():
                    continue

                text = _norm(await node.inner_text())
                aria = _norm(await node.get_attribute("aria-label"))
                title = _norm(await node.get_attribute("title"))

                direct_match = (
                    _semantic_text_match(wanted, text)
                    or _semantic_text_match(wanted, aria)
                    or _semantic_text_match(wanted, title)
                )

                # Angular Material delivery rows expose the delivery name in a
                # sibling mat-cell while the actual radio control has no name.
                row_match = False
                if selector in ("mat-radio-button", "[role='radio']"):
                    for ancestor in ("mat-row", "[role='row']", "tr"):
                        parent = node.locator(
                            f"xpath=ancestor::{ancestor}[1]"
                        )
                        if await parent.count():
                            row_match = _semantic_text_match(
                                wanted,
                                await parent.inner_text(),
                            )
                            if row_match:
                                break

                if direct_match or row_match:
                    candidates.append(node)
            except Exception:
                continue

    return candidates


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

    # 5. Generic semantic control fallback. It is independent of
    # individual scenario IDs and complements the primary ARIA/label lookup.
    for value in (label, placeholder, name, text):
        if value:
            candidates.extend(
                await _semantic_control_candidates(page, str(value))
            )
            candidates.extend(
                await _visible_text_control(page, str(value))
            )

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

    # 7. Generic DOM attribute fallbacks for legacy/Angular controls.
    # These attributes are stable semantic metadata, not scenario-specific selectors.
    # Legacy Juice Shop screens can expose native inputs through id/name while
    # the label relationship is not recognized by Playwright's get_by_label().
    for value in (name, label, text, placeholder):
        if not value:
            continue
        wanted = _norm(str(value))
        if not wanted:
            continue

        # Exact semantic attributes first. This is generic and derived from
        # the scenario target rather than from any scenario ID.
        for attr in ("name", "id", "formcontrolname"):
            try:
                candidates.append(
                    page.locator(
                        f"input[{attr}='{str(value)}'], "
                        f"textarea[{attr}='{str(value)}'], "
                        f"select[{attr}='{str(value)}']"
                    )
                )
            except Exception:
                pass

        nodes = page.locator(
            "input, textarea, select, mat-select, "
            "[role='textbox'], [role='combobox']"
        )
        try:
            count = await nodes.count()
        except Exception:
            count = 0

        for index in range(count):
            node = nodes.nth(index)
            try:
                if not await node.is_visible():
                    continue

                attrs = [
                    await node.get_attribute("id"),
                    await node.get_attribute("name"),
                    await node.get_attribute("formcontrolname"),
                    await node.get_attribute("aria-label"),
                    await node.get_attribute("placeholder"),
                    await node.get_attribute("title"),
                ]
                if any(_semantic_text_match(wanted, attr) for attr in attrs if attr):
                    candidates.append(node)
                    break
            except Exception:
                continue

    # Some Juice Shop screens expose native inputs with id/name but no accessible
    # label that Playwright can resolve directly.
    for value in (name, label, text, placeholder):
        if not value:
            continue
        wanted = _norm(str(value))
        if not wanted:
            continue

        nodes = page.locator("input, textarea, select, mat-select, [role='textbox'], [role='combobox']")
        try:
            count = await nodes.count()
        except Exception:
            continue

        for index in range(count):
            node = nodes.nth(index)
            try:
                if not await node.is_visible():
                    continue

                attrs = [
                    await node.get_attribute("id"),
                    await node.get_attribute("name"),
                    await node.get_attribute("formcontrolname"),
                    await node.get_attribute("aria-label"),
                    await node.get_attribute("placeholder"),
                    await node.get_attribute("title"),
                ]
                if any(_semantic_text_match(wanted, attr) for attr in attrs if attr):
                    candidates.append(node)
                    break
            except Exception:
                continue

    # 8. Attribute fallbacks for Angular-generated controls.
    # has_text() inspects descendants, not attribute values, so aria-label
    # and title must be checked explicitly.
    for value in (name, label, text):
        if not value:
            continue
        wanted = _norm(str(value))
        if not wanted:
            continue

        for selector, attr_name in (
            ("[aria-label]", "aria-label"),
            ("[title]", "title"),
        ):
            nodes = page.locator(selector)
            try:
                count = await nodes.count()
            except Exception:
                continue

            for index in range(count):
                node = nodes.nth(index)
                try:
                    if not await node.is_visible():
                        continue
                    attr = await node.get_attribute(attr_name)
                    normalized_attr = _norm(attr)
                    if _semantic_text_match(wanted, normalized_attr):
                        candidates.append(node)
                except Exception:
                    continue

    return await first_visible(candidates)
