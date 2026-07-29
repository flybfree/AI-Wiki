---
title: Lloyd's $K$-Means Clustering Algorithm Is Frank-Wolfe in Disguise
published: 2026-07-28T01:42:48Z
authors: Michael Pokojovy, J. Marcus Jobe, Simon Lacoste-Julien
url: http://arxiv.org/abs/2607.25190v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lloyd's $K$-Means Clustering Algorithm Is Frank-Wolfe in Disguise

## Abstract
Lloyd's $K$-means algorithm, also known as naïve $K$-means, is a widely used ad hoc optimization heuristic, designed to minimize the sum of squared errors (SSE) across all $K$-partitions of a dataset via iterative cluster refinement. In this work, we establish a novel connection between Lloyd's algorithm and the Frank-Wolfe (FW) algorithm, a prominent first-order method for projection-free optimization. We demonstrate that Lloyd's algorithm is a special case of FW. Leveraging recent advances in FW methods for concave objectives, we derive a non-asymptotic $\mathcal{O}(1/t)$ convergence rate to a local minimum of the SSE objective. To account for empty clusters, an outcome possible under Lloyd's greedy assignment, we develop an FW variant for semismooth objectives while retaining the same convergence rate that is solely controlled by the initial SSE value. We illustrate our findings with a simulation study for spherical Gaussian mixtures and a real-world image segmentation dataset.

## Metadata
- **Published**: 2026-07-28T01:42:48Z
- **Authors**: Michael Pokojovy, J. Marcus Jobe, Simon Lacoste-Julien
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25190v1)