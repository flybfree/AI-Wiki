---
title: MiNO: Cotangent-bundle propagator learning for PDEs
url: http://arxiv.org/abs/2608.15187v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_12-02-03Z_MiNO_Cotangent_bundlepropagatorlearningforPDEs.md
generated_at: 2026-08-17 21:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MiNO, a neural network that learns the propagator of partial differential equations rather than their solution fields. By using the eikonal equation for phase and transport equation for amplitude, MiNO recovers solutions via an oscillatory integral with sharp fronts and caustics tied to propagation geometry. Experiments on discontinuous‑advection benchmarks show MiNO reaches a theoretical accuracy limit after 10 000 steps, outperforming physics‑informed neural networks.

## Key Takeaways
- MiNO learns the smooth propagator that generates nonsmooth fields, allowing singularities to be captured by propagation geometry instead of pointwise reconstruction.  
- The learned canonical relation is validated through small residuals that certify more than the reconstructed field and isolate trainable error from frequency‑truncation tails.  
- On a matched‑budget discontinuous advection problem MiNO stops improving within 10 000 steps, matching the closed‑form accuracy limit, whereas competing methods stagnate.

## Context
This work advances AI for PDEs by focusing on geometric objects that drive evolution, complementing existing approaches that target solution fields. It demonstrates how neural operators can be guided to learn canonical relations, offering a path toward more robust and interpretable deep learning models in scientific computing.

## Implications
MiNO provides a framework for training generators that handle unseen initial conditions without retraining, reducing computational overhead. Practitioners can leverage this method to achieve near‑optimal accuracy on complex PDE problems where pointwise errors are insufficient, opening new possibilities for automated simulation design and optimization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15187v1)
