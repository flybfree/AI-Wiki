---
title: DualMiT-Net: Local-Global Transformer-Convolutional Fusion for Breast Mass Segmentation in Mammographic Regions of Interest
published: 2026-08-15T04:08:26Z
authors: Alibek Kamiluly, Milana Muratova, Yash Patel, Fan Li
url: http://arxiv.org/abs/2608.15019v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DualMiT-Net: Local-Global Transformer-Convolutional Fusion for Breast Mass Segmentation in Mammographic Regions of Interest

## Abstract
Breast mass segmentation is an important step in computer-aided mammography, but it remains difficult because masses can have low contrast, irregular shapes, and boundaries that blend with surrounding breast tissue. To address this problem, we present DualMiT-Net, a dual-branch network that uses both a focused view of the mass and a wider view of the surrounding tissue. The local branch uses a Mix Transformer (MiT-B5) encoder to learn mass shape, texture, and boundary information, while the global branch uses an EfficientNet-B5 encoder to learn surrounding breast context. Features from the two branches are shared at the deeper encoder levels and are then progressively fused in a single decoder. A spatial gate controls how much global information is added during decoding. We also evaluated four input representations and selected a percentile-windowed mammogram combined with a Gabor texture response. The model was trained and evaluated on the mass subset of the Curated Breast Imaging Subset of the Digital Database for Screening Mammography (CBIS-DDSM) using a patient-level split. Across three training runs, DualMiT-Net with exponential moving average weights achieved a mean Dice coefficient of 0.9375 and a mean Intersection over Union of 0.8834. It also achieved better Dice and IoU scores than six standard encoder-decoder baselines trained using the same data and training settings. These results show that combining local mass information with wider breast context can provide accurate and consistent breast mass segmentation.

## Metadata
- **Published**: 2026-08-15T04:08:26Z
- **Authors**: Alibek Kamiluly, Milana Muratova, Yash Patel, Fan Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15019v1)