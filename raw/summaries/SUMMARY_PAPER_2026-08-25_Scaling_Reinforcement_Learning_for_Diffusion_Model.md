---
title: Scaling Reinforcement Learning for Diffusion Models via Velocity Matching
url: http://arxiv.org/abs/2608.23664v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_17-13-43Z_ScalingReinforcementLearningforDiffusionModelsviaV.md
generated_at: 2026-08-25 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces reward‑based velocity matching (RVM), a method for fine‑tuning diffusion models that updates the model’s velocity field directly using preference rewards. By avoiding likelihood calculations, RVM achieves comparable or better performance than existing trajectory‑based approaches while requiring far less computational effort.

## Key Takeaways
- RVM updates the velocity field instead of constructing trajectory likelihoods, eliminating the need for expensive likelihood estimation.
- The method can recover recent fine‑tuning techniques such as RAM and DiffusionNFT as special cases when anchor terms are set appropriately.
- For video generation, a dynamic‑tracking reward that emphasizes motion improves both visual quality and VBench scores.

## Context
Diffusion models generate high‑quality images but lack tractable likelihoods for reward optimization. Traditional fine‑tuning methods rely on approximating these likelihoods, which adds computational overhead and algorithmic complexity. This paper shows that a simpler velocity‑based approach can match or surpass those methods.

## Implications
RVM offers practitioners a scalable way to align diffusion models with human preferences without costly likelihood approximations. The insight that reward design matters more than loss variants could simplify future fine‑tuning pipelines, benefiting both research and industry applications in image and video generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23664v1)
