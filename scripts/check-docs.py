#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def iter_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )


def check_trailing_whitespace(path: Path, text: str, errors: list[str]) -> None:
    for index, line in enumerate(text.splitlines(), start=1):
        if line.rstrip(" \t") != line:
            errors.append(f"{path.relative_to(ROOT)}:{index}: trailing whitespace")


def check_local_links(path: Path, text: str, errors: list[str]) -> None:
    pattern = re.compile(r"(?<!!)((?:\[[^\]]*])+?)\(([^)]+)\)")
    for match in pattern.finditer(text):
        target = match.group(2).strip()
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if not (path.parent / target).exists():
            line = text.count("\n", 0, match.start()) + 1
            errors.append(f"{path.relative_to(ROOT)}:{line}: missing link target {target}")


def check_local_images(path: Path, text: str, errors: list[str]) -> None:
    pattern = re.compile(r"!\[[^\]]*]\(([^)]+)\)")
    for match in pattern.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(("http://", "https://")):
            continue
        target = target.split("#", 1)[0]
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if not (path.parent / target).exists():
            line = text.count("\n", 0, match.start()) + 1
            errors.append(f"{path.relative_to(ROOT)}:{line}: missing image target {target}")


def check_heading_spacing(path: Path, text: str, errors: list[str]) -> None:
    lines = text.splitlines()
    for index, line in enumerate(lines, start=1):
        if not line.startswith("#"):
            continue
        if not re.match(r"^#{1,6} ", line):
            errors.append(f"{path.relative_to(ROOT)}:{index}: heading should use a space after #")


def main() -> int:
    errors: list[str] = []
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        check_trailing_whitespace(path, text, errors)
        check_local_links(path, text, errors)
        check_local_images(path, text, errors)
        check_heading_spacing(path, text, errors)

    if errors:
        print("\n".join(errors))
        return 1

    print("Documentation checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
