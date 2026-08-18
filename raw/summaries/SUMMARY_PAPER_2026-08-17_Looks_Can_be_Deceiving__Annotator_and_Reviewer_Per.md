---
title: Looks Can be Deceiving: Annotator and Reviewer Performance Across Imagery Sources in Crowd-Sourced Aerial Damage Assessment
url: http://arxiv.org/abs/2608.14942v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_23-43-35Z_LooksCanbeDeceiving_AnnotatorandReviewerPerformanc.md
generated_at: 2026-08-17 21:41
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how annotator and reviewer performance differ across drone, crewed aviation, and satellite imagery in a post‑disaster building damage dataset spanning nine disasters. It finds that higher‑resolution sources generate more revisions by the final committee than lower‑resolution ones, and that even after a single review many labels remain disputed.

## Key Takeaways
- The revision rate climbs sharply from crewed aviation (25.27%) to satellite imagery (36.95%), indicating that finer visual detail drives more corrections.
- A single reviewer reduces but does not eliminate disagreement, leaving 6.85% of drone labels, 14.05% of crewed aviation labels, and 20.86% of satellite labels to be revised later.
- These patterns suggest that uniform review allocation is inefficient for multi‑source datasets, especially when lower‑resolution imagery carries higher residual uncertainty.

## Context
Crowd‑sourced remote sensing labeling remains a bottleneck in large‑scale disaster response systems, where allocating human effort across heterogeneous image sources is rarely optimized. This study contributes empirical evidence that resolution alone shapes the volume of quality‑control work needed, informing resource planning for AI training pipelines.

## Implications
Practitioners should adopt adaptive task assignment that matches reviewer capacity to source complexity and consider budgeting more labor for lower‑resolution imagery. Such adjustments can reduce annotation costs and improve dataset consistency, supporting better performance of AI models trained on multi‑source aerial data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14942v1)
