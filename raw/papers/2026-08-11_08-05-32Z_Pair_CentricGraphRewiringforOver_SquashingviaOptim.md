---
title: Pair-Centric Graph Rewiring for Over-Squashing via Optimal Transport-Guided Communication Alignment
published: 2026-08-11T08:05:32Z
authors: Yan Wang, Chuan-Xian Ren
url: http://arxiv.org/abs/2608.10619v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pair-Centric Graph Rewiring for Over-Squashing via Optimal Transport-Guided Communication Alignment

## Abstract
Message-passing neural networks (MPNNs) often struggle when task-relevant information is distributed across distant regions of a graph, since local propagation must compress remote signals through limited structural interfaces. Graph rewiring provides a structural response to over-squashing. Most existing methods rely on edge-level bottleneck scores or graph-level connectivity surrogates. With a limited rewiring budget, the key question is which pairwise communications most need structural support. This paper proposes PairAlign, a pair-centric graph rewiring framework that makes this question explicit through demand-support shortage. Specifically, PairAlign combines original-graph structural demand with current-graph finite-hop propagation support; their ratio highlights interactions whose communication demand is poorly supported by topology, and our theory shows that this score provides a computable proxy for the corresponding Jacobian-based shortage with a pair-level interpretation of over-squashing. Our theory reveals a two-sided effect of edge insertion: a new edge can create useful walks and simultaneously dilute existing normalized transition mass. Guided by this observation, PairAlign optimizes shortage to favor edge additions that alleviate over-squashing. Beyond selecting useful additions, PairAlign further introduces an Optimal Transport-guided rewiring mechanism to coordinate the finite edge budget for pair-level structural compatibility and shortage-target coverage. It formulates communication alignment between the candidate edge budget and the shortage targets, and the theory shows that this allocation covers shortage targets more broadly and effectively than a greedy-local assignment. Experiments on standard graph benchmarks show PairAlign's improvement across message-passing backbones, validating pair-level repair as an effective route for alleviating over-squashing.

## Metadata
- **Published**: 2026-08-11T08:05:32Z
- **Authors**: Yan Wang, Chuan-Xian Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10619v1)