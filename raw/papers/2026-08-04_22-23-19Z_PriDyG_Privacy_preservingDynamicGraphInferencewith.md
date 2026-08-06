---
title: PriDyG: Privacy-preserving Dynamic Graph Inference with LLM-GNN Collaboration
published: 2026-08-04T22:23:19Z
authors: Yuyang Xia, Ruixuan Liu, Li Xiong
url: http://arxiv.org/abs/2608.04255v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PriDyG: Privacy-preserving Dynamic Graph Inference with LLM-GNN Collaboration

## Abstract
Graph inference over relational data can expose sensitive edge information, and this risk becomes more severe in dynamic graphs, where repeated model updates cause privacy loss to accumulate. We formulate Edge-level Differentially Private Dynamic Graph Inference (EDG) and propose PriDyG, a private inference framework that combines GNN-based structural learning with LLM-based semantic reasoning. PriDyG introduces incremental private multi-hop aggregation, which buffers newly arrived edges and processes each edge exactly once. By parallel composition, the total privacy cost equals that of a single static release, independent of the number or schedule of model updates. Compared with geometrically decaying budget allocation, incremental aggregation avoids exponentially increasing noise while preserving exact one-hop signals and at least half of two-hop information transfers. PriDyG further complements privatized GNN outputs with LLM predictions derived solely from node text, incurring no additional edge-level privacy cost. Experiments on four benchmarks for node classification and link prediction show that PriDyG consistently outperforms geometrically decaying baselines under the same privacy budget and matches the utility of naive per-update retraining while reducing cumulative privacy cost by up to three orders of magnitude.

## Metadata
- **Published**: 2026-08-04T22:23:19Z
- **Authors**: Yuyang Xia, Ruixuan Liu, Li Xiong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04255v1)