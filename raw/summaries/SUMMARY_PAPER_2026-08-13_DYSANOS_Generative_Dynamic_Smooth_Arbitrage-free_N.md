---
title: DYSANOS Generative Dynamic Smooth Arbitrage-free Non-parametric Option Surfaces
url: http://arxiv.org/abs/2608.12587v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_21-01-33Z_DYSANOSGenerativeDynamicSmoothArbitrage_freeNon_pa.md
generated_at: 2026-08-13 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DYSANOS, a generative model that creates smooth SANOS option surfaces free of static arbitrage for any strike and expiry over years. It employs an AR(1) hidden state to generate daily paths of spot and option prices. Results show the model outperforms a pure implied‑vol PCA approach on historical S&P 500 data from 2020 to 2025.

## Key Takeaways
- The model generates entire multi‑year paths of daily spot and option prices using an AR(1) hidden state generative framework.  
- It ensures smoothness and arbitrage‑free surfaces across all strikes and expiries by design.  
- Numerical tests demonstrate superior performance compared to a standard implied‑vol PCA approach on historical S&P 500 data.

## Context
This work advances AI‑driven financial modeling by applying generative hidden state concepts to option pricing, moving beyond traditional statistical methods. It shows how deep learning can produce realistic market dynamics with minimal assumptions, offering a new baseline for synthetic risk analysis.

## Implications
Practitioners can leverage DYSANOS for risk management and product design, obtaining arbitrage‑free surfaces that simplify hedging strategies. The model’s robustness provides a scalable alternative to manual calibration, supporting long‑term strategic planning in options markets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12587v1)
