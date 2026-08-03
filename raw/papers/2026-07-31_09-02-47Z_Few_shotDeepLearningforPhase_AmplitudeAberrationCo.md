---
title: Few-shot Deep Learning for Phase-Amplitude Aberration Correction in Transcranial Focused Ultrasound
published: 2026-07-31T09:02:47Z
authors: Minju Seol, Minjee Seo, Seonaeng Cho, Kyungho Yoon
url: http://arxiv.org/abs/2607.29182v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Few-shot Deep Learning for Phase-Amplitude Aberration Correction in Transcranial Focused Ultrasound

## Abstract
Transcranial focused ultrasound (tFUS) is a non-invasive technique that delivers focused acoustic energy through the skull for neuromodulation and therapeutic applications. However, the heterogeneous structure of the skull induces complex, patient-specific phase and amplitude aberrations that distort the acoustic focus and deviate it from the intended target, compromising therapeutic efficacy and safety. Conventional time-reversal (TR) simulations can correct these aberrations but rely on computationally expensive full-wave solvers, making them impractical for real-time use and iterative treatment planning. We propose a few-shot deep surrogate framework that predicts per-element phase and amplitude corrections for a 96-element 3D phased-array transducer from patient CT images. A geometry-aware encoder extracts skull-path features shared across dedicated phase classification and amplitude regression branches, where phase periodicity is handled via circular expectation decoding. The framework is pretrained on diverse skull geometries and fine-tuned with only ten target points, enabling rapid adaptation to unseen patients without full patient-specific simulation. Evaluated via leave-one-out cross-validation across 12 skulls, it achieves a mean phase CMAE of 0.155 rad and amplitude rMAE of 9.089%, a focal centroid error of 0.467 mm, Dice score of 94.422%, and peak pressure ratio of 92.332%, with an approximately 2,535 times speedup over TR simulation. The code is available at https://github.com/Minju-Seol/fewshot-tfus-correction.

## Metadata
- **Published**: 2026-07-31T09:02:47Z
- **Authors**: Minju Seol, Minjee Seo, Seonaeng Cho, Kyungho Yoon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29182v1)