---
title: Muon Meets Mamba: Spectral Optimization for State Space Models
published: 2026-08-04T17:10:47Z
authors: Arslan Battalov, Karim Kramin, Alexander Markotenko, Sofia Sinitsina
url: http://arxiv.org/abs/2608.03941v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Muon Meets Mamba: Spectral Optimization for State Space Models

## Abstract
Muon is a recent optimizer that orthogonalizes the update to each weight matrix with a Newton-Schulz iteration, which performs steepest descent under the spectral norm. Almost all the evidence for it comes from Transformer models, and its behavior on state-space models is largely unreported. We compare Muon with AdamW on Mamba-2 130M under a controlled protocol that varies only which weight groups are trained with Muon. The benefit is localized. Muon on the output projection alone beats Muon on the input projection or on both. The advantage is mainly one of token efficiency. It holds on two corpora and two token budgets, and persists when training continues well past the compute-optimal point. Conditioning does not explain the gain. Muon lowers the condition number of whichever projection it trains, but the better-conditioned input projection is not the one that helps.

## Metadata
- **Published**: 2026-08-04T17:10:47Z
- **Authors**: Arslan Battalov, Karim Kramin, Alexander Markotenko, Sofia Sinitsina
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03941v1)