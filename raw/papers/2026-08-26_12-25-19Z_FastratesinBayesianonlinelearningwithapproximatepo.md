---
title: Fast rates in Bayesian online learning with approximate posteriors
published: 2026-08-26T12:25:19Z
authors: Ilsang Ohn
url: http://arxiv.org/abs/2608.25706v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fast rates in Bayesian online learning with approximate posteriors

## Abstract
Exact Bayes prediction enjoys fast predictive regret guarantees, but exact posterior updating or representation may be too costly for online use. We study when these statistical guarantees are preserved by computational approximations. We show that the cumulative price of posterior approximation can be governed by the interaction between the contraction radius of the exact Gibbs posterior and the Wasserstein distance between the approximate and exact posteriors. Our general theorem shows that whenever exact Bayes prediction achieves a fast regret bound, any approximate posterior method that tracks the exact posterior with sufficient accuracy inherits the same fast regret, up to an additive term determined by the approximation error. Three online learning examples are developed. For linear models with strongly convex regularized losses, a projected Langevin algorithm yields an approximate posterior that achieves logarithmic regret. For an infinite-dimensional canonical exponential family sequence model over a Sobolev ellipsoid, a prior-preserving truncation method attains the minimax predictive regret rate with sublinear memory and constant update cost per observation. For random-design Gaussian process (GP) regression, a sparse variational posterior with inducing variables achieves the same predictive regret rate as the exact GP, but at substantially lower computational cost.

## Metadata
- **Published**: 2026-08-26T12:25:19Z
- **Authors**: Ilsang Ohn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25706v1)