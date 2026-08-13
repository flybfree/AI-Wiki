---
title: How to Spend Your Oracle Budget: Practical Guidance for Protein Structure Prediction Models
published: 2026-08-12T15:46:57Z
authors: Aleksandra Kalisz, Jack Simons, Krisztina Sinkovics, Noam Ghenassia, Shikha Surana, Henry Moss, Paul Duckworth
url: http://arxiv.org/abs/2608.12192v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How to Spend Your Oracle Budget: Practical Guidance for Protein Structure Prediction Models

## Abstract
Foundation models for protein structure prediction remain unreliable on certain targets. External oracles can flag and correct these failures, but biological oracles are expensive, making oracle budget a critical constraint. Existing guidance methods, such as FK-steering, DPO, and Best K-of-N sampling, differ in how they spend this budget, yet no systematic comparison exists to guide method selection. To bridge this gap, we benchmark these methods alongside the recently proposed Optimisation Over Outputs (O3), which applies off-the-shelf optimisers within a generative model's latent subspace. We extend the usage of O3 to protein structure prediction models. Overall, our work provides the first practical reference for oracle budget-aware guidance. Our evaluation on two protein targets, calmodulin (1CLL) and E. coli aspartate transcarbamoylase (9EEH), reveals that no single method consistently dominates across all budgets and oracles. Specifically, O3 proves most effective at low oracle budgets, while FK-steering and DPO demonstrate improved performance as the budget increases. We distil these findings into actionable recommendations for practitioners operating under real-world oracle-budget constraints.

## Metadata
- **Published**: 2026-08-12T15:46:57Z
- **Authors**: Aleksandra Kalisz, Jack Simons, Krisztina Sinkovics, Noam Ghenassia, Shikha Surana, Henry Moss, Paul Duckworth
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12192v1)