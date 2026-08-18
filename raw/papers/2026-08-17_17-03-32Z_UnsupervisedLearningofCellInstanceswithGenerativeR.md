---
title: Unsupervised Learning of Cell Instances with Generative Routing Pyramids
published: 2026-08-17T17:03:32Z
authors: Ziwen Liu, Martin Weigert
url: http://arxiv.org/abs/2608.16810v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unsupervised Learning of Cell Instances with Generative Routing Pyramids

## Abstract
Identifying and representing object instances such as cells or nuclei is a common task in microscopy image analysis. Established machine learning workflows typically use supervised detection or segmentation followed by feature extraction or classification, which requires manual annotations and treats instance segmentation and cell representation as separate stages. We describe a new unsupervised method for cell instance segmentation and phenotypic classification from unlabeled microscopy images. Our method is based on reconstructing each image using a coarse-to-fine routing pyramid that associates pixels with spatially sparse latent sources. The resulting pixel-to-latent associations yield instance masks, while the source latents encode cell morphology. We demonstrate competitive performance in instance segmentation across diverse cell morphologies and imaging modalities, as well as generative modeling of cellular phenotypes under perturbations. Source code and checkpoints are available at https://github.com/weigertlab/routing-pyramids.

## Metadata
- **Published**: 2026-08-17T17:03:32Z
- **Authors**: Ziwen Liu, Martin Weigert
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16810v1)