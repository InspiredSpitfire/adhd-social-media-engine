---
name: hooks
description: 30 linted, scored hooks for one post, with the best 5 picked and explained.
argument-hint: <topic of the post>
---

Run the `hook-lab` skill for this topic: $ARGUMENTS

If no topic was given, ask for it.

Take platform, audience, voice, and proof from the `receipts/` workspace. Ask only for the desired reaction (save, share, comment, follow, or click) and the creator's point of view on this topic if they were not given. Run the lint script and fix every FAIL before presenting anything.
