---
title: ReOrder-OPD:Reliability-Aware Prompt Ordering for On-Policy Distillation
url: http://arxiv.org/abs/2608.10905v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_13-27-56Z_ReOrder_OPD_Reliability_AwarePromptOrderingforOn_P.md
generated_at: 2026-08-11 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ReOrder-OPD, a method that orders on‑policy distillation prompts by their teacher continuation reliability. By replacing unreliable local confidence signals with a global proxy derived from ROUGE‑5 F1 scores between student rollouts and verifier‑correct teacher trajectories, the authors achieve higher gains across multiple model settings.

## Key Takeaways
- The paper defines prompt‑level teacher continuation reliability R as the average probability that a teacher can complete a correct answer from any student prefix induced by the current student.  
- High‑R prompts produce larger OPD improvements and descending‑R training outperforms both random and ascending orders on fixed prompt pools.  
- Using ROUGE‑5 F1 between independent student rollouts and verifier‑correct teacher trajectories provides a reliable proxy that separates coarse reliability levels across ten equal‑frequency bins.

## Context
On‑policy distillation relies heavily on token‑level supervision, yet many existing weighting schemes treat local confidence as an isolated signal. This can mask the true ability of a teacher to continue from a student prefix, leading to suboptimal training. The need for a more robust reliability metric is especially acute in large language models where prompt ordering directly influences learning efficiency.

## Implications
For practitioners, ReOrder‑OPD offers a simple yet effective way to prioritize prompts that maximize distillation gains without requiring costly teacher continuations. In industry settings, this can reduce compute costs while improving model performance across diverse tasks such as mathematics and code generation. The approach also highlights the importance of trajectory‑level supervision when combined with prompt ordering.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10905v1)
