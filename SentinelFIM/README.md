# SentinelFIM

SentinelFIM checks whether files in a directory have changed. It calculates a
SHA-256 hash for each file and stores those hashes in a JSON baseline.

## What happens when you run it?

1. On the first run, SentinelFIM scans the directory and creates a baseline
   JSON file.
2. On later runs, it scans the directory again and compares the results with
   that baseline.
3. It reports files that were added, modified, or deleted.

The program does **not** run continuously or update the baseline after finding
changes. You run it whenever you want to check the directory.

## Requirements

- Python 3.9 or newer
- No additional packages are required

## Choose the directory and baseline file

Open [`examples/basic_usage.py`](examples/basic_usage.py) and edit `ROOT` and
`BASELINE_PATH` near the top of the file:

```python
ROOT = Path("/path/to/the/folder-you-want-to-monitor")
BASELINE_PATH = Path("/path/to/save/sentinelfim-baseline.json")
```

`ROOT` must point to an existing directory. `BASELINE_PATH` must be a file
path, not just a directory. Keep the baseline outside the monitored directory.

If you run the program in **WSL**, use Linux paths. For example:

```python
ROOT = Path("/path/to/be/monitored")
BASELINE_PATH = Path("path/to/baseline.json")
```

If you run it directly in **Windows PowerShell**, use Windows paths instead:

```python
ROOT = Path(r"path\to\monitor")
BASELINE_PATH = Path(r"path\to\baseline.json")
```

Use paths that exist on your computer; the examples above are only examples.

## Run the program

Open a terminal and go to the project folder, the one containing `sentinel`
and `examples`.

In WSL:

```bash
cd /path/to/SentinelFIM
python3 -m examples.basic_usage
```

In Windows PowerShell:

```powershell
Set-Location "C:\path\to\SentinelFIM"
python -m examples.basic_usage
```

Replace the example project-folder path with the location where you saved
SentinelFIM.

The first run creates the baseline at `BASELINE_PATH`. Now add, change, or
delete a file inside the monitored directory and run the same command again.
SentinelFIM prints a report of the changes.

### Start a new baseline

To accept the current directory contents as a new starting point, delete or
rename the baseline JSON file, then run the program again. It will create a
new baseline. Review any reported changes before doing this, because the new
baseline replaces the old reference point.

## Project layout

```text
sentinel/
    __init__.py
    scanner.py
    hasher.py
    baseline.py
    reporter.py
tests/
examples/
docs/
```

## Run the tests

From the project folder:

```bash
python3 -m unittest discover -s tests -v
```

On Windows, `python -m unittest discover -s tests -v` can be used instead.

## License

Released under the MIT License; see [LICENSE](LICENSE).
