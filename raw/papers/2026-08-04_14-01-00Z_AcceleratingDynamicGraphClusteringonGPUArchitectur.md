---
title: Accelerating Dynamic Graph Clustering on GPU Architectures with cuGraph
published: 2026-08-04T14:01:00Z
authors: Nelson Aloysio Reis de Almeida Passos, Emanuele Carlini, Salvatore Trani
url: http://arxiv.org/abs/2608.03695v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Accelerating Dynamic Graph Clustering on GPU Architectures with cuGraph

## Abstract
This work addresses community detection in temporal networks through GPU-accelerated extensions of spectral clustering and modularity-based algorithms originally designed for static graphs. Built on the NVIDIA RAPIDS ecosystem, the framework enables the characterization and tracking of communities in snapshot-based dynamic graphs, either by Leiden greedy optimization with multi-GPU support via Dask-based workload distribution, or eigendecomposition of a symmetric Bethe-Hessian operator. Our multislice modularity backend achieves up to roughly three orders of magnitude speedup over the CPU reference under an equal-work budget, depending on graph density and snapshot count, while preserving compatibility with existing graph analytics pipelines. We demonstrate its applicability on real-world and synthetic datasets, facilitating exploratory analysis of structural network properties over time. Such capabilities are relevant across several application domains, such as epidemic spreading, financial systems, cybersecurity, and trajectory and mobility analysis. We release our implementation as free and open-source software, including Python bindings through the NetworkX-Temporal library for ease of use and zero-code acceleration with existing codebases.

## Metadata
- **Published**: 2026-08-04T14:01:00Z
- **Authors**: Nelson Aloysio Reis de Almeida Passos, Emanuele Carlini, Salvatore Trani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03695v1)