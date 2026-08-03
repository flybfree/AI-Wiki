---
title: StraightDP: Geometry-Aware Differential Privacy for Rectified-Flow Transformers
published: 2026-07-31T07:27:52Z
authors: Xujun Che, Depeng Xu, Xintao Wu
url: http://arxiv.org/abs/2607.29100v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StraightDP: Geometry-Aware Differential Privacy for Rectified-Flow Transformers

## Abstract
Differentially private (DP) training of text-conditioned generative models suffers a utility cliff at strong privacy. We revisit this problem through the geometry of rectified flows: along the straight interpolation between noise and data, the Bayes-optimal velocity is governed to leading order at the noise end by a few class-conditional moments, and increasingly sample-specific structure matters toward the data end. StraightDP exploits this heterogeneity end to end. A small budget share releases whitened class-conditional moments once, to be distilled into the weights or injected at sampling time. The rest is spent by pre-declared DP-SGD toward the data end, beyond the moments' reach. At $\varepsilon=1$ on MNIST, the released moments alone already attain $0.76$ downstream accuracy with prototype-like samples and an FID of $237$, and uniform DP-SGD attains $0.21$. The pipeline built on the release reaches $0.81$ accuracy at FID $56$ in a public latent space. Constraining per-token stream norms of the multimodal backbone leaves the pretraining loss unchanged yet improves downstream accuracy in the extreme-noise pixel-space regime, and its accuracy effect becomes monotonically more favorable as privacy strengthens. The released moments also port to frozen SD3-medium, where sampling-time injection beats DP-LoRA training at a fraction of the budget.

## Metadata
- **Published**: 2026-07-31T07:27:52Z
- **Authors**: Xujun Che, Depeng Xu, Xintao Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29100v1)