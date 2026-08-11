---
title: PreGress: Ranking-Native Pre-training and Prompting for Graph Node Ranking
published: 2026-08-10T02:16:37Z
authors: Lujie Ban, Jiasheng shi, Yingli Zhou, Kaiwen Xue, Daiyin Wang, Xubin Li, Shuanghua Li, Chenhao Ma
url: http://arxiv.org/abs/2608.09016v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PreGress: Ranking-Native Pre-training and Prompting for Graph Node Ranking

## Abstract
Node ranking is a fundamental problem in graph information retrieval, measuring the relative importance of nodes and supporting a wide range of applications such as influence analysis, recommendation, and graph-based retrieval augmented generation. However, exact computation of graph-based ranking measures is often computationally prohibitive at scale. Existing GNN-based ranking methods provide scalable approximations, but they are typically tailored to individual ranking criteria and require retraining for each downstream task, which limits their transferability and efficiency. Recent graph pre-training approaches aim to enable knowledge transfer across tasks, yet their learning objectives are largely misaligned with node ranking, resulting in suboptimal adaptability to ranking-oriented applications. To address these limitations, we propose PreGress, the first ranking-native pre-training and prompting framework for supporting a wide range of node ranking tasks. PreGress performs multi-task pre-training using our carefully designed objectives, including degree centrality prediction and attribute reconstruction, to jointly capture structural and attribute information. To support heterogeneous ranking criteria, we design lightweight, task-specific prompt modules that adapt a frozen ranking backbone to downstream tasks without full retraining. Experiments on six public graphs and two real-world query-to-item benchmarks---Yelp2018 and MovieLens-100K---together with a controlled five-criterion graph-access study demonstrate strong ranking quality with low task-specific state overhead.

## Metadata
- **Published**: 2026-08-10T02:16:37Z
- **Authors**: Lujie Ban, Jiasheng shi, Yingli Zhou, Kaiwen Xue, Daiyin Wang, Xubin Li, Shuanghua Li, Chenhao Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09016v1)