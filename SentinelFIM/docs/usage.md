# Usage

SentinelFIM is a small library for creating and comparing SHA-256 file
integrity baselines.

```python
from sentinel.baseline import compare_baseline, load_baseline, save_baseline
from sentinel.reporter import format_report
from sentinel.scanner import scan_directory

root = "path/to/monitored-directory"
baseline_path = "baseline.json"

current = scan_directory(root)
previous = load_baseline(baseline_path)
print(format_report(compare_baseline(previous, current)), end="")

# After reviewing changes, save the accepted state:
save_baseline(current, baseline_path)
```

The scanner includes regular files recursively, skips symlinks, and uses
relative POSIX-style paths as baseline keys. The baseline is JSON containing
those paths and their SHA-256 hex digests. Missing baseline files and I/O
errors are raised to the caller rather than hidden.

For a first run, call `save_baseline(scan_directory(root), baseline_path)` to
create the initial baseline. See [`../examples/basic_usage.py`](../examples/basic_usage.py)
for a runnable example.
