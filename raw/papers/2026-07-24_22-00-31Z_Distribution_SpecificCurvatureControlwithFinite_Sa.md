---
title: Distribution-Specific Curvature Control with Finite-Sample Guarantees for Open-Weight Safety
published: 2026-07-24T22:00:31Z
authors: Domenic Rosati, Ali Dadsetan, Hong Huang, Xijie Zeng, Hassan Chowdhry, Subhabrata Majumdar, Hassan Sajjad, Frank Rudzicz
url: http://arxiv.org/abs/2607.22929v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distribution-Specific Curvature Control with Finite-Sample Guarantees for Open-Weight Safety

## Abstract
A short fine-tuning run can undo the safety guards of an open-weight model---retraining a refusal-trained assistant to aid weapons development or produce hate speech. Preventing such harmful fine-tuning while retaining benign adaptability remains difficult: the only prior method with an explicit curvature certificate, spectral deformation, inflates curvature globally and thereby obstructs benign adaptation along with harmful adaptation. We propose HarmAlign, which applies function-preserving spectral deformation along a estimated contrastive activation subspace. We derive finite-sample bounds for the estimated subspace energy and the resulting local harmful-distribution curvature lower bound. A stability--progress dichotomy for constant-step gradient descent turns the certified curvature into conditional convergence-rate control. Empirically, within a fixed-architecture, finite-budget first-order threat model, HarmAlign blocks direct fine-tuning and three data- or objective-adaptive attacks across a hazardous-knowledge relearning setting and a harmful-assistance fine-tuning setting, while the protected benign tasks remain trainable. The block persists across the tested first-order optimizer variants over every attack checkpoint, and under out-of-distribution harmful fine-tuning, and it extends to important cases in our threat model: accidental safety degradation and emergent misalignment.

## Metadata
- **Published**: 2026-07-24T22:00:31Z
- **Authors**: Domenic Rosati, Ali Dadsetan, Hong Huang, Xijie Zeng, Hassan Chowdhry, Subhabrata Majumdar, Hassan Sajjad, Frank Rudzicz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22929v1)