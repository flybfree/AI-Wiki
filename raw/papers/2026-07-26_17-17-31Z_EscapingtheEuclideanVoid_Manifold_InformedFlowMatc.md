---
title: Escaping the Euclidean Void: Manifold-Informed Flow Matching for Sequential Recommendation
published: 2026-07-26T17:17:31Z
authors: Dengzhao Fang, Jingtong Gao, Yu Li, Xiangyu Zhao, Yi Chang
url: http://arxiv.org/abs/2607.23762v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Escaping the Euclidean Void: Manifold-Informed Flow Matching for Sequential Recommendation

## Abstract
Conventional recommenders capture users' preferences by optimizing observed user-item relations, whereas continuous generative recommendation additionally learns the trajectory of synthesizing a target item. Flow matching drives this process by gradually shaping initial noise into a definitive next-item representation through intermediate states in a continuous embedding space. However, item catalogs are discrete and sparsely supported, meaning even a straight Euclidean path can cross continuous regions that contain little evidence of valid item semantics. Formalizing this failure as the Euclidean void, we propose MIRAGE, a Manifold-Informed Rectification framework for Accelerated Generation of Embeddings in sequential recommendation, which rectifies the learned embedding geometry around an unchanged straight probability path. By leveraging an item co-occurrence graph as a proxy for the underlying semantic manifold, MIRAGE aligns interpolated path states with local anchors, reorganizing the embedding space to ground the trajectory in valid item support. MIRAGE retains the original probability path and uses the graph only during training, thereby enabling accurate and efficient one-step inference. Extensive experiments on four real-world datasets reveal that MIRAGE consistently outperforms state-of-the-art baselines, effectively boosting performance on sparsely observed targets while achieving robust overall accuracy. Our code will be made publicly available upon publication.

## Metadata
- **Published**: 2026-07-26T17:17:31Z
- **Authors**: Dengzhao Fang, Jingtong Gao, Yu Li, Xiangyu Zhao, Yi Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23762v1)