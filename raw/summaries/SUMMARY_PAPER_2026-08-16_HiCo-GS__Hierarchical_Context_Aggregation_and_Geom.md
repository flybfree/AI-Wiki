---
title: HiCo-GS: Hierarchical Context Aggregation and Geometric Consistency for Octree Gaussian Splatting
url: http://arxiv.org/abs/2608.14136v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_09-41-58Z_HiCo_GS_HierarchicalContextAggregationandGeometric.md
generated_at: 2026-08-16 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HiCo-GS, a framework that improves octree‑based Gaussian Splatting for city‑scale novel view synthesis by addressing cross‑level feature isolation. It combines two modules: Cross‑Level Context Aggregation and Depth‑Normal Geometric Consistency, achieving higher fidelity and cleaner geometry.

## Key Takeaways
- CLCA uses the octree's spatial containment to create parent‑self‑child triplets of context vectors that are fused with a lightweight MLP plus residual connection, allowing hierarchical prior injection both upward and downward.  
- DNGC enforces agreement between rendered normals and depth‑derived normals via an alpha‑weighted consistency loss and edge‑aware smoothness losses with progressive warmup, reducing floating artifacts especially on planar surfaces.  
- The framework is evaluated on the China‑Pagoda dataset of 8 pagodas with over 1200 images each, showing state‑of‑the‑art rendering quality and substantially cleaner geometry across urban benchmarks.

## Context
This work advances Gaussian Splatting by integrating explicit inter‑level communication, a step toward more coherent multi‑scale representations in neural radiance fields. It demonstrates that lightweight hierarchical priors can significantly improve realism without sacrificing scalability.

## Implications
For practitioners, HiCo‑GS offers a practical method to improve rendering quality with minimal computational overhead, making high‑fidelity city views feasible for real‑time applications. The approach could be adopted by game engines and virtual reality platforms seeking realistic urban scenes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14136v1)
