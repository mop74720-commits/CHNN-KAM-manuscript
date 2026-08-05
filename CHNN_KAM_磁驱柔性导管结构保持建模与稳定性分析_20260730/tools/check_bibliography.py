#!/usr/bin/env python3
"""Check BibTeX keys and active citation references without external packages."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "bibliography" / "references.bib"
ACTIVE = ROOT / "manuscript"

bib_text = BIB.read_text(encoding="utf-8", errors="replace")
keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib_text)
duplicates = sorted({k for k in keys if keys.count(k) > 1})

cited: set[str] = set()
for tex in ACTIVE.rglob("*.tex"):
    text = tex.read_text(encoding="utf-8", errors="replace")
    for group in re.findall(r"\\cite\w*\s*(?:\[[^]]*\]\s*)*\{([^}]+)\}", text):
        cited.update(k.strip() for k in group.split(",") if k.strip())

missing = sorted(cited - set(keys))
print(f"BibTeX entries: {len(keys)}")
print(f"Active cited keys: {len(cited)}")
print(f"Unused database entries: {len(set(keys) - cited)}")
if duplicates:
    print("Duplicate keys:", ", ".join(duplicates), file=sys.stderr)
if missing:
    print("Missing keys:", ", ".join(missing), file=sys.stderr)
raise SystemExit(1 if duplicates or missing else 0)
