---
title: What Makes Graph Unified? Principles and Generative Sliding-Window Transformer for Graph Foundation Models
published: 2026-07-30T10:13:59Z
authors: Dongxiao He, Siqi Liu, Jitao Zhao, Yawen Li, Yi Wang, Di Jin
url: http://arxiv.org/abs/2607.27966v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Makes Graph Unified? Principles and Generative Sliding-Window Transformer for Graph Foundation Models

## Abstract
Graph Foundation Models (GFMs) have recently emerged as a promising paradigm for general-purpose graph learning, aiming to learn reusable knowledge that generalizes across diverse graph domains and downstream tasks, reducing the need for specific model development. Achieving this goal requires reconciling the substantial heterogeneity in node features, graph structures, and semantic information across domains. Among them, heterogeneous node features constitute a fundamental input-level barrier, as their dimensionality and semantics vary substantially across datasets. Existing studies typically project or map heterogeneous node features into a fixed-dimensional space, often implicitly equating dimensional uniformity with effective feature unification. Yet dimensional consistency alone does not ensure that the unified features preserve informative semantics and capture transferable patterns that can support cross-domain knowledge transfer. To bridge this conceptual gap, we distill four desiderata for cross-domain graph feature unification: formal uniformity, cross-domain transferability, information preservation, and backbone compatibility. Guided by these principles, we propose SliGFM, a graph foundation model built upon topology-aware sliding-window feature encoding and generative reconstruction. SliGFM orders feature dimensions by topological smoothness and scans the reordered features with a shared sliding-window feature encoder, transforming heterogeneous features into a common space of ordered fixed-dimensional feature tokens. This formulation enables a smoothness-aware transformer to capture transferable relational patterns among feature tokens within each node, while the generative reconstruction objective encourages preservation of the original feature information.

## Metadata
- **Published**: 2026-07-30T10:13:59Z
- **Authors**: Dongxiao He, Siqi Liu, Jitao Zhao, Yawen Li, Yi Wang, Di Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27966v1)