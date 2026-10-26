"""File hashing helpers."""

import hashlib
from pathlib import Path
from typing import Union


def sha256_file(path: Union[str, Path], chunk_size: int = 64 * 1024) -> str:
    """Return the SHA-256 hex digest for a file, reading it in chunks."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")

    digest = hashlib.sha256()
    with Path(path).open("rb") as file:
        for chunk in iter(lambda: file.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()
