---
title: BATS: Resource-Efficient Volumetric Segmentation with Boundary-Aware Mixed-Resolution Tokens
published: 2026-07-29T12:21:40Z
authors: David Hagerman, Roman Naeem, Fredrik Kahl
url: http://arxiv.org/abs/2607.26829v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BATS: Resource-Efficient Volumetric Segmentation with Boundary-Aware Mixed-Resolution Tokens

## Abstract
Many high-performing volumetric segmentation models maintain dense multi-scale feature maps, leading to high activation memory and inference cost. We present BATS (Boundary-Aware Token Selection), a 3D medical image segmentation architecture that concentrates fine-resolution processing near predicted class boundaries. A dense boundary predictor identifies where additional resolution is needed, while a fine-first context cascade constructs an input-dependent mixed-resolution hierarchy. Homogeneous regions are represented coarsely, with finer tokens retained around boundaries, thin structures, and small targets. The sparse hierarchy is refined and rasterised into a dense segmentation.   BATS predicts boundary relevance independently at every resolution level, preventing an erroneous coarse-scale decision from suppressing fine-scale evidence. Parent cluster attention further injects hierarchical ancestor tokens into local attention neighbourhoods, providing cross-scale context without dense multi-scale feature maps or cross-scale neighbour search.   We evaluate BATS on five public CT and MRI datasets using the standardised nnU-Net Revisited protocol. BATS achieves the highest LiTS Dice among the compared methods and averages within 0.37 Dice points of the strongest dense baseline, MedNeXt-L, across the five datasets. Relative to MedNeXt-L, it reduces peak allocated GPU memory by more than 53% on KiTS, LiTS, and BraTS. Inference is up to 30% faster on KiTS and LiTS, which retain fewer tokens, but slower on the more token-dense BraTS. Mixed-resolution processing therefore provides consistent memory savings, while runtime and accuracy gains depend on dataset boundary density.

## Metadata
- **Published**: 2026-07-29T12:21:40Z
- **Authors**: David Hagerman, Roman Naeem, Fredrik Kahl
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26829v1)