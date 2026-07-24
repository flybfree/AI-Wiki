---
title: Physics-Aware Complex-Valued State Space Model with Scattering-Prior Feature Modulation for PolSAR Image Classification
published: 2026-07-22T06:10:53Z
authors: Fangyan Zhang, Fan Zhang, Shiqi Zhou, Jun Ni, Carlos López-Martínez, Qiang Yin
url: http://arxiv.org/abs/2607.19787v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Physics-Aware Complex-Valued State Space Model with Scattering-Prior Feature Modulation for PolSAR Image Classification

## Abstract
Polarimetric synthetic aperture radar (PolSAR) image classification is a representative task for physics-aware GeoAI, where land-cover semantics are closely coupled with electromagnetic scattering mechanisms. Many existing complex-valued networks can preserve amplitude-phase information, but they are often limited in long-range spatial dependency modeling and usually incorporate polarimetric priors only as input-level or shallow auxiliary features. As a result, physical knowledge is insufficiently used to guide deep feature evolution. To address this issue, this paper proposes CV-SSMNet, a physics-aware complex-valued state-space network with scattering-aware feature modulation for PolSAR image classification. The proposed method builds a complex-valued state-space model (CV-SSM) in the original complex domain to capture long-range spatial dependencies while preserving polarimetric amplitude-phase coupling. Meanwhile, seven physically meaningful scattering priors, are encoded as FiLM-style modulation signals to adaptively recalibrate complex-valued representations during feature evolution. CV-SSMNet further integrates multi-scale complex convolutions, branch-wise CV-SSM encoding, prior-guided recalibration, and lightweight global context aggregation, enabling physically guided representation learning from local scattering structures to global spatial context. Experiments on three L-band benchmark datasets and an additional P-band BIOMASS evaluation demonstrate that CV-SSMNet achieves competitive accuracy, improved regional consistency, and better boundary preservation, supporting the effectiveness of embedding polarimetric scattering mechanisms into complex-valued long-range GeoAI representation learning.

## Metadata
- **Published**: 2026-07-22T06:10:53Z
- **Authors**: Fangyan Zhang, Fan Zhang, Shiqi Zhou, Jun Ni, Carlos López-Martínez, Qiang Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19787v1)