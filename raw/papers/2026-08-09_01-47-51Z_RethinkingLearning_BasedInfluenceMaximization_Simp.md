---
title: Rethinking Learning-Based Influence Maximization: Simple Neural Surrogates and Native Discrete Search
published: 2026-08-09T01:47:51Z
authors: Yiqiao Liao, Parinaz Naghizadeh
url: http://arxiv.org/abs/2608.08406v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking Learning-Based Influence Maximization: Simple Neural Surrogates and Native Discrete Search

## Abstract
Existing learning-based influence maximization frameworks rely heavily on complex neural architectures and continuous optimization over seed representations. We challenge this paradigm with SIMBA, a diffusion-model-agnostic framework pairing a lightweight neural surrogate with direct discrete search. SIMBA introduces three key components: 1) uniformly anchored node embeddings that eliminate initialization noise and encourage learning driven by graph topology and diffusion pattern, 2) a shallow two-layer graph neural network surrogate predicting final infection states, and 3) batched multi-swap simulated annealing that explores combinatorial seed space without gradients or continuous relaxation. By shifting compute from complex representation learning to effective discrete search, SIMBA drastically cuts time-to-solution while achieving superior influence spread and data efficiency. Our code is available at https://github.com/yl489/rethink-IM.

## Metadata
- **Published**: 2026-08-09T01:47:51Z
- **Authors**: Yiqiao Liao, Parinaz Naghizadeh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08406v1)