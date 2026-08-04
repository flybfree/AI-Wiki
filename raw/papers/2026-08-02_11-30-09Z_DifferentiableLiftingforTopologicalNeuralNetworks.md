---
title: Differentiable Lifting for Topological Neural Networks
published: 2026-08-02T11:30:09Z
authors: Jorge Luiz Franco, Gabriel Duarte, Alexander Nikitin, Moacir Ponti, Diego Mesquita, Amauri H. Souza
url: http://arxiv.org/abs/2608.01160v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Differentiable Lifting for Topological Neural Networks

## Abstract
Topological neural networks (TNNs) enable leveraging high-order structures on graphs (e.g., cycles and cliques) to boost the expressive power of message-passing neural networks. In turn, however, these structures are typically identified a priori through an unsupervised graph lifting operation. Notwithstanding, this choice is crucial and may have a drastic impact on a TNN's performance on downstream tasks. To circumvent this issue, we propose $\partial$lift (DiffLift), a general framework for learning graph liftings to hypergraphs and cellular- and simplicial complexes in an end-to-end fashion. In particular, our approach leverages learned vertex-level latent representations to identify and parameterize distributions over candidate higher-order cells for inclusion. This results in a scalable model which can be readily integrated into any TNN. Our experiments show that $\partial$lift outperforms existing lifting methods on multiple benchmarks for graph and node classification across different TNN architectures. Notably, our approach leads to gains of up to 45% over static liftings, including both connectivity- and feature-based ones.

## Metadata
- **Published**: 2026-08-02T11:30:09Z
- **Authors**: Jorge Luiz Franco, Gabriel Duarte, Alexander Nikitin, Moacir Ponti, Diego Mesquita, Amauri H. Souza
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01160v1)