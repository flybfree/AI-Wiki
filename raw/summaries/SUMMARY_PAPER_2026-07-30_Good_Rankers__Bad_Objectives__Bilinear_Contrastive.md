---
title: Good Rankers, Bad Objectives: Bilinear Contrastive Critics under Expressive Policy Search
url: http://arxiv.org/abs/2607.27422v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_19-43-40Z_GoodRankers_BadObjectives_BilinearContrastiveCriti.md
generated_at: 2026-07-30 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates bilinear contrastive critics that rank actions in AI environments and shows that their unbounded scores can be misled by large embedding norms, causing them to select off‑support actions. It demonstrates that cosine bounding and hybrid approaches still suffer from similar failures, while a value‑calibrated scalar is needed for reliable action selection.

## Key Takeaways
- Unbounded bilinear scores let large embedding norms inflate values of unsupported actions, leading to regret even after cosine normalization.
- The loss in ordering stems primarily from cosine training objectives that do not preserve true value order at inference time.
- Realized costs vary across tasks: single‑step selection works well on PointMaze and the exact‑Q* toy task, but nulls are observed where self‑correction is possible.

## Context
This work addresses a growing trend in reinforcement learning where contrastive ranking objectives replace explicit value functions for action selection. While such critics improve compatibility with existing models, they often introduce hidden biases that degrade performance on complex navigation and manipulation tasks.

## Implications
Practitioners must move beyond simple similarity‑based rankers to incorporate calibrated scalar values when guiding agents through decision loops. Ignoring norm drift can lead to systematic off‑support actions, increasing safety risks in real‑world robotics applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27422v1)
