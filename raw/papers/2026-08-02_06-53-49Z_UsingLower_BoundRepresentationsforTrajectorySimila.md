---
title: Using Lower-Bound Representations for Trajectory Similarity Learning
published: 2026-08-02T06:53:49Z
authors: Liwei Deng, Haotian Meng, Yupu Zhang, Yan Zhao, Torben Bach Pedersen, Kai Zheng, Christian S. Jensen
url: http://arxiv.org/abs/2608.01039v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Using Lower-Bound Representations for Trajectory Similarity Learning

## Abstract
Trajectory similarity learning is fundamental to efficient trajectory retrieval under complex distance measures. Existing learning-based methods typically rely on embeddings trained to approximate trajectory distances or rankings, but they often lack guarantees with respect to the original distances, exhibit unstable performance across distance measures, and incur substantial training costs. We revisit trajectory similarity learning from a lower-bound representation perspective and propose LB-TrajRep, a unified lower-bound representation framework independent of deep neural embeddings. This framework constructs single-vector representations from a set of lower-bound components, enabling admissible and interpretable lower bounds for multiple classical trajectory distances, including Dynamic Time Warping (DTW), Hausdorff distance, and Discrete Fréchet Distance (DFD). Within this framework, we instantiate point-pivot components, which naturally support both metric and non-metric distances and remain compatible with standard vector-based retrieval pipelines. To improve ranking quality, we develop two data-driven pivot selection strategies that explicitly optimize lower-bound tightness and prioritize hard near-neighbor trajectory pairs, respectively. Extensive experiments on real-world trajectory datasets show that the proposed lower-bound representations are able to consistently outperform state-of-the-art neural trajectory embeddings across diverse distance measures, improving top-$k$ ranking accuracy by up to 20\%--60\% on the Hausdorff distance and DFD and by 15\%--40\% on DTW.

## Metadata
- **Published**: 2026-08-02T06:53:49Z
- **Authors**: Liwei Deng, Haotian Meng, Yupu Zhang, Yan Zhao, Torben Bach Pedersen, Kai Zheng, Christian S. Jensen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01039v1)