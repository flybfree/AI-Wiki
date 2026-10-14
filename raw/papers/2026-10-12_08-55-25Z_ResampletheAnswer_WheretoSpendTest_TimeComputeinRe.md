---
title: Resample the Answer: Where to Spend Test-Time Compute in Recursive Reasoning
published: 2026-10-12T08:55:25Z
authors: Maxime Illouz
url: http://arxiv.org/abs/2610.16427v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Resample the Answer: Where to Spend Test-Time Compute in Recursive Reasoning

## Abstract
Recursive reasoning models such as the Tiny Recursive Model (TRM) iteratively refine two latent states: an answer state y, decoded into the output, and a reasoning state z, which is never decoded. Many of their failures have been attributed to bad basins, regions of latent space that trap the recursion on wrong answers. Recent test-time approaches perturb y, z or both to recover these failures, but the impact of this choice on performance, test-time compute efficiency and scaling properties remains unclear. Through controlled experiments on TRM, we find that a failed trajectory carries its failure in its answer state. At equal compute, in depth and in width, resampling y recovers more failures than any perturbation of z we tested, and the performance gap widens as the test-time compute budget grows. Our approach, Gated Answer Resampling (GAR), pairs this resampling of the answer state with the model's own halting head and restarts only the puzzles that the head rejects. With at most 64 restarts per puzzle and no training or hyperparameter search, GAR takes TRM from 85.9% to 99.4% on Sudoku-Extreme and from 68.8% to 85.6% on Pencil Puzzle Bench validation. On the same checkpoints, GAR also outperforms Probabilistic TRM (PTRM), which perturbs z at each step, even when PTRM uses 42 to 197 times as much compute.

## Metadata
- **Published**: 2026-10-12T08:55:25Z
- **Authors**: Maxime Illouz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16427v1)