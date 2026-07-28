---
title: Patient-Agnostic Synthetic Pretraining for Efficient Patient-Specific Intraoperative 2D/3D Registration
published: 2026-07-25T19:39:54Z
authors: Minheng Chen, Youyong Kong
url: http://arxiv.org/abs/2607.23343v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Patient-Agnostic Synthetic Pretraining for Efficient Patient-Specific Intraoperative 2D/3D Registration

## Abstract
Intraoperative 2D/3D registration aligns preoperative CT volumes with intraoperative X-ray or fluoroscopic images and is essential for image-guided interventions. Recent learning-based and differentiable registration methods have shown promising accuracy, especially in patient-specific settings where abundant digitally reconstructed radiographs (DRRs) can be synthesized from the target CT. However, training a separate patient-specific model from scratch for every new patient is computationally inefficient and limits practical deployment. In this work, we propose an efficient patient-specific 2D/3D registration framework based on patient-agnostic synthetic pretraining and spherical similarity learning. The model is first pretrained on synthetic DRRs generated from multiple CT volumes to learn transferable pose-sensitive representations, and is then adapted to a new patient using only a limited number of synthetic projections from the target CT. To improve synthetic-to-real robustness without requiring anatomical labels, we introduce a segmentation-free domain randomization strategy that perturbs image intensity, projection physics, field-of-view, occlusion, and fluoroscopic artifacts. The adapted model provides an initial pose estimate, which is further refined using spherical similarity learning and differentiable Levenberg-Marquardt optimization. Experiments on multiple anatomical datasets evaluate whether patient-agnostic synthetic pretraining can improve the efficiency of patient-specific registration, with particular focus on the trade-off between adaptation cost and registration accuracy. The results demonstrate that patient-agnostic synthetic pretraining can significantly reduce patient-specific training requirements while preserving accurate intraoperative 2D/3D registration.

## Metadata
- **Published**: 2026-07-25T19:39:54Z
- **Authors**: Minheng Chen, Youyong Kong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23343v1)