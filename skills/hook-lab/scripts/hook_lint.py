#!/usr/bin/env python3
"""Lint a list of hooks for the things a model is bad at checking by eye:
word count, bait phrasing, numbers with no receipt, openers that need context,
and near-duplicates.

Input: a text file with one hook per line. Leading numbering/bullets are ignored.
A receipt can be attached to a hook with a trailing tag, e.g.

    I cut my edit time from 3 hours to 40 minutes [P-04]

Without --locker the lint only checks that a tag is present. With --locker it reads the
grades from proof-locker.md and enforces the Receipts Rule: a quantity may only ride on
a SHOWN receipt, UNVERIFIED receipts cannot be used, and unknown ids are rejected.

FAIL blocks (exit code 1). WARN is a judgment call for the writer. Exit code 2 means
there was nothing to lint.

With --renewals the file holds mid-post attention renewals instead of opening hooks:
the default word range becomes 2–20 (an explicit --min or --max always wins) and the
needs-no-context check is skipped, because a renewal is allowed to lean on what came
before it. Every claim check still applies.

Usage:
  python3 hook_lint.py hooks.txt
  python3 hook_lint.py renewals.txt --renewals --locker receipts/proof-locker.md
  python3 hook_lint.py hooks.txt --min 8 --max 14 --locker receipts/proof-locker.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Phrases that promise more than a post can deliver, or that manufacture urgency. FAIL.
BAIT = [
    "you won't believe", "you wont believe", "nobody is talking about", "no one is talking about",
    "they don't want you to know", "they dont want you to know", "this one trick", "one weird trick",
    "will change your life", "changed my life forever", "wait for it", "watch until the end",
    "stop scrolling", "before it's too late", "before its too late", "before it gets deleted",
    "guaranteed", "insane results", "go viral", "blow up your",
]
# Single words that are bait in one niche and plain vocabulary in another
# (overnight oats, a secret ingredient). WARN, so the writer decides.
BAIT_MAYBE = ["overnight", "instantly", "effortlessly", "secret", "secrets", "shocking", "hack", "hacks"]
ABSOLUTES = {"always", "never", "everyone", "everybody", "nobody", "every", "all"}
# Quantities written as words are still claims; digits are caught by NUMBER below.
WORD_NUMBERS = {
    "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "twenty", "thirty",
    "forty", "fifty", "hundred", "thousand", "million", "half", "double", "doubled", "tripled",
}
# First words that usually point at something the viewer has not seen yet.
CONTEXT_OPENERS = {"this", "that", "it", "these", "those", "so", "and", "but", "also", "then"}

# "Most people…", "most creators…": a claim about a population, which needs a receipt or an honest "I think".
POPULATION = re.compile(
    r"\b(?:most|the majority of|nine out of ten|9 out of 10)\s+"
    r"(?:of\s+(?:us|them|you|my\s+[a-z]+s|your\s+[a-z]+s)|people|folks|women|men|users|viewers|followers|clients|customers|students|beginners|businesses|brands|accounts|experts"
    r"|[a-z]+(?:ers|ors|ists))\b",
    re.IGNORECASE,
)

RECEIPT_TAG = re.compile(r"\[(P-\d+|opinion)\]\s*$", re.IGNORECASE)
LEADING_MARK = re.compile(r"^\s*(?:\d+[.)]|[-*•])\s*")
NUMBER = re.compile(r"(?<![A-Za-z-])\$?\d[\d,.]*\s*(?:%|k\b|x\b|m\b)?", re.IGNORECASE)


LOCKER_ROW = re.compile(r"^\|\s*(P-\d+)\s*\|[^|]*\|\s*\**\s*(SHOWN|STATED|UNVERIFIED)\s*\**\s*\|", re.IGNORECASE)


def has_phrase(phrase: str, lowered: str) -> bool:
    return re.search(r"(?<![a-z0-9])" + re.escape(phrase) + r"(?![a-z0-9])", lowered) is not None


def load_grades(path: Path) -> dict[str, str]:
    """Read `| P-01 | what it is | SHOWN | …` rows out of proof-locker.md."""
    grades: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = LOCKER_ROW.match(line.strip())
        if match:
            grades[match.group(1).upper()] = match.group(2).upper()
    return grades


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9$%']+", text)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("path", type=Path)
    parser.add_argument("--min", type=int, default=None, dest="min_words", help="default 8 (2 with --renewals)")
    parser.add_argument("--max", type=int, default=None, dest="max_words", help="default 14 (20 with --renewals)")
    parser.add_argument("--locker", type=Path, help="proof-locker.md, to check receipt grades and ids")
    parser.add_argument("--renewals", action="store_true", help="lint mid-post renewals: word floor 2, no needs-no-context check")
    args = parser.parse_args()
    if args.min_words is None:
        args.min_words = 2 if args.renewals else 8
    if args.max_words is None:
        args.max_words = 20 if args.renewals else 14

    for path in filter(None, (args.path, args.locker)):
        if not path.is_file():
            sys.exit(f"{path}: no such file")
    grades = load_grades(args.locker) if args.locker else None

    raw_lines = [line for line in args.path.read_text(encoding="utf-8").splitlines() if line.strip()]
    hooks = []
    for line in raw_lines:
        text = LEADING_MARK.sub("", line).strip()
        if text.startswith("#"):
            continue
        tag = RECEIPT_TAG.search(text)
        receipt = tag.group(1) if tag else None
        hooks.append((RECEIPT_TAG.sub("", text).strip().strip('"“”').strip(), receipt))

    if not hooks:
        print(f"{args.path}: no hooks found — nothing was linted")
        sys.exit(2)

    fails = warns = 0
    seen: dict[str, int] = {}
    kind = "renewals" if args.renewals else "hooks"
    print(f"# Hook lint: {len(hooks)} {kind}, target {args.min_words}–{args.max_words} words\n")
    print("| # | Words | Result | Hook | Notes |")
    print("|---|---|---|---|---|")

    for index, (hook, receipt) in enumerate(hooks, start=1):
        tokens = words(hook)
        lowered = hook.lower()
        problems: list[tuple[str, str]] = []

        if not args.min_words <= len(tokens) <= args.max_words:
            problems.append(("FAIL", f"{len(tokens)} words, outside {args.min_words}–{args.max_words}"))
        for phrase in BAIT:
            if has_phrase(phrase, lowered):
                problems.append(("FAIL", f"bait phrase: “{phrase}”"))
        for word in BAIT_MAYBE:
            if has_phrase(word, lowered):
                problems.append(("WARN", f"“{word}” reads as bait unless it is literal here"))

        has_digits = NUMBER.search(hook) is not None
        spelled = sorted(WORD_NUMBERS.intersection(t.lower() for t in tokens))
        backed = receipt is not None and receipt.lower() != "opinion"
        grade = None
        if backed and grades is not None:
            grade = grades.get(receipt.upper())
            if grade is None:
                problems.append(("FAIL", f"{receipt.upper()} is not in the Proof Locker"))
            elif grade == "UNVERIFIED":
                problems.append(("FAIL", f"{receipt.upper()} is UNVERIFIED — cannot be used until checked"))
        if has_digits and not backed:
            problems.append(("FAIL", "contains a number with no receipt tag — add [P-xx] or remove the number"))
        elif has_digits and grade == "STATED":
            problems.append(("FAIL", f"headline number rides on {receipt.upper()}, which is STATED — needs a SHOWN receipt"))
        elif spelled and not backed:
            problems.append(("WARN", "spelled-out quantity (" + ", ".join(spelled) + ") with no receipt — is it a claim?"))
        elif spelled and grade == "STATED":
            problems.append(("WARN", f"quantity ({', '.join(spelled)}) rides on {receipt.upper()}, which is STATED — say it as experience, not a headline"))
        if receipt is None:
            problems.append(("WARN", "no receipt tag — mark [P-xx] or [opinion]"))
        population = POPULATION.search(hook)
        if population and receipt is None:
            problems.append(("WARN", f"population claim (“{population.group(0)}”) — tag a receipt, or tag [opinion] and say it as your own view"))
        if not args.renewals and tokens and tokens[0].lower() in CONTEXT_OPENERS:
            problems.append(("WARN", f"opens with “{tokens[0]}” — does it make sense with no context?"))
        hit = sorted(ABSOLUTES.intersection(t.lower() for t in tokens))
        if hit:
            problems.append(("WARN", "absolute claim: " + ", ".join(hit)))

        key = " ".join(t.lower() for t in tokens[:4])
        if key in seen:
            problems.append(("WARN", f"same opening as #{seen[key]}"))
        else:
            seen[key] = index

        level = "FAIL" if any(p[0] == "FAIL" for p in problems) else "WARN" if problems else "ok"
        fails += level == "FAIL"
        warns += level == "WARN"
        notes = "; ".join(f"{lvl}: {msg}" for lvl, msg in problems) or ""
        print(f"| {index} | {len(tokens)} | {level} | {hook.replace('|', '/')} | {notes} |")

    print(f"\n{fails} FAIL, {warns} WARN, {len(hooks) - fails - warns} clean.")
    if grades is None:
        print("Receipt tags were checked for presence only. Pass --locker proof-locker.md to check grades.")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
