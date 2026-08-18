---
title: ENAF: A Multi-Exit Network with an Adaptive Patch Fusion for Large Image Super Resolution
published: 2026-08-15T18:06:28Z
authors: Duong M. Nguyen, Tuan Nghia Nguyen, Xuan Truong Nguyen
url: http://arxiv.org/abs/2608.15349v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ENAF: A Multi-Exit Network with an Adaptive Patch Fusion for Large Image Super Resolution

## Abstract
To accelerate single image super-resolution (SISR) networks on large images (2K-8K), many recent approaches decompose an image into small patches and dynamically determine an execution path according to its difficulty (referred to as a dynamic network). To quantify the hardness of a patch, they mainly rely on a handcrafted assessment score, e.g., edge, which weakly associates a patch's texture with the computational complexity of a SISR model. To address the problem, we introduce ENAF - a dynamic network for SISR with an adaptive patch fusion. Built on top of a backbone, ENAF incorporates multiple early exits (EEs) to tackle the over-parameterized SISR model. More importantly, ENAF plugs a tiny network that estimates PSNR to associate data texture with a computation cost at an EE. Based on the scores, ENAF effectively assigns image patches to an exit, enhancing the quality-complexity trade-off. Extensive experiments on common datasets with popular SISR backbones demonstrate the effectiveness of ENAF in various settings. The source code is provided in https://github.com/nmduonggg/ENAF

## Metadata
- **Published**: 2026-08-15T18:06:28Z
- **Authors**: Duong M. Nguyen, Tuan Nghia Nguyen, Xuan Truong Nguyen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15349v1)