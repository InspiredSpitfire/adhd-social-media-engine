# ADHD Social Media Engine (Claude Code plugin)

Proof-first content system for one-person social accounts. Product name: **ADHD Social Media Engine** (named by Inspired Spitfire 2026-09-20; briefly `receipts-social`, then `social-media-expert`). The daily-routing feature is called **brain-mode** — her name, do not rename. "Receipts" is the name of the METHOD inside it (Receipts Rule, Proof Locker, `receipts/` workspace, `receipts-editor` agent) and stays. Status: v0.2.0 (2026-09-21; v0.1.0 built 2026-09-20). First live run on the owner's own account started 2026-09-20; no results claimed yet.

## Layout
- `RULES.md` — the shared rulebook every skill reads (workspace, Receipts Rule, evidence labels). Change rules here, not in ten places.
- `skills/` — the 11 skills (the product). `brain-mode` carries Inspired Spitfire's four-state Brain-State System (Feral, Froggy, Foggy, Fried): always four, never renamed, definitions come from `she-rebels-brand-kit`, which is authoritative. Three carry their own `scripts/`: hook-lab, content-calendar, performance-review.
- `agents/receipts-editor.md` — independent PASS / NEEDS REVISION reviewer.
- `commands/` — `/start`, `/brain`, `/hooks`, `/autopsy`, `/weekly-review`.
- `templates/` — blank workspace files copied by account-setup.
- `examples/` — fixtures with planted defects; the scripts must keep catching them.
- `scripts/check_plugin.py` — component reachability check.

## Rules
- Retention structure (`script-writer` renewals, loop ledger; RULES §7 open-loops-vs-bait) is original wording, added 2026-09-21. No third-party images, wording, templates, timings, or example lines go into this product. Keep it that way.
- The product's promise is "nothing invented". Never add hardcoded algorithm claims, benchmark numbers, or platform specs to a skill; skills tell the model to verify at run time.
- Skill edits are product changes: test with `~/dev/skill-evals` before merging behaviour changes.
- After any change run: `python3 scripts/check_plugin.py && claude plugin validate .` and the three example commands in README "Verify".
- Publishing, pushing to a public repo, or listing for sale is an outward action: needs explicit go.
- Sales page, launch posts, and README marketing copy are Inspired Spitfire territory: load `she-rebels-brand-kit` before writing them. The skills themselves stay brand-neutral; buyers bring their own voice.
- Public author name is "Inspired Spitfire".
- This is an Inspired Spitfire / She Rebels product, not brand-neutral: it ships her Brain-State IP. Skill internals stay plain and usable in any creator's voice; sales copy follows the brand kit. Never label the dopamine triggers "NICU" in buyer-facing text. No medical claims anywhere.
