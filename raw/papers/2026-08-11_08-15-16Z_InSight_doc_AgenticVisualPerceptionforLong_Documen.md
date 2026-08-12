---
title: InSight-doc: Agentic Visual Perception for Long-Document Understanding
published: 2026-08-11T08:15:16Z
authors: Kaican Li, Weiyan Xie, Lewei Yao, Jiannan Wu, Lanqing Hong, Yongxiang Huang, Nevin L. Zhang
url: http://arxiv.org/abs/2608.10628v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# InSight-doc: Agentic Visual Perception for Long-Document Understanding

## Abstract
Long-document understanding often requires reasoning over many visually rich pages, making inference costly and prone to context rot. In this work, we propose InSight-doc, an agentic visual perception framework that treats visual resolution as an adaptive reasoning-time resource. InSight-doc starts from low resolution and selectively zooms into high-resolution regions for finer evidence, without relying on any external retriever. To train such an agent, we construct an active-perception corpus of 17.9K high-quality SFT examples with region-level zoom-in trajectories, accompanied by 19.2K hard RL examples. Through SFT+RL, InSight-doc-8B improves the baseline by 4.3--16.4 accuracy points over document VQA benchmarks. On long documents, it reduces hallucination by more than 40% and inference latency by 41%--68% while maintaining an accuracy lead. Our code, datasets, and model are released at https://github.com/m-Just/InSight-doc .

## Metadata
- **Published**: 2026-08-11T08:15:16Z
- **Authors**: Kaican Li, Weiyan Xie, Lewei Yao, Jiannan Wu, Lanqing Hong, Yongxiang Huang, Nevin L. Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10628v1)