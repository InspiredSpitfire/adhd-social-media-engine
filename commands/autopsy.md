---
name: autopsy
description: Diagnose one underperforming post in a fixed order and get three rewritten versions to test.
---

Run the `post-autopsy` skill on the post the user provides. If they have not pasted it yet, ask once for: platform, format, exact hook, script or caption, what was on screen in the first 3 seconds, and the results. Compute the baseline from `receipts/post-log.csv` when it has enough rows; otherwise use the baseline they state and label it as stated.
