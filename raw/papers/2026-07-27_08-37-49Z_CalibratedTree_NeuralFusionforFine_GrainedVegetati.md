---
title: Calibrated Tree-Neural Fusion for Fine-Grained Vegetation Community Classification
published: 2026-07-27T08:37:49Z
authors: Dristi Datta, Md Khalid Hasan Sakib, Manoranjan Paul
url: http://arxiv.org/abs/2607.24160v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Calibrated Tree-Neural Fusion for Fine-Grained Vegetation Community Classification

## Abstract
Accurate vegetation-community classification is essential for ecological monitoring, habitat assessment, and evidence-based environmental management in heterogeneous landscapes. Existing studies often rely on standalone tree ensembles or generic neural networks, although fine-grained ecological classes frequently exhibit overlapping spectral, topographic, and structural characteristics. Many frameworks also provide limited protection against stacking leakage, insufficient probability calibration, weak minority-class evaluation, and little evidence of stability across repeated data splits. To address these limitations, this study proposes Calibrated EcoTreeFuseNet-Plus, a tree-neural probability-fusion framework that combines out-of-fold tree probabilities, EcoFuseNet-V2 outputs, validation-selected meta-learning, and post-hoc temperature scaling. Raster values from six LiDAR-derived terrain and canopy variables and two hyperspectral vegetation indices were extracted at coordinate-based reference locations. Quality control removed 26 samples with missing elevation and one sample with non-finite NDWI, producing 1,833 complete records across 29 vegetation and non-vegetation classes. On the held-out test set, the proposed model achieved an accuracy of 0.8000, a macro F1-score of 0.7768, a balanced accuracy of 0.7903, and an MCC of 0.7903. Calibration reduced the expected calibration error from 0.3866 to 0.0651 without changing class predictions. Five-seed evaluation yielded a macro F1-score of 0.7717 +/- 0.0112, indicating stable performance across repeated splits. The results demonstrate a reliable discrimination-calibration trade-off for small-sample, fine-grained ecological classification.

## Metadata
- **Published**: 2026-07-27T08:37:49Z
- **Authors**: Dristi Datta, Md Khalid Hasan Sakib, Manoranjan Paul
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24160v1)