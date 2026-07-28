---
title: Harmonized Interpretable ECG Waveform Features for Robust Cross-Dataset Clinical Prediction
published: 2026-07-26T02:04:13Z
authors: Jie Lin, Weijie Sun, Sunil V. Kalmady, Anita Khalafbeigi, Abram Hindle, Padma Kaul, Russell Greiner
url: http://arxiv.org/abs/2607.23412v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Harmonized Interpretable ECG Waveform Features for Robust Cross-Dataset Clinical Prediction

## Abstract
Electrocardiograms (ECGs) are widely used for cardiovascular risk prediction, yet models often fail to transfer across hospitals because of protocol, population, and measurement differences. We benchmark cross-dataset generalization on three tasks - heart failure classification, 30-day all-cause mortality, and 30-day mortality among sinus-rhythm ECGs - using two large cohorts (MIMIC-IV and the Alberta Cohort). To reduce vendor-specific measurement mismatch, we build a harmonized, interpretable feature representation computed directly from raw waveforms: FeatureDB morphology/heart-rate-variability summaries plus compact time-frequency descriptors (autoregressive and wavelet features). We train XGBoost models on this unified feature space and evaluate with patient-disjoint internal and bidirectional external testing. We pre-specify two hypotheses: (H1) external AUROC retains at least 90% of source-site internal AUROC under transfer, and (H2) internal AUROC of the harmonized feature set stays within 10% of dataset-native machine-measurement models. Across tasks, internal AUROC is 0.79-0.82 and cross-dataset AUROC is 0.74-0.78, with larger and direction-dependent AUPRC shifts under transfer. As an exploratory benchmark, an end-to-end ConvNeXt model trained directly on raw ECG waveforms with age and sex achieves higher internal AUROC, while the harmonized representation remains competitive in relative cross-dataset transfer stability. These findings show that a consistent waveform-derived feature interface preserves performance, supports realistic external validation, and provides a transparent alternative for cross-site clinical prediction.

## Metadata
- **Published**: 2026-07-26T02:04:13Z
- **Authors**: Jie Lin, Weijie Sun, Sunil V. Kalmady, Anita Khalafbeigi, Abram Hindle, Padma Kaul, Russell Greiner
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23412v1)