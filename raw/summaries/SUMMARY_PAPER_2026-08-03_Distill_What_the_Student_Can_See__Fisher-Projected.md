---
title: Distill What the Student Can See: Fisher-Projected On-Policy Distillation for Vision-Language Models
url: http://arxiv.org/abs/2608.01263v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_14-16-14Z_DistillWhattheStudentCanSee_Fisher_ProjectedOn_Pol.md
generated_at: 2026-08-03 23:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Fisher‑Projected On‑Policy Distillation (FP‑OPD) to improve vision‑language model distillation by aligning student targets with locally realizable teacher corrections. It replaces the full teacher distribution with a capacity‑aware target estimated via visual tangent space and improves multimodal benchmarks.

## Key Takeaways
- FP‑OPD projects the centered teacher–student log‑probability gap onto the student’s Fisher metric in the local visual tangent space, yielding a more realistic target than the complete teacher distribution.
- The method uses continuous visual perturbations to estimate the student's local visual tangent space and optimizes with full‑vocabulary reverse KL on student trajectories.
- In 8B‑to‑2B distillation, FP‑OPD raises average scores by 2.77 points over pretrained students and by 1.60 points over standard OPD across seven benchmarks.

## Context
Vision‑language reasoning models face a mismatch between teacher knowledge and the limited visual capacity of compact student networks. Traditional on‑policy distillation assumes a uniform target, which can misalign when teacher corrections depend on fine visual distinctions. This work addresses that limitation by focusing on locally realizable adjustments.

## Implications
Practitioners can adopt FP‑OPD to create more efficient, capacity‑aware training objectives without sacrificing performance. The approach offers a scalable path for distilling large vision‑language models into smaller ones while preserving multimodal reasoning abilities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01263v1)
