---
title: REOPD: Reliability-Adaptive Reward Extrapolation for On-Policy Distillation
url: http://arxiv.org/abs/2608.11698v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_06-15-33Z_REOPD_Reliability_AdaptiveRewardExtrapolationforOn.md
generated_at: 2026-08-12 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces REOPD, a reliability‑adaptive reward extrapolation method for on‑policy distillation that adapts token‑level coefficients based on teacher‑reference compatibility and batch budgets. It avoids the use of a single global λ, preventing reward hacking and training instability while preserving alignment with the teacher. The main finding is that REOPD delivers fine‑grained adaptation without requiring extra components such as verifiers or value models.

## Key Takeaways
- REOPD uses a token‑wise coefficient λ_{b,t}=1+γ_b q_t to preserve alignment while selectively extrapolating along reliable teacher‑reference directions.  
- It eliminates the need for a global λ, thus removing reward hacking and instability caused by extreme peaks in the implicit reward.  
- The method requires no verifier, reward model, or extra rollout beyond standard OPD.

## Context
On‑policy distillation aims to train efficient student models from teacher outputs using token‑level supervision. Traditional reward extrapolation methods rely on coarse‑grained scaling that can misalign with domain‑specific reliability, limiting performance across varied settings.

## Implications
This approach enables more robust training across diverse domains and teachers without costly parameter sweeps. Practitioners can adopt REOPD directly in existing OPD pipelines to improve generalization and reduce the risk of reward gaming.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11698v1)
