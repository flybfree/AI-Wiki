---
title: Selectivity Matters: Source Node Influence Pruning for Unsupervised Graph Domain Adaptation
published: 2026-07-20T08:19:34Z
authors: Ridong Han, Yawen Shen, Zhongnian Li, Tongfeng Sun, Xinzheng Xu, Abdulmotaleb El Saddik
url: http://arxiv.org/abs/2607.17668v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Selectivity Matters: Source Node Influence Pruning for Unsupervised Graph Domain Adaptation

## Abstract
Unsupervised Graph Domain Adaptation (UGDA) aims to facilitate knowledge transfer from a labeled source graph to an unlabeled target graph by mitigating cross-domain distribution shifts. Existing methods primarily focus on node-level feature alignment in latent spaces, relying on the implicit assumption that all source nodes contribute positively to the alignment. However, this assumption often fails because a node's semantic information is intrinsically coupled with its topological graph structure. Due to structural shifts, source nodes with severe structural deviations (e.g., structural outliers) lack semantic counterparts in the target graph, and forcing alignment on them introduces severe noise and causes negative transfer. To bridge this gap, we argue that selective source node utilization is superior to full-graph training, thereby shifting the research paradigm from feature-level alignment to data-level refinement. To this end, we propose Source Node Influence Pruning (SNIP), a novel model-agnostic, data-centric refinement framework. Specifically, SNIP quantifies the structural discrepancy between individual source nodes and the target domain by integrating multiple centrality measures, assigning each source node an influence score. A rank-based normalization mechanism is further employed to eliminate scale variations across different measures, allowing SNIP to effectively identify and filter out structurally incompatible nodes with low influence scores. As a plug-and-play method, SNIP constructs a refined "sub-source" graph that is inherently more beneficial for subsequent alignment. Comprehensive experiments across eight transfer scenarios on five real-world datasets demonstrate that SNIP consistently outperforms competitive baselines and significantly enhances adaptation performance, validating the superiority of selective node utilization over full-graph training.

## Metadata
- **Published**: 2026-07-20T08:19:34Z
- **Authors**: Ridong Han, Yawen Shen, Zhongnian Li, Tongfeng Sun, Xinzheng Xu, Abdulmotaleb El Saddik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17668v1)