---
title: PXDepth: Pixel-Space Modeling for Structure Preserving Monocular Depth Estimation
published: 2026-08-17T18:00:02Z
authors: Zhiyuan Yuan, Guanying Chen, Lingteng Qiu, Ruimao Zhang, Shuguang Cui, Xiaochun Cao
url: http://arxiv.org/abs/2608.16984v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PXDepth: Pixel-Space Modeling for Structure Preserving Monocular Depth Estimation

## Abstract
Recent monocular depth estimators achieve strong zero-shot generalization, yet often struggle to preserve fine-grained structures and object boundaries. We attribute this limitation to the prevalent combination of large-patch ViT encoders and convolutional decoders, as coarse tokenization can weaken pixel-level cues that upsampling cannot fully recover. To address this issue, we propose PXDepth, a discriminative monocular depth model that separates global context modeling from pixel-level depth prediction. Specifically, a large-patch ViT captures global scene context, while a pixel-space predictor composed of Context-Modulated Pixel Transformer blocks maintains high-resolution spatial representations throughout depth estimation. This design preserves fine structures and sharp boundaries without sacrificing global depth consistency. Across diverse zero-shot benchmarks, PXDepth combines faithful local geometry with competitive global depth accuracy while remaining efficient at inference. Our code and model are available at https://yuanzhy29.github.io/PXDepth-Page/.

## Metadata
- **Published**: 2026-08-17T18:00:02Z
- **Authors**: Zhiyuan Yuan, Guanying Chen, Lingteng Qiu, Ruimao Zhang, Shuguang Cui, Xiaochun Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16984v1)