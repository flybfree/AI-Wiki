---
title: Sustainability of TSFM Deployment and Pretraining: From Carbon Footprint Analysis to Mitigation via Pruning
published: 2026-10-23T16:32:29Z
authors: Cécile Luc, Nathanaël Lemonnier, Ievgen Redko
url: http://arxiv.org/abs/2610.32859v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sustainability of TSFM Deployment and Pretraining: From Carbon Footprint Analysis to Mitigation via Pruning

## Abstract
Time Series Foundation Models (TSFMs) offer strong zero-shot forecasting capabilities, but their high pretraining cost raises a practical sustainability question: does this upfront investment pay off over a full deployment lifecycle, compared to supervised standalone models that must be periodically retrained? We model the cumulative carbon cost of different approaches across a realistic industrial scenario: Chronos-2 amortizes its pretraining cost within months for large or frequently queried deployments, but a classical model remains cheaper indefinitely for small or rarely queried ones. For cases where reducing the TSFM's own cost matters, we show that removing a single encoder block (7.9% of parameters) via a gradient-free pruning criterion yields a consistent 6 to 9% reduction in FLOPs, CO2 emissions, and latency, at essentially no cost to zero-shot forecasting performance across a 25-task benchmark.

## Metadata
- **Published**: 2026-10-23T16:32:29Z
- **Authors**: Cécile Luc, Nathanaël Lemonnier, Ievgen Redko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.32859v1)