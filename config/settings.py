from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")


def _bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("JUICE_SHOP_BASE_URL", "http://localhost:3000").rstrip("/")
    headless: bool = _bool("JUICE_SHOP_HEADLESS", False)
    action_timeout_ms: int = int(os.getenv("JUICE_SHOP_ACTION_TIMEOUT_MS", "10000"))
    navigation_timeout_ms: int = int(os.getenv("JUICE_SHOP_NAVIGATION_TIMEOUT_MS", "15000"))
    scenario_timeout_seconds: int = int(os.getenv("JUICE_SHOP_SCENARIO_TIMEOUT_SECONDS", "180"))
    max_steps: int = int(os.getenv("JUICE_SHOP_MAX_STEPS", "30"))
    screenshot_dir: Path = ROOT / os.getenv("JUICE_SHOP_SCREENSHOT_DIR", "reports/executions")
    report_dir: Path = ROOT / os.getenv("JUICE_SHOP_REPORT_DIR", "reports/executions")
    user_email: str = os.getenv("JUICE_SHOP_USER_EMAIL", "teste@example.com")
    user_password: str = os.getenv("JUICE_SHOP_USER_PASSWORD", "Teste@12345")
    admin_email: str = os.getenv("JUICE_SHOP_ADMIN_EMAIL", "")
    admin_password: str = os.getenv("JUICE_SHOP_ADMIN_PASSWORD", "")


settings = Settings()
