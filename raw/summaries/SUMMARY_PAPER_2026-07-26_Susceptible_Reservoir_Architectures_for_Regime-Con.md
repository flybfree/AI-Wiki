---
title: Susceptible Reservoir Architectures for Regime-Conditional Volatility Forecasting
url: http://arxiv.org/abs/2607.22491v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_17-03-08Z_SusceptibleReservoirArchitecturesforRegime_Conditi.md
generated_at: 2026-07-26 21:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Susceptible Architectures (SUSA), a reservoir‑design framework for volatility forecasting that leverages complex‑valued open‑chain and periodic reservoirs together with regime‑conditioned experts to capture residual structure across calm, onset, recovery, and persistent‑stress states. Experiments on 16 U.S. equity and exchange‑traded‑fund series show that SUSA models achieve statistically significant QLIKE improvements over GARCH, especially for assets such as IWM and XLP, and a stacked ensemble of HARQ‑style predictions improves mean QLIKE by 0.0116 while winning in 75 % of test scenarios.

## Key Takeaways
- SUSA uses reservoir design to capture residual structure across calm, onset, recovery, and persistent‑stress states.
- Models achieve statistically significant QLIKE improvements over GARCH for specific assets like IWM and XLP.
- A stacked ensemble of HARQ‑style predictions improves mean QLIKE by 0.0116 and wins in 75 % of test scenarios.

## Context
This work advances AI‑driven financial modeling by showing that reservoir architectures can outperform traditional GARCH models, integrating classical AR‑Ridge anchors with quantum‑inspired q‑qubit counterparts while retaining a bounded residual correction. The approach illustrates how hybrid classical‑quantum methods can enhance predictive power in volatile markets.

## Implications
For practitioners, SUSA provides a flexible framework for regime‑aware volatility forecasting that improves risk management and ensemble performance. The results suggest that combining reservoir design with HARQ‑style stacking offers tangible gains over single‑model GARCH approaches in real‑world trading and portfolio optimization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22491v1)
