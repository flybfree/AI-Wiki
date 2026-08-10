---
title: Accounting Graph Transformer for Short-History Multi-KPI Forecasting in Small Businesses
published: 2026-08-07T09:47:44Z
authors: Shrutendra Harsola, Vignesh Subrahmaniam
url: http://arxiv.org/abs/2608.07037v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Accounting Graph Transformer for Short-History Multi-KPI Forecasting in Small Businesses

## Abstract
Small businesses often have only 12-24 months of accounting history, yet planning and risk workflows require coordinated forecasts across financial statements. We study joint 12-month forecasting of 13 income-statement, balance-sheet, cash-flow, and working-capital key performance indicators (KPIs) from 71 monthly ledger series. We introduce the Accounting Graph Transformer (AGT), which represents each ledger series as a masked token, exchanges information through typed attention on a fixed accounting-relation graph, pools target-specific context, and fuses it with a gated three-month recency path. Across 11,993 forecast origins from 1,060 unseen companies, AGT achieves sample-weighted KPI-macro mean absolute error (MAE) $0.6990 \pm 0.0013$ over three independent seeds, compared with $0.7378 \pm 0.0014$ for the strongest baseline, LightGBM. At the pre-specified seed 42, a paired company-clustered bootstrap gives a LightGBM-minus-AGT difference of 0.0395 with 95% confidence interval (CI) $[0.0350,0.0439]$. AGT is best on all 13 KPIs against LightGBM, TimeMixer, and SOFTS in the matched seed-42 comparison, while final-architecture ablations show that relational attention, accounting topology, and the recency path each improve validation and test accuracy. On 7,094 additional unseen companies with origins sampled from January-May 2025, AGT obtains 0.7548 MAE versus 0.7694 for SOFTS. A single 5.3M-parameter model produces 156 aligned forecasts without company-specific fitting, providing one forecasting layer for integrated planning, liquidity, and working-capital analysis.

## Metadata
- **Published**: 2026-08-07T09:47:44Z
- **Authors**: Shrutendra Harsola, Vignesh Subrahmaniam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07037v1)