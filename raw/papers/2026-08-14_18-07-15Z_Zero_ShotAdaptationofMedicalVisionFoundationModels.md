---
title: Zero-Shot Adaptation of Medical Vision Foundation Models for High-Frequency Micro-Ultrasound Prostate Segmentation
published: 2026-08-14T18:07:15Z
authors: Ayusha Abbas, Saram Abbas, Kabita Adhikari
url: http://arxiv.org/abs/2608.14796v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Zero-Shot Adaptation of Medical Vision Foundation Models for High-Frequency Micro-Ultrasound Prostate Segmentation

## Abstract
Prostate cancer claims a life every 80 seconds. Early detection is needed to prevent disease progression, and both PSA density calculation and biopsy decisions rely on knowing the exact boundary of the gland. Conventional ultrasound at 6-12 MHz blurs this boundary, missing one in three high-risk cancers. Micro-ultrasound (29 MHz) improves resolution threefold but introduces dense acoustic speckle that obscures the outer wall; given the same image, two clinicians draw outlines differing by over 10% in area. Supervised methods are costly and generalise poorly across scanners. Can a foundation model segment the prostate with no training data?   We present the first zero-shot pipeline for this modality: MedSAM, pre-trained on over 1.5 million medical images, localises the prostate; we then apply CLAHE to sharpen the outer wall, binary dilation to recover missed pixels, and Fourier smoothing (4 modes, s=1.05) to refine the boundary. MedSAM requires a spatial prompt, so we evaluate bounding-box and point-click strategies across 75 patients of the Micro-Ultrasound Prostate Segmentation dataset (2,621 slices).   On the 20-patient held-out test set, the pipeline reduces mean boundary-distance error by 45% (Dice 0.749+/-0.043 to 0.865+/-0.029; HD95 217.2+/-36.9 to 120.1+/-26.1 px), reaching Dice 0.859 across the cohort. Its mean overlap shows no significant difference from the three non-expert rater groups (p>0.19), while segmenting 38-52% more consistently (lower inter-patient standard deviation). Point-click prompts fail regardless of placement (best Dice=0.350), because speckle gives no stable local contrast. Only an approximate bounding box is required, so any clinic can deploy it without data collection, annotation, or retraining.

## Metadata
- **Published**: 2026-08-14T18:07:15Z
- **Authors**: Ayusha Abbas, Saram Abbas, Kabita Adhikari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14796v1)