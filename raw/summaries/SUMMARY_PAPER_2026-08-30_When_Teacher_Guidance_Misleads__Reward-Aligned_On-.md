---
title: When Teacher Guidance Misleads: Reward-Aligned On-Policy Distillation
url: http://arxiv.org/abs/2608.27960v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_06-05-50Z_WhenTeacherGuidanceMisleads_Reward_AlignedOn_Polic.md
generated_at: 2026-08-30 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Reward‑Aligned On‑Policy Distillation (RA‑OPD), a method that filters teacher‑guided trajectories based on their consistency with outcome rewards to avoid misleading the student model. Experiments on math and code benchmarks show RA‑OPD outperforms standard OPD and other variants, demonstrating improved performance without extra cost.

## Key Takeaways
- The paper proposes filtering out trajectory‑level distillation returns that do not align with the actual outcome reward, thereby removing unreliable teacher guidance.
- RA‑OPD selects only those trajectories whose updates move the student toward correct responses or away from incorrect ones, preserving alignment between distilled signals and rewards.
- On seven math benchmarks and three code benchmarks, RA‑OPD significantly improves model performance compared to baseline OPD methods.

## Context
On‑policy distillation is a growing technique for transferring knowledge from large language models to smaller student models. However, teacher guidance can be inconsistent with the true reward signal, leading to suboptimal learning. This work addresses that gap by introducing a reward‑aware filtering mechanism within the existing OPD framework.

## Implications
RA‑OPD offers practitioners a practical way to enhance model transfer without costly fine‑tuning or extra compute. By ensuring that distillation signals are reward‑aligned, it can lead to more robust and accurate student models in real‑world applications such as automated reasoning and code generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27960v1)
