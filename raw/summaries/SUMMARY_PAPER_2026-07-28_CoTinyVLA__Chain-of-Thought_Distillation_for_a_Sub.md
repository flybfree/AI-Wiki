---
title: CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model
url: http://arxiv.org/abs/2607.25487v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_09-24-17Z_CoTinyVLA_Chain_of_ThoughtDistillationforaSub_Bill.md
generated_at: 2026-07-28 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CoTinyVLA, a vision-language-action model that operates within the sub‑billion‑parameter budget of embedded robots while achieving competitive performance on the LIBERO‑Plus robustness benchmark. By replacing larger backbones with structured supervision and efficient data augmentation, CoTinyVLA reaches 90.8% Spatial accuracy and outperforms all seven‑billion‑parameter baselines across four evaluation suites.

## Key Takeaways
- The model uses a Qwen3.5‑0.8B backbone and a 0.9B action head to keep GPU memory low while still delivering high scores.
- Structured supervision, including hierarchical chain‑of‑thought distillation and paraphrase augmentation, enables the small model to surpass larger baselines on all four task suites.
- The episode‑level Plan is identified as load‑bearing; its replacement reduces success by 40–45 points, highlighting the importance of proper planning in inference.

## Context
Embedded robotics demands lightweight models that can handle noisy or perturbed tasks without exceeding memory limits. Traditional approaches rely on massive parameter counts, which are impractical for real‑time deployment. CoTinyVLA demonstrates that structured supervision and clever augmentation can compensate for size constraints, opening the door to affordable, robust vision‑language‑action systems.

## Implications
For robot developers, this work shows a path toward deploying high‑performing VLA agents on resource‑constrained hardware without sacrificing accuracy. Practitioners can adopt similar distillation strategies to shrink model footprints while preserving performance, accelerating innovation in affordable robotic assistants and autonomous navigation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25487v1)
