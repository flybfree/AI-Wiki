---
title: Normalizing Trajectory Models
url: http://arxiv.org/abs/2605.08078v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-08_17-57-14Z_NormalizingTrajectoryModels.md
generated_at: 2026-06-11 10:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Normalizing Trajectory Models, a framework that treats each reverse step of diffusion as an invertible normalizing flow with exact likelihood training. The model generates high-quality images in four steps and maintains the full likelihood over the trajectory.

## Key Takeaways
- NTM replaces distillation or adversarial objectives with exact likelihood training on conditional normalizing flows.
- The architecture uses shallow invertible blocks per step combined with a deep parallel predictor across the whole trajectory.
- Self‑distillation enables a lightweight denoiser trained on the model’s own score to produce high‑quality samples in four steps.

## Context
Diffusion models rely on many fine‑grained Gaussian denoising steps, which become impractical when compressed into few coarse transitions. Existing methods often abandon likelihood frameworks for simplicity or speed. NTM restores the exact likelihood while enabling efficient generation.

## Implications
By preserving likelihood, NTM offers a principled baseline for evaluating diffusion quality and can guide future model improvements. Practitioners may adopt NTM’s architecture to balance performance with computational cost in real‑time applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.08078v1)
