#!/usr/bin/env python3
"""Check a content calendar against the capacity the creator actually has.

A calendar that ignores capacity is a guilt document. This verifies the plan is one a
single person can execute, and that the four content jobs are all represented.

Input CSV columns (see templates/calendar.csv):
  date, platform, pillar, format, job, angle, hook, film, cta, metric, difficulty, batch, receipt

  job        discovery | trust | community | conversion
  difficulty low | medium | high
  batch      any label grouping posts filmed/designed in one session (B1, B2, …)
  receipt    a Proof Locker id (P-04) or "opinion"
  brain      OPTIONAL. The lowest brain state that could still make this post:
             feral | froggy | foggy | fried. `fried` means already finished and banked:
             the slot is publish-only. When the column is present, every week must hold
             at least one foggy or fried post. Blank cells are skipped with a warning.

Usage:
  python3 calendar_check.py calendar.csv --capacity "video=4,carousel=2"
  python3 calendar_check.py calendar.csv --capacity "video=4,carousel=2" --max-high 1

Capacity is posts per ISO week, per format. Formats not named in --capacity are
reported but not limited.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

JOBS = ["discovery", "trust", "community", "conversion"]
BRAINS = ["feral", "froggy", "foggy", "fried"]
LOW_ENERGY = {"foggy", "fried"}
REQUIRED = ["date", "platform", "format", "job", "angle", "hook", "film", "cta", "metric", "difficulty", "batch", "receipt"]
# Columns that must have a value on every row (job, difficulty, receipt, date are checked separately).
NON_EMPTY = ["platform", "format", "angle", "hook", "film", "cta", "metric", "batch"]


def parse_capacity(raw: str) -> dict[str, int]:
    capacity: dict[str, int] = {}
    for part in raw.split(","):
        if not part.strip():
            continue
        name, _, count = part.partition("=")
        try:
            capacity[name.strip().lower()] = int(count)
        except ValueError:
            sys.exit(f"bad --capacity entry {part!r}; expected format=count")
    return capacity


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("path", type=Path)
    parser.add_argument("--capacity", required=True, help='posts per week per format, e.g. "video=4,carousel=2"')
    parser.add_argument("--max-high", type=int, default=1, help="high-difficulty posts allowed per week")
    args = parser.parse_args()
    capacity = parse_capacity(args.capacity)
    if not args.path.is_file():
        sys.exit(f"{args.path}: no such file")

    overflow_rows: list[int] = []
    with args.path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        headers = [h.strip().lower() for h in (reader.fieldnames or [])]
        missing_columns = [c for c in REQUIRED if c not in headers]
        if missing_columns:
            sys.exit("missing columns: " + ", ".join(missing_columns))
        rows = []
        for line_no, row in enumerate(reader, start=2):
            if None in row:  # more fields than the header: almost always an unquoted comma
                overflow_rows.append(line_no)
            rows.append({k.strip().lower(): (v or "").strip() for k, v in row.items() if isinstance(k, str)})

    errors: list[str] = [
        f"row {n}: more fields than the header — wrap any field containing a comma in double quotes"
        for n in overflow_rows
    ]
    warnings: list[str] = []
    per_week: dict[str, Counter] = defaultdict(Counter)
    high_per_week: Counter = Counter()
    jobs: Counter = Counter()
    hooks: dict[str, int] = {}
    has_brain = "brain" in headers
    brain_per_week: dict[str, Counter] = defaultdict(Counter)
    blank_brain = 0

    for line_no, row in enumerate(rows, start=2):
        week_key = None
        try:
            year, week, _ = date.fromisoformat(row["date"]).isocalendar()
            week_key = f"{year}-W{week:02d}"
        except ValueError:
            errors.append(f"row {line_no}: date {row['date']!r} is not YYYY-MM-DD")
        if week_key and row["format"]:
            per_week[week_key][row["format"].lower()] += 1

        for column in NON_EMPTY:
            if not row.get(column):
                errors.append(f"row {line_no}: empty {column}")
        job = row["job"].lower()
        if job not in JOBS:
            errors.append(f"row {line_no}: job {row['job']!r} is not one of {', '.join(JOBS)}")
        else:
            jobs[job] += 1
        difficulty = row["difficulty"].lower()
        if difficulty not in {"low", "medium", "high"}:
            errors.append(f"row {line_no}: difficulty {row['difficulty']!r} is not low/medium/high")
        elif difficulty == "high" and week_key:
            high_per_week[week_key] += 1
        if not row["receipt"]:
            errors.append(f"row {line_no}: no receipt — cite a Proof Locker id or write 'opinion'")
        if has_brain:
            brain = row.get("brain", "").lower()
            if not brain:
                blank_brain += 1
            elif brain not in BRAINS:
                errors.append(f"row {line_no}: brain {row.get('brain', '')!r} is not one of {', '.join(BRAINS)}")
            elif week_key:
                brain_per_week[week_key][brain] += 1

        hook_key = row["hook"].lower()
        if hook_key and hook_key in hooks:
            warnings.append(f"row {line_no}: same hook as row {hooks[hook_key]}")
        elif hook_key:
            hooks[hook_key] = line_no

    print(f"# Calendar check: {args.path.name}\n")
    print(f"{len(rows)} posts over {len(per_week)} week(s). Capacity: {args.capacity}\n")
    print("| Week | " + " | ".join(sorted({f for c in per_week.values() for f in c})) + " | high-difficulty |")
    formats = sorted({f for c in per_week.values() for f in c})
    print("|---|" + "---|" * (len(formats) + 1))
    for week_key in sorted(per_week):
        cells = []
        for name in formats:
            count = per_week[week_key][name]
            limit = capacity.get(name)
            over = limit is not None and count > limit
            cells.append(f"{count}/{limit} OVER" if over else f"{count}/{limit}" if limit is not None else f"{count}")
            if over:
                errors.append(f"{week_key}: {count} {name} posts planned, capacity is {limit}")
        if high_per_week[week_key] > args.max_high:
            warnings.append(f"{week_key}: {high_per_week[week_key]} high-difficulty posts (max {args.max_high})")
        print(f"| {week_key} | " + " | ".join(cells) + f" | {high_per_week[week_key]} |")

    unlimited = [f for f in formats if f not in capacity]
    if unlimited:
        warnings.append("formats with no stated capacity: " + ", ".join(unlimited))

    total = sum(jobs.values()) or 1
    print("\n| Job | Posts | Share |")
    print("|---|---|---|")
    for job in JOBS:
        print(f"| {job} | {jobs[job]} | {jobs[job] / total:.0%} |")
        if jobs[job] == 0:
            errors.append(f"no {job} posts in the plan")
    if jobs["conversion"] / total > 0.34:
        warnings.append(f"conversion is {jobs['conversion'] / total:.0%} of the plan — over a third is a lot of asking; keep it only if that is deliberate")

    if has_brain and blank_brain:
        warnings.append(f"{blank_brain} row(s) have no brain state — fill them in, or drop the brain column if Brain-mode is off")
    if has_brain:
        print("\n| Week | " + " | ".join(BRAINS) + " |")
        print("|---|" + "---|" * len(BRAINS))
        for week_key in sorted(brain_per_week):
            counts = brain_per_week[week_key]
            print(f"| {week_key} | " + " | ".join(str(counts[b]) for b in BRAINS) + " |")
            if not any(counts[b] for b in LOW_ENERGY):
                warnings.append(f"{week_key}: every post needs a feral or froggy day — add one a foggy brain could make, or plan to cover it from the Bank")
            if counts["feral"] > 1:
                warnings.append(f"{week_key}: {counts['feral']} posts need a feral day — hyperfocus cannot be scheduled; batch them into one session or bank them ahead")

    batches = Counter(row["batch"] for row in rows if row["batch"])
    singles = [name for name, count in batches.items() if count == 1]
    print(f"\nBatches: {len(batches)} ({', '.join(f'{k}={v}' for k, v in sorted(batches.items()))})")
    if len(singles) > len(batches) / 2 and len(batches) > 2:
        warnings.append("most batches hold a single post — that is not batching, it is a list")

    print()
    for message in errors:
        print(f"ERROR  {message}")
    for message in warnings:
        print(f"WARN   {message}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s).")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
