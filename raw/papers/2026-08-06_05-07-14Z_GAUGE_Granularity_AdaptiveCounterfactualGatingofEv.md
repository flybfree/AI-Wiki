---
title: GAUGE: Granularity-Adaptive Counterfactual Gating of Evidence for Incomplete Multimodal Classification
published: 2026-08-06T05:07:14Z
authors: Yunping Shi, En Yu, Kairui Guo, Jie Lu
url: http://arxiv.org/abs/2608.05608v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GAUGE: Granularity-Adaptive Counterfactual Gating of Evidence for Incomplete Multimodal Classification

## Abstract
Multimodal classification typically assumes all modalities are available, yet real-world inputs are often incomplete. Imputation and dynamic fusion can mitigate such incompleteness, but existing methods operate at a coarse modality level and thus cannot retain reliable components while suppressing misleading ones within the same recovered modality, compromising prediction reliability. To address this issue, we propose GAUGE, a lightweight counterfactual gating framework for incomplete multimodal classification. GAUGE first imputes missing modalities with a frozen imputer and encodes observed and recovered inputs uniformly as fine-grained evidence units. Rather than intervening on each unit explicitly, GAUGE scores the counterfactual effect of replacing every unit with a reference representation through prediction-aware Taylor evidence scores, all obtained in a single forward-backward pass. These scores are mapped to continuous gates, which are converted into additive attention-logit biases for unit-wise evidence modulation without altering the backbone architecture. Experiments across six benchmarks demonstrate that GAUGE outperforms strong baselines across diverse incomplete-input settings. Furthermore, a Taylor remainder theoretical analysis characterizes the error of the first-order approximation relative to the exact counterfactual effect, establishing GAUGE as a principled and scalable framework for fine-grained evidence control under modality incompleteness.

## Metadata
- **Published**: 2026-08-06T05:07:14Z
- **Authors**: Yunping Shi, En Yu, Kairui Guo, Jie Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05608v1)