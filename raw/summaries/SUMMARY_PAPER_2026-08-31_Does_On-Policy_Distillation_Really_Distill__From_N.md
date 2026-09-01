---
title: Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement
url: http://arxiv.org/abs/2608.31046v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_16-22-10Z_DoesOn_PolicyDistillationReallyDistill_FromNoisyTe.md
generated_at: 2026-08-31 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates on‑policy distillation (OPD) and shows that teacher supervision introduces noise that does not affect student learning, revealing OPD’s gains come from suppressing low‑log‑probability tokens rather than the noisy scores. It demonstrates that a single fixed negative advantage yields comparable results to teacher‑provided ones. The authors propose On‑Policy Self‑Adaptation (OPSA) as a supervision‑free alternative.

## Key Takeaways
- Teacher supervision is noisy and its prevalence rises with model scale, yet the student policy remains insensitive to this noise.
- The student converges to comparable performance whether noisy or clean teacher scores are used.
- OPD’s improvement originates from focusing on low‑log‑probability tokens, making a fixed negative advantage sufficient.

## Context
On‑policy distillation offers dense token‑level supervision as an alternative to sparse RL rewards, but its reliability is questioned because the teacher operates off‑policy. This study clarifies that the method’s effectiveness stems from simple token suppression rather than complex teacher feedback.

## Implications
For practitioners, OPSA provides a lightweight, teacher‑free way to boost model performance by targeting high‑entropy positions and redistributing probability mass, offering a scalable path beyond noisy distillation. The findings suggest that many RL‑style methods may be unnecessary when token suppression alone suffices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.31046v1)
