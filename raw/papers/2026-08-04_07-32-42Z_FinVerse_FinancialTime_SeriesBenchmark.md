---
title: FinVerse: Financial Time-Series Benchmark
published: 2026-08-04T07:32:42Z
authors: Jaehoon Lee, Jun Seo, Seunghan Lee, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Minjae Kim, Sungdong Yoo, Junhyeok Kang, Sangjun Han, Soonyoung Lee, Wonbin Ahn
url: http://arxiv.org/abs/2608.03259v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FinVerse: Financial Time-Series Benchmark

## Abstract
As time-series foundation models have emerged, the need for benchmarks that can evaluate their forecasting ability in meaningful ways has become increasingly important. Existing time-series forecasting benchmarks provide useful standardized comparisons, but they often evaluate heterogeneous series with uniform error-based metrics. Strong performance under such metrics does not necessarily imply that a model's forecasts will support the best real-world decisions across domains. For example, in stock forecasting, correctly predicting whether a price will rise or fall can be more directly relevant to realized returns than minimizing point-wise forecast error alone. To this end, we introduce FinVerse, a finance-domain time-series forecasting benchmark that takes a first step toward more realistic evaluation. The released FinVerse data artifact contains 116,897 financial time series with 171.1M observations, of which 60,232 series with 17.4M observations are selected as evaluated targets based on their economic relevance to financial decisions. Unlike generic forecasting benchmarks that primarily emphasize uniform point-forecast or probabilistic accuracy, FinVerse defines 11 metric families comprising 78 evaluation metrics and assigns the most appropriate evaluation metrics to each individual time series based on its underlying economic meaning. Our analysis of 43 public time-series forecasting foundation models shows that strong performance under generic forecasting criteria does not necessarily translate into useful financial forecasts. This finding highlights the need for domain-aware benchmarks that evaluate models under objectives closer to real-world decision making.

## Metadata
- **Published**: 2026-08-04T07:32:42Z
- **Authors**: Jaehoon Lee, Jun Seo, Seunghan Lee, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Minjae Kim, Sungdong Yoo, Junhyeok Kang, Sangjun Han, Soonyoung Lee, Wonbin Ahn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03259v1)