---
title: ARD-REFSM: Enhancing Reflection Symmetry Detection with Asymmetric Denoising and Rotation Equivariance
published: 2026-07-30T09:40:10Z
authors: Dongfu Yin, Rourou Su, Cong Zhao, Fei Yu
url: http://arxiv.org/abs/2607.27927v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ARD-REFSM: Enhancing Reflection Symmetry Detection with Asymmetric Denoising and Rotation Equivariance

## Abstract
Reflection symmetry detection remains challenging due to interference from asymmetric regions and arbitrary orientations of symmetric patterns. Asymmetric regions introduce background clutter that disrupts symmetric pattern matching, whereas conventional convolutional neural networks lack rotation equivariance, leading to inconsistent feature representations under rotational transformations. To address these issues, we propose an Asymmetric Region Denoising (ARD) module and a Rotation Equivariant Feature Similarity Matching (REFSM) module. The ARD module suppresses asymmetric interference to refine symmetric patterns, while the REFSM module enhances rotation equivariance through feature similarity matching between original and rotated images. Specifically, our dual-input REFSM framework leverages rotation loss to maximize consistency between the score maps of original and rotated images, thereby enabling precise prediction of rotation-equivariant symmetry axes. Furthermore, we introduce GMSYM, a new benchmark dataset that categorizes images into diverse scenarios and incorporates various interferences to address the limitations of existing reflection symmetry detection benchmarks. Extensive experiments on four standard datasets (DENDI, NYU, LDRS, SDRW) and our proposed GMSYM dataset demonstrate that our method achieves state-of-the-art performance in both accuracy and robustness.

## Metadata
- **Published**: 2026-07-30T09:40:10Z
- **Authors**: Dongfu Yin, Rourou Su, Cong Zhao, Fei Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27927v1)