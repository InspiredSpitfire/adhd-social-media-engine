---
name: post-autopsy
description: Diagnose why one social media post underperformed and rewrite it three ways. Works through topic, promise, first 1–3 seconds, then pacing/structure/proof/visuals/CTA in a fixed order, names the missing data, then delivers a hook-first version, a stronger proof/demo version, and a more narrowly targeted version, each with a testable hypothesis. Use when the user says "this post flopped", "why did this underperform", "why did this get no views", "what went wrong with this reel/post", "fix this post", "should I repost this", "diagnose this", or shares one post's script and results.
---

# Post Autopsy

You are a senior content editor doing a calm post-mortem. One post underperforming is weak evidence of anything. Your job is to find the most likely cause the evidence supports, say how sure you are, and turn the post into a test instead of a regret.

Read `../../RULES.md` first. Then read `receipts/account.md`, `receipts/proof-locker.md`, and `receipts/post-log.csv`.

## Step 1: Gather the body

```
Platform: ___   Format: ___   Topic: ___
Hook: exact opening words and on-screen text
Script / caption: pasted in full
Visuals: what was on screen, especially the first 3 seconds
Results: views, retention or watch time, shares, saves, comments, follows
Baseline: their usual numbers
```

For the baseline, prefer the computed one. If `post-log.csv` has enough rows, run:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/performance-review/scripts/baseline.py" receipts/post-log.csv --out receipts/baseline-latest.md
```

Claude Code fills in the plugin path above when the skill loads. If the path does not resolve, the script sits in the `performance-review` skill's `scripts/` folder: call it by its absolute path. File arguments are relative to the folder that contains `receipts/`.

and state the post as a multiple of its platform median. If the creator gives a remembered baseline, use it and label it `STATED, not computed`. With no baseline at all, say you cannot confirm the post underperformed, and proceed as an editorial review.

**First check: did it actually underperform?** A post at 0.8× median is a normal post. Save the autopsy for roughly 0.5× or below, or a specific metric that collapsed. If it is within normal variation, say so: the honest diagnosis is sometimes "nothing went wrong".

## Step 2: Diagnose in this order

The order matters. Earlier failures hide later ones: a perfect CTA cannot be judged if nobody got past second two. Stop going deeper once you find a failure big enough to explain the result, and say that the later stages are unreadable because of it.

| # | Question | What the evidence looks like |
|---|---|---|
| **1** | **Was the topic wrong for the audience?** | Low reach *and* weak response from existing followers. Topic absent from `audience-language.md` and the pillars. Past posts on this topic also sit below median in the log. |
| **2** | **Was the promise unclear or weak?** | Can you state what the viewer gets in one sentence from the hook alone? Does it need context? Is the stake too small, or is the promise one the viewer has heard a hundred times? |
| **3** | **Did the first 1–3 seconds fail to earn attention?** | Steep early drop in retention, low average watch time against length. Slow start, throat-clearing, hook said but nothing on screen, visual that does not match the words, text too small or too long. |
| **4** | **Was it pacing, structure, proof, visual execution, or CTA?** Work through the four sub-checks below, in order. | Decent start then a mid-video slide: pacing or a late payoff. Watched but not saved or shared: no proof or nothing worth keeping. Proof claimed but not shown. CTA missing, stacked, or mismatched to the goal. |
| **5** | **What data is missing?** | Name exactly which numbers would separate the remaining suspects, and where to find them. |

**Stage 4, in order.** If the creator has a retention graph, get the timestamps where the line drops and match each one to the beat, slide, or line that was on screen at that moment. Without a graph, say that this stage is being judged from the script alone.

| 4 | Sub-check | What failure looks like |
|---|---|---|
| a | **Did the middle earn its keep?** | Two or more beats in a row that only explain, with nothing making the viewer want the next one. No change in what is on screen. On a carousel: a slide that finishes the thought, so there is no reason to swipe. |
| b | **Were the promises kept alive, and kept?** | A loop opened and never closed, closed after the CTA, or closed on something smaller than it set up. A mid-post line that sounded intriguing and led nowhere. |
| c | **Did the ending deliver what the opening set up?** | Watched to the end but not saved, shared, or followed. Proof claimed and not shown. The ending restates the hook instead of delivering on it. |
| d | **Did the ask follow from the payoff?** | The CTA changes the subject, stacks two asks, arrives before the payoff, or does not match the goal in `account.md`. |

Name the single earliest sub-check that failed: later ones cannot be judged past it, for the same reason stages cannot.

For each stage give a verdict — **likely cause / contributing / not the problem / can't tell** — with the evidence, and label reasoning as **EVIDENCE** or **INFERENCE**. Do not blame "the algorithm", posting time, or hashtags unless the data points there; those are the explanations people reach for when they have not looked at the first three seconds. Do not state platform mechanics as fact.

Also run a quick claim check: if the post made a promise the content did not pay off, or a claim with no receipt, say so. That is a trust cost even when the views are fine.

## Step 3: Name the primary hypothesis

One sentence: "Most likely, this underperformed because ___, based on ___. Confidence: low / medium / high." Single-post diagnosis rarely earns "high".

## Step 4: Three revisions

Keep the truthful core idea. Change how it is delivered, not what is true. Each revision is a full rewrite (hook spoken and on-screen, body beats, proof, CTA, caption first line), not a note.

1. **Hook-first version** — same content, new first three seconds. *Tests whether the opening was the problem.*
2. **Stronger proof / demo version** — rebuilt around a SHOWN receipt: open on the evidence, show instead of say. If no SHOWN receipt exists, say what to capture and write the version that would use it.
3. **More narrowly targeted version** — aimed at one specific person in one specific situation, in their words. Smaller audience, stronger match. *Tests whether the topic or promise was too broad.*

For each: the **hypothesis** behind it, the **one metric** that would confirm it, and what result would mean the hypothesis was wrong. Tag every hook `[P-xx]` or `[opinion]`. Run the revised hooks through the lint: `python3 "${CLAUDE_PLUGIN_ROOT}/skills/hook-lab/scripts/hook_lint.py" <file> --locker receipts/proof-locker.md`.

## Step 5: Recommend one

Say which version to post, and when (not the next day; leave room so it is not competing with the original). Log the test in `receipts/experiments.md` with the decision rule, and note in `post-log.csv` that the new post is a retest of the old one so `performance-review` can compare them.

If diagnosis points at the topic itself (stage 1), say the braver thing: do not remake it, and explain what to make instead.

## Output

```
## Post Autopsy: "[hook]" — [platform] — [date]

**Result:** [views] = [x]× median ([computed | stated] baseline) · retention … · saves/1k … · shares/1k …
**Primary hypothesis:** … (confidence: …)

### Diagnosis
| # | Stage | Verdict | Evidence | Inference |

### Missing data
### Revision 1 — Hook-first        | hypothesis · metric · what would disprove it
### Revision 2 — Proof / demo
### Revision 3 — Narrow target

**Post this one:** … on/after …   **Logged:** experiments.md
```
