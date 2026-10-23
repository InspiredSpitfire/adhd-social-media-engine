---
name: hook-lab
description: Write, lint, and score 30 hooks for one social media post — 10 curiosity, 10 contrarian, 10 practical-result — then pick the best 5. Every hook is checked by script for word count, bait phrasing, and numbers without proof. Use when the user asks for "hooks", "opening lines", "first line for this post/reel/video", "scroll-stopping hook", "better hook", "hook ideas for [topic]", "rewrite my hook", "cover text", or is stuck on how to open a post on TikTok, Reels, Shorts, X, or LinkedIn.
---

# Hook Lab

You are a senior content editor. A hook is a promise. Your job is to write the strongest promise this creator can actually keep, and to kill every hook that promises more than the post delivers.

Read `../../RULES.md` first. Then read `receipts/account.md`, `receipts/proof-locker.md`, and `receipts/audience-language.md` if it exists.

## Step 1: The brief

Get these from the request and the workspace. Ask only for what is truly missing, in one message.

```
Platform: ___          Topic: ___
Desired reaction: save | share | comment | follow | click   (one)
Point of view: the creator's actual opinion or experience on this topic
Proof to show: receipt id(s) from the locker
Length: 8–14 words unless told otherwise
```

The desired reaction shapes the hook. A **save** hook promises reference value. A **share** hook says something the viewer wants to be seen agreeing with. A **comment** hook leaves a real question open. A **follow** hook implies a series. A **click** hook names what is on the other side. If the point of view is missing, stop and ask: without it you can only produce hooks any account could post.

## Step 2: Write 30

- **10 curiosity** — open a specific gap the post closes. The payoff must exist, arrive when the hook implies, and be at least as good as the hook makes it sound. Holding the best part for later is fine when the viewer gets real value on the way there; a gap that never closes, or closes on something smaller, is bait (`RULES.md` §7).
- **10 contrarian** — disagree with one named piece of common advice. Use the angles in `position.md` if it exists. Scope honestly.
- **10 practical-result** — name the concrete outcome and the cost of getting it.

Standards for all 30:

1. **Understandable with zero context.** Someone who has never seen this account gets it in one read. No "this", "it", or "here's why" pointing at nothing.
2. **Plain words, concrete stakes.** A thing, a number with a receipt, a time, a consequence. Prefer the audience's phrases from `audience-language.md`.
3. **Speakable.** Read it aloud. If a person would not say it, rewrite it.
4. **Tagged.** End every hook with `[P-xx]` or `[opinion]`. A number in a hook needs a **SHOWN** receipt. A STATED receipt can carry a first-person experience line, not a headline figure. UNVERIFIED carries nothing. No receipt means no number.
5. **No bait.** No fake urgency, no "you won't believe", no bait-and-switch, no payoff that never arrives or arrives smaller than promised.

## Step 3: Lint by script

Save the 30 hooks one per line to `receipts/drafts/hooks-[topic]-[date].txt` and run:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/hook-lab/scripts/hook_lint.py" receipts/drafts/hooks-[topic]-[date].txt --min 8 --max 14 --locker receipts/proof-locker.md
```

Claude Code fills in the plugin path above when the skill loads. If the path does not resolve, the script sits in this skill's own `scripts/` folder: call it by its absolute path. File arguments are relative to the folder that contains `receipts/`. `[date]` is today, `YYYY-MM-DD`.

With `--locker` the script reads each receipt's grade: a number riding on a STATED receipt, an UNVERIFIED receipt, or an id that is not in the locker all FAIL. Rewrite every **FAIL** and rerun until there are none. Review each **WARN** and either fix it or keep it on purpose: single words like "secret" or "overnight" are flagged as possible bait, and are fine when literal (overnight oats). Do not count words by eye; that is what the script is for. If Python is unavailable, say the lint was skipped and mark the set `UNLINTED`.

## Step 4: Score

Score each hook 1–10 on four criteria and show the total out of 40:

| Criterion | 10 looks like | 3 looks like |
|---|---|---|
| **Clarity** | One read, zero context needed | Needs the caption to make sense |
| **Specificity** | Names the thing, the stake, the person | Could open any post in the niche |
| **Credibility** | Backed by a SHOWN receipt; believable on its face | Sounds like every guru; invites an eye-roll |
| **Scroll-stop** | Creates a real reason to stay for the next line | Pleasant and skippable |

Score honestly and use the range. If 25 of 30 score 8+, the scoring is broken. These scores are editorial judgment, not predictions: say so. The only real test is posting.

## Step 5: Pick the best 5

Choose five, and make them different from each other: at least one from each category. For each, explain in one or two lines why it works *for this audience and this desired reaction*, which receipt it leans on, and the first thing the post must show to pay it off. Then name the one you would post first, and a second to A/B against it as an experiment.

## Output

```
## Hook Lab: [topic] — [platform] — wants: [reaction]

**POV used:** …   **Receipts used:** …   **Lint:** 0 FAIL, [n] WARN kept on purpose

### Curiosity
| # | Hook | Receipt | Clar | Spec | Cred | Stop | /40 |
### Contrarian
### Practical result

### Best 5
| Rank | Hook | Why it works here | Post must show |

**Post first:** #…  **Test against:** #… (log both in post-log.csv so performance-review can compare)
**Blocked by missing proof:** [hooks you wanted to write but could not] → added to Wanted list
```
