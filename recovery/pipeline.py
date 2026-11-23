from __future__ import annotations

import argparse
import asyncio

from recovery.discover import DiscoveryConfig, discover


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="AMBOLS — exploração comportamental da UI do Juice Shop")
    parser.add_argument("--domains", action="append", default=[])
    parser.add_argument("--scenario", action="append", default=[])
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--max-steps", type=int, default=30)
    parser.add_argument("--max-variants", type=int, default=6)
    parser.add_argument("--zap", action="store_true")
    args = parser.parse_args(argv)
    result = asyncio.run(discover(DiscoveryConfig(
        timeout_seconds=args.timeout, domains=tuple(args.domains),
        scenario_ids=tuple(args.scenario), max_steps_per_scenario=args.max_steps,
        max_variants_per_input=args.max_variants, zap=args.zap)))
    print(f"[recovery] cenários: {result['counts']['scenarios']}")
    print(f"[recovery] comportamentos: {result['counts']['behaviors']}")
    print(f"[recovery] alternativas: {result['counts']['alternatives']}")
    print("[recovery] artifacts: reports/recovery/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
