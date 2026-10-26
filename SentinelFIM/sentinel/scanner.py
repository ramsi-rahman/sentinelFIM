"""Directory scanning helpers."""

from pathlib import Path
from typing import Dict, Union

from sentinel.hasher import sha256_file


def scan_directory(root: Union[str, Path]) -> Dict[str, str]:
    """Hash regular files under *root*, keyed by relative POSIX path."""
    directory = Path(root)
    if not directory.exists():
        raise FileNotFoundError("Scan root does not exist: {}".format(directory))
    if not directory.is_dir():
        raise NotADirectoryError("Scan root is not a directory: {}".format(directory))

    hashes = {}
    for path in sorted(directory.rglob("*")):
        if path.is_file() and not path.is_symlink():
            relative_path = path.relative_to(directory).as_posix()
            hashes[relative_path] = sha256_file(path)
    return hashes
