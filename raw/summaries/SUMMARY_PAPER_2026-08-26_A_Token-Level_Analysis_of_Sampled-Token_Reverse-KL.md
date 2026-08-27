---
title: A Token-Level Analysis of Sampled-Token Reverse-KL On-Policy Distillation
url: http://arxiv.org/abs/2608.25643v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_11-14-42Z_AToken_LevelAnalysisofSampled_TokenReverse_KLOn_Po.md
generated_at: 2026-08-26 20:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how sampled-token reverse-KL loss in on-policy distillation distributes gradients across tokens, showing that low-probability student tokens dominate the gradient norm and are linked to large teacher-student gaps. It introduces Surprise-aware Reweighting (SuRe) as a lightweight intervention that rebalances this allocation without retraining.

## Key Takeaways
- The per-token K2 estimator gradient magnitude is proportional to both the absolute log-probability gap between teacher and student and a softmax factor that increases when the sampled token is unlikely under the student.
- Low-student-probability tokens contribute disproportionately to the sum of per-token norms, especially those with large teacher-student discrepancies.
- SuRe mitigates this imbalance by applying a bounded weighting rule that amplifies updates for low-probability tokens, improving math metrics on Qwen3 models.

## Context
On-policy distillation aims to transfer knowledge from a frozen teacher to a student model using its own trajectories. Understanding loss allocation is crucial because non-uniform token contributions can degrade performance and make optimization unstable.

## Implications
This insight provides practitioners with a principled way to adjust gradient weighting in distillation, potentially leading to more robust training without complex modifications. It highlights the importance of analyzing loss components beyond aggregate metrics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25643v1)
