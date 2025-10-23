"""Command line tool for analysing log files by severity level."""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
from typing import List, Sequence

LogEntry = dict[str, str]
LEVEL_ORDER: Sequence[str] = ("INFO", "DEBUG", "ERROR", "WARNING")

def parse_log_line(line: str) -> LogEntry:
    """Parse a single log line into its components.

    The expected format is ``"YYYY-MM-DD HH:MM:SS LEVEL message"``.
    If the line does not match this layout a :class:`ValueError` is raised.
    """

    parts = line.strip().split(maxsplit=3)

    if len(parts) < 4:
        raise ValueError("Log line has an unexpected format")

    date_value, time_value, level, message = parts
    
    return {
        "date": date_value,
        "time": time_value,
        "level": level.upper(),
        "message": message.strip(),
    }


def load_logs(file_path: str | Path) -> List[LogEntry]:
    """Load and parse all log entries from *file_path*.

    Malformed lines are skipped with a warning printed to ``stderr``.
    """

    path = Path(file_path)

    logs: List[LogEntry] = []

    with path.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):

            stripped = raw_line.strip()

            if not stripped:
                continue

            try:
                logs.append(parse_log_line(stripped))
            except ValueError as ex:
                print(f"Skipping malformed line {line_number}: {ex}")

    return logs


def filter_logs_by_level(logs: Sequence[LogEntry], level: str) -> List[LogEntry]:
    """Return all log entries that match *level* (case-insensitive)."""

    normalized = level.upper()

    return list(filter(lambda entry: entry["level"] == normalized, logs))


def count_logs_by_level(logs: Sequence[LogEntry]) -> dict[str, int]:
    """Count log entries per severity level."""

    counter = Counter(entry["level"] for entry in logs)

    return {level: counter.get(level, 0) for level in LEVEL_ORDER}


def display_log_counts(counts: dict[str, int]) -> None:
    """Pretty-print the amount of log entries for each level."""

    header_level = "Log level"
    header_count = "Count"
    level_width = max(len(header_level), max(len(level) for level in LEVEL_ORDER))
    count_width = max(len(header_count), max(len(str(value)) for value in counts.values()))

    print(f"{header_level.ljust(level_width)} | {header_count}")
    print(f"{'-' * level_width}-|{'-' * count_width}")
    for level in LEVEL_ORDER:
        print(f"{level.ljust(level_width)} | {str(counts.get(level, 0)).ljust(count_width)}")


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for the command line interface."""

    argumentParser = argparse.ArgumentParser(
        description="Summarise log levels and optionally display detailed entries.",
    )
    argumentParser.add_argument(
        "logfile",
        type=Path,
        help="Path to the log file that should be analysed.",
    )
    argumentParser.add_argument(
        "level",
        nargs="?",
        help="Optional log level to display detailed entries for (e.g. error).",
    )

    args = argumentParser.parse_args(argv)

    try:
        logs = load_logs(args.logfile)
    except FileNotFoundError:
        print(f"Log file '{args.logfile}' does not exist.")
        return 1

    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if args.level:
        level = args.level.upper()
        matching_logs = filter_logs_by_level(logs, level)
        print(f"\n'{level}' log details:")
        if matching_logs:
            for entry in matching_logs:
                print(f"{entry['date']} {entry['time']} - {entry['message']}")
        else:
            print("No entries with such log level.")

    return 0

if __name__ == "__main__":
    main()