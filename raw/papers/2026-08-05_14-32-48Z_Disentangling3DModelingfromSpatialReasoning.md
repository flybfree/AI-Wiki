---
title: Disentangling 3D Modeling from Spatial Reasoning
published: 2026-08-05T14:32:48Z
authors: Haoze Sun, Jiequan Cui, Qingshan Xu, Richang Hong
url: http://arxiv.org/abs/2608.05242v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Disentangling 3D Modeling from Spatial Reasoning

## Abstract
In this work, we explore an alternative paradigm for spatial reasoning by explicitly disentangling 3D perception from reasoning, rather than jointly acquiring implicit 3D perception and reasoning through large-scale training. Our key observation is that modern perception models excel at estimating continuous 3D geometry, whereas large language models (LLMs) are particularly effective at compositional and symbolic reasoning. Motivated by these complementary strengths, we propose the Disentangled Spatial Reasoner (DiSR), a simple yet effective framework that reconstructs the physical world into structured 3D evidence using off-the-shelf expert perception models and fine-tunes an LLM with LoRA to perform reasoning solely over this explicit geometric evidence. Without large-scale 3D VQA training or complex tool-use policies, DiSR achieves competitive performance on popular spatial reasoning benchmarks. Beyond its strong performance, DiSR offers improved interpretability, modularity, and computational efficiency, demonstrating that explicit separation of perception and reasoning is a scalable and effective alternative paradigm to end-to-end modeling for spatial intelligence.

## Metadata
- **Published**: 2026-08-05T14:32:48Z
- **Authors**: Haoze Sun, Jiequan Cui, Qingshan Xu, Richang Hong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05242v1)