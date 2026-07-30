---
title: Try Again, Don't Look Back: Blind Resampling Outperforms Self-Repair in Small Code Models
url: http://arxiv.org/abs/2607.26117v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_16-58-27Z_TryAgain_Don_tLookBack_BlindResamplingOutperformsS.md
generated_at: 2026-07-29 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why self-repair in code agents is often compared to a no‑retry baseline and finds that blind resampling outperforms many feedback‑based methods. Experiments on MBPP+ at 1.5B, 3B, and 7B models show blind resampling uses far fewer tokens while still yielding the best performance.

## Key Takeaways
- Blind resampling consumes 2.5–5.5 times fewer tokens than self‑repair with execution feedback yet matches or exceeds it in accuracy.
- The cost of conditioning on a failed attempt is 6.1 points at 1.5B (p=0.006), indicating strong anchoring to the previous program.
- Retrieval of other tasks changes results only by up to ±3.5 points, showing the effect is localized to self‑conditioning.

## Context
Code agents rely on feedback loops to improve performance, but current baselines ignore the value of extra attempts. This study reveals that simply reusing a failed output can be more effective than providing detailed execution logs without incurring high token costs.

## Implications
For practitioners, blind resampling offers a low‑cost alternative to self‑repair that does not require costly feedback loops. The finding suggests future model design should prioritize minimizing initial attempt errors rather than relying on post‑mortem corrections.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26117v1)
