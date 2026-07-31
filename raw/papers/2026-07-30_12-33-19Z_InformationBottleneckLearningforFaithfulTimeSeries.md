---
title: Information Bottleneck Learning for Faithful Time Series Forecasting Explanations
published: 2026-07-30T12:33:19Z
authors: Xu Zheng, Wei Cheng, Zhuomin Chen, Mo Sha, Jingchao Ni, Dongsheng Luo
url: http://arxiv.org/abs/2607.28124v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Information Bottleneck Learning for Faithful Time Series Forecasting Explanations

## Abstract
As forecasts increasingly drive decisions in fields such as energy, transportation, and healthcare, understanding the historical data behind these predictions has become as crucial as the predictions themselves. Although existing interpretable-by-design forecasters reveal their internal structures, they offer no guarantee that these structures faithfully reflect the underlying evidence driving the predictions. In contrast, while faithfulness-oriented methods explicitly verify model behavior, they are almost exclusively designed for post-hoc classification tasks. To bridge this gap, we propose IB-Forecast, an inherently interpretable multivariate time-series forecasting framework. It decomposes forecasting into a learned periodic component and a residual component computed with explainable masks over input tokens. With a budget-constrained information bottleneck, end-to-end optimization enables users to directly control explanation sparsity. With a rigorous faithfulness evaluation protocol, extensive experiments demonstrate that IB-Forecast matches the forecasting error of leading black-box models while providing faithful explanations at no additional inference cost. Furthermore, under a matched sparsity budget, these native explanations consistently surpass gradient-based, occlusion-based, and optimization-based baselines across all evaluated datasets. Ultimately, whereas the native explanations of existing interpretable forecasters exhibit poor faithfulness, IB-Forecast guarantees high explanation fidelity, requiring only 14-20% of the observations to deliver low-error predictions.

## Metadata
- **Published**: 2026-07-30T12:33:19Z
- **Authors**: Xu Zheng, Wei Cheng, Zhuomin Chen, Mo Sha, Jingchao Ni, Dongsheng Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28124v1)