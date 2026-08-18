---
title: Hierarchical Adaptive Feature Refinement Network for VHR Remote Sensing Image Segmentation
published: 2026-08-16T09:26:58Z
authors: Shuaishuai Cao, Meng Tang, Shuwei Peng, Xuan Liu, Min Huang, Jie Chen, Jiacheng Niu, Yong Chen, Edore Akpokodje, Hui Lin
url: http://arxiv.org/abs/2608.15647v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hierarchical Adaptive Feature Refinement Network for VHR Remote Sensing Image Segmentation

## Abstract
Semantic segmentation of very-high-resolution (VHR) remote sensing imagery increasingly benefits from strong pretrained hierarchical encoders, yet exploiting their multi-stage representations remains difficult. Nearby regions demand different balances between fine detail and semantic context, aggressive task-specific transformations perturb useful pretrained features, and conventional semantic supervision provides limited structural guidance. We present HAFR-Net, a progressive refinement framework that adaptively organizes and conservatively refines hierarchical representations instead of replacing them with a monolithic decoder transformation. Heterogeneity-Guided Stage-Adaptive Fusion (HG-SAF) predicts dense stage weights conditioned on local feature variation. A Frequency-Residual Adapter (FRA) then injects frequency information through a bounded, zero-initialized residual branch that keeps the fused representation as its reference. A Confusion-Aware Tri-Prior Decoder (CATP) finally regularizes the prediction with boundary, objectness, and training-derived class-relation cues. Under a matched Swin-B training and single-scale inference protocol, HAFR-Net attains 84.12%, 87.86%, 55.17%, and 67.70% mIoU on ISPRS Vaihingen, ISPRS Potsdam, LoveDA, and OpenEarthMap, improving the matched UPerNet baseline by 0.55, 0.95, 1.55, and 1.84 percentage points, respectively. Controlled analyses further show consistent spatial reweighting beyond content-only routing, improved boundary and thin-structure accuracy over matched spatial and spectral alternatives, and reduced confusion on pre-declared class pairs.

## Metadata
- **Published**: 2026-08-16T09:26:58Z
- **Authors**: Shuaishuai Cao, Meng Tang, Shuwei Peng, Xuan Liu, Min Huang, Jie Chen, Jiacheng Niu, Yong Chen, Edore Akpokodje, Hui Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15647v1)