---
title: Forecast Collapse in Time-Series Foundation Models
url: http://arxiv.org/abs/2608.14106v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_09-08-02Z_ForecastCollapseinTime_SeriesFoundationModels.md
generated_at: 2026-08-16 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a study of forecast collapse in time‑series foundation models when predicting hourly returns of many equities, showing that predictions flatten and ranking deteriorates despite good per‑stock accuracy. The authors attribute this to low predictability limiting amplitude and per‑series objectives ignoring cross‑series structure, revealing a calibration‑ranking tradeoff. They introduce CalibRank to balance both goals.

## Key Takeaways
- Low predictability of returns constrains the magnitude of calibrated forecasts, leading to near‑flat predictions that perform poorly in cross‑sectional correlation.
- Optimizing only squared error for each series ignores the inter‑series relationship, causing flat forecasts across many stocks.
- The new CalibRank objective improves cross‑sectional correlation by roughly threefold while keeping forecast amplitude stable.

## Context
Time‑series foundation models are increasingly used to generate predictions for thousands of assets simultaneously. Conventional evaluation focuses on per‑stock metrics such as mean absolute error, which can mask systemic issues like flat forecasts that harm portfolio ranking and risk management.

## Implications
Practitioners must adopt evaluation criteria that capture cross‑sectional structure, not just individual series performance. The paper highlights a blind spot in current AI forecasting practices and suggests integrating CalibRank into model training pipelines to achieve both accurate and useful predictions for downstream decision making.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14106v1)
