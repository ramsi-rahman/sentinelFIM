"""Baseline persistence and comparison."""

import json
from pathlib import Path
from typing import Dict, List, Mapping, Union

Baseline = Dict[str, str]
Changes = Dict[str, List[str]]


def save_baseline(baseline: Mapping[str, str], destination: Union[str, Path]) -> None:
    """Write a file-hash mapping as a readable JSON baseline."""
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(dict(sorted(baseline.items())), file, indent=2, sort_keys=True)
        file.write("\n")


def load_baseline(source: Union[str, Path]) -> Baseline:
    """Load a JSON baseline and reject invalid data with a clear error."""
    with Path(source).open("r", encoding="utf-8") as file:
        baseline = json.load(file)

    if not isinstance(baseline, dict) or any(
        not isinstance(path, str) or not isinstance(digest, str)
        for path, digest in baseline.items()
    ):
        raise ValueError("Baseline must be a JSON object of string paths and hashes")
    return baseline


def compare_baseline(previous: Mapping[str, str], current: Mapping[str, str]) -> Changes:
    """Return sorted lists of added, modified, and deleted relative paths."""
    previous_paths = set(previous)
    current_paths = set(current)
    return {
        "added": sorted(current_paths - previous_paths),
        "modified": sorted(
            path
            for path in previous_paths & current_paths
            if previous[path] != current[path]
        ),
        "deleted": sorted(previous_paths - current_paths),
    }
