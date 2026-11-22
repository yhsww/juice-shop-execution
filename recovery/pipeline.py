from __future__ import annotations

import argparse
import asyncio

from recovery.discover import DiscoveryConfig, discover


def main() -> int:
    parser = argparse.ArgumentParser(description="AMBOLS deterministic reverse-engineering pipeline")
    parser.add_argument("--max-pages", type=int, default=30)
    parser.add_argument("--max-depth", type=int, default=2)
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()
    result = asyncio.run(discover(DiscoveryConfig(args.max_pages, args.max_depth, args.timeout)))
    print(f"[recovery] páginas: {result['pages_observed']}")
    print(f"[recovery] transições: {result['transitions_observed']}")
    print(f"[recovery] requisitos candidatos: {len(result['candidate_requirements'])}")
    print("[recovery] artifacts: reports/recovery/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
