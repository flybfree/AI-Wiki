---
title: Bayes-Optimal BER and AUC: Estimation and Evaluation of Estimators
published: 2026-09-02T08:49:23Z
authors: Ryota Ushio, Takashi Ishida, Masashi Sugiyama
url: http://arxiv.org/abs/2609.02304v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bayes-Optimal BER and AUC: Estimation and Evaluation of Estimators

## Abstract
A fundamental quantity in machine learning is the optimal performance achievable by any model on a given task. Estimating this quantity allows us to distinguish the irreducible part of the error from a deficiency of the model, telling us how much room for improvement remains. Recent work has shown that the Bayes error, or equivalently the optimal accuracy, can be estimated from soft labels in binary classification. However, accuracy is often a poor summary of performance in settings with severe class imbalance or noisy annotations, where metrics such as the balanced error rate (BER) and the area under the ROC curve (AUC) are more appropriate. We address this gap with two complementary contributions. (i) Estimation. We propose soft-label-based estimators for the optimal BER and AUC. We first consider the clean setting in which true soft labels and the class prior are known, and then extend the estimators to a more realistic setting in which the class prior is unknown and the observed soft labels are corrupted by an unknown order-preserving transformation, possibly followed by additive noise. In the latter setting, we approximately recover the clean soft labels via isotonic regression with auxiliary hard labels, estimate the class prior with a clipped mean of the hard labels, and derive finite-sample error bounds for the resulting plug-in estimators. (ii) Evaluation. Since the optimum is unobservable on real datasets, evaluating any such estimator is itself nontrivial. We extend the FeeBee framework, originally proposed for evaluating Bayes-error estimators, to the optimal BER and AUC. The resulting procedure provides practical evaluation scores without requiring knowledge of the optimum, and applies to any estimator of the optimal BER or AUC, not only our proposed ones. Experiments on synthetic and real-world datasets validate both the estimators and the evaluation procedure.

## Metadata
- **Published**: 2026-09-02T08:49:23Z
- **Authors**: Ryota Ushio, Takashi Ishida, Masashi Sugiyama
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02304v1)