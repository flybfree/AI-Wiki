---
title: Eliciting ESG Preferences for Reinforcement Learning-Based Portfolio Optimization
url: http://arxiv.org/abs/2609.02677v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_14-48-03Z_ElicitingESGPreferencesforReinforcementLearning_Ba.md
generated_at: 2026-09-02 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a Multi‑Objective Reinforcement Learning framework that simultaneously incorporates ESG ratings from three different agencies to optimize portfolios while respecting human sustainability preferences. By using Gaussian Processes for preference elicitation, the system learns latent utility functions through pairwise comparisons of portfolio Sharpe ratios and aggregate ESG scores, revealing regionally distinct weighting patterns.

## Key Takeaways
- The framework treats ESG optimization as a multi‑objective RL problem, integrating three distinct agency ratings to avoid bias from a single provider.  
- Gaussian Process‑based preference elicitation captures human intuition by allowing portfolio managers to rank options via Sharpe ratios and aggregate ESG scores, yielding latent utility functions that the algorithm can exploit.  
- Empirical simulations with LLM personas show that European‑based managers prioritize ESG alignment over returns, whereas Texas‑based managers favor risk‑adjusted performance, indicating that regional backgrounds shape preference weights.

## Context
The integration of reinforcement learning into portfolio management has advanced significantly, yet most implementations rely on a single ESG rating source and ignore the heterogeneity across agencies. This work highlights how multi‑objective RL can model complex trade‑offs more faithfully to human decision making, aligning with broader AI research that seeks interpretable and adaptable optimization methods.

## Implications
Practitioners will benefit from a flexible framework that accommodates diverse ESG methodologies without manual weighting, reducing implementation risk. For the industry, this aligns portfolio strategies with real‑world sustainability preferences across regions, potentially improving both regulatory compliance and investor satisfaction.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02677v1)
