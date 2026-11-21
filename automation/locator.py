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
    # Resolve the explicit DOM label relationship before broader heuristics.
    # This keeps the resolver generic while avoiding dependence on generated
    # CSS classes or scenario-specific selectors.
    if label:
        associated = await _associated_field(page, str(label))
        if associated is not None:
            candidates.insert(0, associated)

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

    # 4. Visible text / semantic table controls.
    # Juice Shop address radios have no accessible name of their own: the
    # semantic word "Address" belongs to the table header, while the same
    # word also appears inside the "Add New Address" button. When a scenario
    # asks for a radio by name/text, resolve the radio from its table column
    # before broad text matching. This applies generically to any unnamed
    # radio whose requested name is a table header.
    if text or name:
        wanted_text = text or name
        if str(role or "").casefold() == "radio":
            candidates.extend(await _table_radio_by_header(page, str(wanted_text)))
        elif role and role.lower() not in _VALID_ROLES:
            candidates.extend(await _table_radio_by_header(page, str(wanted_text)))
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
    if name:
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

        # Some Angular Material variants omit table semantics entirely.
        # Only then fall back to the first visible radio, and only when the
        # target name matches a visible header somewhere on the page.
        if not candidates:
            headers = page.locator("th, mat-header-cell")
            try:
                header_count = await headers.count()
            except Exception:
                header_count = 0
            header_matches = False
            for index in range(header_count):
                header = headers.nth(index)
                try:
                    if await header.is_visible() and _semantic_text_match(
                        wanted, _norm(await header.inner_text())
                    ):
                        header_matches = True
                        break
                except Exception:
                    continue

            if header_matches:
                first_radio = await first_visible([
                    page.locator("mat-radio-button"),
                    page.locator("[role='radio']"),
                ])
                if first_radio is not None:
                    candidates.append(first_radio)

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
    attempts = 8
    for attempt in range(attempts):
        result = await _resolve_once(page, target)
        if result is not None:
            return result
        if attempt < attempts - 1:
            await page.wait_for_timeout(150)

    return None
