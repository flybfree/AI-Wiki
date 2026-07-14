---
title: "Summary: Learning Action Priors for Cross-embodiment Robot Manipulation"
url: http://arxiv.org/abs/2606.26095v1
type: paper-summary
date: 2026-06-24
source_paper: 2026-06-24_17-59-56Z_LearningActionPriorsforCross_embodimentRobotManipu.md
generated_at: 2026-06-24 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a two-stage training framework that equips the action module of Vision-Language-Action models with motion priors before cross-embodiment VLA alignment. By learning temporal structure from unconditioned trajectories in Stage 1, the model transfers this prior to downstream tasks, resulting in faster convergence and higher success rates. Experiments across 13 tasks show improved performance especially on data-scarce real-world settings.

## Key Takeaways
- The action module is pretrained with a flow-matching encoder-decoder that learns temporal motion without visual or language input, establishing a cross‑embodiment prior.
- This learned prior is reused in VLA training via decoder reuse and latent distillation, aligning visual‑language features with the action embedding space while preserving end‑to‑end refinement.
- The encoder compresses state‑action histories into a single token at negligible cost, enabling history‑aware modeling.

## Context
Vision-Language-Action models rely on a Vision-Language backbone to provide rich visual and linguistic priors but leave motion planning to the action module, which often lacks an explicit prior. This gap is especially problematic in cross‑embodiment settings where each robot has unique dynamics. By decoupling motion learning from multimodal alignment, the proposed approach addresses this limitation.

## Implications
The method offers a scalable way to bootstrap action policies with generic temporal priors, reducing reliance on task‑specific data and accelerating deployment. Practitioners can leverage the compact history compressor to integrate long histories without heavy computation, making cross‑embodiment manipulation more robust and efficient.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.26095v1)
