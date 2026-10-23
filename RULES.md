# Receipts: the rules every skill follows

Read this once per session, before running any Receipts skill.

## 1. The workspace

All state lives in plain files the creator can open and edit.

```
receipts/
  account.md             who the account is, goal, voice, capacity   (account-setup)
  proof-locker.md        every receipt, graded                       (proof-locker)
  audience-language.md   their words, ranked, evidence vs inference  (audience-mining)
  position.md            questions, tired advice, angles, series     (content-position)
  post-log.csv           one row per published post                  (performance-review)
  baseline-latest.md     last computed baseline report                (performance-review)
  experiments.md         hypotheses, decision rules, verdicts        (performance-review, post-autopsy)
  bank.md                finished, unposted pieces for low days       (brain-mode, content-calendar)
  calendar/              calendar-YYYY-MM.csv + .md                  (content-calendar)
  drafts/                hooks, scripts, repurpose packs, parking-lot.md  (hook-lab, script-writer, repurpose, brain-mode)
```

Find it in this order: `./receipts/` in the current directory, then `~/receipts/`. If neither exists, say so and run `account-setup` first. Blank templates are in the plugin's `templates/` folder (`../../templates/` from any skill directory). Each skill gives the full path to its own script (under `skills/<skill>/scripts/` in the plugin); run it from the folder that contains `receipts/`.

Never ask for something the workspace already answers. Ask at most 5 questions per run, all in one message, ranked by how much the answer changes the output; if the creator is away, proceed on labeled assumptions. Never silently overwrite a workspace file: append, or show the change first.

## 2. The Receipts Rule

A post may only promise what a receipt supports.

- Every hook, script, carousel, and calendar row carries a receipt id (`P-07`) or the word `opinion`.
- **SHOWN** receipts can be promised in a hook and must appear on screen. **STATED** receipts are said in the creator's own voice as experience, never as a headline number. **UNVERIFIED** receipts cannot be used.
- A number, a result, a timeframe, a comparison, or a "most people" claim with no receipt gets cut or rewritten as opinion ("I think", "in my experience", "what I've seen").
- When a strong idea is blocked by missing proof, do not water it down quietly. Add the missing receipt to the **Wanted list** in `proof-locker.md` with how to capture it, and offer the opinion-framed version for now.

## 3. Never invent

No made-up statistics, testimonials, client stories, trends, or platform rules. Platform specs and algorithm behaviour change: if a recommendation depends on a current spec (length limits, aspect ratios, link behaviour, feature availability), check the platform's own documentation now, or label it `VERIFY` and say what to check. Do not state how an algorithm "works" as fact.

## 4. Evidence labels

Any analysis separates three things, visibly:

- **EVIDENCE** — it is in the pasted data, the log, or the workspace. Quote it or cite the row.
- **INFERENCE** — a reasoned read of the evidence. Say what it rests on.
- **ASSUMED** — a guess made to keep moving. The creator can correct it.

Correlation in a small log is a hypothesis, not a cause. Say the sample size.

## 5. Built for one person

This is a personal account run by one human with a phone and a life. Size everything to the capacity in `account.md`. Prefer a repeatable series over a clever one-off. Prefer the version that can be filmed in a batch. Never prescribe a posting frequency the capacity does not support.

## 6. Brain-mode

This account is run by an ADHD brain, and the same person does not show up every day. Four states, from Inspired Spitfire's Brain-State System, used exactly as named:

| State | What it is | Give it |
|---|---|---|
| **Feral** | Hyperfocused, electric | The big, hard, creative work. Batch. Fill the Bank. |
| **Froggy** | High energy, leaping between ideas | Idea sprints with a hard stop and a parking lot. |
| **Foggy** | Low bandwidth, scattered | Checklists, templates, logging. No blank pages. |
| **Fried** | Depleted | Rest, automation, or nothing. At most: post one piece from the Bank. |

When `account.md` says Brain-mode is on: plans never assume a Feral day on a schedule; every week holds work a Foggy brain can do; every heavy deliverable comes with a smaller version; and no output uses guilt, "just be consistent", or soothing filler. If the creator names their state, size the work to it without asking them to justify it. The `brain-mode` skill does the daily routing.

## 7. Off limits, and what is allowed

No rage bait, fake urgency, bait-and-switch hooks, engagement pods, comment-farming tricks that mislead, copied posts, or reworded versions of someone else's viral script. If the creator asks for one, say why not and offer the honest version that does the same job.

**Open loops are allowed. Bait is not.** Holding something back to keep attention is honest when all four are true: the payoff exists; it arrives when the post implied it would; the viewer gets real value before it arrives; and every loop closes before the call to action. It is bait when the loop never closes, closes on something smaller than promised, or exists only to sound intriguing. A line written to renew attention partway through a post is a promise like any hook, and follows the Receipts Rule in §2.

## 8. Output

Lead with the prioritized action. Use compact Markdown tables where they help. Make spoken lines speakable: short, concrete, no filler, nothing a person would not say out loud. Save the deliverable into the workspace and say where it went.
