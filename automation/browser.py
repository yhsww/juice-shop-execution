from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncIterator

from playwright.async_api import Browser, BrowserContext, Page, async_playwright

from config.settings import settings


@asynccontextmanager
async def browser_session() -> AsyncIterator[tuple[Browser, BrowserContext, Page]]:
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=settings.headless,
            args=["--disable-dev-shm-usage"],
        )
        context = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            ignore_https_errors=True,
        )
        page = await context.new_page()
        page.set_default_timeout(settings.action_timeout_ms)
        page.set_default_navigation_timeout(settings.navigation_timeout_ms)
        try:
            yield browser, context, page
        finally:
            await context.close()
            await browser.close()


async def open_juice_shop(page: Page) -> None:
    await page.goto(f"{settings.base_url}/#/", wait_until="domcontentloaded")
    await page.locator("app-root").wait_for(state="attached", timeout=settings.navigation_timeout_ms)
    await page.wait_for_timeout(500)
