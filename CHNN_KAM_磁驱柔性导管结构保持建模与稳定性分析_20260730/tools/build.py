#!/usr/bin/env python3
"""Portable bilingual build wrapper for the CHNN-KAM LaTeX project."""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
RELEASE = ROOT / "release"
PROVENANCE = ROOT / "FIGURE_TABLE_PROVENANCE.csv"

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
    stem = Path(entry).stem
    log_path = outdir / f"{stem}.log"

    def run_tex_pass() -> None:
        print("+", " ".join(tex_args))
        result = subprocess.run(tex_args, cwd=ROOT, check=False)
        if result.returncode == 0:
            return
        log = log_path.read_text(encoding="utf-8", errors="replace") if log_path.exists() else ""
        hard_errors = (
            "Missing $ inserted",
            "Emergency stop",
            "Fatal error occurred",
            "! LaTeX Error",
        )
        if any(pattern in log for pattern in hard_errors) or not (outdir / f"{stem}.pdf").exists():
            raise subprocess.CalledProcessError(result.returncode, tex_args)
        print(
            "WARNING: XeLaTeX returned nonzero after producing a PDF without a "
            "logged TeX fatal error; continuing to accommodate the local MiKTeX host warning."
        )

    run_tex_pass()
    aux_stem = (outdir / stem).relative_to(ROOT)
    run([bibtex, str(aux_stem)])
    for pass_index in range(4):
        run_tex_pass()
        if pass_index < 1:
            continue
        log = log_path.read_text(encoding="utf-8", errors="replace")
        if not any(pattern in log for pattern in RERUN_PATTERNS):
            break
    else:
        raise RuntimeError(
            f"Cross-references did not stabilize after four post-BibTeX passes: {entry}"
        )


def check_assets_and_provenance(*, allow_mismatch: bool) -> None:
    """Fail closed on missing manuscript assets and frozen provenance drift."""
    missing: list[str] = []
    for tex_path in (ROOT / "manuscript").rglob("*.tex"):
        text = tex_path.read_text(encoding="utf-8", errors="replace")
        for match in re.finditer(r"\\(?:includegraphics|input)\{([^}]+)\}", text):
            asset = match.group(1)
            if asset.startswith("figures/") or asset.startswith("tables/"):
                candidates = [ROOT / asset]
                if not Path(asset).suffix:
                    candidates.extend(ROOT / f"{asset}{suffix}" for suffix in (".tex", ".pdf", ".png"))
                if not any(path.exists() for path in candidates):
                    missing.append(f"{tex_path.relative_to(ROOT)} -> {asset}")

    mismatches: list[str] = []
    if PROVENANCE.exists():
        with PROVENANCE.open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                asset_path = row.get("asset_path", "")
                expected = row.get("asset_sha256", "").strip().upper()
                path = ROOT / asset_path
                if not path.exists():
                    missing.append(f"provenance -> {asset_path}")
                    continue
                digest = hashlib.sha256(path.read_bytes()).hexdigest().upper()
                if expected and digest != expected:
                    mismatches.append(f"{asset_path}: expected {expected}, got {digest}")
    else:
        mismatches.append("FIGURE_TABLE_PROVENANCE.csv is missing")

    if missing:
        raise RuntimeError("Missing manuscript assets:\n" + "\n".join(sorted(set(missing))))
    if mismatches and not allow_mismatch:
        raise RuntimeError(
            "Provenance mismatch (use --allow-provenance-mismatch only for diagnostic builds):\n"
            + "\n".join(mismatches)
        )
    if mismatches:
        print("WARNING: provenance mismatches allowed for this diagnostic build:")
        print("\n".join(mismatches))


def build_language(language: str, *, clean: bool, check: bool, allow_provenance_mismatch: bool) -> Path:
    profile = PROFILES[language]
    outdir = BUILD / language
    if clean and outdir.exists():
        shutil.rmtree(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    RELEASE.mkdir(parents=True, exist_ok=True)

    check_assets_and_provenance(allow_mismatch=allow_provenance_mismatch)

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
    parser.add_argument(
        "--allow-provenance-mismatch",
        action="store_true",
        help="allow known frozen-table hash drift for diagnostic PDF generation",
    )
    args = parser.parse_args()

    languages = ("zh", "en") if args.language == "both" else (args.language,)
    try:
        for language in languages:
            build_language(
                language,
                clean=args.clean,
                check=not args.no_check,
                allow_provenance_mismatch=args.allow_provenance_mismatch,
            )
    except (subprocess.CalledProcessError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 4
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
