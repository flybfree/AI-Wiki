# Summary: 2026-08-08_15-57-15Z_BeyondAggregateCalibration_DecomposingIncome_Condi.md
Saved: 2026-08-10 23:03
Source: 2026-08-08_15-57-15Z_BeyondAggregateCalibration_DecomposingIncome_Condi.md
Model: None

---

## Summary  
The paper investigates why automated credit default prediction models exhibit larger recall disparities for high‑income defaulters, focusing on the failure of simple calibration and feature blinding to eliminate bias. It finds a 16.86‑point gap in true positive rates between high‑ and low‑income borrowers, which persists after removing income and interest‑rate features. The authors decompose this disparity into three mechanisms: reliance on self‑reported income, absorption of upstream pricing bias, and residual bias driven by structural proxies. Their sequential feature‑blinding method isolates each driver.

## Key Contributions  
- [Finding 1] High‑income defaulters are classified as label noise at a rate corresponding to Cramer’s V ≈0.03–0.07.  
- [Finding 2] A 16.86 percentage point recall gap exists between high‑ and low‑income defaulters, violating equal‑opportunity fairness.  
- [Finding 3] Residual disparity remains (≈3.55 points CV, 2.56 points test) even after removing income and interest rates.

## Methodology  
The authors apply a sequential feature‑blinding pipeline to the LendingClub dataset (N=1,344,936). First they compute aggregate calibration metrics, then re‑evaluate equal‑opportunity gaps. They use SHAP signed values for out‑of‑sample attribution and perform cross‑validation and held‑out test splits. The pipeline isolates three mechanisms: direct income usage, algorithmic absorption of origination interest rates, and residual bias.

## Results  
Cramer’s V ~0.03–0.07 indicates weak correlation between income and label noise. Recall gap = 16.86 points (high‑income vs low‑income). Residual gap persists after feature removal; SHAP shows loan amount and home ownership drive the residual disparity (Z=-4.04, p<0.0001).

## Significance  
The findings show that blind algorithms to sensitive attributes are insufficient when institutional pricing and behavioral proxies reconstruct omitted signals. This calls for auditing data‑centric AI workflows in regulated finance.

## Related Concepts  
aggregate calibration; equal opportunity; feature blinding; Cramer’s V; SHAP values; residual bias; structural proxies; loan amount; home ownership; lending credit default prediction.
