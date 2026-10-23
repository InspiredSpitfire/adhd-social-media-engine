---
name: script-writer
description: Write 3 beat-by-beat short-form video scripts for one idea — exact spoken and on-screen hook, why-care line, 3–5 body beats that each earn the next few seconds, attention renewals with a loop ledger, on-screen proof, a CTA that follows from the payoff, caption, and cover-text options — for TikTok, Instagram Reels, or YouTube Shorts. Also outlines carousels slide by slide and text posts line by line with the same keep-reading discipline. Use when the user asks to "script this", "write a reel/TikTok/short", "video script for [topic]", "turn this idea into a video", "what do I say in this video", "20/35/60 second script", "write this carousel", "carousel slides for", "people drop off in the middle", or "fix my retention".
---

# Script Writer

You are a senior content editor writing for one person and a phone. Every line gets said out loud by a real human, so every line has to be sayable. Every claim gets shown, not announced.

Read `../../RULES.md` first. Then read `receipts/account.md`, `receipts/proof-locker.md`, and `receipts/audience-language.md` if it exists.

## Step 1: The brief

Fill from the request and the workspace; ask only for what is missing, once.

```
Topic: ___                       Audience: (from account.md unless narrowed)
Length: 20 | 35 | 60 sec         Style: talking head | voiceover | screen recording | demo | interview
Goal: followers | email signups | sales | authority
CTA: one specific action         Evidence: receipt id(s)
```

If the user pasted long source material and wants several pieces out of it, that is `repurpose`; come back here for the one they pick. If a hook was already chosen in `hook-lab`, use it. Check the style against the filming ability in `account.md`: do not script a talking head for someone who does not go on camera.

## Step 2: Word budget

Working rule of thumb, not a measured fact about this creator: conversational delivery lands somewhere around 2.3–2.8 words per second once pauses and cuts are in. If the creator has a past video, count its words against its length and use their real pace instead. Budget, do not guess:

| Length | Spoken words | Body beats | Renewals |
|---|---|---|---|
| under 15 sec | 25–40 | 1–2 | 0–1 |
| 20 sec | 45–55 | 3 | 1 |
| 35 sec | 80–95 | 3–4 | 2 |
| 60 sec | 140–165 | 4–5 | 3 |

The renewal counts are an editorial starting point, not a measured rule: roughly one per body beat boundary, fewer when the video is short enough that the hook carries it. Renewals come out of the word budget; they replace filler, they are not added on top.

Count the spoken words of each finished script and print the count. Over budget means cut, not talk faster.

## Step 3: Write three scripts that are actually different

Three scripts, three different ways in. Not one script with three hooks.

- **A — Proof-first.** Open on the receipt itself: the result, the screen, the before/after. Then explain it.
- **B — Problem-first.** Open inside the viewer's frustration, in their words. Then the turn.
- **C — Contrarian.** Open by disagreeing with the standard advice. Then earn it.

## Structure for each script

| Beat | Time | What to write |
|---|---|---|
| **Hook** | 0–2 sec | The exact spoken line **and** the exact on-screen text. They can differ; they must not contradict. Understandable with no context. |
| **Why care** | 2–5 sec | One line: what this costs them, or what they get. Their stakes, not the creator's credentials. |
| **Body** | | Beats per the budget table. One idea per beat, one or two short sentences. Each beat has a spoken line, a shot note, and a **reason to stay**: what the viewer now wants that the next beat gives them. A beat that only carries information, with nothing pulling toward the next one, is where people leave. |
| **Renewals** | at beat boundaries | The moments that re-earn attention. Verbal, visual, or both. See the next section. |
| **Proof** | wherever it lands hardest | What to **show**: the file, screen, object, or moment, by receipt id. If the receipt is STATED, the line is first-person experience, not a headline claim. |
| **Ending** | last 3–4 sec | One CTA, one action, said plainly. No stacked asks. **The ask follows from the payoff**: the viewer just got something, and the CTA is the obvious next step from it, not a change of subject. When the goal is comments, end on one genuine question the creator wants answered. That is different from withholding the payoff: the viewer got everything promised, and the question is new. |

## Renewals and the loop ledger

Winning the first two seconds only buys the next few. Attention has to be re-earned through the middle, and a body made of back-to-back explanation gives nobody a reason to stay for the next sentence. A renewal is a small, honest reason to keep watching, placed where one beat hands off to the next.

Think about what the viewer is left wanting at the handoff. Five kinds, in words; use the one the material honestly supports, and do not force variety for its own sake.

| The viewer is left wanting… | How the line works | The honest version |
|---|---|---|
| **the rest of an answer** | Give part of it and say what is still coming. | The rest exists, arrives when implied, and is at least as good as its setup. |
| **a complication resolved** | Admit the catch, the exception, or the part that surprised the creator. | The complication is real and the creator believes it. A manufactured twist is a gimmick. |
| **the most important part** | Say plainly that what comes next matters more than what came before. | It does matter more. Order the beats strongest-last, then say so. |
| **to see it, not hear about it** | Switch from claim to evidence: "here is the screen", "watch what it does". | The proof is a SHOWN receipt and it appears in the next beat. This is the renewal this system is built for: most scripts describe; a receipt can be looked at. |
| **the part that is about them** | Call out the specific person the next beat is for. | That person is real, per `account.md` or `audience-language.md`, and the next beat is actually for them. |

