#!/usr/bin/env python3
"""Portable bilingual build wrapper for the CHNN-KAM LaTeX project."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
RELEASE = ROOT / "release"

PROFILES = {
    "zh": {
        "entry": "main-zh.tex",
        "release": "CHNN_KAM_Manuscript_ZH.pdf",
    },
    "en": {
        "entry": "main-en.tex",
        "release": "CHNN_KAM_Manuscript_EN.pdf",
    },
}

FATAL_PATTERNS = (
    "There were undefined references",
    "multiply defined",
    "Citation `",
    "Reference `",
    "Missing character:",
    "Overfull \\hbox",
    "Rerun to get cross-references right",
    "Label(s) may have changed",
)

RERUN_PATTERNS = (
    "Rerun to get cross-references right",
    "Label(s) may have changed",
)


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def run_tex_toolchain(entry: str, outdir: Path) -> None:
    """Build with latexmk when usable, otherwise run XeLaTeX/BibTeX directly."""
    latexmk = shutil.which("latexmk")
    perl = shutil.which("perl")
    if latexmk is not None and perl is not None:
        run([
            latexmk, "-xelatex", "-interaction=nonstopmode", "-halt-on-error",
            "-file-line-error", f"-outdir={outdir}", entry,
        ])
        return

    xelatex = shutil.which("xelatex")
    bibtex = shutil.which("bibtex")
    if xelatex is None or bibtex is None:
        missing = [
            name for name, path in (("xelatex", xelatex), ("bibtex", bibtex))
            if path is None
        ]
        raise RuntimeError(
            "latexmk is unavailable without Perl, and the direct fallback is "
            f"missing: {', '.join(missing)}"
        )

    print(
        "latexmk/Perl unavailable; using XeLaTeX -> BibTeX -> "
        "XeLaTeX until cross-references stabilize."
    )
    tex_args = [
        xelatex, "-interaction=nonstopmode", "-halt-on-error",
        "-file-line-error", f"-output-directory={outdir}", entry,
    ]
    run(tex_args)
    stem = Path(entry).stem
    aux_stem = (outdir / stem).relative_to(ROOT)
    run([bibtex, str(aux_stem)])
    log_path = outdir / f"{stem}.log"
    for pass_index in range(4):
        run(tex_args)
        if pass_index < 1:
            continue
        log = log_path.read_text(encoding="utf-8", errors="replace")
        if not any(pattern in log for pattern in RERUN_PATTERNS):
            break
    else:
        raise RuntimeError(
            f"Cross-references did not stabilize after four post-BibTeX passes: {entry}"
        )


def build_language(language: str, *, clean: bool, check: bool) -> Path:
    profile = PROFILES[language]
    outdir = BUILD / language
    if clean and outdir.exists():
        shutil.rmtree(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    RELEASE.mkdir(parents=True, exist_ok=True)

    run([sys.executable, "tools/audit_semantics.py", "--language", language])
    run([sys.executable, "tools/check_bibliography.py"])
    if language == "en":
        run([sys.executable, "tools/audit_bilingual.py"])

    run_tex_toolchain(profile["entry"], outdir)

    stem = Path(profile["entry"]).stem
    pdf = outdir / f"{stem}.pdf"
    if not pdf.exists():
        raise RuntimeError(f"Expected output missing: {pdf}")

    release_pdf = RELEASE / profile["release"]
    shutil.copy2(pdf, release_pdf)

    if check:
        log_path = outdir / f"{stem}.log"
        log = log_path.read_text(encoding="utf-8", errors="replace")
        found = [p for p in FATAL_PATTERNS if p in log]
        blg_path = outdir / f"{stem}.blg"
        blg = blg_path.read_text(encoding="utf-8", errors="replace") if blg_path.exists() else ""
        bib_warnings = [line for line in blg.splitlines() if line.startswith("Warning--")]
        if found or bib_warnings:
            if found:
                print(f"[{language}] Post-build LaTeX check failed: " + ", ".join(found), file=sys.stderr)
            if bib_warnings:
                print(f"[{language}] Post-build BibTeX check failed: " + "; ".join(bib_warnings), file=sys.stderr)
            raise RuntimeError(f"Post-build checks failed for {language}")

    print(f"Built [{language}]: {release_pdf.relative_to(ROOT)}")
    return release_pdf


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", choices=("zh", "en", "both"), default="zh")
    parser.add_argument("--clean", action="store_true", help="remove generated files before building")
    parser.add_argument("--no-check", action="store_true", help="skip post-build log checks")
    args = parser.parse_args()

    languages = ("zh", "en") if args.language == "both" else (args.language,)
    try:
        for language in languages:
            build_language(language, clean=args.clean, check=not args.no_check)
    except (subprocess.CalledProcessError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 4
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
