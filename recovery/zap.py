from __future__ import annotations

import os
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
import socket


@dataclass(frozen=True)
class ZapConfig:
    enabled: bool = False
    proxy: str = ""
    docker: bool = False
    port: int = 8080
    compose_file: Path = Path(__file__).with_name("zap-compose.yml")


def load_config(enabled: bool = False) -> ZapConfig:
    proxy = os.getenv("AMBOLS_ZAP_PROXY", "").strip()
    return ZapConfig(enabled=enabled, proxy=proxy, docker=enabled and not proxy)


def ensure_zap(config: ZapConfig) -> str | None:
    if not config.enabled:
        return None
    if config.proxy:
        return config.proxy
    command = ["docker", "compose", "-f", str(config.compose_file), "up", "-d"]
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    proxy = f"http://127.0.0.1:{config.port}"
    deadline = time.monotonic() + 30
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(('127.0.0.1', config.port), timeout=1):
                return proxy
        except OSError:
            time.sleep(1)
    return None


def stop_zap(config: ZapConfig) -> None:
    if not config.docker:
        return
    try:
        subprocess.run(["docker", "compose", "-f", str(config.compose_file), "down"],
                       check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        pass
