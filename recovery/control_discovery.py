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
      const text = el => (el.innerText || el.textContent || '').replace(/\s+/g,' ').trim();
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
