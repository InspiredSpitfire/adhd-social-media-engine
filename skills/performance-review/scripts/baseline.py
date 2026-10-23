#!/usr/bin/env python3
"""Compute an account's real baseline from a post log, so the analysis quotes numbers
instead of inventing them.

Reads a CSV (see templates/post-log.csv for the columns; extra columns are ignored,
missing ones are skipped) and prints a Markdown report:

  - per-platform baseline (median views, median engagement rates per 1,000 views)
  - every post as a multiple of its own platform's median
  - overperformers and underperformers against that baseline
  - group medians by format, by topic, and by renewals (how many attention renewals the
    script used, when that column is filled in), with a LOW SAMPLE flag

Medians, not means: one viral post should not redefine "normal". Groups are compared
within a platform only, because a TikTok view and a LinkedIn impression are not the
same unit.

Usage:
  python3 baseline.py post-log.csv
  python3 baseline.py post-log.csv --over 1.5 --under 0.5 --min-sample 5
  python3 baseline.py post-log.csv --out baseline-latest.md   # saved only if the run succeeds
"""

from __future__ import annotations

import argparse
import contextlib
import csv
import io
import statistics
import sys
from collections import defaultdict
from pathlib import Path

RATE_FIELDS = ["likes", "comments", "shares", "saves", "follows", "profile_visits", "clicks"]
NUMERIC_FIELDS = ["views", "length_sec", "avg_watch_sec", "retention_pct", *RATE_FIELDS]


def to_number(raw: str | None) -> float | None:
    """'12,400' -> 12400.0, '41%' -> 41.0, '' / 'n/a' -> None."""
    if raw is None:
        return None
    cleaned = raw.strip().replace(",", "").replace("%", "")
    if not cleaned or cleaned.lower() in {"n/a", "na", "-", "none", "null"}:
        return None
    multiplier = 1.0
    if cleaned[-1].lower() == "k":
        multiplier, cleaned = 1_000.0, cleaned[:-1]
    elif cleaned[-1].lower() == "m":
        multiplier, cleaned = 1_000_000.0, cleaned[:-1]
    try:
        return float(cleaned) * multiplier
    except ValueError:
        return None


def load(path: Path) -> tuple[list[dict], list[str]]:
    notes: list[str] = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            sys.exit(f"{path}: no header row")
        headers = {h.strip().lower(): h for h in reader.fieldnames if h}
        if "views" not in headers:
            sys.exit(f"{path}: needs a 'views' column (use reach/impressions there if that is what the platform reports)")
        posts = []
        for line_no, row in enumerate(reader, start=2):
            post = {key: (row.get(original) or "").strip() for key, original in headers.items()}
            for field in NUMERIC_FIELDS:
                post[field] = to_number(post.get(field))
            if post["views"] is None or post["views"] <= 0:
                notes.append(f"row {line_no}: no usable views value, skipped")
                continue
            post["platform"] = (post.get("platform") or "unknown").lower()
            post["_row"] = line_no
            posts.append(post)
    return posts, notes


def median(values: list[float]) -> float | None:
    values = [v for v in values if v is not None]
    return statistics.median(values) if values else None


def rate_per_k(post: dict, field: str) -> float | None:
    value = post.get(field)
    return None if value is None else value / post["views"] * 1000


def ratio(value: float | None) -> str:
    """Multiples and per-1k rates always keep two decimals, whatever their size."""
    return "—" if value is None else f"{value:,.2f}"


def fmt(value: float | None, digits: int = 1) -> str:
    if value is None:
        return "—"
    if abs(value) >= 100 or float(value).is_integer():
        return f"{value:,.0f}"
    return f"{value:,.{digits}f}"


def label(post: dict) -> str:
    text = post.get("hook") or post.get("topic") or f"row {post['_row']}"
    return (text[:57] + "…") if len(text) > 58 else text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--over", type=float, default=1.5, help="multiple of median that counts as overperforming")
    parser.add_argument("--under", type=float, default=0.5, help="multiple of median that counts as underperforming")
    parser.add_argument("--min-sample", type=int, default=5, help="groups smaller than this are flagged LOW SAMPLE")
    parser.add_argument("--out", type=Path, help="also save the report here; an existing file is only replaced when the run succeeds")
    args = parser.parse_args()

    if args.out is None:
        report(args)
        return
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        report(args)  # exits before this line returns if anything is wrong, leaving --out untouched
    args.out.write_text(buffer.getvalue(), encoding="utf-8")
    print(buffer.getvalue(), end="")
    print(f"\nSaved to {args.out}")


