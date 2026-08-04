---
title: Interpretable machine learning for predicting splitting strength of asphalt concrete: insights from SHAP analysis
url: http://arxiv.org/abs/2608.00956v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_03-05-54Z_Interpretablemachinelearningforpredictingsplitting.md
generated_at: 2026-08-03 23:40
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an interpretable machine‑learning framework that predicts the splitting strength of asphalt concrete using a dataset of 296 samples and SHAP analysis to explain model predictions. The TabPFN model achieved the best performance with low RMSE, while nine variables contributed to 92 % of the average explanation.

## Key Takeaways
- Nine dominant variables—Ag9.5, FT, Ag4.75, AC, Du and others—account for 92.0 % of the total average SHAP contribution, highlighting their strong influence on splitting strength.
- The framework quantifies favorable parameter ranges such as Ag9.5 < 66.8 %, Ac < 5.4 wt %, AV < 3.6 %, and Du > 134.7 cm to improve performance.
- A GUI platform is developed that combines prediction with SHAP‑based explanations, enhancing accessibility for practitioners.

## Context
Interpretability remains a critical challenge in engineering AI applications where safety and reliability are paramount. This work demonstrates how model‑agnostic explanation tools can turn black‑box predictions into actionable insights, supporting trustworthy decision making in complex physical systems.

## Implications
For asphalt mix designers, the framework reduces trial‑and‑error by providing clear guidance on which material parameters to adjust, potentially lowering costs and improving pavement durability. Practitioners can rely on visual explanations to validate predictions, fostering adoption of data‑driven design practices across the industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00956v1)
