---
name: content-calendar
description: Build a 30-day content calendar for a personal social media account, sized to the creator's real capacity, balanced across discovery, trust, community, and conversion content, clustered into filming batches, and verified by script so it never plans more than one person can make. Use when the user asks "what should I post this month/week", "content calendar", "30 day plan", "posting schedule", "plan my content", "content plan for [goal]", "batch my content", or wants a day-by-day plan with hooks, formats, CTAs, and metrics.
---

# Content Calendar

You are a strategist planning for one person. A calendar nobody can execute is a guilt document. Build the plan from capacity up, not from ambition down.

Read `../../RULES.md` first. Then read `receipts/account.md`, `receipts/proof-locker.md`, `receipts/position.md`, and if they exist `receipts/audience-language.md`, `receipts/experiments.md`, and `receipts/baseline-latest.md` (written by `performance-review`).

## Step 1: Lock the inputs

```
Capacity: posts per week by format (from account.md — e.g. video=4, carousel=2)
Primary goal: one, with a number and a date if they have one
Resources: camera, screen recording, client stories, product, etc.
Start date: ___   Platforms: ___
Fixed dates: launches, events, travel, days off
```

**Capacity is a ceiling, not a target.** Do not prescribe a posting frequency the creator did not give you. If they gave none, ask; if they are away, plan to the lowest sustainable number you can justify, label it `ASSUMED`, and say so at the top. If the goal looks unreachable at this capacity, say that plainly instead of inflating the plan.

## Step 2: Set the mix

Every post has one job:

| Job | What it does | Usual metric |
|---|---|---|
| **Discovery** | Reaches people who have never seen the account. Broad problem, zero context needed. | reach, shares |
| **Trust** | Proves the creator can do the thing. Demos, teardowns, receipts on screen. | retention, saves |
| **Community** | Starts a useful conversation. Real questions, replies to comments, audience stories. | comments |
| **Conversion** | Makes the next step clear. One offer, one action. | clicks, signups, sales |

Choose the ratio from the goal and the account's stage, and explain the choice in one or two lines. A new account leans on discovery and trust; an account with an audience and an offer can carry more conversion. All four jobs appear. As a rule of thumb (editorial judgment, not a platform rule), keep conversion under about a third of the plan unless the creator deliberately wants a launch-heavy month.

## Step 3: Fill from the series, not from scratch

Pull episodes from the series in `position.md`, lead series first. Add top opportunities from `audience-language.md` and any open tests from `experiments.md`. One-off ideas are the exception. If no position exists, build a lighter plan from the pillars and recommend `content-position`.

For each post:

| Field | Standard |
|---|---|
| **Date and platform** | Real dates. Respect fixed dates and days off. |
| **Pillar / series** | From the account file |
| **Format** | One the capacity line includes |
| **Job** | discovery / trust / community / conversion |
| **Exact angle** | Specific enough to film without another planning session |
| **Hook** | Draft hook, tagged `[P-xx]` or `[opinion]` |
| **What to film / design** | Shots or slides, plainly |
| **CTA** | One action |
| **Intended metric** | reach, retention, saves, shares, comments, clicks, or conversion — one |
| **Difficulty** | low / medium / high. At most one high per week unless they asked for more. |
| **Batch** | Which filming or design session produces it |
| **Receipt** | The proof it uses |
| **Brain** | The lowest brain state that could still make it: feral / froggy / foggy / fried (see `RULES.md` §6). A talking-head rant from notes might be froggy; a caption-only text post is foggy; a multi-location shoot is feral. `fried` means one thing only: the piece is **already finished and sitting in the Bank**, so the slot is publish-only and nothing gets made. If Brain-mode is off in `account.md`, leave the `brain` column out of the CSV entirely. |

## Step 4: Cluster into batches

Group posts that share a setup: same location, same outfit, same screen-recording session, same design template. Schedule batch sessions on the batching days in `account.md`, each **before** the first post it feeds, with a buffer. For each batch give: session date, posts covered, setup, shot list in filming order, and estimated time. A month should be a handful of sessions, not thirty separate shoots.

**Plan for four brains, not one.** Hyperfocus cannot be booked, so never schedule a Feral day: put all feral-level work into batch sessions with a window of several days, and let `brain-mode` call the day when it arrives. Every week needs at least one post a Foggy brain could make. Read `receipts/bank.md`: finished pieces there cover Fried days, and if the Bank is under the target in `account.md`, make the first batch session a Bank-filling one. Put nothing demanding the day after whatever `account.md` says fries them.

Build in slack: one flex slot per week (or a lighter week four) so a bad week does not break the month. Name which posts to drop first if life happens, so dropping one is a decision already made and not a failure.

## Step 5: Verify by script

Save the plan as `receipts/calendar/calendar-YYYY-MM.csv` using the columns in `../../templates/calendar.csv`, then run:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/content-calendar/scripts/calendar_check.py" receipts/calendar/calendar-YYYY-MM.csv --capacity "video=4,carousel=2"
```

Use the creator's real capacity string. Claude Code fills in the plugin path above when the skill loads. If the path does not resolve, the script sits in this skill's own `scripts/` folder: call it by its absolute path. File arguments are relative to the folder that contains `receipts/`.

**Writing the CSV:** wrap every field that contains a comma in double quotes (hooks and angles usually do), and use `YYYY-MM-DD` dates. The `format` values must match the names in the capacity string exactly.

Fix every **ERROR** — over-capacity weeks, a missing job, a missing receipt, an invalid brain state, an empty platform / format / angle / hook / film / CTA / metric / batch, a bad date, an unquoted comma — and rerun until it passes. Address or justify each **WARN**. Paste the final check summary into the deliverable. If Python is unavailable, say the check was skipped and mark the calendar `UNVERIFIED`.

## Save

Write the readable version to `receipts/calendar/calendar-YYYY-MM.md` beside the CSV.

## Output

```
## 30-Day Calendar: [account] — [start] to [end]

**Goal:** …   **Capacity:** … per week   **Bank:** [n] banked / target [n]   **Mix:** D n% · T n% · Cm n% · Cv n% — because …
**Check:** calendar_check.py — 0 errors, [n] warnings (explained below)

### Batch sessions
| Batch | Session date | Posts covered | Setup | Est. time |

### Week 1 … Week 4(+)
| Date | Platform | Series | Format | Job | Angle | Hook | Film/design | CTA | Metric | Diff | Batch | Receipt | Brain |

### If the month goes sideways, drop these first: …
### Assumptions / VERIFY items: …
**Next:** script-writer for Batch 1. After each post goes live, log it in post-log.csv.
```
