from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BUILD_MODULE_PATH = PROJECT_ROOT / "tools" / "build.py"
FORMAL_MANIFEST = PROJECT_ROOT / "FIGURE_TABLE_PROVENANCE.csv"


def load_build_module():
    spec = importlib.util.spec_from_file_location("chnn_kam_build", BUILD_MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {BUILD_MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUILD = load_build_module()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


class FormalProvenanceStructureTests(unittest.TestCase):
    def run_build_with_manifest(
        self,
        source_paths: list[str],
        source_hashes: list[str],
        *,
        diagnostic: bool = False,
        allow_mismatch: bool = False,
    ) -> tuple[int, str, dict[str, str]]:
        release_hashes = {
            path.name: sha256(path)
            for path in BUILD.RELEASE.glob("CHNN_KAM_Manuscript_*.pdf")
        }
        formal_manifest_hash = sha256(FORMAL_MANIFEST)
        asset = "tables/README.md"
        row = {
            "asset_path": asset,
            "asset_sha256": "0" * 64,
            "formal_source_paths": ";".join(source_paths),
            "formal_source_sha256": ";".join(source_hashes),
        }
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary = Path(temporary_directory)
            manifest = temporary / "provenance.csv"
            with manifest.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(row))
                writer.writeheader()
                writer.writerow(row)

            original = {
                "PROVENANCE": BUILD.PROVENANCE,
                "BUILD": BUILD.BUILD,
                "DIAGNOSTIC_BUILD": BUILD.DIAGNOSTIC_BUILD,
            }
            BUILD.PROVENANCE = manifest
            BUILD.BUILD = temporary / "build"
            BUILD.DIAGNOSTIC_BUILD = temporary / "diagnostic"
            old_argv = sys.argv
            sys.argv = [
                "build.py",
                "--language",
                "zh",
                "--clean",
            ]
            if diagnostic:
                sys.argv.append("--diagnostic")
            if allow_mismatch:
                sys.argv.append("--allow-provenance-mismatch")
            stdout = io.StringIO()
            stderr = io.StringIO()
            try:
                with redirect_stdout(stdout), redirect_stderr(stderr):
                    exit_code = BUILD.main()
            finally:
                sys.argv = old_argv
                for name, value in original.items():
                    setattr(BUILD, name, value)

        self.assertEqual(formal_manifest_hash, sha256(FORMAL_MANIFEST))
        after_release_hashes = {
            path.name: sha256(path)
            for path in BUILD.RELEASE.glob("CHNN_KAM_Manuscript_*.pdf")
        }
        self.assertEqual(release_hashes, after_release_hashes)
        return exit_code, stdout.getvalue() + stderr.getvalue(), release_hashes

    def test_t1_equal_lists_reach_existing_provenance_gate(self) -> None:
        source = "review/first-review.md"
        code, output, _ = self.run_build_with_manifest(
            [source], [sha256(PROJECT_ROOT / source)]
        )
        self.assertEqual(code, 4)
        self.assertIn("Provenance mismatch", output)
        self.assertNotIn("one-to-one correspondence", output)

    def test_t2_extra_path_is_rejected(self) -> None:
        source = "review/first-review.md"
        code, output, _ = self.run_build_with_manifest(
            [source, source], [sha256(PROJECT_ROOT / source)]
        )
        self.assertEqual(code, 4)
        self.assertIn("formal_source_paths count=2", output)
        self.assertIn("formal_source_sha256 count=1", output)
        self.assertIn("provenance.csv", output)
        self.assertIn("one-to-one correspondence", output)

    def test_t3_extra_hash_is_rejected(self) -> None:
        source = "review/first-review.md"
        code, output, _ = self.run_build_with_manifest(
            [source], [sha256(PROJECT_ROOT / source), sha256(PROJECT_ROOT / source)]
        )
        self.assertEqual(code, 4)
        self.assertIn("formal_source_paths count=1", output)
        self.assertIn("formal_source_sha256 count=2", output)
        self.assertIn("one-to-one correspondence", output)

    def test_t4_empty_path_list_with_hash_is_rejected(self) -> None:
        source = "review/first-review.md"
        code, output, _ = self.run_build_with_manifest(
            [], [sha256(PROJECT_ROOT / source)]
        )
        self.assertEqual(code, 4)
        self.assertIn("formal_source_paths count=0", output)
        self.assertIn("formal_source_sha256 count=1", output)
        self.assertIn("one-to-one correspondence", output)

    def test_t5_diagnostic_mode_cannot_bypass_structure_gate(self) -> None:
        source = "review/first-review.md"
        code, output, _ = self.run_build_with_manifest(
            [source, source],
            [],
            diagnostic=True,
            allow_mismatch=True,
        )
        self.assertEqual(code, 4)
        self.assertIn("formal_source_paths count=2", output)
        self.assertIn("formal_source_sha256 count=0", output)
        self.assertIn("one-to-one correspondence", output)

    def test_t6_consecutive_empty_path_entry_is_rejected(self) -> None:
        source = "review/first-review.md"
        digest = sha256(PROJECT_ROOT / source)
        code, output, _ = self.run_build_with_manifest(
            [source, "", source], [digest, digest]
        )
        self.assertEqual(code, 4)
        self.assertIn("formal_source_paths", output)
        self.assertIn("empty provenance entry", output)
        self.assertIn("index 1", output)

    def test_t7_consecutive_empty_hash_entry_is_rejected(self) -> None:
        source = "review/first-review.md"
        digest = sha256(PROJECT_ROOT / source)
        code, output, _ = self.run_build_with_manifest(
            [source, source], [digest, "", digest]
        )
        self.assertEqual(code, 4)
        self.assertIn("formal_source_sha256", output)
        self.assertIn("empty provenance entry", output)
        self.assertIn("index 1", output)

    def test_t8_leading_empty_path_entry_is_rejected(self) -> None:
        source = "review/first-review.md"
        code, output, _ = self.run_build_with_manifest(
            ["", source], [sha256(PROJECT_ROOT / source)]
        )
        self.assertEqual(code, 4)
        self.assertIn("formal_source_paths", output)
        self.assertIn("empty provenance entry", output)
        self.assertIn("index 0", output)

    def test_t9_trailing_empty_hash_entry_is_rejected(self) -> None:
        source = "review/first-review.md"
        digest = sha256(PROJECT_ROOT / source)
        code, output, _ = self.run_build_with_manifest(
            [source, source], [digest, ""]
        )
        self.assertEqual(code, 4)
        self.assertIn("formal_source_sha256", output)
        self.assertIn("empty provenance entry", output)
        self.assertIn("index 1", output)

    def test_t10_whitespace_only_entry_is_rejected(self) -> None:
        source = "review/first-review.md"
        digest = sha256(PROJECT_ROOT / source)
        code, output, _ = self.run_build_with_manifest(
            [source, "   ", source], [digest, digest]
        )
        self.assertEqual(code, 4)
        self.assertIn("formal_source_paths", output)
        self.assertIn("empty provenance entry", output)
        self.assertIn("index 1", output)

    def test_t11_formal_and_diagnostic_modes_reject_empty_entries(self) -> None:
        source = "review/first-review.md"
        digest = sha256(PROJECT_ROOT / source)
        for diagnostic, allow_mismatch in ((False, False), (True, True)):
            code, output, _ = self.run_build_with_manifest(
                [source, "", source],
                [digest, digest],
                diagnostic=diagnostic,
                allow_mismatch=allow_mismatch,
            )
            self.assertEqual(code, 4)
            self.assertIn("formal_source_paths", output)
            self.assertIn("empty provenance entry", output)
            self.assertIn("index 1", output)

    def test_t12_both_lists_empty_are_allowed_by_current_contract(self) -> None:
        code, output, _ = self.run_build_with_manifest([], [])
        self.assertEqual(code, 4)
        self.assertIn("Provenance mismatch", output)
        self.assertNotIn("empty provenance entry", output)
        self.assertNotIn("one-to-one correspondence", output)


if __name__ == "__main__":
    unittest.main()
