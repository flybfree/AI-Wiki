---
title: CARDIAG: A Dense Segment Classification Benchmark of Deep Learning Architectures for Coronary Angiography
url: http://arxiv.org/abs/2607.22139v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_09-35-18Z_CARDIAG_ADenseSegmentClassificationBenchmarkofDeep.md
generated_at: 2026-07-26 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CARDIAG, a benchmark for pixel-level classification of coronary angiograms into SYNTAX classes or background. It evaluates 24 deep learning architectures and reports that the ConvNeXt V2 encoder with DeepLab V3 Plus decoder achieves macro F1 0.456 while an ensemble improves to 0.479.

## Key Takeaways
- The benchmark includes 24 diverse architectures ranging from classic convnets to state-space vision models, providing a comprehensive evaluation of deep learning performance on coronary angiography segmentation.
- The top model reaches macro F1 0.456 and an ensemble with Mamba U-Net and Feature Pyramid Network raises it to 0.479, demonstrating strong accuracy in dense pixel classification.
- All evaluated methods are well calibrated across different patient demographics, vessel sides, and projection angles, highlighting robustness of the benchmark.

## Context
Coronary angiography segmentation is a key task in cardiovascular AI, yet existing datasets lack standardization, leading to inconsistent model comparisons. CARDIAG addresses this gap by offering a multi-center, multi-label dataset with detailed annotations.

## Implications
The release of CARDIAG enables researchers and clinicians to compare new architectures on a common ground, accelerating progress toward accurate lesion detection and disease assessment. Practitioners can rely on these metrics for trustworthy deployment in clinical workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22139v1)
