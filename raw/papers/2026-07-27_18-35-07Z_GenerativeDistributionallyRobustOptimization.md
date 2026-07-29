---
title: Generative Distributionally Robust Optimization
published: 2026-07-27T18:35:07Z
authors: Ziwei Zhang, Jonathan Yu-Meng Li, Zhihao Jin
url: http://arxiv.org/abs/2607.24983v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generative Distributionally Robust Optimization

## Abstract
Generative models are increasingly adopted in distributionally robust optimization (DRO), but existing approaches trade off model compatibility and adversarial structure: methods that accept arbitrary samplers do not restrict worst-case laws to a generator family, while generator-parameterized adversaries rely on model-specific access such as likelihoods, scores, or training data. We propose Generative Distributionally Robust Optimization (GDRO), a principled framework that accepts any sampleable conditional generator as the nominal model and restricts worst-case laws to a chosen conditional generator family. The key is the sampler-Sinkhorn pairing: samplers represent the conditional laws exactly, while Sinkhorn divergence compares their induced distributions without likelihood access and can be estimated from samples alone. The resulting population problem admits a direct finite-sample approximation and differentiable primal-dual implementation at the active decision context. For Lipschitz losses, the population Sinkhorn radius bounds downstream degradation. Across explicit and implicit generators, our method reduces rare-context inventory regret by 60% and SocialGAN navigation collisions by 50% relative to nominal decisions.

## Metadata
- **Published**: 2026-07-27T18:35:07Z
- **Authors**: Ziwei Zhang, Jonathan Yu-Meng Li, Zhihao Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24983v1)