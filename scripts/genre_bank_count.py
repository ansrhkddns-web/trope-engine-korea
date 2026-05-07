#!/usr/bin/env python3
"""Verify genre cliche bank markdown sections contain the expected item counts.

Usage:
  python genre_bank_count.py references/genre-cliche-bank-100-a.md references/genre-cliche-bank-100-b.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SECTION_RE = re.compile(r"^##\s+(G\d{2})\s+(.+?)\s*$")
ITEM_RE = re.compile(r"^-\s+([A-Z]{3}-\d{3})\s+\|")


def count_file(path: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    current: str | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        section_match = SECTION_RE.match(line)
        if section_match:
            current = section_match.group(1)
            counts.setdefault(current, 0)
            continue
        if current and ITEM_RE.match(line):
            counts[current] += 1

    return counts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Count cliche seeds in genre bank markdown files.")
    parser.add_argument("paths", nargs="+", help="Markdown files to inspect.")
    parser.add_argument("--expected", type=int, default=100, help="Expected item count per genre.")
    args = parser.parse_args(argv)

    failed = False
    for raw_path in args.paths:
        path = Path(raw_path)
        counts = count_file(path)
        if not counts:
            print(f"{path}: no genre sections found")
            failed = True
            continue
        for genre_id, count in sorted(counts.items()):
            status = "OK" if count == args.expected else "FAIL"
            print(f"{path.name} {genre_id}: {count} ({status})")
            if count != args.expected:
                failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
