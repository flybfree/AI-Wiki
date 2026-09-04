---
title: Statistical Feature Augmentation for Anomaly Detection in Dynamic Graphs
published: 2026-09-02T07:20:54Z
authors: Philipp Schlinge, Jean-Luc Schnipper, Martin Atzmueller
url: http://arxiv.org/abs/2609.02965v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Statistical Feature Augmentation for Anomaly Detection in Dynamic Graphs

## Abstract
Dynamic networks are being applied in many domains, from social media to logistics systems, each with their own set of special characteristics. A model employed on this type of data must capture the duality between temporal/structural and feature-based information. Yet state-of-the-art deep learning models often struggle to learn especially short-term behavioral interaction signals, such as sender intensity or interaction inertia, directly from raw event streams. To address this gap, we propose a statistical feature augmentation method that explicitly encodes behavioral interaction statistics into the input feature space. We evaluate our proposed method on an anomaly detection task across three real-world datasets (Reddit, Wikipedia, MOOC) and seven models spanning both continuous-time and discrete-time architectures. As a baseline, we apply the same models trained on the original embeddings. Our results show, that augmentation consistently improves detection performance. Beyond performance, the enriched input enables fine-grained post-hoc analysis of behavioral importance, since each statistic occupies a dedicated input dimension. In particular, this work showcases a promising approach for merging classical network analysis with deep learning.

## Metadata
- **Published**: 2026-09-02T07:20:54Z
- **Authors**: Philipp Schlinge, Jean-Luc Schnipper, Martin Atzmueller
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02965v1)