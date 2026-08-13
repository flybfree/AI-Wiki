---
title: Long-Horizon Forecasting of Complete Financial Statements with Forma
published: 2026-08-11T18:21:19Z
authors: Travis L. Johnson, Jiannan Jiang, Soumyabrata Chaudhuri, Yihao Chen, Lauren Falvey, Donal O'Cofaigh
url: http://arxiv.org/abs/2608.11327v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Long-Horizon Forecasting of Complete Financial Statements with Forma

## Abstract
Specialist training beats generalist scale when forecasting financial statements. To our knowledge, no prior work jointly forecasts complete financial statements beyond one year, yet in a discounted-cash-flow valuation most firm value sits past that window. We release ProForma-20Q, a reproducible benchmark for forecasting 78 statement line items 1-20 quarters ahead, for anonymized firms, from past statements and an industry code, scored by change-space $R^2$. On it, Forma, a transformer that reads statements as sets of (account, quarter, value) tuples and maximizes a masked-tuple Gaussian likelihood, beats every competitor we field: classical machine learning, chained gradient boosting, a zero-shot time-series foundation model, and frontier large language models. Its lead widens with horizon, where valuation needs accuracy most, and its Gaussian predictive intervals never under-cover. Forma's forecasts nearly satisfy accounting identities; exact coherence is recoverable at no statistically significant accuracy cost. Its tuple interface supports scenario analysis without retraining, and we show that pinning future revenue paths sharpens the rest of the statement.

## Metadata
- **Published**: 2026-08-11T18:21:19Z
- **Authors**: Travis L. Johnson, Jiannan Jiang, Soumyabrata Chaudhuri, Yihao Chen, Lauren Falvey, Donal O'Cofaigh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11327v1)