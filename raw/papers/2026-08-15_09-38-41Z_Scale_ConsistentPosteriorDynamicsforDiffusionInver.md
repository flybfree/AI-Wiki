---
title: Scale-Consistent Posterior Dynamics for Diffusion Inverse Problems
published: 2026-08-15T09:38:41Z
authors: Zhaoqiang Liu, Tongyao Pang, Ruibing Wang, Yang Zheng
url: http://arxiv.org/abs/2608.15144v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scale-Consistent Posterior Dynamics for Diffusion Inverse Problems

## Abstract
Posterior sampling with a pretrained diffusion prior is governed by a conditional score whose intermediate likelihood component is generally intractable. We begin from an ideal one-parameter posterior SDE family in which a stochasticity parameter controls probability-flow transport and stochastic exploration without changing the posterior marginals. To obtain a tractable model, we express the likelihood in a rescaled clean-image coordinate and use log-SNR to organize the resulting posterior proxies. Projecting the diffusion uncertainty through the forward operator then yields a noise-conditioned covariance path whose targets approach the clean posterior. Because endpoint consistency of these targets does not ensure that a surrogate transport follows them, we interleave the transport with a frozen-target Langevin corrector, producing a continuous surrogate SDE. We discretize this model with an outer Lie--Trotter splitting and a variance-matched split-step IMEX predictor that treats the learned prior explicitly, the linear likelihood implicitly, and the stochastic innovation after the implicit solve. We prove marginal invariance of the ideal family, posterior convergence of the continuous surrogate under mixing and transport-defect conditions, and a first-order weak error bound for the discrete algorithm. Experiments on FFHQ and ImageNet with 100 score evaluations demonstrate competitive reconstruction fidelity for super-resolution and deblurring. A controlled 100-image ablation separates scale consistency from the finite-step effects of stochastic-increment placement, continuation, and corrector allocation. A separate noiseless box-inpainting study shows that large exploration reaches a performance plateau only when the matched innovation is injected after the stiff likelihood solve.

## Metadata
- **Published**: 2026-08-15T09:38:41Z
- **Authors**: Zhaoqiang Liu, Tongyao Pang, Ruibing Wang, Yang Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15144v1)