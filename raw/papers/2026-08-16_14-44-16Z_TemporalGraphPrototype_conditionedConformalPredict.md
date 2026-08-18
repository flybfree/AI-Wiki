---
title: Temporal Graph Prototype-conditioned Conformal Prediction for Fraud Detection
published: 2026-08-16T14:44:16Z
authors: Xudong Chen, Shengbo Gong, Lu Cheng, Wei Jin
url: http://arxiv.org/abs/2608.15768v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Temporal Graph Prototype-conditioned Conformal Prediction for Fraud Detection

## Abstract
Conformal prediction (CP) provides distribution-free coverage guarantees and has emerged as a principled tool for uncertainty quantification. In edge-level fraud detection on temporal interaction graphs, where false positives and false negatives both carry substantial cost, such coverage guarantees are particularly appealing for risk-aware decision making. However, directly applying existing graph conformal predictors yields inefficient prediction sets due to two recurring properties of fraud data. Fraudulent interactions are often embedded in benign-dominated neighborhoods that dilute calibration signals, while extreme class imbalance leaves scarce labeled-fraud support in the calibration split and leads to overly conservative class-conditional thresholds. To address these issues, we propose ProtoCP, a conformal prediction framework for edge-level fraud detection on temporal graphs. ProtoCP improves calibration efficiency by focusing calibration on fraud-relevant subgraph context and producing more stable nonconformity scores under class imbalance and temporal drift. Specifically, it leverages learned prototypes to suppress benign-dominated noise in the calibration context and introduces a neighborhood-relative scoring mechanism with temporal score diffusion for stable class-conditional calibration. Experiments on four fraud benchmarks (YelpChi, S-FFSD, FTFD, and BankSim) show that ProtoCP achieves the target coverage with consistently smaller prediction sets than state-of-the-art baselines. Our codes are available at https://github.com/Picard1701ent/ProtoCP.git

## Metadata
- **Published**: 2026-08-16T14:44:16Z
- **Authors**: Xudong Chen, Shengbo Gong, Lu Cheng, Wei Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15768v1)