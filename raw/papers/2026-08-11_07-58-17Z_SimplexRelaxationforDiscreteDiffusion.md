---
title: Simplex Relaxation for Discrete Diffusion
published: 2026-08-11T07:58:17Z
authors: Jinya Sakurai, Patrick Pynadath, Satoshi Hayakawa, Jaehong Yoon, Xulei Yang, Nancy F. Chen, Xun Xu
url: http://arxiv.org/abs/2608.10615v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Simplex Relaxation for Discrete Diffusion

## Abstract
Discrete diffusion models for categorical generation are defined by a corruption kernel, which determines the intermediate state space and the associated reverse prediction problem. We study uniform discrete diffusion and ask whether its training objective and reverse transitions can be enriched without changing the underlying categorical corruption process. We introduce Simplax, an exact Dirichlet--categorical augmentation that couples each corrupted categorical state with an auxiliary simplex-valued variable while preserving the original uniform diffusion process as its categorical marginal. This augmentation yields a tractable Rao--Blackwellized reverse-bridge objective and a corresponding stochastic reverse sampler, while retaining the corrupted categorical state as the denoiser input. Empirically, Simplax improves the generative perplexity--entropy tradeoff on unconditional OpenWebText generation. On Sudoku, a model trained exclusively on $30$-clue puzzles achieves the highest accuracy among the compared methods across all evaluated clue densities, including the minimum uniquely solvable $17$-clue regime, and also achieves the highest validity in unconditional generation.

## Metadata
- **Published**: 2026-08-11T07:58:17Z
- **Authors**: Jinya Sakurai, Patrick Pynadath, Satoshi Hayakawa, Jaehong Yoon, Xulei Yang, Nancy F. Chen, Xun Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10615v1)