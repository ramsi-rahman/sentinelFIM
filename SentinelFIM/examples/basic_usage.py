"""Create or compare a baseline for a directory named 'monitored'."""

from pathlib import Path

from sentinel.baseline import compare_baseline, load_baseline, save_baseline
from sentinel.reporter import format_report
from sentinel.scanner import scan_directory


ROOT = Path("monitored")
BASELINE_PATH = Path("baseline.json")


def main():
    current = scan_directory(ROOT)
    if not BASELINE_PATH.exists():
        save_baseline(current, BASELINE_PATH)
        print("Created baseline at {}".format(BASELINE_PATH))
        return

    previous = load_baseline(BASELINE_PATH)
    print(format_report(compare_baseline(previous, current)), end="")


if __name__ == "__main__":
    main()
