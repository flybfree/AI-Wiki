---
title: DOPD: Dual On-policy Distillation
url: http://arxiv.org/abs/2606.30626v1
type: paper-summary
date: 2026-06-30
source_paper: 2026-06-29_17-55-53Z_DOPD_DualOn_policyDistillation.md
generated_at: 2026-06-30 01:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DOPD, a dual on-policy distillation method that mitigates privilege illusion by dynamically routing token-level supervision between teacher and student based on advantage gaps. It achieves higher capacity transfer than vanilla OPD in both LLM and VLM tasks. Experiments show improved performance, stability, robustness, continual learning, and out-of-distribution handling.

## Key Takeaways
- The method identifies a "privilege illusion" where supervision conflates capability gap with information asymmetry, leading to suboptimal training.
- Supervision is dynamically assigned to teacher or student depending on their advantage gap and relative probabilities, providing varied strength and strategy per token.
- This dynamic routing yields higher performance across LLM and VLM benchmarks compared to existing distillation baselines.

## Context
On-policy distillation aims to transfer model knowledge efficiently by using teacher-student trajectories. Token-level supervision is valuable but limited because only a few tokens encode crucial capabilities, causing uneven learning signals. The field seeks solutions that preserve privacy while maximizing utility.

## Implications
For practitioners, DOPD offers a practical framework to enhance model training without extra data, reducing reliance on large labeled datasets. It also improves robustness and continual learning, making it valuable for deploying models in production where stability is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.30626v1)
