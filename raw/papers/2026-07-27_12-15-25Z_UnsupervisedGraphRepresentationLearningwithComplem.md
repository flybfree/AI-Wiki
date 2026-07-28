---
title: Unsupervised Graph Representation Learning with Complementary View Alignment
published: 2026-07-27T12:15:25Z
authors: Zengyi Wo, Shiyu Zhang, Qiyao Peng, Tianpeng Li, Xuan Guo
url: http://arxiv.org/abs/2607.24338v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unsupervised Graph Representation Learning with Complementary View Alignment

## Abstract
Unsupervised graph representation learning aims to derive meaningful node embeddings by capturing both structural and attribute information without relying on labeled data. Existing methods, such as GAEs, have demonstrated effectiveness but typically rely on message-passing mechanisms that assume homophily, leading to performance degradation on heterophilous graphs, where connected nodes exhibit dissimilar features. This homophily bias results in the loss of critical high-frequency components that are essential for identifying heterophilous patterns. To address these challenges, we propose \textsc{AlignGAE}, a novel extension of \textit{MaskGAE} that preserves the full frequency spectrum through complementary view alignment. Our framework introduces a dual-encoder architecture that separately processes structural and attribute information, incorporates node positional encoding to approximate Neighborhood Identity Distribution (NID), and employs dual reconstruction tasks for both edges and node attributes. We further propose theoretically grounded NID alignment strategies that ensure semantic consistency across views while preserving their distinct characteristics. Through comprehensive spectral analysis, we demonstrate that \textsc{AlignGAE} achieves optimal representation properties when the alignment loss converges. Extensive experiments across 12 benchmark datasets validate our approach, showing that \textsc{AlignGAE} outperforms state-of-the-art methods by up to 18.7\% on heterophilous graphs in node classification, while maintaining competitive performance on homophilous graphs. Our results establish a new paradigm for frequency-aware graph representation learning.

## Metadata
- **Published**: 2026-07-27T12:15:25Z
- **Authors**: Zengyi Wo, Shiyu Zhang, Qiyao Peng, Tianpeng Li, Xuan Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24338v1)