---
title: VISTA: Verifier-Informed Student-to-Teacher Adaptation for On-Policy Self-Distillation
url: http://arxiv.org/abs/2608.28306v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_13-10-34Z_VISTA_Verifier_InformedStudent_to_TeacherAdaptatio.md
generated_at: 2026-08-30 20:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces VISTA, a method that adapts the teacher in on‑policy self‑distillation by using outcome‑verified rollouts to guide adaptation toward the student distribution while preserving the standard OPSD update. Experiments on AIME24, AIME25, and HMMT25 show VISTA outperforms OPSD with gains of 0.6, 0.7, and 2.1 points at model sizes 1.7B, 4B, and 8B respectively.

## Key Takeaways
- VISTA restricts teacher adaptation to the top‑k positions with the largest teacher‑student KL divergence within each verified rollout.
- The method reuses OPSD’s rollout and loss function, adding no extra sampling or reward objective.
- VISTA achieves the highest Avg@12 scores across all model scales tested.

## Context
On‑policy self‑distillation aims to improve reasoning by leveraging teacher feedback but often assumes a fixed teacher distribution. This assumption can mislead students when teacher outputs are not aligned with valid reasoning paths, highlighting a gap in current adaptation strategies for large language models.

## Implications
VISTA demonstrates that student‑driven teacher alignment can yield significant gains without altering the core OPSD pipeline. Practitioners may adopt this approach to fine‑tune teacher responses dynamically, enhancing model performance across competitive benchmarks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28306v1)
