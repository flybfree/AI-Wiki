---
title: Accounting Graph Transformer for Short-History Multi-KPI Forecasting in Small Businesses
url: http://arxiv.org/abs/2608.07037v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_09-47-44Z_AccountingGraphTransformerforShort_HistoryMulti_KP.md
generated_at: 2026-08-09 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces the Accounting Graph Transformer (AGT) to forecast 13 key performance indicators jointly from only 12‑24 months of accounting data for small businesses. Across a large test set, AGT achieves lower mean absolute errors than state‑of‑the‑art baselines such as LightGBM and SOFTS.

## Key Takeaways
- AGT reduces the sample‑weighted KPI‑macro MAE to 0.699 ± 0.0013, compared with 0.738 ± 0.0014 for LightGBM on 11,993 forecast origins from 1,060 unseen companies.  
- In a paired company‑clustered bootstrap at seed 42, AGT beats LightGBM by an average of 0.0395 points with a 95% CI of [0.0350, 0.0439].  
- The model’s three components—relational attention, accounting topology, and the recency path—each improve both validation and test accuracy.

## Context
The work addresses a growing need for AI models that can generate reliable forecasts from limited historical data while handling multiple interrelated financial metrics simultaneously. Graph‑based transformers have shown promise in integrating heterogeneous information structures, making them suitable for complex forecasting tasks where temporal and relational dependencies matter.

## Implications
For small businesses, AGT provides a single, scalable model that delivers aligned forecasts across income statements, balance sheets, cash flows, and working capital without requiring separate company‑specific training. Practitioners can thus improve planning, liquidity management, and risk analysis with one unified forecasting layer.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07037v1)
