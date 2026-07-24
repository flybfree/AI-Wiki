---
title: TypiCore: A Hybrid Active Query Strategy for Class-Incremental Learning on Time Series
published: 2026-07-20T07:39:17Z
authors: Gabor Szucs, Samuel Jacsev, Marcell Nemeth, Davide Dalle Pezze, Gian Antonio Susto
url: http://arxiv.org/abs/2607.17632v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TypiCore: A Hybrid Active Query Strategy for Class-Incremental Learning on Time Series

## Abstract
Time series data play a pivotal role across numerous domains, including healthcare and manufacturing. In real-world environments, models must cope with distribution shifts over time, a challenge commonly addressed through Continual Learning (CL) techniques. However, existing CL methods face a critical limitation: real-world data streams are rarely fully labeled, making annotation cost a major practical constraint. This paper investigates Active Class-Incremental Learning (ACIL) for multivariate time series, where a model must sequentially learn new classes while selectively querying labels under a fixed annotation budget. We present a systematic evaluation of a wide range of query strategies combined with multiple rehearsal-based approaches, assessing their impact on plasticity, stability, and label efficiency across four benchmark datasets. Our analysis reveals the limitations of uncertainty-based and distribution-aware methods in achieving strong performance under constrained labeling budgets. To address these shortcomings, we propose TypiCore, a novel hybrid query strategy that alternates between typicality-based and diversity-based sample selection across active learning cycles, enabling the construction of memory buffers that are both representative and diverse. Evaluated on the TSCIL benchmark, TypiCore delivers statistically significant improvements over all baselines and matches or surpasses fully supervised continual learning performance on multiple datasets while requiring a fraction of the available labels.

## Metadata
- **Published**: 2026-07-20T07:39:17Z
- **Authors**: Gabor Szucs, Samuel Jacsev, Marcell Nemeth, Davide Dalle Pezze, Gian Antonio Susto
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17632v1)