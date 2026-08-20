---
title: Sobolev Regularized Score Difference Estimation in Diffusion Models
published: 2026-08-18T18:23:30Z
authors: Chenghan Xie, Jose Blanchet, Renyuan Xu
url: http://arxiv.org/abs/2608.18237v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sobolev Regularized Score Difference Estimation in Diffusion Models

## Abstract
Estimating the difference of two Stein's score functions is a fundamental problem in generative modeling. In particular, score differences arise naturally in transfer learning, where the score difference provides the mechanism for adapting a pre-trained model to a new target distribution, and in diffusion model-based post-training methods such as discriminator guidance. Existing estimators for score differences in these settings either lack of statistical consistency or are difficult to scale up in high-dimensions. We propose a statistically consistent and scalable estimator for score differences based on Sobolev regularization, which plays a crucial role in ensuring consistency and stablizing the training in the small-sample regime. Mathematically, we establish a convergence rate of $O(n^{-\frac{s-1}{d+2s-2}})$ where $d$ is the dimension and $s$ denotes the smoothness of the underlying densities, and provide a minimax lower bound of $\tildeΩ(n^{-\frac{2(s-1)}{d+2s}})$ (in mean-squared error). Empirically, our estimator exhibits significantly improved stability in small-sample regimes compared to existing methods. We demonstrate its effectiveness on real-world tasks, including transfer learning for ECG signal generation, where it substantially outperforms non-regularized score difference estimators in downstream classification performance.

## Metadata
- **Published**: 2026-08-18T18:23:30Z
- **Authors**: Chenghan Xie, Jose Blanchet, Renyuan Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18237v1)