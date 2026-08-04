---
title: CoRe-GNN: Multilevel Message passing on Coarsened graphs
published: 2026-08-03T12:18:58Z
authors: Antonin Joly, Nicolas Keriven, Aline Roumy
url: http://arxiv.org/abs/2608.02128v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoRe-GNN: Multilevel Message passing on Coarsened graphs

## Abstract
Training Graph Neural Networks on large graphs is challenged by the memory cost of storing all node representations across layers. We show that several existing scalable approaches can be written as structured modifications of the GNN propagation matrix, providing a unified perspective that exposes their respective limitations. In particular, graph coarsening replaces it by a low-rank approximation that enables spectral guarantees but assigns uniform representations to clustered nodes, while Cluster-GCN restricts the propagation matrix to intra-cluster connections that allow efficient batching but sever long-range information. These are complementary failures of the \emph{same} decomposition of the graph into groups of nodes. To obtain the best of both worlds, we propose \textbf{CoRe-GNN}, which performs both propagations in parallel at each layer: a coarsened inter-cluster term capturing long-range structure, and a local intra-cluster term preserving per-node discriminability. We prove that CoRe-GNN inherits analogous approximation guarantees to those of graph coarsening, and introduce a natural cluster-based \emph{batching scheme} that scales to graphs with millions of nodes. On node classification benchmarks spanning homophilic, heterophilic, large-scale, and long-range graphs, CoRe-GNN outperforms both graph coarsening and Cluster-GCN baselines. Notably, CoRe-GNN reaches competitive accuracy on \emph{long-range} tasks, while remaining memory-efficient through batching.

## Metadata
- **Published**: 2026-08-03T12:18:58Z
- **Authors**: Antonin Joly, Nicolas Keriven, Aline Roumy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02128v1)