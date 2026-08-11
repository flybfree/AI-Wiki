---
title: Beyond Aggregate Calibration: Decomposing Income-Conditional Recall Disparities in Automated Credit Default Prediction
url: http://arxiv.org/abs/2608.08202v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_15-57-15Z_BeyondAggregateCalibration_DecomposingIncome_Condi.md
generated_at: 2026-08-10 22:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why automated credit default prediction models misclassify high‑income defaulters as label noise more often than low‑income ones, revealing a large recall disparity. It shows that after removing income and interest rates, a residual gap persists due to structural proxies like loan amount and home ownership.

## Key Takeaways
- High‑income defaulters are flagged as noisy labels at roughly 0.03–0.07 Cramer’s V relative to low‑income peers, indicating systematic misclassification.
- A 16.86 percentage point gap in true positive rate remains after blinding income and interest rates, persisting even on held‑out data (Z = -4.04, p < 0.0001).
- Structural proxies such as loan amount and home ownership sustain the residual disparity, showing that fairness cannot be achieved by simple attribute removal.

## Context
This work highlights a common pitfall in AI auditing: removing sensitive attributes does not eliminate bias when institutions embed bias in pricing or behavioral signals. The findings underscore the need for deeper analysis of proxy variables beyond tokenized features.

## Implications
For financial institutions, these results call for rigorous fairness testing that accounts for institutional practices and residual proxies. Practitioners must adopt sequential feature‑blinding pipelines to uncover hidden sources of disparity before deploying credit models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08202v1)
