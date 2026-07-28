---
title: Sparse Gaussian-Mixture-Model Q-Functions via Hadamard Overparametrization for Online Reinforcement Learning
published: 2026-07-26T05:58:23Z
authors: Minh Vu, Konstantinos Slavakis
url: http://arxiv.org/abs/2607.23474v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sparse Gaussian-Mixture-Model Q-Functions via Hadamard Overparametrization for Online Reinforcement Learning

## Abstract
This paper develops an online, off-policy policy-iteration framework for reinforcement learning (RL), based on sparse Gaussian-mixture-model Q-functions (S-GMM-QFs). The framework reconciles streaming, non-stationary data with the Riemannian structure of the parameter space while handling distributional mismatch through experience replay. S-GMM-QFs are introduced via Hadamard overparametrization, enabling interpretable sparsification through smooth regularization that facilitates Riemannian-based optimization. Overparametrization allows the framework to adaptively identify meaningful components from a large initial pool, yielding sparse models where interpretability emerges naturally from geometry: each component's parameters (means and covariances) explicitly encode its geometric role in the ambient state-action space. These geometric roles are learned through online gradient descent on a smooth objective over a (Cartesian-product) Riemannian manifold. Numerical tests demonstrate that S-GMM-QFs match or exceed deep RL methods while using substantially fewer parameters and achieving faster improvement per observed transition. Notably, parameter efficiency and interpretability combine to maintain strong generalization in low-parameter regimes where sparsified deep RL approaches degrade.

## Metadata
- **Published**: 2026-07-26T05:58:23Z
- **Authors**: Minh Vu, Konstantinos Slavakis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23474v1)