---
title: Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress
url: http://arxiv.org/abs/2608.19408v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-19_19-45-32Z_BeyondImitation_FilteringOn_PolicyDistillationbyRe.md
generated_at: 2026-08-20 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses a limitation in on-policy distillation where teacher rewards may not align with true reasoning progress, leading to suboptimal student policies. The authors introduce R2-OPD, which filters out contradictory supervision by comparing teacher-derived and progress-estimated rankings of reasoning spans. Experiments show consistent gains over standard OPD, especially for tasks requiring logical reasoning.

## Key Takeaways
- Teacher rewards often misrepresent genuine reasoning advancement because they prioritize output similarity rather than logical correctness, causing the distillation process to suppress valuable reasoning steps that deviate from the teacher's answer.
- The method builds two within‑trajectory rankings—one based on teacher feedback and another estimated independently—and suppresses distillation rewards only when these rankings conflict, thereby preserving alignment with actual progress.
- R2-OPD yields measurable improvements in reasoning performance across benchmarks compared to baseline OPD, demonstrating that filtering misaligned supervision can enhance model learning.

## Context
Current post‑training techniques rely heavily on teacher feedback as a proxy for desirable behavior, yet this assumption breaks down when the teacher’s knowledge is outdated or its output style differs from what truly advances reasoning. This paper highlights a gap between surface similarity and underlying cognitive improvement, prompting a need for more nuanced reward mechanisms.

## Implications
For practitioners developing large language models, R2-OPD offers a practical way to refine distillation pipelines without retraining the teacher model, reducing computational cost while improving output quality. The approach may become standard in AI research as it directly links supervision to measurable reasoning gains, encouraging better alignment between training signals and desired capabilities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19408v1)
