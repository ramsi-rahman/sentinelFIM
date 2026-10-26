import tempfile
import unittest
from pathlib import Path

from sentinel.baseline import compare_baseline, load_baseline, save_baseline


class BaselineTests(unittest.TestCase):
    def test_saves_and_loads_baseline(self):
        baseline = {"nested/file.txt": "abc123", "other.txt": "def456"}
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "data" / "baseline.json"

            save_baseline(baseline, path)

            self.assertEqual(load_baseline(path), baseline)

    def test_rejects_invalid_baseline_data(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "baseline.json"
            path.write_text('{"file.txt": 42}', encoding="utf-8")

            with self.assertRaises(ValueError):
                load_baseline(path)

    def test_compares_added_modified_and_deleted_files(self):
        previous = {"same.txt": "a", "changed.txt": "old", "removed.txt": "b"}
        current = {"same.txt": "a", "changed.txt": "new", "added.txt": "c"}

        self.assertEqual(
            compare_baseline(previous, current),
            {
                "added": ["added.txt"],
                "modified": ["changed.txt"],
                "deleted": ["removed.txt"],
            },
        )


if __name__ == "__main__":
    unittest.main()
