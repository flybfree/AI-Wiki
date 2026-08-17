---
title: Forecast Collapse in Time-Series Foundation Models
published: 2026-08-14T09:08:02Z
authors: Shu Wan, Miles Ma, Hank Zhu, Guangqi Liu, Stephen Wang, Qingsong Wen, Huan Liu
url: http://arxiv.org/abs/2608.14106v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Forecast Collapse in Time-Series Foundation Models

## Abstract
When forecasting hourly returns for 1,000 US equities, we observe an unexpected phenomenon: predictions become nearly flat and show poor stock ranking, as measured by cross-sectional correlation. We call this forecast collapse. Surprisingly, the phenomenon largely disappears when forecasting trading volume under the same setting. We investigate forecast collapse across time-series foundation models (TSFMs), twelve deep-learning forecasting models, and 97 public benchmark configurations, and find that it is closely tied to target predictability. We identify two distinct reasons behind it: low predictability limits the amplitude of calibrated point forecasts, while per-series objectives leave cross-series structure unidentified. These findings reveal a calibration-ranking tradeoff: optimizing squared error leads to flat predictions, whereas directly optimizing cross-sectional correlation improves ranking but can inflate forecast amplitude by more than an order of magnitude. To address this tradeoff, we introduce CalibRank, a simple objective that balances calibration and ranking. On Finance1K, CalibRank nearly triples cross-sectional correlation while keeping amplitude close to the target, and improves correlation on all tested models. Our results reveal a blind spot in conventional time-series evaluation: per-series metrics can hide failures in cross-series structure needed by downstream decisions.

## Metadata
- **Published**: 2026-08-14T09:08:02Z
- **Authors**: Shu Wan, Miles Ma, Hank Zhu, Guangqi Liu, Stephen Wang, Qingsong Wen, Huan Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14106v1)