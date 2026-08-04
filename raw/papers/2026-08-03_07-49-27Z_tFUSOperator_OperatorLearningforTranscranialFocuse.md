---
title: tFUSOperator: Operator Learning for Transcranial Focused Ultrasound Digital Twins
published: 2026-08-03T07:49:27Z
authors: Minjee Seo, Haris Ghafoor, Minju Seol, Seonaeng Cho, Kyungho Yoon
url: http://arxiv.org/abs/2608.01839v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# tFUSOperator: Operator Learning for Transcranial Focused Ultrasound Digital Twins

## Abstract
Transcranial focused ultrasound (tFUS) requires accurate estimation of the intracranial acoustic field, which is distorted by skull-induced aberrations. Numerical solvers are accurate but computationally expensive for digital twins, where the field must be re-estimated repeatedly as treatment conditions change. Existing deep-learning surrogates are fast but typically use voxel-to-voxel regression on a fixed grid, with no mechanism reflecting how acoustic energy propagates through the skull. We instead cast tFUS simulation as an operator learning problem and propose tFUSOperator, a coordinate-aware neural operator that maps the free-field pressure, skull anatomy, and treatment parameters to the intracranial field within a shared physical coordinate frame. To our knowledge, this is the first operator-based formulation of tFUS field prediction. On both seen and unseen skulls, the model localizes the acoustic focus accurately-reaching about 90% and 72% Dice, respectively-and it performs nearly as well from magnetic resonance (MR) as from computed tomography (CT) input while running $5.6 \times 10^4$ times faster than numerical simulation. These results suggest a fast, radiation-free route to safe and practical digital twins for patient-specific tFUS treatment. The code is available at: https://github.com/CMME-Lab/tFUSOperator.git.

## Metadata
- **Published**: 2026-08-03T07:49:27Z
- **Authors**: Minjee Seo, Haris Ghafoor, Minju Seol, Seonaeng Cho, Kyungho Yoon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01839v1)