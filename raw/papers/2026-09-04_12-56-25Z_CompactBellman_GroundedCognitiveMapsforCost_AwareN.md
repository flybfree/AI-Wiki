---
title: Compact Bellman-Grounded Cognitive Maps for Cost-Aware Navigation
published: 2026-09-04T12:56:25Z
authors: Yuzhe Han, Mingkun Xu, Yujie Wu
url: http://arxiv.org/abs/2609.05104v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Compact Bellman-Grounded Cognitive Maps for Cost-Aware Navigation

## Abstract
Biological agents navigate familiar environments not by re-solving routes for each new goal, but by reusing a learned map built once and read off as goals change. Existing artificial cognitive-map models mimic this reuse, yet their guidance is not explicitly grounded in additive heterogeneous route costs. Furthermore, they often struggle with memory efficiency: representative state-indexed and high-rank spectral constructions incur substantial storage growth as the environment scales. We present BCM, which grounds a reusable cognitive map in local edge costs through a self-supervised Bellman-grounded objective and a compact coordinate encoding, supporting changing goal queries without per-goal retraining. On weighted grids of up to $N=1600$ nodes, BCM maintains full success and only a 5\% mean Gap relative to exact Dijkstra search, compared with about $45\%$ for a connectivity-based spectral baseline. Notably, as the graph size increases from $N=400$ to $N=3600$, its memory footprint grows sublinearly while maintaining competitive performance, making our method scalable to complex environments. Together, these results show that additive route costs can be written into a compact, reusable cognitive-map representation, bridging the gap between biological flexibility and optimal path planning.

## Metadata
- **Published**: 2026-09-04T12:56:25Z
- **Authors**: Yuzhe Han, Mingkun Xu, Yujie Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05104v1)