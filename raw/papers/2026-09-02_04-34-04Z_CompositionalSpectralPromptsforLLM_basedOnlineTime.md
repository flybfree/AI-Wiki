---
title: Compositional Spectral Prompts for LLM-based Online Time Series Forecasting
published: 2026-09-02T04:34:04Z
authors: Seungyoon Choi, Hyunchul Kim, Jae-Gil Lee, Chanyoung Park
url: http://arxiv.org/abs/2609.02093v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Compositional Spectral Prompts for LLM-based Online Time Series Forecasting

## Abstract
To address the sequential and evolving nature of time series, the Online Time Series Forecasting (OTSF) task has been extensively studied in multiple domains. Existing research focuses on adapting to non-stationary environments by employing memory buffer-based retrieval strategies. However, we observe that such frameworks struggle with long-term adaptation and fail to generalize to unseen patterns. To this end, we introduce CoSPOT, an LLM-based online time series forecasting framework that leverages a pre-trained LLM as the backbone online forecaster, motivated by its strong few-shot capabilities. For efficient online adaptation, CoSPOT keeps the LLM frozen and employs compositional spectral prompts grounded in frequency-domain bases to guide the model with the overall distribution of the input, thereby substantially reducing the number of parameters updated during the online phase. Specifically, CoSPOT decomposes time series into frequency bases and composes the corresponding spectral basis prompts according to their amplitudes, allowing unseen patterns to be represented as new combinations of learned basis prompts. Our extensive experiments on real-world datasets demonstrate the superiority and practicality of CoSPOT across challenging online scenarios, including extended online phases and cross-dataset settings with substantial distribution shifts. Our code is available at https://github.com/seungyoon-Choi/CoSPOT.

## Metadata
- **Published**: 2026-09-02T04:34:04Z
- **Authors**: Seungyoon Choi, Hyunchul Kim, Jae-Gil Lee, Chanyoung Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02093v1)