---
title: Don't Contrast the Impossible: Region-Constrained Batching for Contrastive User Modeling on a Local Community Platform
published: 2026-07-31T02:47:43Z
authors: Seungho Han, Byeongchang Kim, Jin Yu
url: http://arxiv.org/abs/2607.28971v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Don't Contrast the Impossible: Region-Constrained Batching for Contrastive User Modeling on a Local Community Platform

## Abstract
Contrastive learning is widely used for user modeling in large-scale recommender systems, where standard in-batch negatives implicitly assume universal exposure that any user can be shown any item. On local community platforms such as Karrot, however, exposure is geographically constrained; many user-item pairs are impossible by design yet still treated as negatives during training, diluting the contrastive learning signal. We address this impossible negatives problem and propose Region-Constrained Batch Sampling (RCBS), a simple yet effective batching method that constructs region-homogeneous mini-batches so that users are contrasted primarily against items they could feasibly see. By replacing impossible negatives with feasible ones, RCBS naturally introduces harder and more informative negatives under realistic exposure constraints. With offline evaluations and online A/B tests, we show that RCBS consistently improves user representation quality and consequently enhances home feed ranking, retrieval, and display ads ranking. The resulting user embeddings have been deployed in production across various applications.

## Metadata
- **Published**: 2026-07-31T02:47:43Z
- **Authors**: Seungho Han, Byeongchang Kim, Jin Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28971v1)