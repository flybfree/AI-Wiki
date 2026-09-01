---
title: Unlearning on Spatio-Temporal Graphs through Subgraph Virtual Edge Reconstruction
published: 2026-08-29T17:01:44Z
authors: Qiming Guo, Wenbo Sun, Chen Pan, Ye Wang, Wenlu Wang
url: http://arxiv.org/abs/2608.29369v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unlearning on Spatio-Temporal Graphs through Subgraph Virtual Edge Reconstruction

## Abstract
Spatio-temporal graphs are widely used in modeling complex dynamic processes such as temporal forecasting, molecular dynamics, and healthcare monitoring. Recently, stringent privacy regulations such as GDPR and CCPA have introduced significant new challenges for existing spatio-temporal graph models, requiring complete unlearning of unauthorized data. Since each node in a spatio-temporal graph diffuses information globally across both spatial and temporal dimensions, existing unlearning methods primarily designed for static graphs and localized data removal cannot efficiently erase a single node without incurring costs nearly equivalent to full model retraining. To address this, we propose CallosumNet, a spatio-temporal graph unlearning framework biologically inspired by the corpus callosum structure. CallosumNet makes two key technical contributions: (1) it reconstructs subgraphs using biologically-inspired virtual edges; and (2) it restores interlinked spatio-temporal dependencies among subgraphs via a lightweight meta-graph integration layer. Empirical results on four diverse real-world datasets show that CallosumNet achieves complete unlearning while maintaining accuracy very close to the gold model. The code is publicly available at https://github.com/wenlu-lab/STGraphUnlearning.

## Metadata
- **Published**: 2026-08-29T17:01:44Z
- **Authors**: Qiming Guo, Wenbo Sun, Chen Pan, Ye Wang, Wenlu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29369v1)