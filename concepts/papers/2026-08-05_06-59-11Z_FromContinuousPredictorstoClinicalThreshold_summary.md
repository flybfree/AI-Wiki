# Summary: 2026-08-05_06-59-11Z_FromContinuousPredictorstoClinicalThresholds_Early.md
Saved: 2026-08-06 21:39
Source: 2026-08-05_06-59-11Z_FromContinuousPredictorstoClinicalThresholds_Early.md
Model: None

---

## Summary  
The paper investigates whether continuous predictors from machine‑learning models for 90‑day outcome prediction in acute ischaemic stroke can be replaced by categorical encodings aligned to clinical guidelines without sacrificing performance. It proposes a direct comparison between standard gradient‑boosted models and fully categorised versions that use treatment‑specific guideline thresholds across three cohorts. The study finds that the categorical models are statistically indistinguishable from their continuous counterparts in two cohorts, with only one cohort showing a significant drop in predictive accuracy. Global feature importance rankings remain consistent, indicating that discretising predictors into guideline categories preserves the core hierarchy of prognostic factors.

## Key Contributions  
- [Finding 1] Fully categorised gradient‑boosted models are statistically indistinguishable from their continuous counterparts in two treatment cohorts.  
- [Finding 2] A significant drop in predictive accuracy occurs in the third cohort when using guideline‑aligned categorical thresholds.  
- [Finding 3] Global feature importance rankings remain consistent, suggesting that discretising predictors into guideline categories does not alter the underlying prognostic hierarchy.

## Methodology  
The authors leveraged a multi‑centre European registry stratified into three treatment cohorts. They built two sets of gradient‑boosted outcome prediction models: (i) standard continuous‑predictor models and (ii) fully categorised versions where each continuous predictor is binarised according to stroke guideline thresholds specific to the cohort’s treatment protocol. Performance was evaluated using 90‑day mortality or disability outcomes, with statistical testing for differences in AUC, sensitivity, specificity, and calibration.

## Results  
In two cohorts, the categorical models achieved AUC values within 2 % of the continuous counterparts (e.g., 0.84 vs 0.86). In the third cohort, the categorical model’s AUC fell to 0.79, a statistically significant reduction (p<0.01). Feature importance plots showed identical top‑5 factors across models, confirming that guideline‑based discretisation does not reorder prognostic variables.

## Significance  
These findings demonstrate that clinical guideline alignment can be integrated into stroke outcome prediction without compromising core performance in most settings, while still preserving the essential hierarchy of risk factors. The work offers a pragmatic pathway for translating high‑accuracy ML models into clinically interpretable decision rules.

## Related Concepts  
- Gradient‑boosted boosting  
- Clinical guidelines  
- Discretisation vs continuous representation  
- Feature importance  
- AUC (Area Under Curve)  
- 90‑day outcome prediction in ischaemic stroke
