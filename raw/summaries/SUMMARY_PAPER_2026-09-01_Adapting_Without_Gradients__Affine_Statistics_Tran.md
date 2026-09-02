---
title: Adapting Without Gradients: Affine Statistics Transport and What Its Certificate Can Tell You
url: http://arxiv.org/abs/2609.00374v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_21-07-36Z_AdaptingWithoutGradients_AffineStatisticsTransport.md
generated_at: 2026-09-01 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes CASTER, a gradient‑free adaptation method that transports source class statistics to the target domain using an affine transformation without updating model parameters. Experiments on four backbones and seven datasets show it beats k‑NN on frozen features while using far less memory. The authors also introduce a certificate that predicts whether transport will degrade performance.

## Key Takeaways
- CASTER stores only source class moments in a low‑dimensional subspace, enabling inference‑only adaptation without backward passes or optimizer state.
- On ImageNet‑C with small batches the unconditional affine transport loses 21.2 top‑1 points, highlighting that transport reliability depends on batch size and class distribution.
- The empirical residual‑to‑margin certificate identifies transports losing more than ten points as unsafe, allowing gating to recover a net gain of about one point.

## Context
Model adaptation is crucial for deploying models in resource‑constrained or inference‑only environments where retraining or gradient updates are impossible. This work addresses the gap between theoretical transport methods and practical deployment constraints by providing a lightweight, memory‑efficient alternative that does not rely on frozen BatchNorm layers.

## Implications
For industry practitioners, CASTER offers a way to improve model performance without sacrificing latency or storage limits, especially for edge devices. The certificate framework gives an explicit safety signal, enabling automated gating that can be integrated into deployment pipelines to balance accuracy and computational cost.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00374v1)
