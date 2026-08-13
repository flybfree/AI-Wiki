---
title: Long-Horizon Forecasting of Complete Financial Statements with Forma
url: http://arxiv.org/abs/2608.11327v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_18-21-19Z_Long_HorizonForecastingofCompleteFinancialStatemen.md
generated_at: 2026-08-12 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Forma, a transformer model that forecasts complete financial statements up to twenty quarters ahead using a masked‑tuple Gaussian likelihood. On the ProForma‑20Q benchmark it outperforms classical machine learning, gradient boosting, zero‑shot time‑series models and frontier large language models. The forecasts preserve accounting identities and their predictive intervals never under‑cover.

## Key Takeaways
- Specialist training beats generalist scale when forecasting financial statements; Forma’s transformer excels over generalist models.
- Forecasts are scored by change‑space $R^2$ on 78 line items for horizons of 1–20 quarters, and the model’s Gaussian predictive intervals never under‑cover.
- The tuple interface enables scenario analysis without retraining, and pinning future revenue sharpens the rest of the statement.

## Context
This work fills a gap in AI research where models forecast only single metrics or short horizons. By forecasting full statements it aligns with discounted cash‑flow valuation which requires long‑term accuracy. The use of masked tuple likelihood is novel for financial data, offering a probabilistic framework that respects accounting constraints.

## Implications
Practitioners can rely on Forma’s forecasts to improve corporate valuation and scenario planning without retraining. Its ability to preserve accounting identities suggests a path toward more transparent, auditable AI‑driven finance tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11327v1)
