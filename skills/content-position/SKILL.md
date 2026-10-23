---
name: content-position
description: Create a differentiated content position for a personal social media account — the audience's 10 most urgent questions, the overused advice in the niche, 10 defensible contrarian angles, and 5 repeatable content series with 10 episodes each. Use when the user asks "what should my account be about", "how do I stand out", "differentiate my content", "content pillars", "content series ideas", "contrarian angles", "everyone in my niche says the same thing", "what should I be known for", or wants a recognizable, repeatable content identity rather than one-off post ideas.
---

# Content Position

You are a strategist building a position one person can hold for a year. A position is not a niche. A niche is where the account lives; a position is the reason someone follows *this* account instead of the forty others saying the same thing.

Read `../../RULES.md` first. Then read `receipts/account.md`, `receipts/proof-locker.md`, and `receipts/audience-language.md` if it exists. If there is no workspace, run `account-setup` first.

## Step 1: The audience's 10 most urgent questions, frustrations, and desired outcomes

Rank by urgency, not by how interesting they are to the creator. For each, give the item in the audience's own words, its type (question / frustration / outcome), and its source.

Source discipline: if `audience-language.md` exists, pull from it and cite it as **EVIDENCE**. Otherwise label the list **ASSUMED**, say so at the top, and recommend `audience-mining` as soon as they have 20 real comments, DMs, or reviews. Do not dress up guesses as research.

## Step 2: The tired advice

List the advice this niche repeats until nobody hears it. For each: the cliché, why it became standard (it is usually partly right), and where it fails *this* audience specifically. Eight to twelve items.

If you can search, check what currently fills the niche on the creator's platforms and label what you saw. If you cannot, label the list **INFERENCE** from general knowledge of the niche. Do not attribute advice to named creators.

## Step 3: 10 defensible contrarian angles

A contrarian angle is only worth holding if the creator can defend it in the comments. Each angle needs all four:

| Field | Standard |
|---|---|
| **The angle** | One sentence that disagrees with a specific item from Step 2. |
| **The honest scope** | Who it is true for, and who it is not. "For people who X" beats "everyone is wrong". |
| **Receipt** | The `P-xx` that backs it, or `opinion`. An angle resting on an UNVERIFIED receipt is not usable yet. |
| **The steelman** | The best objection, and the creator's answer to it. |

Throw out angles that are contrarian only in tone: same advice, angrier voice. Throw out anything that needs an exaggerated claim to land. If fewer than ten survive, deliver the ones that did and say how many you cut and why. Seven real angles beat ten padded ones.

## Step 4: 5 repeatable series

A series is a promise the audience can recognize in the first second and the creator can repeat without reinventing the format. Each series must clear four bars:

1. **Recognizable** — a fixed name, a fixed opening line or visual, the same structure every time.
2. **Repeatable** — at least 10 episodes are obvious today, and episode 30 is imaginable.
3. **Provable** — the format itself shows proof (a demo, a teardown, a real-time attempt, a receipt on screen), so trust builds per episode.
4. **Producible** — fits the filming ability and weekly capacity in `account.md`, and batches well.

Reject generic series ("Tips Tuesday", "Motivation Monday", "behind the scenes") unless made so specific to this audience that no other account could run it under the same name.

For each series deliver:

- **Series name**
- **Audience promise** — what the viewer gets every episode, in their words
- **Ideal format and platform** — and why this format for this promise
- **Fixed elements** — the repeating open, visual, and structure
- **10 episode ideas** — specific enough to film; each tagged with a receipt id or `opinion`
- **Why someone follows after one post** — the unanswered next episode they now want
- **Proof or personal experience to show** — what goes on screen, not what gets claimed
- **Production load** — low / medium / high per episode, and how many fit in one batch session

## Step 5: Pick the lead series

Recommend one series to launch first and say why: the strongest receipt, the lowest production load, and the clearest line to the goal. One person cannot launch five series at once. The other four are the bench.

## Save and hand off

Write the full position to `receipts/position.md` and add the five series to the Series table in `account.md`. Add any proof gaps you hit to the Wanted list in `proof-locker.md`.

## Output

```
## Content Position: [account]

**The position in one line:** …
**Evidence base:** EVIDENCE from audience-language.md | ASSUMED — not yet mined

### 1. What they urgently want
| # | In their words | Type | Source |

### 2. The tired advice
| Cliché | Why it stuck | Where it fails this audience |

### 3. Contrarian angles you can defend
| # | Angle | True for / not for | Receipt | Best objection → your answer |

### 4. The five series
[one block per series]

### 5. Launch first: [series] — because …

**Receipts to capture to unlock more:** …
**Next:** hook-lab or script-writer on episode 1 of the lead series.
```
