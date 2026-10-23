---
name: weekly-review
description: The weekly loop — log new results, recompute your baseline, close open experiments, and get next week's tests and posts.
---

Run the weekly Receipts loop, in order:

1. Ask the user to paste this week's post results (or point to an export). Append them to `receipts/post-log.csv` using the `performance-review` skill's logging rules. No new data means stop here and say so.
2. Run the `performance-review` skill. Close any open experiment in `receipts/experiments.md` whose posts now have results, applying its decision rule exactly as written.
3. For any post at or below 0.5× its platform median, offer a `post-autopsy`.
4. Finish with a short list: what to keep doing, what to stop, the experiments for the next two weeks, and the next three posts to make. Keep it to one screen.
