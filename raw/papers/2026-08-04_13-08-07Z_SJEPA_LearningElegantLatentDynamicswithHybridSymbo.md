---
title: SJEPA: Learning Elegant Latent Dynamics with Hybrid Symbolic-Neural Predictors
published: 2026-08-04T13:08:07Z
authors: Yongchao Huang
url: http://arxiv.org/abs/2608.04060v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SJEPA: Learning Elegant Latent Dynamics with Hybrid Symbolic-Neural Predictors

## Abstract
Joint-embedding predictive architectures learn abstract states by predicting target embeddings from context embeddings, but their transition models are typically opaque neural maps. We introduce SJEPA, a reconstruction-free JEPA framework that learns predictive representations whose induced dynamics admit compact symbolic descriptions. Its hybrid transition combines a symbolic law with a regularised neural correction for dynamics outside the selected grammar. The central principle is to learn the simplest adequate dynamics: representation constraints preserve informative, non-collapsed predictive coordinates, while operator compression favours low-complexity symbolic-neural transitions that remain predictively adequate. We formalise this principle through induced-dynamics complexity, analyse predictive-coordinate non-identifiability, and show that unconstrained operator compression creates a direct shortcut to representation collapse. The framework supports both alternating representation-equation learning and symbolic dynamics fitted to fixed representations. In controlled pendulum experiments, joint learning discovers substantially simpler symbolic dynamics with lower long-horizon rollout error and divergence than post-hoc fitting, while an unconstrained one-step diagnostic realises the predicted collapse shortcut. Under grammar misspecification, correction regularisation preserves the representable symbolic mechanism and directs the neural component towards residual dynamics. The results expose a controllable trade-off among predictive fidelity, representation quality, symbolic parsimony, and symbolic-neural allocation.

## Metadata
- **Published**: 2026-08-04T13:08:07Z
- **Authors**: Yongchao Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04060v1)