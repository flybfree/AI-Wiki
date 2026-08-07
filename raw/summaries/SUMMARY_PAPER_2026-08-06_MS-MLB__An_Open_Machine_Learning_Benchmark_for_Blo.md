---
title: MS-MLB: An Open Machine Learning Benchmark for Blood-Based MS Classification
url: http://arxiv.org/abs/2608.05196v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-04_11-20-36Z_MS_MLB_AnOpenMachineLearningBenchmarkforBlood_Base.md
generated_at: 2026-08-06 21:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MS‑MBL, an open machine learning benchmark that evaluates classification of multiple sclerosis from whole blood RNA expression data using the GSE17048 cohort. The study reports Gradient Boosting as the top performer with a high MS Research Score and strong AUC‑ROC values.

## Key Takeaways
- The benchmark employs nested cross‑validation, an untouched stratified holdout set, bootstrap confidence intervals, ROC and precision‑recall analysis, calibration measurement, and an exploratory MS Research Score to ensure rigorous evaluation.  
- Gradient Boosting achieved the highest MS Research Score of 93.83 on the holdout set, delivering AUC‑ROC of 0.989, sensitivity of 0.950, specificity of 0.778, F1 score of 0.927 and Brier score of 0.050.  
- The framework provides a documented external model submission pathway, making it the first open benchmark focused on MS versus healthy control classification from whole blood RNA data.

## Context
Machine learning models applied to transcriptomic data aim to support early disease detection but often lack reproducible benchmarks that compare algorithms under identical conditions. This work addresses that gap by offering a controlled pipeline and clear scoring metrics for researchers working with blood‑based MS classifiers.

## Implications
The benchmark enables fair comparison of new methods, guiding future research toward more reliable diagnostic tools without clinical validation. Practitioners can leverage the open code to integrate their models into the submission pathway, accelerating progress in AI‑driven MS detection.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05196v1)
