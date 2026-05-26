#!/usr/bin/env python3
"""Regenerate README.md from data/military-ranges.yaml."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "military-ranges.yaml"
README_FILE = ROOT / "README.md"


def hex_key(entry: dict) -> int:
    return int(entry["hex_start"], 16)


def render_range_row(entry: dict) -> str:
    unit = entry.get("unit", "") or ""
    return f"| `{entry['hex_start']}`–`{entry['hex_end']}` | {entry['country']} | {unit} |"


def render_disabled_row(entry: dict) -> str:
    return f"| `{entry['hex_start']}`–`{entry['hex_end']}` | {entry['country']} | {entry.get('notes', '')} |"


def render_source(entry: dict) -> str:
    line = f"- [{entry['title']}]({entry['url']})"
    if note := entry.get("note"):
        line += f" ({note})"
    return line


def build_readme(data: dict) -> str:
    ranges = sorted(data.get("ranges", []), key=hex_key)
    disabled = sorted(data.get("disabled", []), key=hex_key)
    gaps = data.get("gaps", [])
    sources = data.get("sources", [])

    out: list[str] = []
    out.append("# icao-mil")
    out.append("Exhaustive list of military ICAO hex ranges")
    out.append("")
    out.append("## Global military ICAO 24-bit hex ranges")
    out.append("")
    out.append(
        "The table below lists ICAO 24-bit aircraft address ranges reserved for, or "
        "commonly used by, military aircraft worldwide. There is no single official "
        "global registry of military allocations — this list is compiled from "
        "community-maintained sources (primarily the `MIL_RANGES` table in "
        "[readsb](https://github.com/wiedehopf/readsb), which is the de facto "
        "standard used by tar1090, ADSB Exchange, and most open-source ADS-B "
        "decoders)."
    )
    out.append("")
    out.append(
        "Ranges are sorted ascending by hex start. The \"Unit / Branch\" column is "
        "left empty where the specific service is not publicly documented."
    )
    out.append("")
    out.append("> This file is generated from [`data/military-ranges.yaml`](data/military-ranges.yaml). Do not edit by hand.")
    out.append("")
    out.append("| Hex Range | Country | Unit / Branch |")
    out.append("|-----------|---------|---------------|")
    out.extend(render_range_row(r) for r in ranges)
    out.append("")

    if disabled:
        out.append("### Disabled / collision-prone ranges")
        out.append("")
        out.append(
            "The following ranges appear in older lists but are disabled in the "
            "upstream community source because they overlap with civilian aircraft "
            "and would generate false positives:"
        )
        out.append("")
        out.append("| Hex Range | Country | Notes |")
        out.append("|-----------|---------|-------|")
        out.extend(render_disabled_row(r) for r in disabled)
        out.append("")

    if gaps:
        out.append("### Notable gaps")
        out.append("")
        out.append(
            "Several major military operators do not have dedicated published "
            "sub-allocations in the community lists, either because they share the "
            "national civilian block, do not broadcast distinguishably on ADS-B, or "
            "their assignments are not publicly documented:"
        )
        out.append("")
        out.extend(f"- {gap}" for gap in gaps)
        out.append("")

    if sources:
        out.append("## Sources")
        out.append("")
        out.extend(render_source(s) for s in sources)
        out.append("")

    return "\n".join(out)


def main(argv: list[str]) -> int:
    check = "--check" in argv

    data = yaml.safe_load(DATA_FILE.read_text())
    rendered = build_readme(data)

    if check:
        existing = README_FILE.read_text() if README_FILE.exists() else ""
        if existing != rendered:
            sys.stderr.write(
                "README.md is out of sync with data/military-ranges.yaml.\n"
                "Run: python scripts/generate_readme.py\n"
            )
            return 1
        return 0

    README_FILE.write_text(rendered)
    print(f"Wrote {README_FILE.relative_to(ROOT)} ({len(data.get('ranges', []))} ranges)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
