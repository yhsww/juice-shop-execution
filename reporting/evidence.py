from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path

from playwright.async_api import Page


@dataclass
class Evidence:
    step: int
    action: str
    user_action: str
    data: str
    url_before: str
    url_after: str
    observed_result: str
    changed: bool
    success: bool
    screenshot: str | None
    error: str | None
    timestamp: str
    visible_text_before: str = ""
    visible_text_after: str = ""
    messages: tuple[str, ...] = ()


async def capture(page: Page, directory: Path, scenario_id: str, step: int) -> str:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{scenario_id}_step_{step:02d}.png"
    await page.screenshot(path=str(path), full_page=True)
    return str(path).replace("\\", "/")


def save_execution(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()
