from __future__ import annotations

import argparse
import asyncio
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

from automation.runner import run_selected

ROOT = Path(__file__).resolve().parent
COMPOSE_FILE = ROOT / "juice-shop" / "docker-compose.yml"
BASE_URL = "http://127.0.0.1:3000"


def _http_ready(url: str, timeout: float = 3.0) -> bool:
    try:
        with urlopen(url, timeout=timeout) as response:
            return 200 <= response.status < 500
    except (URLError, TimeoutError, OSError):
        return False


def _docker_compose(*args: str) -> None:
    import subprocess
    if not COMPOSE_FILE.is_file():
        raise FileNotFoundError(f"Arquivo Docker Compose não encontrado: {COMPOSE_FILE}")
    command = ["docker", "compose", "-f", str(COMPOSE_FILE), *args]
    try:
        completed = subprocess.run(command, cwd=ROOT, check=False)
    except FileNotFoundError as exc:
        raise RuntimeError("Docker CLI não encontrado. Instale/abra o Docker Desktop e tente novamente.") from exc
    if completed.returncode != 0:
        raise RuntimeError(f"Falha no comando: {' '.join(command)} (código {completed.returncode}).")


def ensure_juice_shop(start_if_needed: bool, wait_seconds: int = 90) -> None:
    if _http_ready(BASE_URL):
        print(f"[app] Juice Shop já está disponível em {BASE_URL}")
        return
    if not start_if_needed:
        raise RuntimeError(f"Juice Shop não respondeu em {BASE_URL}. Inicie-o com --start-app.")
    print("[app] Juice Shop indisponível. Iniciando o serviço incorporado...")
    _docker_compose("up", "-d")
    deadline = time.monotonic() + wait_seconds
    while time.monotonic() < deadline:
        if _http_ready(BASE_URL):
            print(f"[app] Juice Shop pronto em {BASE_URL}")
            return
        time.sleep(2)
    try:
        _docker_compose("logs", "--tail", "60")
    except RuntimeError:
        pass
    raise TimeoutError(f"O Juice Shop não respondeu em {BASE_URL} após {wait_seconds}s.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Executa cenários e exploração comportamental do OWASP Juice Shop.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--scenario", action="append")
    group.add_argument("--domain", action="append")
    group.add_argument("--all", action="store_true")
    group.add_argument("--discover", "--reverse-engineer", dest="discover", action="store_true")
    parser.add_argument("--start-app", action="store_true")
    parser.add_argument("--wait-app", type=int, default=90)
    parser.add_argument("--stop-app", action="store_true")
    parser.add_argument("--zap", action="store_true")
    parser.add_argument("--recovery-domain", action="append", default=[])
    parser.add_argument("--recovery-scenario", action="append", default=[])
    parser.add_argument("--recovery-timeout", type=int, default=180)
    parser.add_argument("--recovery-max-steps", type=int, default=30)
    parser.add_argument("--recovery-max-variants", type=int, default=6)
    args = parser.parse_args()
    if args.stop_app and not args.start_app:
        parser.error("--stop-app requer --start-app.")
    if args.zap and not args.discover:
        parser.error("--zap só pode ser usado com --discover/--reverse-engineer.")

    try:
        ensure_juice_shop(args.start_app, args.wait_app)
        if args.discover:
            from recovery.pipeline import main as recovery_main
            recovery_args = ["--timeout", str(args.recovery_timeout),
                             "--max-steps", str(args.recovery_max_steps),
                             "--max-variants", str(args.recovery_max_variants)]
            for domain in args.recovery_domain:
                recovery_args += ["--domains", domain]
            for scenario in args.recovery_scenario:
                recovery_args += ["--scenario", scenario]
            if args.zap:
                recovery_args.append("--zap")
            return recovery_main(recovery_args)

        ids = None if args.all or args.domain else set(args.scenario or [])
        domains = None if args.all or args.scenario else {item.upper() for item in (args.domain or [])}
        results = asyncio.run(run_selected(ids=ids, domains=domains))
        for result in results:
            print(f"[{result['status']}] {result['scenario_id']}")
        failed = sum(result.get("status") != "PASSED" for result in results)
        print(f"[summary] {len(results) - failed}/{len(results)} cenários aprovados; {failed} com falha.")
        return 1 if failed else 0
    except (RuntimeError, TimeoutError, FileNotFoundError, ValueError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 2
    finally:
        if args.stop_app:
            try:
                _docker_compose("down")
                print("[app] Container Juice Shop encerrado.")
            except RuntimeError as exc:
                print(f"[warning] Não foi possível encerrar o container: {exc}", file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
