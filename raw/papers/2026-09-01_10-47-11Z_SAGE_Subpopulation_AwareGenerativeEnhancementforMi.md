---
title: SAGE: Subpopulation-Aware Generative Enhancement for Mitigating Spurious Correlations
published: 2026-09-01T10:47:11Z
authors: Yiming Luo, Rongqiang Zhao, Jie Liu
url: http://arxiv.org/abs/2609.01051v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAGE: Subpopulation-Aware Generative Enhancement for Mitigating Spurious Correlations

## Abstract
Spurious correlations pose a significant challenge to the robustness of modern machine learning. The inherent imbalance in dataset distributions often leads traditional Empirical Risk Minimization (ERM) models to rely on majority spurious attributes for classification, resulting in poor performance on minority groups. This problem becomes particularly challenging when the spurious attributes are unavailable. Existing group-label-free methods often upsample minority groups or misclassified real training examples; repeating the same instances can reduce effective diversity and encourage overfitting. To mitigate these spurious correlations from a data-centric perspective in the absence of prior knowledge, we introduce Subpopulation-Aware Generative Enhancement (SAGE), a two-stage generative augmentation framework. Using cluster-derived sub-labels and class labels, we fine-tune a conditional generative model and text encoder, generating targeted synthetic data to fill underrepresented regions in the training set and construct a balanced validation set for last-layer reweighting. We experimentally show that SAGE achieves 89.5%, 85.7%, and 79.1% worst-group accuracy on Waterbirds, CelebA, and MetaShift, respectively, outperforming the best group-label-free baselines by up to 7.7 percentage points.

## Metadata
- **Published**: 2026-09-01T10:47:11Z
- **Authors**: Yiming Luo, Rongqiang Zhao, Jie Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01051v1)