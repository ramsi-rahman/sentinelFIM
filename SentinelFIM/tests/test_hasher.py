import hashlib
import tempfile
import unittest
from pathlib import Path

from sentinel.hasher import sha256_file


class Sha256FileTests(unittest.TestCase):
    def test_hashes_file_contents(self):
        content = b"SentinelFIM test data"
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "sample.txt"
            path.write_bytes(content)

            self.assertEqual(sha256_file(path), hashlib.sha256(content).hexdigest())

    def test_rejects_nonpositive_chunk_size(self):
        with self.assertRaises(ValueError):
            sha256_file("unused", chunk_size=0)


if __name__ == "__main__":
    unittest.main()
