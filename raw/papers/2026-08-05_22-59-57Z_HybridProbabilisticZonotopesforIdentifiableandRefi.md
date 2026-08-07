---
title: Hybrid Probabilistic Zonotopes for Identifiable and Refinable Predictive Uncertainty
published: 2026-08-05T22:59:57Z
authors: Zhen Zhang, Amr Alanwar
url: http://arxiv.org/abs/2608.05454v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hybrid Probabilistic Zonotopes for Identifiable and Refinable Predictive Uncertainty

## Abstract
Probabilistic prediction heads in neural networks typically output either a Gaussian mixture or a single conformal region. Neither separates the distinct sources of uncertainty often present in real prediction tasks: a discrete choice among modes, bounded systematic drift within the chosen mode, and irreducible stochastic noise. We introduce the Hybrid Probabilistic Zonotope (HProbZ), an output head that represents these three sources as binary, bounded, and stochastic generators of a zonotope, and admits a closed-form likelihood by convolution. Sharing the bounded generator across prediction steps couples future predictions algebraically, so observing one step refines the predictive distribution at every remaining step in a single forward pass. We establish that the three generators are identifiable from the likelihood up to permutation, and that an HProbZ density is representationally distinct from any finite Gaussian mixture. The same shared structure provides analytic per-mode risk and distribution-free multi-modal conformal sets at inference time. Empirical analysis on representative prediction benchmarks supports the effectiveness of the design relative to same-encoder mixture baselines, while offering structural properties that mixture or convex-conformal predictors do not jointly provide.

## Metadata
- **Published**: 2026-08-05T22:59:57Z
- **Authors**: Zhen Zhang, Amr Alanwar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05454v1)