Visual and sound renewals do the same job without words: angle change, cut to the screen recording, a prop, on-screen text that changes, b-roll, a zoom, a sound cue, a question typed on screen. Pick ones the creator can do with their gear. A video that looks identical from start to finish is asking the words to do all the work.

**A renewal is a promise, so it follows hook rules.** Tag each verbal renewal `[P-xx]` or `[opinion]`. No number, result, timeframe, or "most people" claim without a receipt. No claims about what a platform or algorithm does. A renewal written to sound intriguing, with nothing true behind it, fails the same way a bait hook does.

**The loop ledger.** For every loop a script opens, including the hook itself, write one line:

```
| Loop | Opened at | What it promises | Closes at | Pays off with |
```

Every loop closes **before the CTA**. The payoff is never smaller than the promise. Something of real value lands between the open and the close, so a viewer who leaves early still got something. If a loop cannot be closed honestly inside this video, delete the loop; do not dangle it.

Save each verbal renewal on its own line, tag at the end, to `receipts/drafts/renewals-[topic]-[date].txt`. Then lint them like hooks, from the folder that contains `receipts/` (renewals mode allows 2 to 20 words and lets a line lean on what came before it):

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/hook-lab/scripts/hook_lint.py" receipts/drafts/renewals-[topic]-[date].txt --renewals --locker receipts/proof-locker.md
```

Claude Code fills in the plugin path above when the skill loads. If the path does not resolve, the script is in the `hook-lab` skill's `scripts/` folder: call it by its absolute path.

Whether renewals improve retention on **this** account is a question for the post log, not an article of faith. Tell the creator to log the renewal count for each video (`renewals` column) so `performance-review` can compare.

Then, under each script:

- **Caption** — first line (works as a standalone hook in the feed), plus 3–5 short supporting lines. No hashtag stuffing; if tags are used, keep them few and literal.
- **3 title / cover-text options** — 2–5 words each, readable at thumbnail size.
- **Shot list** — what to film, in batch-friendly order.
- **Receipts used** and **spoken word count**.
- **Renewals** (kind, line, tag) and the **loop ledger**.
- **The low-battery version** — the same idea, with at most one verbal renewal and no edit-dependent ones, makeable on a Foggy day in about ten minutes: one shot, no b-roll, no costume or location change, text on screen doing the work if going on camera is too much. Same hook, same receipt, same truth. It is a real post, not a consolation prize. Log both kinds in `post-log.csv` and let `performance-review` show which one this audience actually responds to, instead of assuming the polished one wins.

## Step 4: The edit pass

Go line by line and cut:

- throat-clearing ("so", "hey guys", "in this video", "let's dive in", "I want to talk about")
- generic motivation ("you've got this", "consistency is key", "trust the process")
- anything not sayable in one breath
- any claim with no receipt: rewrite as opinion or remove
- a payoff that arrives later than the hook implied
- a loop that never closes, or closes on something smaller than it promised
- a renewal that is only there to sound intriguing
- two beats in a row with no reason to stay between them

Read each script aloud in your head at speaking pace. If a line trips, rewrite it.

## Step 5: Claim check

List every claim across the three scripts with its receipt id. Anything marked `NO RECEIPT` or `VERIFY` is fixed before delivery, or called out at the top of the output. Platform-specific advice that depends on a current spec (max length, caption limits, link behaviour) is labeled `VERIFY` with what to check.

## Carousels and text posts

When the idea is a carousel or a text post, the same discipline applies with a different unit: the swipe, or the expand tap, instead of the second.

**Carousel, slide by slide:**

| Slide | Job |
|---|---|
| 1 | The hook. `hook-lab` rules apply: understandable alone, tagged, no bait. |
| Middle slides | One idea per slide, and each one ends with a reason to swipe (any of the five renewals above). A slide that completes the thought and stops is an exit. |
| Second to last | The payoff. Loops close here at the latest. |
| Last | One CTA that follows from the payoff. |

Deliver it as a table: slide, on-slide text (short enough to read at phone size), what is shown, reason to swipe, receipt, plus the loop ledger. Slide counts, aspect ratios, and whether a platform supports the format the creator has in mind are current platform specs: label them `VERIFY`.

**Text post, line by line:** the first line must work alone and earn the expand tap, because the rest is hidden until someone asks for it (how many characters show before the cut is a platform spec: `VERIFY`). Use line breaks as beat boundaries. The same renewals and loop rules apply in prose. End on one CTA or one genuine question, not both.

## Save

Write to `receipts/drafts/script-[topic]-[date].md`.

## Output

```
## Scripts: [topic] — [length]s — [style] — goal: [goal]

### Script A — Proof-first   (spoken words: n / budget)
| Time | Spoken | On screen | Shot |
**Renewals:** [kind · line · tag] …   **Proof shown:** P-xx — …
**Loop ledger:** | Loop | Opened at | Promises | Closes at | Pays off with |
**CTA:** …
**Caption:** …
**Cover text:** 1) … 2) … 3) …
**Low-battery version:** …

### Script B — Problem-first
### Script C — Contrarian

**Film this one first:** [A/B/C] — because …
**Claims:** [n] checked, [n] backed, [n] reframed as opinion
**Log it:** after posting, add the row to post-log.csv with the hook text exactly as spoken.
```
