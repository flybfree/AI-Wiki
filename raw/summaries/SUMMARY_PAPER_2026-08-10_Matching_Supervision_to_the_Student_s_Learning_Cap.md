---
title: Matching Supervision to the Student's Learning Capacity: A Unified Framework for On-Policy Self-Distillation
url: http://arxiv.org/abs/2608.08176v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_15-13-07Z_MatchingSupervisiontotheStudent_sLearningCapacity_.md
generated_at: 2026-08-10 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Unified On-Policy Self-Distillation (USD) which merges two optimization variables—token selection and privileged information adjustment—into a single framework that matches supervision to the student's learning capacity. It formalizes a constrained maximization of teacher-student divergence with a budget on learning difficulty, and proposes an online Lagrangian solver USD that yields a dual variable governing both decisions.

## Key Takeaways
- The unified model treats token weighting and privileged information adjustment as coupled variables rather than independent choices.
- A single dual variable simultaneously sets the threshold for which tokens are learned from and the direction of teacher guidance, optimizing overall divergence within a learning capacity budget.
- USD outperforms existing OPSD baselines across multiple model scales and reasoning benchmarks.

## Context
Current self-distillation methods often treat token selection and information adjustment separately, leading to suboptimal supervision that ignores how much difficulty a student can handle. This limitation hampers progress in scaling reasoning abilities of large language models.

## Implications
USD offers a principled way to align teacher feedback with student capacity, enabling more efficient training pipelines. Practitioners can adopt the unified framework to improve model performance without increasing computational overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08176v1)
