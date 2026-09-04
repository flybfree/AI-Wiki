---
title: Flip, Don't Shuffle: Watermarking LLMs at the Speed of Inference
published: 2026-09-03T13:38:49Z
authors: Simone Ceppi, Ignacio Sanchez
url: http://arxiv.org/abs/2609.03844v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Flip, Don't Shuffle: Watermarking LLMs at the Speed of Inference

## Abstract
We introduce Stateless Bernoulli Watermarking (SBW), a new statistical watermark for Large Language Models that determines green list membership through independent per-token Bernoulli trials. Unlike KGW's vocabulary permutation or SynthID's multi-layer tournament, SBW requires only a single comparison per token against a counter-based random number generator, reducing membership complexity to $O(1)$ and enabling single-kernel execution with zero intermediate allocations. We prove that this formulation preserves the same detection guarantees as fixed-size green lists: the z-score test remains $\mathcal{N}(0,1)$ under the null. The stateless architecture enables capabilities unavailable to existing methods: full-vocabulary self-salt watermarking (over 6000$\times$ faster than KGW's self-salt and 2$\times$ faster than SynthID despite biasing the entire vocabulary with candidate-dependent seeding) and architectural compatibility with distributed inference. In end-to-end generation benchmarks, SBW adds less than 1\% overhead at all batch sizes. We additionally identify hash function design as a previously unexplored axis for watermark quality, showing that a GPU-native Jenkins hash improves null calibration by 1.8$\times$ while producing more diverse text. Experiments across two seeding schemes and eight $(γ, δ)$ configurations confirm statistical equivalence with ROC-AUC differences below 0.01.

## Metadata
- **Published**: 2026-09-03T13:38:49Z
- **Authors**: Simone Ceppi, Ignacio Sanchez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03844v1)