def report(args: argparse.Namespace) -> None:
    if not args.csv_path.is_file():
        sys.exit(f"{args.csv_path}: no such file")
    posts, notes = load(args.csv_path)
    if not posts:
        sys.exit("no usable rows")

    by_platform: dict[str, list[dict]] = defaultdict(list)
    for post in posts:
        by_platform[post["platform"]].append(post)

    print(f"# Baseline report: {args.csv_path.name}\n")
    print(f"{len(posts)} posts across {len(by_platform)} platform(s). All figures computed from the log; nothing here is estimated.\n")

    for platform, group in sorted(by_platform.items()):
        base_views = median([p["views"] for p in group])
        flag = "" if len(group) >= args.min_sample else f" — LOW SAMPLE (n<{args.min_sample}): treat every pattern below as a hunch"
        print(f"## {platform} (n={len(group)}){flag}\n")

        print("### Baseline (medians)\n")
        print("| Metric | Median | Posts with data |")
        print("|---|---|---|")
        print(f"| views | {fmt(base_views)} | {len(group)} |")
        for field in ("avg_watch_sec", "retention_pct"):
            values = [p[field] for p in group if p[field] is not None]
            if values:
                print(f"| {field} | {fmt(median(values))} | {len(values)} |")
        for field in RATE_FIELDS:
            values = [rate_per_k(p, field) for p in group if p[field] is not None]
            if values:
                print(f"| {field} per 1k views | {ratio(median(values))} | {len(values)} |")
        print()

        print("### Every post vs baseline\n")
        print("| Date | Format | Topic | Hook / label | Views | × median | Shares/1k | Saves/1k | Follows/1k |")
        print("|---|---|---|---|---|---|---|---|---|")
        ranked = sorted(group, key=lambda p: p["views"], reverse=True)
        for post in ranked:
            multiple = post["views"] / base_views if base_views else None
            print(
                f"| {post.get('date', '')} | {post.get('format', '')} | {post.get('topic', '')} | {label(post)} | "
                f"{fmt(post['views'])} | {ratio(multiple)} | {ratio(rate_per_k(post, 'shares'))} | "
                f"{ratio(rate_per_k(post, 'saves'))} | {ratio(rate_per_k(post, 'follows'))} |"
            )
        print()

        over = [p for p in ranked if base_views and p["views"] / base_views >= args.over]
        under = [p for p in ranked if base_views and p["views"] / base_views <= args.under]
        print(f"### Overperformers (≥ {args.over}× median views): {len(over)}\n")
        for post in over:
            print(f"- {ratio(post['views'] / base_views)}× — {label(post)} ({post.get('format', '?')}, {post.get('topic', '?')})")
        print(f"\n### Underperformers (≤ {args.under}× median views): {len(under)}\n")
        for post in under:
            print(f"- {ratio(post['views'] / base_views)}× — {label(post)} ({post.get('format', '?')}, {post.get('topic', '?')})")
        print()

        for dimension in ("format", "topic", "renewals"):
            groups: dict[str, list[dict]] = defaultdict(list)
            for post in group:
                groups[(post.get(dimension) or "unlabeled").lower()].append(post)
            if dimension == "renewals":
                groups.pop("unlabeled", None)  # rows logged before the column existed
            if len(groups) < 2:
                continue
            print(f"### By {dimension}\n")
            print(f"| {dimension} | n | Median views | × platform median | Median retention_pct | Median avg_watch_sec | Median shares/1k | Median saves/1k | Sample |")
            print("|---|---|---|---|---|---|---|---|---|")
            def order(kv):
                # renewals reads best in count order (0, 1, 2…); format and topic by reach
                if dimension == "renewals":
                    count = to_number(kv[0])
                    return count if count is not None else float("inf")
                return -(median([p["views"] for p in kv[1]]) or 0)

            for name, members in sorted(groups.items(), key=order):
                group_median = median([p["views"] for p in members])
                sample = "ok" if len(members) >= args.min_sample else "LOW SAMPLE"
                print(
                    f"| {name} | {len(members)} | {fmt(group_median)} | "
                    f"{ratio(group_median / base_views if base_views and group_median else None)} | "
                    f"{fmt(median([p['retention_pct'] for p in members]))} | {fmt(median([p['avg_watch_sec'] for p in members]))} | "
                    f"{ratio(median([rate_per_k(p, 'shares') for p in members]))} | "
                    f"{ratio(median([rate_per_k(p, 'saves') for p in members]))} | {sample} |"
                )
            print()

    missing = [f for f in ("avg_watch_sec", "retention_pct", "shares", "saves", "follows") if all(p[f] is None for p in posts)]
    print("## Data gaps\n")
    if missing:
        print("No values logged for: " + ", ".join(missing) + ". Patterns that depend on these cannot be read from this log.")
    else:
        print("All core columns have at least some data.")
    for note in notes:
        print(f"- {note}")
    print("\nReminder: these are correlations inside a small log. A pattern is a hypothesis to test, not a cause.")


if __name__ == "__main__":
    main()
