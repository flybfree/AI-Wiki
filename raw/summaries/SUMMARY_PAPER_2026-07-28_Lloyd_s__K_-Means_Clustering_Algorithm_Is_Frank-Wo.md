---
title: Lloyd's $K$-Means Clustering Algorithm Is Frank-Wolfe in Disguise
url: http://arxiv.org/abs/2607.25190v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_01-42-48Z_Lloyd_s_K__MeansClusteringAlgorithmIsFrank_Wolfein.md
generated_at: 2026-07-28 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper shows that Lloyd’s K‑means algorithm can be interpreted as a special case of the Frank‑Wolfe optimization method, establishing a theoretical link between these two widely used techniques. By applying recent non‑asymptotic convergence results for concave objectives to Lloyd’s SSE objective, the authors obtain an O(1/t) rate that depends only on the initial sum of squared errors. They also propose an FW variant that handles empty clusters while preserving the same convergence guarantee.

## Key Takeaways
- The connection between Lloyd’s K‑means and Frank‑Wolfe is demonstrated through a mathematical reformulation that treats clustering as a projection‑free optimization problem.
- An O(1/t) non‑asymptotic convergence rate to a local minimum of the SSE objective is achieved, which is independent of the number of iterations beyond the initial value.
- The authors introduce an FW variant designed for semismooth objectives that accommodates empty clusters without sacrificing the established convergence bound.

## Context
In machine learning and data mining, clustering algorithms are central to unsupervised learning pipelines. Lloyd’s K‑means remains popular because it is simple and fast, yet its theoretical analysis has been limited compared with modern first‑order methods like Frank‑Wolfe. This work bridges that gap by providing a rigorous convergence guarantee for an algorithm historically treated as heuristic.

## Implications
Practitioners can now rely on the proven O(1/t) performance of Lloyd’s K‑means, allowing them to set realistic expectations about runtime and accuracy. The framework also suggests that other greedy clustering methods may benefit from similar theoretical analysis, opening avenues for more robust and efficient unsupervised learning tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25190v1)
