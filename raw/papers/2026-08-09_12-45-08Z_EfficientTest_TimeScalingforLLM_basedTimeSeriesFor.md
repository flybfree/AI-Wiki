---
title: Efficient Test-Time Scaling for LLM-based Time Series Forecasting
published: 2026-08-09T12:45:08Z
authors: Xuan-May Le, Minh-Tuan Tran, Ling Luo, Uwe Aickelin, Dinh Phung, Trung Le
url: http://arxiv.org/abs/2608.08675v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient Test-Time Scaling for LLM-based Time Series Forecasting

## Abstract
Long-term time series forecasting benefits from preserving global structure such as trends and seasonality. Recent LLM-based forecasters often improve accuracy through test-time scaling (e.g., iterative refinement), but these methods are computationally expensive and increasingly prone to global-shape mismatch as the prediction horizon extends. We propose SCALER, a coarse-to-fine forecasting framework that first employs a lightweight Transformer tailored to long-term shape modeling to predict a coarse representation of future dynamics. This predicted shape then serves as a compact guide for an LLM to perform test-time scaling via iterative coarse-to-fine residual token refinement, while processing substantially fewer tokens at each step. By guiding refinement with an explicit future-shape prediction, SCALER reduces reliance on long description prompts, and its fixed-step refinement avoids costly reward-model-based selection, further lowering computational overhead. Experimental results demonstrate that SCALER outperforms strong forecasting baselines in long-term, short-term and zero-shot forecasting while significantly reducing the inference cost associated with scaled LLM for time series forecasting. Code: https://github.com/xuanmay2701/SCALER.

## Metadata
- **Published**: 2026-08-09T12:45:08Z
- **Authors**: Xuan-May Le, Minh-Tuan Tran, Ling Luo, Uwe Aickelin, Dinh Phung, Trung Le
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08675v1)