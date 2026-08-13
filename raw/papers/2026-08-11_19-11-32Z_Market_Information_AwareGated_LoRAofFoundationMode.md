---
title: Market-Information-Aware Gated-LoRA of Foundation Models for Transferable Day-Ahead Electricity Price Forecasting
published: 2026-08-11T19:11:32Z
authors: Hang Fan, Wei Wei, Shengwei Mei
url: http://arxiv.org/abs/2608.11359v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Market-Information-Aware Gated-LoRA of Foundation Models for Transferable Day-Ahead Electricity Price Forecasting

## Abstract
Electricity price forecasting is crucial for market participants but remains difficult because prices are volatile, market-specific, and closely tied to anticipated system conditions. Existing supervised methods depend largely on market-specific historical data, limiting their use in newly established or data-scarce markets. This paper proposes a market-information-aware adaptation framework that transfers the Chronos-2 time-series foundation model to day-ahead electricity price forecasting. It first constructs a multi-source market information (MSMI) interface aligning 7-day price context with pre-clearing supply--demand, reserve, maintenance, generator-capacity, and intertie variables, and then trains a source-domain gated low-rank adapter (LoRA), updating about $1\%$ of model parameters without target-market labels. The gate scales the frozen source adapter according to reserve-tightness and operating-state signals. A leave-one-market-out protocol is adopted for evaluating cross-market transferability. Experiments on four Chinese provincial day-ahead spot markets show that the proposed framework reduces the average MAE/RMSE by $6.24\%/7.99\%$ relative to market-information-aware zero-shot Chronos-2 and by $3.05\%/3.52\%$ relative to vanilla Source-LoRA. Experiments show that the gain is not reproduced by a learned global scalar or by random gate initialization, while the additional improvement over Source-LoRA is limited. These results suggest that market-structured inputs and state-dependent gated LoRA can provide a practical transfer path for data-scarce electricity markets.

## Metadata
- **Published**: 2026-08-11T19:11:32Z
- **Authors**: Hang Fan, Wei Wei, Shengwei Mei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11359v1)