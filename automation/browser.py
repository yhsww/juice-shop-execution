from __future__ import annotations

import asyncio
import os
from contextlib import asynccontextmanager
from typing import AsyncIterator

from playwright.async_api import Browser, BrowserContext, Page, async_playwright

from config.settings import settings

@asynccontextmanager
async def browser_session() -> AsyncIterator[tuple[Browser, BrowserContext, Page]]:
    async with async_playwright() as p:
        launch_kwargs = {'headless': settings.headless, 'args': ['--disable-dev-shm-usage']}
        proxy = os.getenv('JUICE_SHOP_PROXY_SERVER', '').strip()
        if proxy: launch_kwargs['proxy'] = {'server': proxy}
        browser = await p.chromium.launch(**launch_kwargs)
        context = await browser.new_context(viewport={'width': 1440, 'height': 900}, ignore_https_errors=True)
        page = await context.new_page()
        page.set_default_timeout(settings.action_timeout_ms)
        page.set_default_navigation_timeout(settings.navigation_timeout_ms)
        try: yield browser, context, page
        finally:
            try: await asyncio.wait_for(context.close(), timeout=5)
            except Exception: pass
            try: await asyncio.wait_for(browser.close(), timeout=5)
            except Exception: pass

async def dismiss_startup_overlays(page: Page) -> None:
    selectors = ('[role=\'dialog\']', '[role=\'alertdialog\']', '.cdk-overlay-container', '.mat-mdc-dialog-container', '.mat-dialog-container')
    for selector in selectors:
        containers = page.locator(selector)
        try: count = await containers.count()
        except Exception: continue
        for index in range(count):
            container = containers.nth(index)
            try:
                if not await container.is_visible(): continue
                dismiss = container.get_by_role('button', name='Dismiss', exact=True)
                if await dismiss.count() == 0: dismiss = container.locator('button, [role=\'button\']').filter(has_text='Dismiss')
                for button_index in range(await dismiss.count()):
                    button = dismiss.nth(button_index)
                    if not await button.is_visible(): continue
                    try: await button.click(timeout=1500)
                    except Exception: await button.click(timeout=1500, force=True)
                    await page.wait_for_timeout(150)
                    return
            except Exception: continue

async def open_juice_shop(page: Page) -> None:
    await page.goto(f'{settings.base_url}/#/', wait_until='domcontentloaded')
    await page.locator('app-root').wait_for(state='attached', timeout=settings.navigation_timeout_ms)
    await page.wait_for_timeout(500)
    await dismiss_startup_overlays(page)