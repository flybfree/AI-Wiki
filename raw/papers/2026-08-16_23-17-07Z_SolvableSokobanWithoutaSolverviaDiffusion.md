---
title: Solvable Sokoban Without a Solver via Diffusion
published: 2026-08-16T23:17:07Z
authors: Sina Baghal
url: http://arxiv.org/abs/2608.15958v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Solvable Sokoban Without a Solver via Diffusion

## Abstract
Deciding whether a Sokoban puzzle is solvable is PSPACE-complete (Culberson, 1997): solutions can be exponentially long and there is no short certificate to check. Solvability is also a fragile property, since even a single misplaced wall can silently render an entire puzzle unsolvable.   In this work, we show that a transformer-based discrete diffusion model trained purely on tile completion, with no access to solvers, rewards, or solvability labels, achieves a solvability rate of 77.4%, with 94.5% of the remaining failures rendered solvable by removing a single wall. In other words, a global, search-heavy property follows from a local training objective: trained only to fill in masked cells, the model inherits solvability it was never trained on.   An autoregressive model factorizes as $p(c_k \mid c_1 \dots c_{k-1})$, meaning a fixed order, always conditioned on a prefix. Masked diffusion does not: it hides a random subset of cells and learns $p(c_k \mid \text{any subset})$, so at generation time it can reveal cells in any order, each one conditioned on everything already placed, wherever it sits on the board. A puzzle's difficulty comes from exactly this kind of non-local interaction, a decision in one part of the grid constraining what will work somewhere else entirely. A generator that is not locked into a single fixed order is therefore a better structural match for the problem than one that is.   The training pipeline is adapted from MD4 (Shi et al., 2024) and the dataset is DeepMind's Boxoban (Guez et al., 2019). The trained model and instructions for generating puzzles are publicly available.

## Metadata
- **Published**: 2026-08-16T23:17:07Z
- **Authors**: Sina Baghal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15958v1)