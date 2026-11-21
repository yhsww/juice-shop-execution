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
COMPOSE_FILE = ROOT / 'juice-shop' / 'docker-compose.yml'
BASE_URL = 'http://127.0.0.1:3000'


def _http_ready(url: str, timeout: float = 3.0) -> bool:
    try:
        with urlopen(url, timeout=timeout) as response:
            return 200 <= response.status < 500
    except (URLError, TimeoutError, OSError):
        return False


def _docker_compose(*args: str) -> None:
    import subprocess

    if not COMPOSE_FILE.is_file():
        raise FileNotFoundError(f'Arquivo Docker Compose não encontrado: {COMPOSE_FILE}')
    command = ['docker', 'compose', '-f', str(COMPOSE_FILE), *args]
    try:
        completed = subprocess.run(command, cwd=ROOT, check=False)
    except FileNotFoundError as exc:
        raise RuntimeError('Docker CLI não encontrado. Instale/abra o Docker Desktop e tente novamente.') from exc
    if completed.returncode != 0:
        raise RuntimeError(f'Falha no comando: {" ".join(command)} (código {completed.returncode}).')


def ensure_juice_shop(start_if_needed: bool, wait_seconds: int = 90) -> None:
    if _http_ready(BASE_URL):
        print(f'[app] Juice Shop já está disponível em {BASE_URL}')
        return
    if not start_if_needed:
        raise RuntimeError(
            f'Juice Shop não respondeu em {BASE_URL}. Inicie-o com '
            '`python run.py --start-app --scenario CEN-IDT-01` ou passe --start-app.'
        )

    print('[app] Juice Shop indisponível. Verificando Docker e iniciando o serviço incorporado...')
    _docker_compose('version')
    _docker_compose('up', '-d')

    deadline = time.monotonic() + wait_seconds
    while time.monotonic() < deadline:
        if _http_ready(BASE_URL):
            print(f'[app] Juice Shop pronto em {BASE_URL}')
            return
        time.sleep(2)

    try:
        _docker_compose('logs', '--tail', '60')
    except RuntimeError:
        pass
    raise TimeoutError(
        f'O Juice Shop não respondeu em {BASE_URL} após {wait_seconds}s. '
        'Confira se o Docker Desktop está ativo e consulte os logs do container.'
    )


def main() -> int:
    parser = argparse.ArgumentParser(description='Executa cenários do OWASP Juice Shop.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--scenario', action='append', help='ID do cenário. Pode ser repetido.')
    group.add_argument('--domain', action='append', help='Domínio dos cenários. Pode ser repetido (ex.: CHK, IDT).')
    group.add_argument('--all', action='store_true', help='Executa todos os cenários cadastrados.')
    parser.add_argument('--start-app', action='store_true', help='Inicia o Juice Shop pelo Docker Compose incorporado se a aplicação ainda não estiver disponível.')
    parser.add_argument('--wait-app', type=int, default=90, help='Tempo máximo em segundos para aguardar a aplicação (padrão: 90).')
    parser.add_argument('--stop-app', action='store_true', help='Encerra o container após os testes; requer --start-app.')
    args = parser.parse_args()

    if args.wait_app <= 0:
        parser.error('--wait-app deve ser maior que zero.')
    if args.stop_app and not args.start_app:
        parser.error('--stop-app requer --start-app.')

    try:
        ensure_juice_shop(start_if_needed=args.start_app, wait_seconds=args.wait_app)
        ids = None if args.all or args.domain else set(args.scenario or [])
        domains = None if args.all or args.scenario else {item.upper() for item in (args.domain or [])}
        results = asyncio.run(run_selected(ids=ids, domains=domains))
        for result in results:
            print(f"[{result['status']}] {result['scenario_id']}")
        failed = sum(result.get('status') != 'PASSED' for result in results)
        print(f'[summary] {len(results) - failed}/{len(results)} cenários aprovados; {failed} com falha.')
        return 1 if failed else 0
    except (RuntimeError, TimeoutError, FileNotFoundError, ValueError) as exc:
        print(f'[error] {exc}', file=sys.stderr)
        return 2
    finally:
        if args.stop_app:
            try:
                _docker_compose('down')
                print('[app] Container Juice Shop encerrado.')
            except RuntimeError as exc:
                print(f'[warning] Não foi possível encerrar o container: {exc}', file=sys.stderr)


if __name__ == '__main__':
    raise SystemExit(main())