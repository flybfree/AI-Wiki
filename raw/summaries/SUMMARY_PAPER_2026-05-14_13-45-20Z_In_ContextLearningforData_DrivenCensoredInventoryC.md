---

title: "Summary: In-Context Learning for Data-Driven Censored Inventory Control"
url: http://arxiv.org/abs/2605.14840v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-14_13-45-20Z_In_ContextLearningforData_DrivenCensoredInventoryC.md
generated_at: "2026-06-11 10:40"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-05-14 13-45-20Z In Contextlearningfordata Drivencensoredinventoryc


## Summary
This paper addresses inventory control under decision‑dependent censoring by proposing in‑context generative posterior sampling (ICGPS). The method learns latent demand completions offline and uses them online to generate optimal orders, achieving sublinear Bayesian regret that matches the best Thompson sampling benchmark plus a small deployment penalty. Experiments on both synthetic R‑Newsvendor problems and the real SuperStore dataset show that ICGPS outperforms myopic and UCB baselines and remains robust to prior mismatch and distribution shift.

## Key Takeaways
- The proposed ICGPS framework learns demand completions offline and uses them in an autoregressive generation process, yielding sublinear Bayesian regret for censored inventory control.  
- Theoretical analysis links the online completion mismatch to the offline censored predictive mismatch, showing that good offline predictions translate into strong online performance.  
- Benchmark results demonstrate that ICGPS matches correctly specified Thompson sampling while being robust to prior mismatch and heavy censoring.

## Context
The work advances AI‑driven decision making by integrating generative modeling with bandit‑style feedback in a real‑time operational setting, highlighting how offline meta‑training can support online inference without explicit retraining. This aligns with broader trends toward leveraging large language model techniques for sequential decision problems.

## Implications
For inventory and supply chain practitioners, ICGPS offers a practical way to handle noisy demand data while maintaining low regret, reducing the need for costly re‑optimizations as conditions shift. The approach can be adapted to other domains where censored feedback is common, such as medical testing or personalized recommendation systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.14840v1)
