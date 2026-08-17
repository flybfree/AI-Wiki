---
title: Model-agnostic Retrieval-Augmented Extended Forecasting for time series
published: 2026-08-14T07:59:17Z
authors: Juan Pablo Villa Serna, Rohan Asthana, Vasileios Belagiannis
url: http://arxiv.org/abs/2608.14054v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Model-agnostic Retrieval-Augmented Extended Forecasting for time series

## Abstract
Time series forecasting with pretrained foundation models has demonstrated strong zero-shot capabilities. However, achieving optimal performance on time series with short or negligible historical data in domain-specific applications typically requires adaptation via either fine-tuning or RAG. While fine-tuning is effective, it incurs substantial computational costs. This work explores RAG within univariate time series (Retrieval Augmented Generation) as a more efficient alternative, in particular RAF (Retrieval Augmented Forecasting), and introduces RAEF (Retrieval-Augmented Extended Forecasting), a model-agnostic method built upon RAF. RAEF incorporates key refinements to the retrieval and aggregation mechanisms: (1) direct retrieval in input-space rather than embedding-space, reducing inference overhead, and (2) concatenation-based aggregation that preserves temporal structure instead of averaging. Empirical evaluation across multiple benchmark datasets demonstrates that RAEF outperforms RAF in both accuracy and inference overhead. Furthermore, comprehensive comparisons with zero-shot and fine-tuned foundation models show that RAEF achieves competitive or superior performance to fine-tuning while avoiding its computational burden, establishing it as a practical and scalable approach for domain adaptation in time series forecasting.

## Metadata
- **Published**: 2026-08-14T07:59:17Z
- **Authors**: Juan Pablo Villa Serna, Rohan Asthana, Vasileios Belagiannis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14054v1)