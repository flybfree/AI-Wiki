---
title: Predictive Extrema, Unprofitable Policies: An AI-Assisted Audit of Candle-Based Binance Spot Timing Models
url: http://arxiv.org/abs/2607.19453v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_14-04-15Z_PredictiveExtrema_UnprofitablePolicies_AnAI_Assist.md
generated_at: 2026-07-23 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper audits whether candle‑based machine‑learning models can generate profitable Binance Spot policies by exploiting predicted cryptocurrency extrema, after accounting for transaction costs. It runs deterministic simulations with fixed seeds and finds that no model consistently beats a simple buy‑and‑hold strategy when costs are included.

## Key Takeaways
- The ten‑pair mandatory daily selector that remained unchanged over 19 July cycles lost 6.72 % at an assumed 31‑basis‑point cost, resulting in three wins and sixteen losses. - Short model‑specific July evaluations showed the validation‑selected local‑minimum policy returned –1.79 %, while a sell‑to‑cash/re‑entry policy underperformed continuous holding by 2.80 %; their gross mean advantages of 11.11 and 12.21 bps were below even a 21‑basis‑point stress level. - A Gurgul‑inspired OHLCV daily adaptation achieved ROC AUCs of 0.874 and 0.896 but average precision of only 0.134 and 0.116, losing 44.30 % over seven cycles versus –41.20 % for buy‑and‑hold.

## Context
This study contributes to the growing body of AI research that evaluates algorithmic trading strategies using synthetic data rather than live markets, highlighting the gap between predictive performance and executable value. By separating model development from decision making, it underscores a methodological principle relevant to responsible AI deployment in finance.

## Implications
For practitioners, the findings suggest that automated models should be tested rigorously under realistic cost structures before being considered viable trading tools. The paper also reinforces the need for transparent documentation of training data and evaluation protocols to avoid hidden biases that compromise model credibility.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19453v1)
