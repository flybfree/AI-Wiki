---
title: Delta2Gamma: Band-Wise Adaptive Contrastive Learning of EEG for Alzheimer's Disease Detection
url: http://arxiv.org/abs/2608.17231v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_00-35-55Z_Delta2Gamma_Band_WiseAdaptiveContrastiveLearningof.md
generated_at: 2026-08-18 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Delta2Gamma, a self‑supervised framework for Alzheimer’s disease detection using EEG recordings that are typically noisy and unlabeled. The method decomposes each recording into five canonical neural rhythms—delta, theta, alpha, beta, and gamma—each processed by its own encoder and projection head. By adaptively balancing the temperature across bands during contrastive training, Delta2Gamma learns robust representations without requiring clinical labels.

## Key Takeaways
- The framework treats EEG as a multi‑band signal, assigning separate encoders to delta, theta, alpha, beta, and gamma rhythms for individualized learning.
- Adaptive temperature prediction balances the contribution of each band during contrastive training, ensuring bands with differing statistical properties are treated equally.
- On an ADFTD cohort evaluated under a leave‑one‑subject‑out protocol, Delta2Gamma achieves 92.4% accuracy, surpassing both supervised backbones and recent dedicated EEG methods.

## Context
Self‑supervised learning has become a cornerstone for medical imaging and signal analysis where labeled data are scarce or expensive to obtain. By applying contrastive techniques to multi‑band neural rhythms, Delta2Gamma demonstrates that deep representation learning can be effective even when clinical annotations are unavailable, highlighting the potential of unsupervised methods in neurodiagnostics.

## Implications
For clinicians, Delta2Gamma offers a low‑cost, scalable screening tool that could integrate into routine neurology workflows. For researchers, the adaptive temperature mechanism provides a practical solution to band imbalance, encouraging broader adoption of self‑supervised EEG analysis across diverse datasets and future studies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17231v1)
