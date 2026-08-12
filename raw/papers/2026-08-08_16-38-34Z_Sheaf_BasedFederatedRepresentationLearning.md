---
title: Sheaf-Based Federated Representation Learning
published: 2026-08-08T16:38:34Z
authors: Gabriele D'Acunto, Enrico Grimaldi, Valeria Avino, Mario Edoardo Pandolfo, Leonardo Di Nino, Sergio Barbarossa, Paolo Di Lorenzo
url: http://arxiv.org/abs/2608.10016v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sheaf-Based Federated Representation Learning

## Abstract
Heterogeneous federated systems require agents to learn and exchange informative representations despite differences in data distributions, sensing modalities, model architectures, latent dimensionalities, and local learning objectives. To address this challenge, we propose Sheaf-based Federated Representation Learning (SFRL), a general framework that jointly optimizes local objectives with a manifold-constrained geometric alignment regularizer based on learnable sheaf restriction maps. Unlike most existing approaches, SFRL does not assume a shared global latent space. Instead, global consistency emerges from the alignment of neighboring latent representations through orthogonal transformations and isometric embeddings. This alignment is enforced by a quadratic gluing regularizer induced by the sheaf Laplacian, whose learnable restriction maps adapt the geometry to the observed data. The penalty is evaluated on a small set of shared pilot samples, ensuring scalability and communication efficiency. We develop a decentralized algorithm for solving SFRL, termed Sheaf-FRL, which alternates between gradient updates of the local models and closed-form Procrustes updates of the edge-wise restriction maps. We further establish convergence of Sheaf-FRL to first-order stationary points in both deterministic and stochastic settings. As an application, we consider a cooperative classification task in the context of semantic communication, under model and data heterogeneity. Our results show that Sheaf-FRL outperforms baseline approaches in terms of local and post-communication classification accuracy across different levels of local distribution shift and exhibits greater robustness to latent-space dimensionality compression.

## Metadata
- **Published**: 2026-08-08T16:38:34Z
- **Authors**: Gabriele D'Acunto, Enrico Grimaldi, Valeria Avino, Mario Edoardo Pandolfo, Leonardo Di Nino, Sergio Barbarossa, Paolo Di Lorenzo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10016v1)