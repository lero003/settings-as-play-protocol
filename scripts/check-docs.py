#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
OKF_TEMPLATE_ROOT = ROOT / "templates" / "sapp-okf"
OKF_BUNDLE_ROOTS = (OKF_TEMPLATE_ROOT, ROOT / "examples" / "okf")
SAPP_STATUSES = {"draft", "public-draft", "released", "archived"}
OKF_STATUSES = {"draft", "stable", "deprecated"}


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects ambiguous duplicate mapping keys."""

    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)
        seen = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                duplicate = key in seen
                seen.add(key)
            except TypeError as error:
                raise yaml.constructor.ConstructorError(
                    None, None, "mapping keys must be hashable", key_node.start_mark
                ) from error
            if duplicate:
                raise yaml.constructor.ConstructorError(
                    None, None, f"duplicate key: {key}", key_node.start_mark
                )
        return super().construct_mapping(node, deep=deep)


def read_front_matter(path: Path, text: str, errors: list[str]) -> dict | None:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return None
    label = path.relative_to(ROOT)
    try:
        closing = lines.index("---", 1)
    except ValueError:
        errors.append(f"{label}: missing closing front matter delimiter")
        return None
    try:
        metadata = yaml.load("\n".join(lines[1:closing]), Loader=UniqueKeyLoader)
    except (yaml.YAMLError, ValueError) as error:
        errors.append(f"{label}: invalid YAML front matter: {error}")
        return None
    if not isinstance(metadata, dict) or any(not isinstance(key, str) for key in metadata):
        errors.append(f"{label}: front matter must be a mapping with string keys")
        return None
    return metadata


def check_metadata(path: Path, metadata: dict, errors: list[str], *, okf: bool = False) -> None:
    """Check the metadata structures used by SaPP's profile, not body meaning."""
    label = path.relative_to(ROOT)

    def fail(message: str) -> None:
        errors.append(f"{label}: {message}")

    def string(mapping: dict, key: str, context: str = "", *, required: bool = False) -> bool:
        if key not in mapping and not required:
            return True
        value = mapping.get(key)
        valid = isinstance(value, str) and bool(value.strip())
        if not valid:
            fail(f"{context}{key} must be a non-empty string")
        return valid

    def timestamp(value, context: str) -> None:
        try:
            instant = datetime.fromisoformat(value.replace("Z", "+00:00")) if isinstance(value, str) else value
            valid = isinstance(instant, datetime) and instant.utcoffset() is not None
        except (ValueError, TypeError):
            valid = False
        if not valid:
            fail(f"{context} must be an ISO 8601 datetime with a UTC offset")

    for key in ("sapp_version", "card_type", "card_id", "card_revision", "derived_from_revision"):
        string(metadata, key)
    if "card_revision" in metadata and (
        not isinstance(metadata.get("card_id"), str) or not metadata["card_id"].strip()
    ):
        fail("card_revision requires card_id")
    if "derived_from_revision" in metadata and (
        not isinstance(metadata.get("derived_from"), str) or not metadata["derived_from"].strip()
    ):
        fail("derived_from_revision requires derived_from")
    if "sapp_status" in metadata and (
        not isinstance(metadata["sapp_status"], str) or metadata["sapp_status"] not in SAPP_STATUSES
    ):
        fail("sapp_status must be draft, public-draft, released, or archived")
    if "status" in metadata:
        allowed = OKF_STATUSES if okf else SAPP_STATUSES
        if not isinstance(metadata["status"], str) or metadata["status"] not in allowed:
            fail("status must be " + ", ".join(sorted(allowed)))
    if not okf:
        if "status" in metadata and "sapp_status" in metadata and metadata["status"] != metadata["sapp_status"]:
            fail("legacy status and sapp_status must agree outside OKF bundles")
        return

    string(metadata, "type", required=True)
    for key in ("title", "description", "resource"):
        string(metadata, key)
    if "tags" in metadata and (
        not isinstance(metadata["tags"], list)
        or any(not isinstance(tag, str) or not tag.strip() for tag in metadata["tags"])
    ):
        fail("tags must be a list of non-empty strings")
    if "sources" in metadata:
        if not isinstance(metadata["sources"], list):
            fail("sources must be a list of mappings")
        else:
            for index, source in enumerate(metadata["sources"]):
                context = f"sources[{index}]."
                if not isinstance(source, dict):
                    fail(f"{context[:-1]} must be a mapping")
                    continue
                string(source, "resource", context, required=True)
                for key in ("id", "title", "author"):
                    string(source, key, context)
    for key in ("generated", "verified"):
        if key not in metadata:
            continue
        value = metadata[key]
        events = value if key == "verified" and isinstance(value, list) else [value]
        for index, event in enumerate(events):
            context = f"{key}[{index}]." if isinstance(value, list) else f"{key}."
            if not isinstance(event, dict):
                fail(f"{context[:-1]} must be a mapping")
                continue
            string(event, "by", context, required=True)
            if "at" in event or key == "verified":
                timestamp(event.get("at"), f"{context}at")
    if "stale_after" in metadata:
        timestamp(metadata["stale_after"], "stale_after")


def iter_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not {".git", ".venv", "__pycache__"}.intersection(path.parts)
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


def check_hidden_unicode(path: Path, text: str, errors: list[str]) -> None:
    for index, character in enumerate(text):
        if unicodedata.category(character) != "Cf":
            continue
        line = text.count("\n", 0, index) + 1
        column = index - text.rfind("\n", 0, index)
        codepoint = f"U+{ord(character):04X}"
        name = unicodedata.name(character, "UNKNOWN FORMAT CHARACTER")
        errors.append(
            f"{path.relative_to(ROOT)}:{line}:{column}: hidden Unicode {codepoint} {name}"
        )


def check_okf_template(front_matters: dict[Path, dict | None], errors: list[str]) -> None:
    if not (OKF_TEMPLATE_ROOT / "index.md").exists() or not (OKF_TEMPLATE_ROOT / "setting.md").exists():
        errors.append("templates/sapp-okf: expected index.md and setting.md")
    for root in OKF_BUNDLE_ROOTS:
        if not root.exists():
            continue
        index_path = root / "index.md"
        metadata = front_matters.get(index_path)
        if metadata is None or metadata.get("okf_version") != "0.2":
            errors.append(f'{index_path.relative_to(ROOT)}: expected okf_version: "0.2"')


def main() -> int:
    errors: list[str] = []
    front_matters: dict[Path, dict | None] = {}
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        check_trailing_whitespace(path, text, errors)
        check_local_links(path, text, errors)
        check_local_images(path, text, errors)
        check_heading_spacing(path, text, errors)
        metadata = read_front_matter(path, text, errors)
        front_matters[path] = metadata
        okf = any(root in path.parents for root in OKF_BUNDLE_ROOTS) and path.name not in {"index.md", "log.md"}
        if metadata is not None:
            check_metadata(path, metadata, errors, okf=okf)
        elif okf:
            errors.append(f"{path.relative_to(ROOT)}: OKF concepts require YAML front matter")
        check_hidden_unicode(path, text, errors)
    check_okf_template(front_matters, errors)

    if errors:
        print("\n".join(errors))
        return 1

    print("Documentation checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
