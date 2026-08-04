---
title: Reassessing the Feasibility of PPG-Based Non-Invasive Blood Glucose Level Estimation
published: 2026-08-03T07:28:24Z
authors: Supraja Ramesh, Markus Neufeld, Michael Küttner, Tobias Röddiger, Michael Beigl
url: http://arxiv.org/abs/2608.01820v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reassessing the Feasibility of PPG-Based Non-Invasive Blood Glucose Level Estimation

## Abstract
Non-invasive blood glucose level (BGL) estimation from photoplethysmography (PPG) holds great promise for wearable health monitoring, but results across studies are hard to compare due to inconsistent datasets, data leakage, and non-standardized evaluation metrics. We present the first reproducible, extensible evaluation pipeline and use it to reassess five representative PPG-based BGL methods on published datasets under three increasingly strict data-split protocols: random window-level, participant-aware, and leave-some-participants-out (LSPO). Models appeared competitive under random splitting but collapsed under participant-aware and LSPO evaluation, with nearly all yielding near-zero or negative R$^2$ values comparable to a mean-prediction baseline. Critically, across every model and split, over 90% of predictions fell within clinically acceptable zones (Clarke Error Grid A+B), including the baseline. This reveals a fundamental disconnect: clinical zone metrics systematically conceal model failure in this domain. Our findings demonstrate that random train-test splits substantially overestimate the generalization of PPG-based BGL models due to sample-level data leakage, and that robust ML evaluation must precede clinical validation to meaningfully assess real-world utility.

## Metadata
- **Published**: 2026-08-03T07:28:24Z
- **Authors**: Supraja Ramesh, Markus Neufeld, Michael Küttner, Tobias Röddiger, Michael Beigl
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01820v1)