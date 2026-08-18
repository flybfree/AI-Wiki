---
title: ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning
url: http://arxiv.org/abs/2608.15291v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_15-46-46Z_ReasonCast_AgenticDemandForecastingwithSelectiveSe.md
generated_at: 2026-08-17 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ReasonCast, a framework that uses structured semantic reasoning to improve demand forecasting by selectively applying event knowledge. It reduces WMAPE on holiday‑sensitive categories by 3.29 pp, mega‑sale‑sensitive categories by 1.25 pp, and M5 event windows by 0.47 pp while avoiding unnecessary intervention.

## Key Takeaways
- ReasonCast translates event context into forecast‑specific operations using structured fields for relevance, demand direction, temporal shape, amplitude, peak intensity.
- The additive path corrects local trends; the multiplicative path captures level shifts, enabling selective interaction with time‑series components.
- A forecast‑grounded curriculum includes schema SFT, semantic‑field RL, and forecast‑utility RL to calibrate interventions.

## Context
This work addresses the challenge of integrating heterogeneous event information into time‑series forecasts without uniform fusion, a common limitation in text‑enhanced methods. By grounding reasoning in the forecast model’s uncertainty and temporal structure, ReasonCast offers a more nuanced approach than generic embeddings.

## Implications
Practitioners can adopt structured semantic fields to tailor interventions, reducing overfitting on stable periods. The framework demonstrates measurable gains across diverse retail scenarios, encouraging industry adoption of context‑aware forecasting pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15291v1)
