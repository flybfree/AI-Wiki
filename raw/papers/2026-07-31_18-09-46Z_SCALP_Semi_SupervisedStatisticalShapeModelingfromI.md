---
title: SCALP: Semi-Supervised Statistical Shape Modeling from Imperfect 3D Photogrammetry via Landmark-Anchored Spectral Warp
published: 2026-07-31T18:09:46Z
authors: Nawazish Khan, Sanjay Bhandari, Sarang Joshi, Alzbeta Novotna, Tiffany Jeong, Loretta Bowman, Michael Hernandez, Tobi Somorin, Viraj Govani, Jesse Glodstein, Shireen Elhabian
url: http://arxiv.org/abs/2608.00187v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCALP: Semi-Supervised Statistical Shape Modeling from Imperfect 3D Photogrammetry via Landmark-Anchored Spectral Warp

## Abstract
Correspondence-based statistical shape modeling (SSM) is vital for population-level morphometric analysis, but conventional pipelines assume clean, fully registered surfaces. Real-world clinical photogrammetry scans are often noisy, partial, and cluttered, hindering the adoption of radiation-free surface imaging as a safe alternative to computed tomography (CT) for infant craniosynostosis. We present SCALP (Semi-supervised Correspondence via lAndmark Localization and sPectral warping), a two-stage framework that constructs consistent shape models directly from raw, imperfect surface scans. First, a semi-supervised Point Transformer leverages a small expert-annotated dataset alongside a large unlabeled cohort to accurately localize craniofacial landmarks with minimal annotation overhead. Second, these landmarks anchor a Laplace--Beltrami spectral deformation of an anatomical template, generating dense correspondences while naturally isolating the cranium from peripheral scanning clutter without manual preprocessing. Experiments on infant photogrammetry scans demonstrate that SCALP consistently outperforms state-of-the-art unsupervised point-cloud approaches, offering a clinically practical pathway toward objective, radiation-free head shape analysis.

## Metadata
- **Published**: 2026-07-31T18:09:46Z
- **Authors**: Nawazish Khan, Sanjay Bhandari, Sarang Joshi, Alzbeta Novotna, Tiffany Jeong, Loretta Bowman, Michael Hernandez, Tobi Somorin, Viraj Govani, Jesse Glodstein, Shireen Elhabian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00187v1)