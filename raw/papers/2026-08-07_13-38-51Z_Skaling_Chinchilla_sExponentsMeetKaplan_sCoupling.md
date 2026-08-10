---
title: Skaling: Chinchilla's Exponents Meet Kaplan's Coupling
published: 2026-08-07T13:38:51Z
authors: Mathurin Videau, Badr Youbi-Idrissi, David Lopez-Paz, Kartik Ahuja
url: http://arxiv.org/abs/2608.07222v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Skaling: Chinchilla's Exponents Meet Kaplan's Coupling

## Abstract
Neural scaling laws are foundational for language model development, yet standard formulations systematically under- and overestimate loss at data-scarce and overtraining extremes. This failure originates in the underlying assumption that model size and training data impact the loss independently. To address this, we introduce the Skaling law, a generalized functional form that couples model capacity and data through a single interaction exponent. This simple extension reduces the Mean Absolute Percentage Error (MAPE) by 1.5-3x across both interpolation and extrapolation regimes. When paired with a sparse grid strategy restricted to low-compute regimes, the Skaling law achieves accurate full-grid extrapolation using approximately 10x less compute than uniform sweeps. By enabling reliable performance prediction from small-scale experiments, the Skaling law provides a more robust and resource-efficient framework for allocating compute budgets in next-generation model training.

## Metadata
- **Published**: 2026-08-07T13:38:51Z
- **Authors**: Mathurin Videau, Badr Youbi-Idrissi, David Lopez-Paz, Kartik Ahuja
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07222v1)