---
title: Dual Co-Train: Cross-Dataset Ultrasound Tongue Segmentation Under Extreme Data Scarcity
published: 2026-08-18T16:31:08Z
authors: Alisher Myrgyyassov, Zhen Song, Bruce Xiao Wang, Yu Sun, Min Ney Wong, Yihao Zhou, Yongping Zheng
url: http://arxiv.org/abs/2608.17983v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dual Co-Train: Cross-Dataset Ultrasound Tongue Segmentation Under Extreme Data Scarcity

## Abstract
Ultrasound tongue contour segmentation remains challenging under cross-dataset domain shift, where limited annotations, probe variability, and acquisition noise often degrade model generalization. We present a source-free domain adaptation framework for robust ultrasound tongue segmentation built on a lightweight UltraUNet backbone. Starting from a checkpoint pretrained on only five labeled source images, simulating an underfitted constrained source model, the proposed method adapts to a fully-unlabeled target domain by iteratively refining pseudo-labels, filtering unreliable masks with a contour-based quality-control module, and generating target-style synthetic image-mask pairs through a segmentation-guided conditional GAN. The student model is then trained on a mixture of clean pseudo-labeled target images, noisy pseudo-labels with consistency regularization, and synthetic samples, enabling closed-loop adaptation without access to source data. We evaluate the method on 12 source-target transfer pairs across eight ultrasound tongue imaging datasets, and conduct source-size scaling experiments and ablation studies. Across all comparisons, the proposed framework improves segmentation overlap and contour accuracy over the baselines, including supervised ones. These results suggest that task-specific pseudo-label refinement and synthetic target-style augmentation can substantially improve source-free adaptation for ultrasound tongue imaging.

## Metadata
- **Published**: 2026-08-18T16:31:08Z
- **Authors**: Alisher Myrgyyassov, Zhen Song, Bruce Xiao Wang, Yu Sun, Min Ney Wong, Yihao Zhou, Yongping Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17983v1)