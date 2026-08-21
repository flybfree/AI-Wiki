---
title: DeltaMomentum: A Key-Value based Anisotropic Momentum Update via Delta Rule
url: http://arxiv.org/abs/2608.19491v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-19_23-04-12Z_DeltaMomentum_AKey_ValuebasedAnisotropicMomentumUp.md
generated_at: 2026-08-20 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
DeltaMomentum integrates a direction‑aware delta rule into the momentum update, allowing each gradient direction to be forgotten at a rate proportional to its query frequency. The method is validated as a proper exponential moving average and achieves faster clearance of stale directions than standard EMA under both fixed and drifting optima.

## Key Takeaways
- The gradient of a linear layer splits into key (input) and value (output error), enabling direction‑aware forgetting via the canonical delta rule, which directly ties forgetting rate to query frequency.  
- Momentum updates remain valid, apply curvature correction without matrix inversion, and clear stale directions faster than EMA under both fixed and drifting optima.  
- DeltaMomentum adds only 22–25 % of a gated‑MLP linear cost to compute.

## Context
Modern optimizers treat momentum as a uniform exponential moving average, which cannot adapt to the anisotropic query patterns of deep networks; this limits efficiency in large‑scale training.

## Implications
DeltaMomentum provides a drop‑in replacement that reduces training steps and improves convergence across models, offering practitioners a lightweight way to handle direction‑specific forgetting without extra memory. The method is especially effective in fineWeb‑Edu pretraining and scales to billions of parameters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19491v1)
