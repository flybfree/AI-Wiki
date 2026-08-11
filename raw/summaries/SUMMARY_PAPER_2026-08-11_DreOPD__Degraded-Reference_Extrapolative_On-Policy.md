---
title: DreOPD: Degraded-Reference Extrapolative On-Policy Distillation for Flow-matching Models
url: http://arxiv.org/abs/2608.09233v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_07-55-57Z_DreOPD_Degraded_ReferenceExtrapolativeOn_PolicyDis.md
generated_at: 2026-08-11 12:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DreOPD, a degraded-reference extrapolative on-policy distillation method for flow-matching models that combines the stability of OPD with closed-form velocity regression to enable extrapolation. Experiments show DreOPD outperforms both OPD and multi‑task RL baselines while surpassing specialized teachers across most metrics.

## Key Takeaways
- DreOPD converts implicit reward extrapolation into a closed‑form velocity regression, providing stable extrapolative guidance beyond the original training distribution.
- The method uses a mildly degraded reference to create a stronger teacher‑reference contrast, sharpening the extrapolation direction for the student model.
- In both single‑teacher and multi‑teacher settings DreOPD achieves higher average performance than OPD and multi‑task RL baselines.

## Context
Flow‑matching models dominate image generation but struggle with seamless task adaptation due to conflicting downstream objectives. On‑policy distillation offers a way to align tasks without high variance, yet conventional approaches remain imitation‑based. This work bridges that gap by merging extrapolation with stable OPD supervision.

## Implications
DreOPD demonstrates that closed‑form regression can replace stochastic reward estimation in RL pipelines for generative models, reducing training instability. Practitioners can adopt this framework to fine‑tune flow generators on new tasks efficiently, accelerating deployment and improving quality across diverse applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09233v1)
