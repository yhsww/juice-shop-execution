from __future__ import annotations

from typing import Any
from playwright.async_api import Page


async def discover_controls(page: Page) -> list[dict[str, Any]]:
    script = """() => {
      const visible = el => {
        const s = getComputedStyle(el);
        return s.display !== 'none' && s.visibility !== 'hidden' &&
          s.opacity !== '0' && !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);
      };
      const text = el => (el.innerText || el.textContent || '').replace(/\\s+/g,' ').trim();
      const nodes = [...document.querySelectorAll(
        'input,textarea,select,button,a,[role="button"],[role="link"],[role="checkbox"],[role="radio"],[role="tab"]'
      )].filter(visible);
      return nodes.map((el, index) => {
        const label = el.getAttribute('aria-label') || el.getAttribute('title') ||
          el.getAttribute('placeholder') || text(el) || el.getAttribute('name') ||
          el.getAttribute('id') || ('controle-' + index);
        const tag = el.tagName.toLowerCase();
        const role = el.getAttribute('role') || tag;
        const enabled = !el.disabled && el.getAttribute('aria-disabled') !== 'true';
        const identity = el.getAttribute('id') || el.getAttribute('name') ||
          el.getAttribute('data-testid') || el.getAttribute('formcontrolname') || label;
        return {
          index, key: tag + '|' + role + '|' + identity.toLowerCase(),
          tag, role, label, type: el.getAttribute('type') || '',
          name: el.getAttribute('name') || '', id: el.getAttribute('id') || '',
          placeholder: el.getAttribute('placeholder') || '',
          aria_label: el.getAttribute('aria-label') || '',
          required: !!el.required || el.getAttribute('aria-required') === 'true',
          disabled: !enabled, enabled, readonly: !!el.readOnly, visible: true,
          checked: 'checked' in el ? !!el.checked : el.getAttribute('aria-checked'),
          selected: 'selected' in el ? !!el.selected : el.getAttribute('aria-selected'),
          value: ('value' in el ? String(el.value || '') : ''),
          minlength: el.getAttribute('minlength'), maxlength: el.getAttribute('maxlength'),
          min: el.getAttribute('min'), max: el.getAttribute('max'),
          options: tag === 'select'
            ? [...el.options].map(o => ({label:o.textContent.trim(), value:o.value})).slice(0,12)
            : []
        };
      });
    }"""
    try:
        return list(await page.evaluate(script))
    except Exception:
        return []


def locator_for(page: Page, control: dict[str, Any]):
    label = str(control.get("label") or "")
    role = str(control.get("role") or "")
    tag = str(control.get("tag") or "")
    element_id = str(control.get("id") or "").strip()
    name = str(control.get("name") or "").strip()

    if role in {"button", "link", "tab", "checkbox", "radio"} and label:
        return page.get_by_role(role, name=label, exact=False).first

    if tag in {"input", "textarea", "select"}:
        if element_id:
            return page.locator(f"#{element_id}").first
        if label:
            by_label = page.get_by_label(label, exact=False).first
            return by_label
        if name:
            return page.locator(
                f'{tag}[name="{name.replace(chr(34), chr(92) + chr(34))}"]'
            ).first
        if tag in {"input", "textarea"} and control.get("placeholder"):
            return page.get_by_placeholder(str(control["placeholder"]), exact=False).first
        return page.locator(tag).nth(int(control.get("index", 0)))

    return page.locator(tag).nth(int(control.get("index", 0)))


async def click_control(page: Page, control: dict[str, Any]) -> bool:
    try:
        loc = locator_for(page, control)
        await loc.scroll_into_view_if_needed(timeout=1500)
        await loc.click(timeout=2500)
        return True
    except Exception:
        try:
            await locator_for(page, control).click(timeout=2500, force=True)
            return True
        except Exception:
            return False


async def fill_control(page: Page, control: dict[str, Any], value: str) -> bool:
    try:
        loc = locator_for(page, control)
        await loc.fill(value, timeout=2500)
        return True
    except Exception:
        try:
            loc = locator_for(page, control)
            await loc.click(timeout=1500)
            await page.keyboard.press("Control+A")
            await page.keyboard.type(value)
            return True
        except Exception:
            return False


async def select_control(page: Page, control: dict[str, Any], option_index: int = 0) -> bool:
    options = control.get("options") or []
    if not options or option_index >= len(options):
        return False
    try:
        await locator_for(page, control).select_option(value=options[option_index].get("value"))
        return True
    except Exception:
        return False
