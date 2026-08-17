---
title: Resource-Adaptive Primal-Dual Learning for One-Warehouse Multi-Store Systems with Censored Demand
url: http://arxiv.org/abs/2608.14096v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_08-56-35Z_Resource_AdaptivePrimal_DualLearningforOne_Warehou.md
generated_at: 2026-08-16 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a resource‑adaptive primal‑dual learning algorithm for one‑warehouse multi‑store inventory allocation where demand is censored and resources deplete over time. It shows that by tracking the primal‑dual resolving path with censored sales, the method achieves logarithmic expected regret, outperforming square‑root order guarantees of prior approaches.

## Key Takeaways
- The algorithm continuously updates the target store allocations based on the current remaining resource rate rather than a fixed initial target. 
- Censored demand provides gradient information that guides dual variable adjustments throughout the horizon. 
- The analysis combines expected‑sales geometry with a moving‑target argument to guarantee logarithmic regret.

## Context
This work addresses online inventory allocation under resource depletion, a problem where the shared stock shrinks as sales are realized. Existing methods rely on static targets calibrated at the start, which become suboptimal when demand patterns shift or resources run low. The new framework adapts these targets dynamically, reflecting real‑time state changes.

## Implications
For practitioners managing multi‑store inventory with limited replenishment, this algorithm offers a more robust and efficient allocation strategy that reduces waste and improves service levels. Its logarithmic regret bound suggests scalability to longer planning horizons, encouraging adoption in supply‑chain optimization systems where resources are scarce and stochastic.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14096v1)
