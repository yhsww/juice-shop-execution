from __future__ import annotations

import argparse
import asyncio

from automation.runner import run_selected


def main() -> None:
    parser = argparse.ArgumentParser(description="Executa cenários do OWASP Juice Shop.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--scenario", action="append", help="ID do cenário. Pode ser repetido.")
    group.add_argument("--all", action="store_true", help="Executa todos os cenários cadastrados.")
    args = parser.parse_args()

    ids = None if args.all else set(args.scenario or [])
    results = asyncio.run(run_selected(ids))

    for result in results:
        print(f"[{result['status']}] {result['scenario_id']}")


if __name__ == "__main__":
    main()
