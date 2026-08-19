---
title: Dual Co-Train: Cross-Dataset Ultrasound Tongue Segmentation Under Extreme Data Scarcity
url: http://arxiv.org/abs/2608.17983v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_16-31-08Z_DualCo_Train_Cross_DatasetUltrasoundTongueSegmenta.md
generated_at: 2026-08-18 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Dual Co‑Train, a source‑free domain adaptation framework for ultrasound tongue segmentation that works with only five labeled source images. By iteratively refining pseudo‑labels, filtering masks, and generating synthetic target‑style samples, the method achieves strong performance across twelve transfer pairs without access to the source data.

## Key Takeaways
- The framework starts from a lightweight UltraUNet pretrained on five source images, simulating an underfitted constrained model that cannot be directly used for adaptation.  
- It refines pseudo‑labels using a contour‑based quality‑control module and creates synthetic image‑mask pairs via a segmentation‑guided conditional GAN to simulate the target domain.  
- The student model is trained on a mixture of clean pseudo‑labeled targets, noisy pseudo‑labels with consistency regularization, and synthetic samples, enabling closed‑loop adaptation.

## Context
Ultrasound tongue imaging suffers from severe data scarcity and probe variability, limiting the use of standard supervised models that require large labeled datasets. This work addresses the need for robust domain transfer when source annotations are unavailable, a common challenge in medical imaging where each scan is unique.

## Implications
The results demonstrate that task‑specific pseudo‑label refinement and synthetic augmentation can markedly boost adaptation accuracy, offering practitioners a practical solution to deploy ultrasound segmentation tools on new scanners. This could reduce reliance on costly re‑annotation pipelines and accelerate clinical deployment of AI‑based diagnostic tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17983v1)
