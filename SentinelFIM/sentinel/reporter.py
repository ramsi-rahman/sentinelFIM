"""Human-readable change reports."""

from typing import Mapping, Sequence


def format_report(changes: Mapping[str, Sequence[str]]) -> str:
    """Format comparison results as a concise text report."""
    categories = ("added", "modified", "deleted")
    if not any(changes.get(category, ()) for category in categories):
        return "No changes detected.\n"

    lines = ["File integrity changes detected:"]
    for category in categories:
        paths = sorted(changes.get(category, ()))
        if paths:
            lines.append("{}:".format(category.capitalize()))
            lines.extend("  {}".format(path) for path in paths)
    return "\n".join(lines) + "\n"
