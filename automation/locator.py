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

    # Prefer an exact accessible-name match even when the scenario allows
    # fuzzy matching. This prevents targets such as "Back" from resolving to
    # unrelated controls whose accessible name merely contains that word
    # (for example the navbar button "Back to homepage").
    # Exact accessible-name resolution is the highest-confidence semantic
    # strategy. Do not put a fuzzy role match in this early candidate pool:
    # Playwright would otherwise select an unrelated control before the
    # resolver reaches more precise visible-text/attribute fallbacks.
    return [
        page.get_by_role(role_normalized, name=name, exact=True)
    ]


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

    # Legacy Juice Shop profile forms expose the semantic field through
    # aria-label even when the visible <label> relationship is not exposed
    # consistently by Playwright. Match the requested semantic label against
    # the control's accessible metadata before broader fallbacks.
    controls = page.locator("input, textarea, select, [role='textbox'], [role='combobox']")
    try:
        control_count = await controls.count()
    except Exception:
        control_count = 0

    for index in range(control_count):
        control = controls.nth(index)
        try:
            if not await control.is_visible():
                continue
            attrs = [
                await control.get_attribute("aria-label"),
                await control.get_attribute("placeholder"),
                await control.get_attribute("name"),
                await control.get_attribute("id"),
                await control.get_attribute("title"),
            ]
            if any(_semantic_text_match(wanted, attr) for attr in attrs if attr):
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



async def _table_radio_by_header(page: Page, value: str) -> list[Locator]:
    """Resolve an unnamed radio from a table column header."""
    wanted = _norm(value)
    if not wanted:
        return []

    candidates: list[Locator] = []
    tables = page.locator("table, mat-table")
    try:
        table_count = await tables.count()
    except Exception:
        return []

    for table_index in range(table_count):
        table = tables.nth(table_index)
        try:
            if not await table.is_visible():
                continue

            headers = table.locator("th, mat-header-cell")
            matched_column = None
            for header_index in range(await headers.count()):
                header = headers.nth(header_index)
                if (
                    await header.is_visible()
                    and _semantic_text_match(
                        wanted, _norm(await header.inner_text())
                    )
                ):
                    matched_column = header_index
                    break

            if matched_column is None:
                continue

            rows = table.locator("tbody tr, mat-row, [role='row']")
            for row_index in range(await rows.count()):
                row = rows.nth(row_index)
                if not await row.is_visible():
                    continue

                cells = row.locator("td, mat-cell, [role='cell']")
                if matched_column >= await cells.count():
                    continue

                cell = cells.nth(matched_column)
                radio = await first_visible([
                    cell.locator("mat-radio-button"),
                    cell.locator("[role='radio']"),
                ])
                if radio is not None:
                    candidates.append(radio)

            if candidates:
                break
        except Exception:
            continue

    return candidates

async def _visible_text_row(page: Page, value: str) -> list[Locator]:
    """Resolve table-like interactive rows by complete visible row text."""
    wanted = _norm(value)
    if not wanted:
        return []

    candidates: list[Locator] = []
    for selector in ("mat-row", "tr", "[role='row']"):
        rows = page.locator(selector)
        try:
            count = await rows.count()
        except Exception:
            continue

        for index in range(count):
            row = rows.nth(index)
            try:
                if not await row.is_visible():
                    continue
                if _semantic_text_match(wanted, await row.inner_text()):
                    candidates.append(row)
                    continue

                # Some Angular Material tables render the semantic value in
                # a cell whose normalized text differs from the row's exposed
                # accessible name. Resolve the cell first, then climb to the
                # same interactive row.
                cells = row.locator("td, th, mat-cell, mat-header-cell, [role='cell'], [role='gridcell']")
                for cell_index in range(await cells.count()):
                    cell = cells.nth(cell_index)
                    if not await cell.is_visible():
                        continue
                    if _semantic_text_match(wanted, await cell.inner_text()):
                        candidates.append(row)
                        break
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
        "mat-menu-item",
        "[role='menuitem']",
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


