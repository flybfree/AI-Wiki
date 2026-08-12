---
title: Beyond Detection Accuracy: Measuring Explanation Cost, Stability, and Utility for Resource-Aware IoT Intrusion Detection
published: 2026-08-11T01:18:07Z
authors: Abdurrahman Tolay
url: http://arxiv.org/abs/2608.10349v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Detection Accuracy: Measuring Explanation Cost, Stability, and Utility for Resource-Aware IoT Intrusion Detection

## Abstract
Machine-learning intrusion-detection studies commonly emphasize predictive accuracy while treating explanation generation as a computationally free post-processing step. This study jointly evaluates predictive effectiveness, explanation cost, local explanation stability, and selective explanation for binary Internet of Things (IoT) intrusion detection. A leakage-safe CICIoT2023 corpus was constructed using exact 39-feature hashes, non-finite-value handling, exact-feature deduplication, conservative label-collision removal, and deterministic hash-level partitioning. Logistic Regression, Decision Tree, Random Forest, and XGBoost were evaluated on natural and balanced test distributions. TreeSHAP cost was measured, stability was assessed under prediction-preserving perturbations, and validation-calibrated policies were used to allocate explanation workload. XGBoost provided the strongest overall predictive profile, while Random Forest produced the lowest false-positive rate. At 5,000 samples, TreeSHAP required 700.759 s for Random Forest and 1.471 s for XGBoost. Random Forest showed the strongest overall base-level explanation stability; XGBoost retained high rank and directional consistency but showed greater top-feature turnover and attribution-magnitude drift. On the balanced test, about 90% false-negative explanation coverage permitted 28-32% compute savings, while about 95% coverage permitted 15-23% savings. Savings were much smaller under the attack-heavy natural prevalence. These results show that operationally useful explainable IoT intrusion detection depends on predictive quality, explanation cost, local stability, workload prevalence, and selective invocation rather than detection accuracy alone.

## Metadata
- **Published**: 2026-08-11T01:18:07Z
- **Authors**: Abdurrahman Tolay
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10349v1)