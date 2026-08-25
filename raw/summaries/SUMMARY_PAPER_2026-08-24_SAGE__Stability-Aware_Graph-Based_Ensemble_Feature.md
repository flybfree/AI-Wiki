---
title: SAGE: Stability-Aware Graph-Based Ensemble Feature Selection for Explainable Postpartum Depression Risk Prediction
url: http://arxiv.org/abs/2608.22809v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_05-11-42Z_SAGE_Stability_AwareGraph_BasedEnsembleFeatureSele.md
generated_at: 2026-08-24 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The authors introduce SAGE, a Stability-Aware Graph-Based Ensemble feature selection system that integrates local explainable AI with a genetically optimized artificial neural network to predict postpartum depression risk. Using a cohort of 766 women, SAGE selects robust predictors and achieves high predictive performance while providing interpretable insights.

## Key Takeaways
- SAGE reaches 87.96% accuracy, 86.32% F1 score, and 0.88 AUC by selecting only 16 features through a GA‑ANN enhanced with GAN oversampling.
- Psychological and socioeconomic factors such as EPDS score, PHQ‑9 score, feelings about motherhood, and abuse history are the strongest predictors, whereas demographic variables contribute little to risk prediction.
- LIME‑based explanations generate instance‑specific insights into which features from the graph drive individual risk assessments.

## Context
Explainable AI remains a challenge in clinical settings where stable feature selection and class imbalance hinder reliable models. This work addresses these issues by combining genetic optimization with graph structures, offering a method that is both accurate and transparent for low‑resource environments.

## Implications
SAGE provides a scalable, interpretable tool that can be deployed in health‑care limited resources to identify postpartum depression early. Practitioners can rely on the model’s stability and explainability to inform personalized care plans without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22809v1)
