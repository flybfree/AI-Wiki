---
title: Explainable Hybrid Feature Selection for Intrusion Detection in Internet of Medical Things Environments
published: 2026-08-01T21:10:24Z
authors: Amira Berrezzek, Hayet Djellali, Giulio Mallardi, Lamia Mahnane
url: http://arxiv.org/abs/2608.00869v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Explainable Hybrid Feature Selection for Intrusion Detection in Internet of Medical Things Environments

## Abstract
Internet of Medical Things (IoMT) networks are hard to protect: devices are heterogeneous, computing resources are scarce, and traffic must be analyzed in real time. We present an intrusion detection system that addresses these constraints through feature selection. A Pearson correlation filter first removes redundant attributes; a hybrid strategy then combines model-based feature importance with SHAP attribution to pick a compact subset, on which we train Random Forest and LightGBM classifiers. SHAP and LIME explain what each retained feature contributes to the decisions. On CIC-IoMT 2024 and CIC-IDS 2017, the method cuts the feature space by up to 88% - from 40 to as few as 5 features - and accuracy and F1-score stay within a few points of models trained on all features. Compact, interpretable detectors of this kind are practical candidates for deployment on resource-limited medical networks.

## Metadata
- **Published**: 2026-08-01T21:10:24Z
- **Authors**: Amira Berrezzek, Hayet Djellali, Giulio Mallardi, Lamia Mahnane
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00869v1)