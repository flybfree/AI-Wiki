---
title: Optimal Self-Distillation for Rectified Flow via Linear Probing
url: http://arxiv.org/abs/2607.14947v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_12-57-00Z_OptimalSelf_DistillationforRectifiedFlowviaLinearP.md
generated_at: 2026-07-23 23:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper studies optimal self-distillation for rectified flow and proves that a student trained on a mixture of true velocity fields can improve the teacher’s risk under certain conditions. It derives an exact affine path identity, finds a closed‑form mixing coefficient that depends on the sign of regularization error, and shows strict improvement in integrated velocity risk when the teacher risk is nonstationary along the ridge path.

## Key Takeaways
- The optimal mixing coefficient follows a simple sign rule: positive values correct under‑regularized teachers while negative values correct over‑regularized ones.
- An exact affine path identity links the student’s loss to the teacher’s regularization path, allowing closed‑form computation of the best mixture weight without grid search.
- One‑shot generalized cross‑validation and validation tuning are provided that avoid repeated refitting and improve velocity estimation for continuous‑time and finite‑step generation.

## Context
Self‑distillation is a promising technique for enhancing generative models by letting them learn from their own outputs. For rectified flow, which interpolates between true and teacher velocities, the standard approach of pure distillation may be suboptimal because the teacher’s risk can vary along its regularization path.

## Implications
This result gives practitioners a principled way to choose mixing weights for student‑teacher mixtures, reducing computational cost while boosting model performance. The improvement in velocity risk translates into clearer flow generation and fewer artifacts, which is valuable for applications such as medical imaging and autonomous vehicle simulation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.14947v1)
