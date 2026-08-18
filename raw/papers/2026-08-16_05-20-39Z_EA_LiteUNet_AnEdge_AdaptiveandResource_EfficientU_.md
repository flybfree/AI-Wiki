---
title: EA-LiteUNet: An Edge-Adaptive and Resource-Efficient U-Net for Boundary-Sensitive Dermoscopic Image Segmentation
published: 2026-08-16T05:20:39Z
authors: Wang Jiangtao, Nur Intan Raihana Ruhaiyem, Fu Panpan, Yang Yu, Huang Yan
url: http://arxiv.org/abs/2608.15537v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EA-LiteUNet: An Edge-Adaptive and Resource-Efficient U-Net for Boundary-Sensitive Dermoscopic Image Segmentation

## Abstract
Accurate boundary delineation remains a persistent challenge in dermoscopic image segmentation because of blurred lesion margins, heterogeneous textures, and complex background artifacts. From a signal-processing perspective, lesion boundaries represent high-frequency components that are highly susceptible to aliasing, noise amplification, and information loss. Consequently, repeated downsampling and feature transformations in conventional convolutional architectures often lead to severely degraded boundary representations. To address these limitations, we propose EA-LiteUNet, an edge-adaptive and computationally efficient U-Net variant specifically designed for boundary-sensitive medical image segmentation. The architecture integrates three core mechanisms: (1) boundary-aware representation learning to suppress aliasing and preserve high-frequency structural details; (2) attention-guided feature modulation to selectively enhance boundary-relevant responses across multi-scale features; and (3) a resource-adaptive inference strategy to dynamically balance segmentation accuracy and computational efficiency. Extensive evaluations across three public dermoscopic datasets demonstrate that EA-LiteUNet consistently achieves superior boundary precision. Specifically, on the ISIC 2018 dataset, the method significantly reduces the 95% Hausdorff Distance (HD95) to 12.89 pixels while maintaining a robust Dice score of 92.08%. Notably, this strong performance is achieved with an ultralightweight configuration of merely 0.29M parameters and 1.17 GFLOPs. Ablation studies further validate the complementary effects of these components, confirming their contribution to enhanced boundary fidelity and stable optimization.

## Metadata
- **Published**: 2026-08-16T05:20:39Z
- **Authors**: Wang Jiangtao, Nur Intan Raihana Ruhaiyem, Fu Panpan, Yang Yu, Huang Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15537v1)