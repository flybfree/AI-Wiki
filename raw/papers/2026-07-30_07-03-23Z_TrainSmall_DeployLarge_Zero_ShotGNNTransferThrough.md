---
title: Train Small, Deploy Large: Zero-Shot GNN Transfer Through Geometric Renormalization
published: 2026-07-30T07:03:23Z
authors: Robert Jankowski, Pedro Almagro-Blanco, Marián Boguñá, Melanie Weber, M. Ángeles Serrano
url: http://arxiv.org/abs/2607.27767v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Train Small, Deploy Large: Zero-Shot GNN Transfer Through Geometric Renormalization

## Abstract
Graph neural networks (GNNs) can operate on large graphs but become infrastructure-sensitive at the scale of millions of nodes and typically require scalable training techniques for even larger graphs. This raises a central question: when can a model trained on a smaller, scaled-down replica of a graph be deployed on the full-resolution graph without retraining? We introduce a zero-shot transfer protocol in which a GNN is trained on a graph coarse-grained by geometric renormalization (GR), and the resulting weights are transferred directly to the original network. Across synthetic and real-world networks, training on GR scaled-down replicas preserves much of the original-scale predictive performance while significantly reducing training cost. We further find that learned representations and predictive trajectories remain aligned across scales. These findings suggest that structural similarity may be more important than network size in determining GNN transferability, opening a path toward scale-equivariant graph architectures.

## Metadata
- **Published**: 2026-07-30T07:03:23Z
- **Authors**: Robert Jankowski, Pedro Almagro-Blanco, Marián Boguñá, Melanie Weber, M. Ángeles Serrano
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27767v1)