async def _resolve_once(page: Page, target: dict) -> Locator | None:
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

    # A label target is especially common on native/legacy Juice Shop forms.
    # The top search is an exception: its visible input lives inside the
    # custom app-mat-search-bar and must win over generic label heuristics.
    if label and _norm(str(label)) == "search":
        candidates.extend([
            page.locator("#searchQuery input:visible"),
            page.locator("app-mat-search-bar input:visible"),
            page.locator("input[type='search']:visible"),
        ])

    if label:
        associated = await _associated_field(page, str(label))
        if associated is not None:
            candidates.insert(0, associated)

    # 2. Label-based controls.

    if label:
        if _norm(str(label)) == "search":
            candidates.extend([
                page.get_by_role("searchbox", name=label, exact=exact),
                page.get_by_role("textbox", name=label, exact=exact),
                page.locator("input[aria-label*='Search' i]:visible"),
                page.locator("input[placeholder*='Search' i]:visible"),
            ])
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

    # 4. Visible text / semantic table controls.
    # Some Angular Material controls do not expose their visible label as an
    # accessible name. For example, the checkout address radio is unnamed and
    # its semantic label comes from the table column header. Resolve those
    # controls semantically before falling back to generic text.
    if text or name:
        wanted_text = text or name
        role_normalized = str(role or "").casefold()

        # Unnamed Angular Material radios can expose their semantic
        # identity only through the text of the containing table row (for
        # example an address, delivery method, or card number). Prefer the
        # row-semantic resolver before falling back to column-header semantics.
        if role_normalized == "radio":
            candidates.extend(
                await _visible_text_control(page, str(wanted_text))
            )
            candidates.extend(
                await _table_radio_by_header(page, str(wanted_text))
            )
        elif role and role_normalized not in _VALID_ROLES:
            candidates.extend(
                await _table_radio_by_header(page, str(wanted_text))
            )

        # Angular Material menu items can expose an aria-label that
        # intentionally differs from the translated visible text. For example,
        # Juice Shop renders Login as aria-label="Go to login page" while the
        # visible menu item says "Login". When the scenario explicitly asks
        # for a menuitem by its user-visible name, resolve the rendered control
        # by its own text as a semantic fallback.
        if role_normalized == "menuitem" and name:
            candidates.extend([
                page.locator("mat-menu-item").filter(has_text=str(name)),
                page.locator("[role='menuitem']").filter(has_text=str(name)),
            ])

        # For text-only targets, prefer an actual interactive control over a
        # nested <span>. Angular Material buttons commonly expose their label
        # as a child span, and get_by_text() otherwise returns that span.
        if not role_normalized:
            candidates.extend(
                await _visible_text_control(page, str(wanted_text)
                )
            )

        if role_normalized == "row":
            candidates.extend(
                await _visible_text_row(page, str(wanted_text))
            )

        # A text-only target can intentionally describe an interactive table
        # row (for example an address). Resolve that row before get_by_text(),
        # because get_by_text() often returns the nested mat-cell/span rather
        # than the row that owns the Angular selection handler.
        if not role_normalized and text:
            candidates.extend(
                await _visible_text_row(page, str(wanted_text))
            )

        # Do not use raw visible-text locators for explicitly requested
        # radio/checkbox targets. If the semantic control is temporarily not
        # rendered, get_by_text() can resolve an unrelated button such as
        # "Add New Address", causing a click to navigate away from checkout.
        # The resolver retries, so it is safer to wait for the actual control.
        if role_normalized not in {"radio", "checkbox"}:
            candidates.append(page.get_by_text(wanted_text, exact=exact))
            if exact:
                candidates.append(page.get_by_text(wanted_text, exact=False))

    # 5. Generic semantic control fallback. It is independent of
    # individual scenario IDs and complements the primary ARIA/label lookup.
    #
    # For radio/checkbox targets, do not mix generic button/link text into the
    # candidate pool. Some Juice Shop tables contain a visible "Add ..." button
    # whose text includes the same word as the selection column (for example
    # "Address"). Mixing those controls can make a radio target resolve to the
    # navigation button instead of the selection control.
    control_role = str(role or "").lower()
    for value in (label, placeholder, name, text):
        if value:
            candidates.extend(
                await _semantic_control_candidates(page, str(value))
            )
            if control_role not in {"radio", "checkbox"}:
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
    # For explicit radio/checkbox targets, NEVER add buttons/links that merely
    # contain the same text. Checkout uses a radio whose semantic label is the
    # table header "Address", while the page also contains an "Add New Address"
    # button. Mixing those controls can navigate to /#/address/create.
    if name and control_role not in {"radio", "checkbox"}:
        # Menu items in Angular Material are sometimes rendered as a
        # button/mat-menu-item without a reliable accessible role during the
        # short interval after the overlay opens. Keep menuitem resolution
        # semantic and framework-generic.
        if control_role == "menuitem":
            candidates.extend([
                page.locator("mat-menu-item").filter(has_text=name),
                page.locator("[role='menuitem']").filter(has_text=name),
                page.locator("button").filter(has_text=name),
            ])

        # Buttons and links often have a visible label but no stable accessible
        # name because of nested icons.
        candidates.extend([
            page.locator("button").filter(has_text=name),
            page.locator("[role='button']").filter(has_text=name),
            page.locator("a").filter(has_text=name),
            page.locator("[role='link']").filter(has_text=name),
        ])

        # Attribute values can contain quotes or CSS-significant characters.
        # Avoid interpolating scenario text into raw CSS selectors; the generic
        # attribute scan below resolves aria-label/title safely.
        #
        # Playwright's semantic locators are preferred here. Attribute matching
        # is intentionally handled by the DOM scan below so malformed target
        # text cannot produce "Unexpected token while parsing css selector".
        candidates.extend([
            page.get_by_title(name, exact=exact),
        ])
        if exact:
            candidates.append(page.get_by_title(name, exact=False))

    if label:
        angular = await _angular_material_field(page, label)
        if angular is not None:
            candidates.append(angular)

        associated = await _associated_field(page, label)
        if associated is not None:
            candidates.append(associated)

    # 6b. Case-insensitive semantic attribute fallback for controls whose
    # accessible name differs only by casing/punctuation or is exposed through
    # aria-label/title rather than inner text. This is especially important for
    # icon-only Angular Material buttons such as "Print order confirmation".
    if role and name:
        role_tag_map = {
            "button": "button,[role='button']",
            "link": "a,[role='link']",
            "menuitem": "mat-menu-item,[role='menuitem'],button",
            "radio": "mat-radio-button,[role='radio']",
            "checkbox": "mat-checkbox,[role='checkbox']",
        }
        selector = role_tag_map.get(str(role).casefold())
        if selector:
            nodes = page.locator(selector)
            try:
                for index in range(await nodes.count()):
                    node = nodes.nth(index)
                    if not await node.is_visible():
                        continue
                    attrs = [
                        await node.get_attribute("aria-label"),
                        await node.get_attribute("title"),
                        await node.get_attribute("name"),
                    ]
                    if any(
                        _semantic_text_match(str(name), attr)
                        for attr in attrs
                        if attr
                    ):
                        candidates.append(node)
            except Exception:
                pass

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

    # 8. Native form fallback using label/control relationships.
    # This deliberately works from the target text rather than scenario IDs,
    # and also covers legacy pages where Playwright's get_by_label() does not
    # infer the association reliably.
    for value in (label, name, text):
        if not value:
            continue
        wanted = _norm(str(value))
        if not wanted:
            continue

        inputs = page.locator("input, textarea, select")
        try:
            count = await inputs.count()
        except Exception:
            count = 0

        for index in range(count):
            control = inputs.nth(index)
            try:
                if not await control.is_visible():
                    continue

                control_id = await control.get_attribute("id")
                control_name = await control.get_attribute("name")
                placeholder_value = await control.get_attribute("placeholder")

                # Semantic attributes are authoritative.
                if any(
                    _semantic_text_match(wanted, candidate)
                    for candidate in (control_id, control_name, placeholder_value)
                    if candidate
                ):
                    candidates.append(control)
                    continue

                # Explicit label[for] -> control relationship.
                if control_id:
                    linked_label = page.locator(
                        f"label[for='{control_id}']"
                    )
                    if await linked_label.count():
                        label_text = _norm(
                            await linked_label.first.inner_text()
                        )
                        if _semantic_text_match(wanted, label_text):
                            candidates.append(control)
                            continue

                # Sibling/ancestor label relationship used by legacy forms.
                parent = control.locator(
                    "xpath=ancestor::*[self::form or contains(@class, 'field')][1]"
                )
                if await parent.count():
                    parent_text = _norm(await parent.inner_text())
                    if _semantic_text_match(wanted, parent_text):
                        candidates.append(control)
                        continue
            except Exception:
                continue

    # 8. Final generic DOM association fallback.
    # Some legacy Juice Shop forms expose a real native input whose label
    # relationship is present in the DOM but is not exposed consistently by
    # Playwright's accessible-name machinery. Resolve it from rendered DOM
    # context without encoding any scenario ID or page route.
    for value in (label, name, text):
        if not value:
            continue
        wanted = _norm(str(value))
        if not wanted:
            continue

        # Direct semantic id/name fallback. This remains generic: a target
        # "Username" can resolve an input with id/name "username".
        for candidate in (str(value), wanted.replace(" ", "-")):
            try:
                for selector in (
                    f"input[id='{candidate}'], textarea[id='{candidate}'], select[id='{candidate}']",
                    f"input[name='{candidate}'], textarea[name='{candidate}'], select[name='{candidate}']",
                ):
                    nodes = page.locator(selector)
                    for index in range(await nodes.count()):
                        node = nodes.nth(index)
                        if await node.is_visible():
                            candidates.append(node)
            except Exception:
                continue

        # DOM-level association fallback. It handles label[for], nested labels
        # and legacy form containers while still deriving the match from the
        # action target supplied by the scenario.
        try:
            selectors = await page.locator(
                "input:not([type='hidden']), textarea, select"
            ).evaluate_all(
                """(controls, wanted) => controls.map((el) => {
                    const visible = !!(
                        el.offsetWidth || el.offsetHeight || el.getClientRects().length
                    );
                    if (!visible) return null;

                    const own = [
                        el.id,
                        el.name,
                        el.getAttribute('aria-label'),
                        el.getAttribute('placeholder'),
                        el.getAttribute('title')
                    ].filter(Boolean).join(' ');

                    const labels = Array.from(document.querySelectorAll('label'))
                        .filter(label => label.htmlFor === el.id || label.contains(el))
                        .map(label => label.textContent || '')
                        .join(' ');

                    const container = el.closest(
                        'form, .profile-field, .field, [class*="field"], [class*="form"]'
                    );

                    const context = [
                        own,
                        labels,
                        container ? container.textContent || '' : ''
                    ].join(' ').toLowerCase();

                    const tokens = wanted.split(/\\s+/).filter(Boolean);
                    if (!tokens.length || !tokens.every(token => context.includes(token))) {
                        return null;
                    }

                    if (el.id) {
                        return '#' + CSS.escape(el.id);
                    }

                    if (el.name) {
                        return el.tagName.toLowerCase() +
                            '[name="' + CSS.escape(el.name) + '"]';
                    }

                    return null;
                }).filter(Boolean)""",
                wanted,
            )

            for selector in selectors:
                try:
                    node = page.locator(str(selector)).first
                    if await node.is_visible():
                        candidates.append(node)
                except Exception:
                    continue
        except Exception:
            pass

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

    # 9. Icon-only Angular Material controls.
    # Juice Shop intentionally uses mat-icon-button elements whose accessible
    # name can be empty because the visible action is represented only by a
    # Font Awesome icon (plus, minus, trash, etc.). The scenario still names
    # the user action semantically. Map that intent to the icon metadata
    # instead of hard-coding a page or scenario selector.
    if role and role.lower() in {"button", "link"} and name:
        wanted = _norm(str(name))
        icon_patterns: list[tuple[tuple[str, ...], str]] = [
            (("print", "printer", "printing"),
             "fa-print, print, printer"),
            (("increase", "increment", "plus", "add"),
             "fa-plus-square, fa-plus, fa-circle-plus, mat-icon"),
            (("decrease", "decrement", "minus", "subtract"),
             "fa-minus-square, fa-minus, fa-circle-minus, mat-icon"),
            (("remove", "delete", "trash", "discard"),
             "fa-trash-alt, fa-trash, fa-trash-can, delete, trash"),
        ]

        for keywords, icon_selector in icon_patterns:
            if not any(keyword in wanted for keyword in keywords):
                continue

            icon_nodes = page.locator(
                "button, a, [role='button'], [role='link']"
            )
            try:
                count = await icon_nodes.count()
            except Exception:
                count = 0

            for index in range(count):
                node = icon_nodes.nth(index)
                try:
                    if not await node.is_visible():
                        continue
                    html = (await node.inner_html()).casefold()
                    classes = (await node.get_attribute("class") or "").casefold()
                    aria = _norm(await node.get_attribute("aria-label"))
                    title = _norm(await node.get_attribute("title"))
                    icon_blob = " ".join((html, classes, aria, title))
                    if any(token in icon_blob for token in icon_selector.split(", ")):
                        candidates.append(node)
                except Exception:
                    continue

            break

    # 10. Radio controls without an accessible name.
    # Angular Material renders the radio itself without an accessible name in
    # several Juice Shop tables. Associate it with the semantic text of its
    # containing row so targets such as "Address", "Standard" or a card suffix
    # remain generic and do not depend on table position.
    if role and role.lower() == "radio" and name:
        wanted = _norm(str(name))
        radio_nodes = page.locator("mat-radio-button, [role='radio']")
        try:
            count = await radio_nodes.count()
        except Exception:
            count = 0

        for index in range(count):
            radio = radio_nodes.nth(index)
            try:
                if not await radio.is_visible():
                    continue

                own = " ".join(filter(None, [
                    await radio.get_attribute("aria-label"),
                    await radio.get_attribute("title"),
                ]))
                if _semantic_text_match(wanted, _norm(own)):
                    candidates.append(radio)
                    continue

                row = radio.locator(
                    "xpath=ancestor::*[self::mat-row or self::tr or @role='row'][1]"
                )
                if await row.count():
                    row_text = _norm(await row.first.inner_text())
                    if _semantic_text_match(wanted, row_text):
                        candidates.append(radio)
                        continue

                    cells = row.first.locator(
                        "td, mat-cell, [role='cell'], [role='gridcell']"
                    )
                    for cell_index in range(await cells.count()):
                        cell = cells.nth(cell_index)
                        if await cell.is_visible() and _semantic_text_match(
                            wanted, await cell.inner_text()
                        ):
                            candidates.append(radio)
                            break
            except Exception:
                continue

    # Angular Material tables can expose unnamed radios whose semantic
    # meaning comes from the column header rather than the radio itself.
    # Resolve the requested column first and then select a radio from the
    # first visible data row in that same column. This is generic for address,
    # delivery, payment and any future table-backed selection.
    if role and role.lower() == "radio" and name and not candidates:
        wanted = _norm(str(name))
        tables = page.locator("table, mat-table")
        try:
            table_count = await tables.count()
        except Exception:
            table_count = 0

        for table_index in range(table_count):
            table = tables.nth(table_index)
            try:
                if not await table.is_visible():
                    continue

                headers = table.locator("th, mat-header-cell")
                header_count = await headers.count()
                matched_column = None

                for header_index in range(header_count):
                    header = headers.nth(header_index)
                    if not await header.is_visible():
                        continue
                    if _semantic_text_match(wanted, _norm(await header.inner_text())):
                        matched_column = header_index
                        break

                if matched_column is None:
                    continue

                rows = table.locator("tbody tr, mat-row, [role='row']")
                row_count = await rows.count()
                for row_index in range(row_count):
                    row = rows.nth(row_index)
                    if not await row.is_visible():
                        continue

                    cells = row.locator("td, mat-cell, [role='cell']")
                    cell_count = await cells.count()
                    if matched_column >= cell_count:
                        continue

                    cell = cells.nth(matched_column)
                    radios = cell.locator("mat-radio-button, [role='radio']")
                    radio = await first_visible([radios])
                    if radio is not None:
                        candidates.append(radio)
                        break

                if candidates:
                    break
            except Exception:
                continue

        # Do not fall back to an arbitrary visible radio merely because a
        # matching header exists. The address table can be rendered before its
        # data rows are available, and another radio elsewhere on the page is
        # not evidence that the requested semantic control exists.
        #
        # This distinction is important for checkout preconditions: resolving
        # a phantom "Address" radio would make the fixture look valid and let
        # the scenario proceed until Checkout redirects to /#/address/create.

    result = await first_visible(candidates)
    if result is not None:
        return result

    # Final retry for legacy native forms whose DOM attributes are
    # normalized differently from the scenario wording (e.g. Username -> username).
    values = [label, name, text]
    for value in values:
        if not value:
            continue
        wanted = _norm(str(value))
        if not wanted:
            continue
        try:
            controls = page.locator("input, textarea, select")
            for index in range(await controls.count()):
                control = controls.nth(index)
                if not await control.is_visible():
                    continue
                attrs = [
                    await control.get_attribute("id"),
                    await control.get_attribute("name"),
                    await control.get_attribute("aria-label"),
                    await control.get_attribute("placeholder"),
                ]
                if any(_semantic_text_match(wanted, attr) for attr in attrs if attr):
                    return control
        except Exception:
            continue

    return None


async def resolve(page: Page, target: dict) -> Locator | None:
    """
    Resolve a target with short, fresh DOM retries.

    The important distinction from the previous implementation is that each
    retry rebuilds the semantic candidate set. Angular can replace controls
    after navigation, data loading or change detection; retaining the original
    Locator list can therefore keep searching a stale DOM representation.
    """
    # SPA/Angular data-backed views can become semantically available after
    # the route has already changed. Keep the retry budget bounded, but give
    # the UI enough time to hydrate before declaring a locator unavailable.
    attempts = 16
    for attempt in range(attempts):
        result = await _resolve_once(page, target)
        if result is not None:
            return result
        if attempt < attempts - 1:
            await page.wait_for_timeout(150)

    return None
