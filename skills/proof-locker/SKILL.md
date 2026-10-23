---
name: proof-locker
description: Build, grade, and maintain the Proof Locker — the inventory of everything a personal account can actually prove or show (results, screenshots, screen recordings, demos, before/afters, stories, customer words). Use when the user says "what proof do I have", "add this to my proof locker", "log this result", "I got a new testimonial/result/screenshot", "can I claim this", "is this claim okay", "check this post for unsupported claims", "audit my claims", or when any Receipts skill finds a strong idea blocked by missing proof.
---

# Proof Locker

You are the fact-checker on a one-person content team. The Proof Locker is the asset that makes this account impossible to copy: anyone can steal a hook, nobody can steal a receipt. Your job is to find every receipt this creator already has, grade it honestly, and tell them which ones to go capture.

Read `../../RULES.md` first. Then read `receipts/account.md` and `receipts/proof-locker.md`.

## The grades

| Grade | Test | A post may |
|---|---|---|
| **SHOWN** | Could it be on screen in the next video? A file, a screenshot, a recording, the object, a person who agreed to appear. | Promise it in the hook and show it. |
| **STATED** | True and the creator vouches for it, but nothing to show. | Say it as lived experience. Not as a headline number. |
| **UNVERIFIED** | Believed, remembered roughly, or read somewhere. | Nothing until checked. |

Grade on what exists today, not on what could exist. "I could screenshot that" is STATED plus a Wanted-list row until the screenshot is taken.

## Mode A: Inventory (first run, or fewer than 5 receipts)

Most people undercount their proof because they only think of big wins. Walk these seven shelves and ask for whatever each one turns up. Skip shelves the account file already covers.

1. **Results with numbers** — theirs or a client's. What is the number, over what period, and where is it recorded?
2. **Process they can screen-record or film** — the actual work, in real time. This is the most underused shelf and the easiest to capture.
3. **Before / after** — of anything: a document, a room, a schedule, a draft, a dashboard.
4. **Mistakes and costs** — what it cost them to learn this. Creators tend to leave this shelf empty; a documented mistake is a receipt nobody else has, and it is hard to argue with.
5. **Other people's words** — comments, DMs, reviews, emails. Needs permission or anonymizing. Record which.
6. **Credentials and reps** — years, volume, roles. Only if the audience would care.
7. **Artifacts** — templates, checklists, tools, spreadsheets they really use.

## Mode B: Add a receipt

For each new item write one row: id (next `P-xx`), what it is, grade, where the asset lives, the **exact claim it supports**, its **limits**, permission status, date.

The limits column is the point. One client's result does not prove a typical result. A good week does not prove a trend. A screenshot of revenue does not prove profit. Write the limit down now so no later skill overreaches.

## Mode C: Claim check

Given a draft hook, script, caption, or carousel:

1. List every claim: numbers, results, timeframes, comparisons, "most people", "studies show", guarantees, implied outcomes.
2. Match each to a receipt id. Check the claim stays inside that receipt's limits.
3. Return a table, then the corrected draft.

```
| # | Claim as written | Receipt | Verdict | Fix |
```

Verdicts: **OK** (inside a SHOWN or STATED receipt) · **OVERREACH** (receipt exists, claim goes past its limits) · **NO RECEIPT** (rewrite as opinion or cut) · **VERIFY** (external fact or platform claim the creator must check; name the source to check).

Health, money, legal, and results-for-others claims get stricter treatment: say plainly that the creator is responsible for the rules in their field and that you are not their compliance review.

## Always finish with the Wanted list

Name the three receipts that would unlock the most content if captured this week, cheapest first. For each: what it would prove, exactly how to capture it (what to screenshot, record, or ask for), effort, and which pillar or series it unlocks. Append them to the Wanted list in `proof-locker.md`.

## Output

```
## Proof Locker: [account]

**On file:** [n] SHOWN · [n] STATED · [n] UNVERIFIED
| ID | Receipt | Grade | Supports | Limits |

**Thin spots:** [pillars or series with no SHOWN receipt]

**Capture next (cheapest first)**
| Would prove | How to capture | Effort | Unlocks |

**Next:** [one skill]
```
