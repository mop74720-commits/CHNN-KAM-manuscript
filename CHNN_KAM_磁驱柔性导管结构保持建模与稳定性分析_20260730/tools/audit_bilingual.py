#!/usr/bin/env python3
"""Verify that Chinese and English manuscript trees retain the same semantic skeleton."""
from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "manuscript" / "zh"
EN = ROOT / "manuscript" / "en"
THEOREM_ENVS = (
    "theorem", "lemma", "proposition", "corollary", "definition",
    "assumption", "problem", "conjecture", "remark", "example", "proof",
    "resultplaceholder",
)


def strip_comments(text: str) -> str:
    out: list[str] = []
    for line in text.splitlines():
        escaped = False
        cut = len(line)
        for i, char in enumerate(line):
            if char == "%" and not escaped:
                cut = i
                break
            escaped = (char == "\\" and not escaped)
            if char != "\\":
                escaped = False
        out.append(line[:cut])
    return "\n".join(out)


def normalize_math(text: str) -> str:
    text = re.sub(r"\\label\{[^}]+\}", "", text)
    # Formula annotations may be translated, but mathematical structure must remain stable.
    previous = None
    while previous != text:
        previous = text
        text = re.sub(r"\\text\{[^{}]*\}", r"\\text{<LANG-TEXT>}", text)
    return re.sub(r"\s+", "", text)


def extract_blocks(text: str, begin: str, end: str) -> list[str]:
    return [normalize_math(x) for x in re.findall(re.escape(begin) + r"(.*?)" + re.escape(end), text, re.S)]


def extract_keys(text: str, command_pattern: str) -> Counter[str]:
    groups = re.findall(command_pattern, text)
    return Counter(key.strip() for group in groups for key in group.split(",") if key.strip())


def digest(items: list[str]) -> str:
    payload = "\0".join(items).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:16]


def compare_file(rel: Path) -> list[str]:
    zpath, epath = ZH / rel, EN / rel
    ztext = strip_comments(zpath.read_text(encoding="utf-8", errors="replace"))
    etext = strip_comments(epath.read_text(encoding="utf-8", errors="replace"))
    issues: list[str] = []

    zlabels = re.findall(r"\\label\{([^}]+)\}", ztext)
    elabels = re.findall(r"\\label\{([^}]+)\}", etext)
    if zlabels != elabels:
        issues.append("label order/set differs")

    section_type_pattern = r"\\(section\*?|subsection\*?|subsubsection\*?)\{"
    zsection_types = re.findall(section_type_pattern, ztext)
    esection_types = re.findall(section_type_pattern, etext)
    if zsection_types != esection_types:
        issues.append("section command type/order differs")

    if re.search(r"[\u3400-\u9fff]", etext):
        issues.append("untranslated CJK text remains in the English manuscript")

    zeq = extract_blocks(ztext, r"\begin{equation}", r"\end{equation}")
    eeq = extract_blocks(etext, r"\begin{equation}", r"\end{equation}")
    if zeq != eeq:
        issues.append(f"display equations differ (zh={len(zeq)}, en={len(eeq)}, signatures={digest(zeq)}/{digest(eeq)})")

    zinline = extract_blocks(ztext, r"\(", r"\)")
    einline = extract_blocks(etext, r"\(", r"\)")
    if zinline != einline:
        issues.append(f"inline mathematics differ (zh={len(zinline)}, en={len(einline)}, signatures={digest(zinline)}/{digest(einline)})")

    env_pattern = r"\\begin\{(" + "|".join(THEOREM_ENVS) + r")\}"
    zenvs = re.findall(env_pattern, ztext)
    eenvs = re.findall(env_pattern, etext)
    if zenvs != eenvs:
        issues.append("theorem/proof/placeholder environment sequence differs")

    cite_pattern = r"\\cite\w*\s*(?:\[[^]]*\]\s*)*\{([^}]+)\}"
    if extract_keys(ztext, cite_pattern) != extract_keys(etext, cite_pattern):
        issues.append("BibTeX citation key multiset differs")

    ref_pattern = r"\\(?:[Cc]ref|eqref|ref)\{([^}]+)\}"
    if extract_keys(ztext, ref_pattern) != extract_keys(etext, ref_pattern):
        issues.append("cross-reference target multiset differs")

    return issues


def body_inputs(path: Path, language: str) -> list[str]:
    text = strip_comments(path.read_text(encoding="utf-8", errors="replace"))
    return re.findall(rf"\\input\{{manuscript/{language}/sections/([^}}]+)\}}", text)


def main() -> int:
    if not ZH.exists() or not EN.exists():
        print("Both manuscript/zh and manuscript/en must exist.", file=sys.stderr)
        return 2

    zfiles = {p.relative_to(ZH) for p in ZH.rglob("*.tex") if p.name != "README.md"}
    efiles = {p.relative_to(EN) for p in EN.rglob("*.tex") if p.name != "README.md"}
    issues: list[str] = []
    if zfiles != efiles:
        missing_en = sorted(str(p) for p in zfiles - efiles)
        extra_en = sorted(str(p) for p in efiles - zfiles)
        if missing_en:
            issues.append("English files missing: " + ", ".join(missing_en))
        if extra_en:
            issues.append("Unexpected English files: " + ", ".join(extra_en))

    zinputs = body_inputs(ZH / "body.tex", "zh")
    einputs = body_inputs(EN / "body.tex", "en")
    if zinputs != einputs:
        issues.append("body.tex section assembly order differs")

    checked = 0
    for rel in sorted(zfiles & efiles):
        if rel.name == "body.tex":
            continue
        file_issues = compare_file(rel)
        checked += 1
        for issue in file_issues:
            issues.append(f"{rel}: {issue}")

    print(f"Bilingual files checked: {checked}")
    print(f"Section assembly entries: {len(zinputs)}")
    if issues:
        for issue in issues:
            print(issue, file=sys.stderr)
        return 1
    print("Bilingual semantic skeleton: consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
