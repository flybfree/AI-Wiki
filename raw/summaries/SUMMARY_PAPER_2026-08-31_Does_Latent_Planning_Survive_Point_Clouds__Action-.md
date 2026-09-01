---
title: Does Latent Planning Survive Point Clouds? Action-Conditioned JEPA World Models for Geometric Observations
url: http://arxiv.org/abs/2608.29434v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_20-41-41Z_DoesLatentPlanningSurvivePointClouds_Action_Condit.md
generated_at: 2026-08-31 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether latent planning remains effective when using point clouds instead of images in JEPA world models. It shows that three variants—frozen-encoder, distribution-prior, and action-sensitive—still plan without collapse on geometric observations.

## Key Takeaways
- The distribution-prior model matches its image counterpart across benchmarks despite only changing the observation type.
- Action-sensitive planning improves most when many points move, indicating attention to few moving points stabilizes predictions.
- Geometry can be used as a goal interface by constructing the latent target from current and target latents without loss of success.

## Context
Point clouds are sparse and self‑occluded, making them challenging for deep models that rely on rich visual cues. This work demonstrates that 3D geometry can serve as an effective supervision signal when combined with latent planning.

## Implications
These results suggest that geometric priors can enhance robustness in autonomous systems where image data is unavailable or noisy. Practitioners may integrate point‑cloud based world models to improve performance without sacrificing goal alignment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29434v1)
