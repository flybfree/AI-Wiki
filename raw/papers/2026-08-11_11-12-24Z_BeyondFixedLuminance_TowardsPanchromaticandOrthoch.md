---
title: Beyond Fixed Luminance: Towards Panchromatic and Orthochromatic Image Colorization
published: 2026-08-11T11:12:24Z
authors: Swarnim Maheshwari, Syed Imam Ali, Vineeth N. Balasubramanian
url: http://arxiv.org/abs/2608.10798v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Fixed Luminance: Towards Panchromatic and Orthochromatic Image Colorization

## Abstract
Most image colorization systems operate in $Lab$ space by predicting chroma ($ab$) while preserving an input-derived luminance channel ($L$). While effective on standard benchmarks, this fixed-luminance design restricts brightness changes and becomes unreliable when grayscale formation deviates from natural-image luminance, as in historical orthochromatic photography. We propose a luminance-agnostic colorization framework that formulates colorization as full-RGB image editing using a foundation image-editing model. To bridge modern panchromatic and historical orthochromatic conditions, we introduce a mixed grayscale objective that trains the model under both standard luminance grayscale and a red-insensitive grayscale formation. Experiments on COCO, ImageNet, and a multi-instance benchmark show that our method is competitive on standard grayscale inputs and substantially more robust under orthochromatic inputs, with qualitative comparisons and a human study indicating fewer visible color artifacts.

## Metadata
- **Published**: 2026-08-11T11:12:24Z
- **Authors**: Swarnim Maheshwari, Syed Imam Ali, Vineeth N. Balasubramanian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10798v1)