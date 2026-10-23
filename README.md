# ADHD Social Media Engine

A content system for one-person social media accounts run by ADHD brains, built as a Claude Code plugin. Two ideas hold it up. **Brain-mode**: the same person does not show up every day, so the work gets routed to the brain that did. **The Receipts method**: nothing gets claimed that you cannot show.

Most AI content tools will happily write "I grew 10,000 followers in 30 days" for an account that did no such thing. This one will not. Every hook, script, and calendar row has to point at something you can actually show or honestly say, and every analytics number is computed by a script instead of guessed by a model.

> Status: v0.2.0 (2026-09-21). First run on a live account is in progress; no results yet.

## How it is different from a prompt pack

| A prompt pack | ADHD Social Media Engine |
|---|---|
| You fill in `[brackets]` every time | You fill in one account file once; every skill reads it |
| "Don't make false claims" is a sentence in the prompt | A **Proof Locker** grades every receipt SHOWN / STATED / UNVERIFIED, and every claim must cite one |
| The model counts words and does your analytics math in its head | Three scripts do it: hook lint, calendar capacity check, baseline calculator |
| A 30-day calendar sized to ambition | A calendar that fails verification if it plans more than you said you can make |
| Assumes you have the same energy every day | **Brain-mode** routes today's job to Feral, Froggy, Foggy, or Fried you; a **Bank** of finished posts covers the days you have nothing |
| Eight separate chats | A loop: post → log → review → experiment → next calendar, with state saved in plain files |
| The author grades their own work | An independent editor agent returns PASS or NEEDS REVISION |

## The skills

**Foundation**
| Skill | What it does |
|---|---|
| `brain-mode` | Say which brain showed up. Get the one content job that fits it, a time box, and a done line. Tracks your Bank of finished posts. |
| `account-setup` | Builds your workspace. Returns your positioning sentence, 3 pillars, and the 5 questions that matter most. |
| `proof-locker` | Inventories and grades everything you can prove. Checks drafts for unsupported claims. Tells you which receipts to capture next. |

**Strategy**
| Skill | What it does |
|---|---|
| `content-position` | The audience's 10 urgent questions, the tired advice in your niche, 10 contrarian angles you can defend, 5 repeatable series with 10 episodes each. |
| `audience-mining` | Turns 20–100 real comments, DMs, or reviews into ranked pains, their exact language, and 15 content opportunities. Evidence kept separate from inference. |

**Production**
| Skill | What it does |
|---|---|
| `hook-lab` | 30 hooks (curiosity, contrarian, practical-result), linted by script, scored, best 5 picked. |
| `script-writer` | 3 genuinely different beat-by-beat scripts with word budgets, attention renewals through the middle, a loop ledger so nothing dangles, on-screen proof, caption, and cover text. Also outlines carousels and text posts. |
| `repurpose` | One insight into 18 pieces across video, carousel, Stories, text posts, email, and FAQ, each with a new angle. |
| `content-calendar` | 30 days, sized to your capacity, balanced across discovery / trust / community / conversion, clustered into filming batches, verified by script. |

**Feedback loop**
| Skill | What it does |
|---|---|
| `performance-review` | Computes your real baseline, then patterns, overperformers, a two-week experiment plan with decision rules written in advance, and 10 next posts. |
| `post-autopsy` | Diagnoses one underperforming post in a fixed order, then rewrites it three ways, each with a testable hypothesis. |

**Agent:** `receipts-editor` — independent pre-publish check.
**Commands:** `/adhd-social-media-engine:start` · `/adhd-social-media-engine:brain <state>` · `/adhd-social-media-engine:hooks <topic>` · `/adhd-social-media-engine:autopsy` · `/adhd-social-media-engine:weekly-review`

## Your workspace

Everything is a plain file you can open and edit.

```
receipts/
  account.md            proof-locker.md        audience-language.md
  position.md           post-log.csv           experiments.md
  baseline-latest.md    bank.md
  calendar/             drafts/
```

## Install

```bash
claude plugin marketplace add /path/to/adhd-social-media-engine
```

```bash
claude plugin install adhd-social-media-engine@adhd-social-media-engine
```

Then run `/adhd-social-media-engine:start`. Scripts need Python 3.9+ and nothing else.

## Verify

The example files contain planted defects. The scripts should catch all of them.

```bash
python3 skills/hook-lab/scripts/hook_lint.py examples/sample-hooks.txt
```

```bash
python3 skills/content-calendar/scripts/calendar_check.py examples/sample-calendar.csv --capacity "video=4,carousel=2"
```

```bash
python3 skills/performance-review/scripts/baseline.py examples/sample-post-log.csv
```

```bash
python3 scripts/check_plugin.py
```

## What it will not do

Rage bait, fake urgency, invented statistics or testimonials, engagement manipulation, copied posts, or confident claims about how a platform's algorithm works. It will not promise you virality. It will tell you when your log is too small to conclude anything.

## Credit

The four-state Brain-State System (Feral, Froggy, Foggy, Fried) is Inspired Spitfire's framework. Brain-mode is a way to plan work. It is not medical advice or treatment.
