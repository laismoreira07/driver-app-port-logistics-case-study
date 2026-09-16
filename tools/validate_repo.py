#!/usr/bin/env python3
"""Validate links and structured examples without external dependencies."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "README.en.md",
    "DISCLAIMER.md",
    "assets/hero.svg",
    "assets/demo-flow.gif",
    "assets/demo-flow-preview.png",
    "examples/conceptual-events.json",
    "examples/test-scenarios.csv",
]

LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def validate_required(errors: list[str]) -> None:
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def validate_json(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON: {path.relative_to(ROOT)}: {exc}")


def validate_csv(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.csv")):
        with path.open(encoding="utf-8", newline="") as stream:
            rows = list(csv.reader(stream))
        if not rows:
            errors.append(f"empty CSV: {path.relative_to(ROOT)}")
            continue
        expected = len(rows[0])
        for index, row in enumerate(rows[1:], start=2):
            if len(row) != expected:
                errors.append(
                    f"CSV column mismatch: {path.relative_to(ROOT)}:{index} "
                    f"expected {expected}, got {len(row)}"
                )


def validate_relative_links(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in LINK_PATTERN.finditer(line):
                target = match.group(1).strip()
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = target.split("#", 1)[0]
                if not target:
                    continue
                resolved = (path.parent / target).resolve()
                try:
                    resolved.relative_to(ROOT.resolve())
                except ValueError:
                    errors.append(f"link escapes repository: {path.relative_to(ROOT)}:{line_number}: {target}")
                    continue
                if not resolved.exists():
                    errors.append(f"broken relative link: {path.relative_to(ROOT)}:{line_number}: {target}")


def validate_assets(errors: list[str]) -> None:
    gif = ROOT / "assets/demo-flow.gif"
    png = ROOT / "assets/demo-flow-preview.png"
    if gif.is_file() and not gif.read_bytes().startswith((b"GIF87a", b"GIF89a")):
        errors.append("demo-flow.gif does not have a GIF signature")
    if png.is_file() and not png.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"):
        errors.append("demo-flow-preview.png does not have a PNG signature")


def main() -> int:
    errors: list[str] = []
    validate_required(errors)
    validate_json(errors)
    validate_csv(errors)
    validate_relative_links(errors)
    validate_assets(errors)

    if errors:
        print("REPOSITORY VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("REPOSITORY VALIDATION PASSED")
    print("Required files, JSON, CSV, local links and asset signatures are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
