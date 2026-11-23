from __future__ import annotations

import argparse
import asyncio

from recovery.discover import DiscoveryConfig, discover
from recovery.report import save_stage1_report

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='AMBOLS evidence-driven reverse engineering pipeline')
    parser.add_argument('--max-pages', type=int, default=30)
    parser.add_argument('--max-depth', type=int, default=2)
    parser.add_argument('--timeout', type=int, default=120)
    parser.add_argument('--max-events', type=int, default=2000)
    parser.add_argument('--zap', action='store_true', help='Use OWASP ZAP as an optional HTTP evidence/proxy layer.')
    args = parser.parse_args(argv)
    result = asyncio.run(discover(DiscoveryConfig(max_pages=args.max_pages, max_depth=args.max_depth, timeout_seconds=args.timeout, max_events=args.max_events, zap=args.zap)))
    print(f'[recovery] páginas observadas: {result["pages_observed"]}')
    print(f'[recovery] transições observadas: {result["transitions_observed"]}')
    print(f'[recovery] comportamentos observados: {result["behaviors_observed"]}')
    print(f'[recovery] eventos de rede: {result["network_events"]}')
    save_stage1_report(__import__('pathlib').Path('reports/recovery'), result)
    print(f'[recovery] ZAP ativo: {"sim" if result["zap_proxy_active"] else "não"}')
    print('[recovery] artifacts: reports/recovery/')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())