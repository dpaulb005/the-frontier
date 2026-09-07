#!/usr/bin/env python3
"""Stitch the research/*.md files into one combined report and print basic stats.

Usage: python3 scripts/build_report.py [--out THE-FRONTIER-REPORT.md]
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "research"

URL_RE = re.compile(r"https?://[^\s)\]>]+")


def stats(text: str) -> dict:
    words = len(text.split())
    urls = set(URL_RE.findall(text))
    cites = len(re.findall(r"\[\d+\]", text))
    return {"words": words, "unique_urls": len(urls), "inline_citations": cites}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "THE-FRONTIER-REPORT.md"))
    args = ap.parse_args()

    files = sorted(RESEARCH.glob("*.md"))
    if not files:
        print("no research files found", file=sys.stderr)
        return 1

    parts = []
    synthesis = ROOT / "SYNTHESIS.md"
    if synthesis.exists():
        parts.append(synthesis.read_text())
        parts.append("\n\n---\n\n")

    total = {"words": 0, "unique_urls": 0, "inline_citations": 0}
    rows = []
    for f in files:
        text = f.read_text()
        s = stats(text)
        for k in total:
            total[k] += s[k]
        rows.append((f.name, s))
        parts.append(f"\n\n<!-- source: research/{f.name} -->\n\n")
        parts.append(text)
        parts.append("\n\n---\n\n")

    Path(args.out).write_text("".join(parts))

    print(f"{'file':55} {'words':>7} {'urls':>5} {'cites':>6}")
    for name, s in rows:
        print(f"{name:55} {s['words']:>7} {s['unique_urls']:>5} {s['inline_citations']:>6}")
    print(f"{'TOTAL':55} {total['words']:>7} {total['unique_urls']:>5} {total['inline_citations']:>6}")
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
