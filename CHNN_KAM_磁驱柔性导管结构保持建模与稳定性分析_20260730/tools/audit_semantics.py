#!/usr/bin/env python3
"""Audit one language tree's semantic LaTeX structure."""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", choices=("zh", "en"), default="zh")
    args = parser.parse_args()

    active_roots = [ROOT / "manuscript" / args.language, ROOT / "frontmatter" / args.language]
    missing_roots = [str(p.relative_to(ROOT)) for p in active_roots if not p.exists()]
    if missing_roots:
        print("Missing active roots: " + ", ".join(missing_roots), file=sys.stderr)
        return 2

    texts: list[tuple[Path, str]] = []
    for base in active_roots:
        for path in sorted(base.rglob("*.tex")):
            texts.append((path, path.read_text(encoding="utf-8", errors="replace")))

    combined = "\n".join(text for _, text in texts)
    labels = re.findall(r"\\label\{([^}]+)\}", combined)
    label_counts = Counter(labels)
    duplicate_labels = sorted(label for label, count in label_counts.items() if count > 1)

    section_count = 0
    section_label_count = 0
    unlabelled_sections: list[str] = []
    for path, text in texts:
        for match in re.finditer(r"\\(?:section\*?|subsection\*?|subsubsection\*?)\{[^}]*\}", text):
            section_count += 1
            following = text[match.end():match.end() + 240]
            if re.search(r"\\label\{sec:[^}]+\}", following):
                section_label_count += 1
            else:
                line_no = text.count("\n", 0, match.start()) + 1
                unlabelled_sections.append(f"{path.relative_to(ROOT)}:{line_no}")

    equation_count = 0
    equation_label_count = 0
    unlabelled_equations: list[str] = []
    for path, text in texts:
        for match in re.finditer(r"\\begin\{equation\}(.*?)\\end\{equation\}", text, re.S):
            equation_count += 1
            if re.search(r"\\label\{eq:[^}]+\}", match.group(1)):
                equation_label_count += 1
            else:
                line_no = text.count("\n", 0, match.start()) + 1
                unlabelled_equations.append(f"{path.relative_to(ROOT)}:{line_no}")

    float_issues: list[str] = []
    for path, text in texts:
        for env, prefix in (("figure", "fig:"), ("table", "tab:")):
            for match in re.finditer(rf"\\begin\{{{env}\}}(.*?)\\end\{{{env}\}}", text, re.S):
                block = match.group(1)
                if not re.search(rf"\\label\{{{re.escape(prefix)}[^}}]+\}}", block):
                    line_no = text.count("\n", 0, match.start()) + 1
                    float_issues.append(f"{path.relative_to(ROOT)}:{line_no} ({env} missing {prefix} label)")

    raw_numeric_cites: list[str] = []
    hardcoded_refs: list[str] = []
    if args.language == "zh":
        for path, text in texts:
            for line_no, line in enumerate(text.splitlines(), 1):
                if re.search(r"［\s*\d", line):
                    raw_numeric_cites.append(f"{path.relative_to(ROOT)}:{line_no}")
                line_without_cite_note = re.sub(r"\\cite\[[^]]*\]\{[^}]+\}", "", line)
                if re.search(r"第\s*\d+(?:\.\d+){0,2}\s*[章节]", line_without_cite_note):
                    hardcoded_refs.append(f"{path.relative_to(ROOT)}:{line_no}")
                if re.search(r"(?:式|公式)\s*[（(]?\d+\.\d+[）)]?", line_without_cite_note):
                    hardcoded_refs.append(f"{path.relative_to(ROOT)}:{line_no}")
                if re.search(r"§\s*\d", line_without_cite_note):
                    hardcoded_refs.append(f"{path.relative_to(ROOT)}:{line_no}")

    cite_groups = re.findall(r"\\cite\w*\s*(?:\[[^]]*\]\s*)*\{([^}]+)\}", combined)
    cited_keys = {key.strip() for group in cite_groups for key in group.split(",") if key.strip()}
    cref_count = len(re.findall(r"\\[Cc]ref\{[^}]+\}", combined))
    result_placeholders = len(re.findall(r"\\begin\{resultplaceholder\}", combined))

    print(f"Language: {args.language}")
    print(f"Sections / sec labels: {section_count} / {section_label_count}")
    print(f"Equations / eq labels: {equation_count} / {equation_label_count}")
    print(f"Unique labels: {len(label_counts)}")
    print(f"Cref calls: {cref_count}")
    print(f"Citation calls / unique keys: {len(cite_groups)} / {len(cited_keys)}")
    print(f"Structured result placeholders: {result_placeholders}")

    issues: list[str] = []
    if duplicate_labels:
        issues.append("Duplicate labels: " + ", ".join(duplicate_labels))
    if unlabelled_sections:
        issues.append("Sections without sec labels: " + ", ".join(unlabelled_sections))
    if unlabelled_equations:
        issues.append("Equations without eq labels: " + ", ".join(unlabelled_equations))
    if float_issues:
        issues.append("Float label issues: " + ", ".join(float_issues))
    if raw_numeric_cites:
        issues.append("Raw numeric citations: " + ", ".join(raw_numeric_cites))
    if hardcoded_refs:
        issues.append("Hard-coded manuscript references: " + ", ".join(sorted(set(hardcoded_refs))))

    if issues:
        for issue in issues:
            print(issue, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
