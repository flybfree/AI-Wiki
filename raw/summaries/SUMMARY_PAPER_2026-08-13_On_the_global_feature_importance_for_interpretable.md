---
title: On the global feature importance for interpretable and trustworthy heat demand forecasting
url: http://arxiv.org/abs/2608.13039v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_10-05-25Z_Ontheglobalfeatureimportanceforinterpretableandtru.md
generated_at: 2026-08-13 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes an ante‑hoc Explainable AI framework to evaluate the global feature importance of machine learning models used for heat demand forecasting in district heating systems. The study combines intrinsic Gradient Boosting interpretability with post‑hoc methods such as Partial Dependence, Accumulated Local Effects, and SHAP, avoiding bias from artificial data perturbations.

## Key Takeaways
- The intrinsic Gradient Boosting approach reveals that temperature anomalies and weather variables dominate the model’s predictions, indicating strong physical relevance.  
- Post‑hoc SHAP values consistently rank energy consumption patterns as a secondary driver, complementing the primary temperature signal without introducing synthetic data artifacts.  
- Accumulated Local Effects highlights interaction effects between demand response measures and supply constraints, offering deeper insight into system stability.

## Context
Explainable AI is essential for trustworthy deployment of predictive models in critical infrastructure where regulatory compliance and stakeholder confidence are paramount. By providing global feature importance without perturbing data, the methods align with real‑world operational constraints and enhance model interpretability within the domain of smart energy management.

## Implications
These findings empower district heating operators to justify model decisions to regulators and customers, reducing liability risks and improving system acceptance. The approach also supports continuous improvement by identifying which features truly influence forecasts, guiding future feature engineering and model selection.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13039v1)
