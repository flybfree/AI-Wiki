---
title: SR-OPSD: Self-Referenced On-Policy Self-Distillation
url: http://arxiv.org/abs/2608.09745v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_15-40-07Z_SR_OPSD_Self_ReferencedOn_PolicySelf_Distillation.md
generated_at: 2026-08-10 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Self-Referenced On-Policy Self-Distillation (SR-OPSD), a method that refines on-policy self-distillation by separating the placement of an adaptive target from its projection geometry using Rényi divergence. Experiments across scientific, mathematical and coding tasks show SR-OPSD attains state-of-the-art or competitive performance.

## Key Takeaways
- The effective distillation target is modeled as a geometric interpolation between the self-teacher policy and a reference policy at fixed student contexts.
- A token-level variational characterization identifies this interpolation coefficient as controlling which adaptive target is used.
- Rényi divergence generalizes the projection geometry, allowing sensitivity to token‑level density ratios.

## Context
On-policy self-distillation aims to turn sparse reward signals into dense supervision for language models. SR-OPSD addresses instability caused by co‑evolving teacher policies and moving targets, offering a principled way to align projections with target distributions.

## Implications
SR-OPSD provides practitioners with a flexible framework that can be integrated into existing RL pipelines without requiring extensive hyperparameter tuning. Its separation of target placement from projection geometry may inspire future work on adaptive curriculum design for large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09745v1)
