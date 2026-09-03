---
title: RouteGraph-Mona: Confusion-Aware Routing Fine-Tuning for Mineral Image Classification
published: 2026-09-02T08:29:08Z
authors: Jierui Li, Zhiyuan Qi, Hao Zhu, Yufan Liu, Jixian Liu, Shaojie Jiang, Jianda Wang, Yaqi Liu, Xiaotong Li, Wei Wang
url: http://arxiv.org/abs/2609.02282v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RouteGraph-Mona: Confusion-Aware Routing Fine-Tuning for Mineral Image Classification

## Abstract
Mineral image classification is important for geological exploration and resource development, but it remains challenging due to substantial intra-class variations in appearance and high inter-class visual similarity. Multi-cognitive Visual Adapter (Mona) is a vision-oriented parameter-efficient adapter that adapts pre-trained visual models by tuning only a few parameters. However, Mona statically aggregates responses from multiple scales, limiting its ability to accommodate sample-specific scale preferences and model confusion among visually similar mineral categories. To address this issue, we propose \textbf{RouteGraph-Mona}, a lightweight route-space regularization method built on Mona. Specifically, we replace Mona's static multi-scale aggregation with sample-adaptive routing. The resulting branch-selection behavior defines a compact routing space that captures each image's scale preferences. We then regularize the resulting routing signatures with class-wise route anchors and confusion-weighted margins. The route anchors encourage class-consistent routing patterns, while the margins promote greater separation between visually similar categories in the routing space. Experiments on three public mineral image datasets with two visual backbones show that RouteGraph-Mona consistently outperforms Mona in mean accuracy and remains competitive with representative fine-tuning methods and mineral image classification baselines.

## Metadata
- **Published**: 2026-09-02T08:29:08Z
- **Authors**: Jierui Li, Zhiyuan Qi, Hao Zhu, Yufan Liu, Jixian Liu, Shaojie Jiang, Jianda Wang, Yaqi Liu, Xiaotong Li, Wei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02282v1)