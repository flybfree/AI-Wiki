---
title: Uncertainty-Aware and Explainable Ensemble Deep Learning Framework for Multi-Class Skin Lesion Classification
published: 2026-08-11T10:55:14Z
authors: Rofiqul Islam, Lilatul Ferdouse
url: http://arxiv.org/abs/2608.11280v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Uncertainty-Aware and Explainable Ensemble Deep Learning Framework for Multi-Class Skin Lesion Classification

## Abstract
Skin cancer diagnosis from dermoscopic images remains challenging due to high intra-class variability, inter-class similarity, class imbalance, and the limited interpretability of deep learning models. This paper proposes an uncertainty-aware and explainable deep learning framework for multi-class skin lesion classification. The framework combines a vision transformer model (MaxViT-Tiny) with CNN-based models (ConvNeXt-Tiny and EfficientNetV2-B0) through deep ensemble learning. Monte Carlo (MC) Dropout estimates predictive uncertainty and identifies unreliable predictions, while Grad-CAM++, an explainable AI (XAI) technique, provides visual explanations by highlighting lesion regions that influence model decisions. Evaluated on the HAM10000 dataset, the framework achieves 96% accuracy and 99% ROC-AUC under uncertainty-aware filtering (entropy < 1.0, confidence >= 0.7), with macro-average precision, recall, and F1-score of 94%, 95%, and 95%, respectively, and 96% weighted-average scores across all three metrics. The results demonstrate accurate, interpretable, and uncertainty-aware skin lesion classification for trustworthy computer-aided diagnosis.

## Metadata
- **Published**: 2026-08-11T10:55:14Z
- **Authors**: Rofiqul Islam, Lilatul Ferdouse
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11280v1)