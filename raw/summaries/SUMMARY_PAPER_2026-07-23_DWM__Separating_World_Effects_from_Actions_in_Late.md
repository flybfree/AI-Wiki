---
title: DWM: Separating World Effects from Actions in Latent World Models
url: http://arxiv.org/abs/2607.18715v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_05-13-26Z_DWM_SeparatingWorldEffectsfromActionsinLatentWorld.md
generated_at: 2026-07-23 23:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DWM (Decomposed World Model), a supervision‑level framework that separates the latent transition into an action‑invariant component and an action‑driven component, thereby improving model‑based control. By adding an auxiliary head regularized with a contrastive objective and coupling it orthogonally to the main predictor, DWM achieves an explicit additive decomposition without changing architecture or inference pipeline. Experiments on W‑variants of PushT‑W, Reacher‑W, and TwoRoom‑W show that DWM matches strong baselines on flat versions and improves CEM planning success by 13.1%.

## Key Takeaways
- Current formulations fuse action‑driven and world‑effect components into a single target, entangling them inside the latent transition.
- DWM uses an auxiliary head regularized to be action‑invariant via a contrastive objective while coupling it orthogonally to the original predictor.
- This decomposition yields an explicit additive split of the predicted transition, leading to measurable gains in planning success.

## Context
In model‑based control, latent world models are essential for generating reliable policies, yet existing approaches treat all state changes as a monolithic target. This entanglement can obscure true causes and limit transferability across similar environments. DWM offers a principled way to disentangle these sources, which could be applied broadly beyond the specific benchmarks.

## Implications
This approach enhances robustness and transferability of learned dynamics, benefiting both research and industry that develop model‑based agents operating in dynamic real‑world settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18715v1)
