import tempfile
import unittest
from pathlib import Path

from sentinel.hasher import sha256_file
from sentinel.scanner import scan_directory


class ScanDirectoryTests(unittest.TestCase):
    def test_scans_files_recursively_with_relative_paths(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "top.txt").write_text("top", encoding="utf-8")
            nested_directory = root / "nested"
            nested_directory.mkdir()
            nested_file = nested_directory / "item.txt"
            nested_file.write_text("nested", encoding="utf-8")

            self.assertEqual(
                scan_directory(root),
                {
                    "nested/item.txt": sha256_file(nested_file),
                    "top.txt": sha256_file(root / "top.txt"),
                },
            )

    def test_rejects_missing_scan_root(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            missing = Path(temporary_directory) / "missing"
            with self.assertRaises(FileNotFoundError):
                scan_directory(missing)


if __name__ == "__main__":
    unittest.main()
