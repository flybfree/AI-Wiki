---
title: Rethinking Video Token Compression with a Global Codebook: Learning Once, Compressing Everywhere
published: 2026-08-02T14:24:13Z
authors: Jiayang He, Tianling Xu, Diancheng Kang, Huaide Jiang, Junyan Bai, Shaoming Zheng, Xuan Song
url: http://arxiv.org/abs/2608.01271v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking Video Token Compression with a Global Codebook: Learning Once, Compressing Everywhere

## Abstract
Video large language models (Video-LLMs) represent videos as dense sequences of visual tokens, whose length grows with the temporal and spatial extent of the input. These tokens often contain substantial redundancy arising from repeated visual patterns, leading to unnecessary computation in the subsequent language-model processing. Existing token compression methods, including pruning and merging, perform compression online during inference, repeatedly incurring additional computation for each input video and often relying on model-specific designs that limit their generality, we instead rethink this paradigm by shifting the costly compression process offline. We propose \textbf{ONCE}, a plug-in video token compression framework that introduces an offline-to-online paradigm: a frequency-aware global codebook is learned once in the visual feature space and reused for lightweight online compression through codebook lookup and aggregation, reducing repeated per-video computation and the need for model-specific compression designs. Extensive experiments across multiple video understanding benchmarks and against diverse compression baselines demonstrate that our approach achieves a strong accuracy-efficiency trade-off, maintaining competitive performance while achieving the lowest inference latency among compared methods.

## Metadata
- **Published**: 2026-08-02T14:24:13Z
- **Authors**: Jiayang He, Tianling Xu, Diancheng Kang, Huaide Jiang, Junyan Bai, Shaoming Zheng, Xuan Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01271v1)