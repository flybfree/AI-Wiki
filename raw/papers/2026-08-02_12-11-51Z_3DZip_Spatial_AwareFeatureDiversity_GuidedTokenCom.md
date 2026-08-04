---
title: 3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D Question Answering
published: 2026-08-02T12:11:51Z
authors: Changwoo Baek, Kyeongbo Kong
url: http://arxiv.org/abs/2608.01185v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# 3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D Question Answering

## Abstract
Recent 3D vision-language models (3D VLMs) construct geometry aware tokens by projecting 2D visual features into world coordinates, enabling spatial reasoning for tasks such as 3D question answering. However, this design generates thousands of tokens per scene, resulting in substantial computational and memory overhead. While token compression has been extensively studied in 2D VLMs, existing approaches rely on semantic relevance or attention-based selection that overlook the structured spatial nature of 3D tokens. Moreover, redundancy in 3D representations cannot be resolved by spatial proximity alone, as object-level token imbalance persists even after spatial aggregation. To address this, we propose 3DZip, a three-stage token compression framework that first applies coarse voxelization to remove point-level redundancy, then selects anchor tokens based on feature-space diversity via a Determinantal Point Process, and finally merges remaining tokens under spatial constraints to preserve geometric coherence. Experiments on three 3D question answering benchmarks demonstrate that 3DZip consistently outperforms existing compression methods, retaining 94.7% of the original performance with only 128 tokens, achieving a $1.92\times$ faster inference speed.

## Metadata
- **Published**: 2026-08-02T12:11:51Z
- **Authors**: Changwoo Baek, Kyeongbo Kong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01185v1)