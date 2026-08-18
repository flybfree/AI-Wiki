---
title: TinyCast: Probabilistic Zero-Shot Forecasting with Computed Periodicity
published: 2026-08-16T14:40:44Z
authors: Armin Steinhauser
url: http://arxiv.org/abs/2608.15767v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TinyCast: Probabilistic Zero-Shot Forecasting with Computed Periodicity

## Abstract
We introduce TinyCast, an attention-free zero-shot forecaster that emits a predictive distribution from 146,505 parameters, on the premise that at this size the periodic structure of a context is worth computing rather than learning. A zero-parameter spectral detector supplies the dominant periods, the context is folded on their phase, and a dilated convolutional encoder and a block-autoregressive quantile decoder model the rest. It is smaller than every zero-shot entry on the GIFT-Eval board whose parameter count can be established. On probabilistic accuracy it defines the size-accuracy frontier. Among zero-shot entries declaring no test-data leakage it is the only one below 1.4M parameters that emits a predictive distribution, and every entry scoring better carries at least that budget. On Chronos-ZS and fev-bench every neural model ahead of it carries at least 28 times its parameters. Because the mixing path is convolutions and matrix multiplications only, it exports to static INT8 and forecasts end to end on an embedded device without per-signal fitting.

## Metadata
- **Published**: 2026-08-16T14:40:44Z
- **Authors**: Armin Steinhauser
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15767v1)