---
title: Multi-Objective Bayesian Optimization for Model Merging
published: 2026-08-14T12:41:37Z
authors: Utkarsh Agarwal, Vamshi Bonagiri, Raul Astudillo, Monojit Choudhury
url: http://arxiv.org/abs/2608.14264v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-Objective Bayesian Optimization for Model Merging

## Abstract
Model merging combines trained models directly in weight space, offering a compute-efficient alternative to additional fine-tuning. Selecting merge parameters is nevertheless difficult because downstream evaluations are expensive, gradients are unavailable, and source capabilities can conflict. We formulate merge-parameter selection as a black-box multi-objective optimization problem and introduce MOBO-Merge, a merge-operator agnostic framework that uses multi-objective Bayesian optimization to approximate the Pareto front under a limited evaluation budget. We evaluate Qwen3-4B and Llama-3.1-8B in two-model instruction-math and three-model instruction-math-code settings using Linear, SLERP, TIES, and block-wise merge operators. On held-out benchmark partitions, MOBO-Merge obtains higher mean hypervolume than random search in 11 of 12 reported comparisons. The gain is small for one-dimensional Linear interpolation but substantially larger for several TIES, block-wise, and three-objective searches. No merge operator is uniformly best: TIES leads in three of four family-setting combinations, whereas Block-Linear 4x is strongest for the Llama three-model merge. These results show that multi-objective Bayesian optimization is valuable as a search layer for expressive merge parameterizations.

## Metadata
- **Published**: 2026-08-14T12:41:37Z
- **Authors**: Utkarsh Agarwal, Vamshi Bonagiri, Raul Astudillo, Monojit Choudhury
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14264v1)