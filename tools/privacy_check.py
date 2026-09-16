#!/usr/bin/env python3
"""Lightweight pre-publication privacy and secret scan for this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".csv",
    ".json",
    ".py",
    ".svg",
    ".yml",
    ".yaml",
    ".gitignore",
}

FORBIDDEN_SUFFIXES = {
    ".mov",
    ".mp4",
    ".m4v",
    ".avi",
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".pem",
    ".key",
    ".p12",
    ".pfx",
}

FORBIDDEN_DIRS = {"source-material", "private", "raw", "uploads"}

PATTERNS = {
    "CPF-like number": re.compile(r"(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)"),
    "CNPJ-like number": re.compile(r"(?<!\d)\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}(?!\d)"),
    "Brazilian plate": re.compile(r"\b[A-Z]{3}[0-9][A-Z0-9][0-9]{2}\b"),
    "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "phone number": re.compile(
        r"(?<!\d)(?:(?:\+?55\s*)?\(?\d{2}\)?\s*(?:9\d{4}|\d{4})[-\s]\d{4}|\+55\d{10,11})(?!\d)"
    ),
    "assigned secret": re.compile(
        r"(?i)(?:password|passwd|secret|access[_-]?token|refresh[_-]?token|api[_-]?key|private[_-]?key)"
        r"\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{8,}"
    ),
    "bearer credential": re.compile(r"(?i)\bbearer\s+[A-Za-z0-9_./+=-]{16,}"),
}


def is_text_file(path: Path) -> bool:
    return path.name == ".gitignore" or path.suffix.lower() in TEXT_SUFFIXES


def main() -> int:
    problems: list[str] = []

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue

        relative = path.relative_to(ROOT)
        lower_parts = {part.lower() for part in relative.parts}

        if lower_parts & FORBIDDEN_DIRS:
            problems.append(f"forbidden source directory: {relative}")

        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            problems.append(f"forbidden source/binary type: {relative}")

        if path.stat().st_size > 5 * 1024 * 1024:
            problems.append(f"file larger than 5 MiB: {relative}")

        if not is_text_file(path):
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            problems.append(f"text file is not valid UTF-8: {relative}")
            continue

        for label, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                line_number = text.count("\n", 0, match.start()) + 1
                problems.append(f"{label}: {relative}:{line_number}")

    if problems:
        print("PUBLICATION CHECK FAILED")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("PUBLICATION CHECK PASSED")
    print("No forbidden source files or common personal/secret patterns were found.")
    print("Manual review is still required before publication.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
