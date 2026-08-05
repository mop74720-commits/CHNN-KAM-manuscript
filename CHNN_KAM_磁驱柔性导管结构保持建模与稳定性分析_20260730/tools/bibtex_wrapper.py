#!/usr/bin/env python3
"""Run the first working BibTeX executable available on the host."""
from __future__ import annotations

import shutil
import subprocess
import sys


def main() -> int:
    candidates = ("bibtex", "bibtex.original", "bibtex8", "bibtexu")
    for name in candidates:
        executable = shutil.which(name)
        if executable:
            return subprocess.run([executable, *sys.argv[1:]], check=False).returncode
    print(
        "No BibTeX executable found. Install BibTeX (MiKTeX/TeX Live) or add it to PATH.",
        file=sys.stderr,
    )
    return 127


if __name__ == "__main__":
    raise SystemExit(main())
