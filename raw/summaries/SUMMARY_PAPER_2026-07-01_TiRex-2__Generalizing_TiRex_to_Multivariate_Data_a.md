---
title: TiRex-2: Generalizing TiRex to Multivariate Data and Streaming
url: http://arxiv.org/abs/2607.01204v1
type: paper-summary
date: 2026-07-01
source_paper: 2026-07-01_17-45-04Z_TiRex_2_GeneralizingTiRextoMultivariateDataandStre.md
generated_at: 2026-07-01 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
TiRex‑2 extends the univariate TiRex model to multivariate forecasting by integrating both past and future covariates using a recurrent xLSTM architecture. The paper demonstrates that this design achieves state‑of‑the‑art zero‑shot performance on benchmark datasets while maintaining constant inference cost per patch under streaming conditions.

## Key Takeaways
- TiRex‑2 combines a bidirectional time mixer with an asymmetric grouped‑attention variate mixer to incorporate future‑known covariates without breaking causality over target variables.  
- The model operates at constant per‑patch cost, enabling stable forecasting across arbitrary context lengths in a streaming setting.  
- Synthetic coupling pipelines generate diverse multivariate samples on the fly from large univariate corpora, supporting scalable pretraining.

## Context
This work addresses a key limitation of Transformer‑based foundation models: their quadratic complexity and need for full‑history recomputation, which hinder real‑time applications. TiRex‑2’s memory‑centric recurrent approach offers a more efficient alternative suitable for continuous data streams.

## Implications
For industry practitioners, TiRex‑2 enables low‑latency multivariate forecasting without sacrificing accuracy, supporting use cases such as finance, energy, and IoT where real‑time predictions are critical. The model’s design also sets a precedent for future research on efficient, causal time series foundation models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.01204v1)
