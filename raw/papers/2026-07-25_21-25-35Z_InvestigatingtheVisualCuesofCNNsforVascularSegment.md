---
title: Investigating the Visual Cues of CNNs for Vascular Segmentation: A Case Study in Microscopy and Fundus Imaging
published: 2026-07-25T21:25:35Z
authors: Weslley dos Santos Silva, Cesar Henrique Comin
url: http://arxiv.org/abs/2607.23371v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Investigating the Visual Cues of CNNs for Vascular Segmentation: A Case Study in Microscopy and Fundus Imaging

## Abstract
Vascular segmentation is a standard procedure for clinical diagnosis, yet the specific visual features determining model decisions remain poorly understood. This paper investigates the visual cues Convolutional Neural Networks (CNNs) use to segment blood vessels across two distinct imaging domains: fluorescence microscopy and retinal fundus photography. We employ a series of experiments to quantify the influence of shape, texture, and receptive field on segmentation performance. First, we isolate texture and intensity by evaluating performance on patches subjected to pixel shuffling and normalization. Second, we assess global shape relevance by training models on sparse contours and centerlines. Lastly, we quantify the required spatial context by systematically varying the network's theoretical and effective receptive fields. Within the scope of the evaluated datasets, we found that pixel intensity is more relevant than texture, though networks maintain surprisingly high accuracy even when both cues are removed. Furthermore, CNNs struggle to extrapolate full vessel geometry from shape cues alone, typically relying on a relatively small effective receptive field of around 20 pixels, though global context provides a modest benefit for fundus images. While specific to the modalities studied, this methodology offers a quantitative foundation to audit and refine deep learning systems in vascular imaging.

## Metadata
- **Published**: 2026-07-25T21:25:35Z
- **Authors**: Weslley dos Santos Silva, Cesar Henrique Comin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23371v1)