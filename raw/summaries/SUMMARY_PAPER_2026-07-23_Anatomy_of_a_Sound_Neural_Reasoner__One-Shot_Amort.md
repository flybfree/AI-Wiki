---
title: Anatomy of a Sound Neural Reasoner: One-Shot Amortization, First-Pass Poisoning, and Search Inertness in Clue-Rich Completion
url: http://arxiv.org/abs/2607.19635v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_00-05-34Z_AnatomyofaSoundNeuralReasoner_One_ShotAmortization.md
generated_at: 2026-07-23 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why neural solvers sometimes behave as one-shot predictors in clue-rich Sudoku completion and explains the phenomenon of first-pass poisoning. It shows that a single forward pass can commit to most blanks, making iterative search unnecessary for many instances. The authors identify learned branching and constraint graphs as tools that reduce waste rather than improve solving ability.

## Key Takeaways
- First-pass poisoning occurs when a model’s initial prediction fills nearly all cells in clue-rich Sudoku, causing hard-slice failures before any search begins.
- Adding learned branching, MRV, backtracking, value exclusion, and shared nogoods only cuts repeated invalid derivations 1,497‑fold but does not change which instances are solved.
- Digit-permutation augmentation boosts 9x9 accuracy to 96.5% across seeds while test‑time union over symmetry passes achieves perfect checkpoint scores without retraining.

## Context
Neural solvers aim to combine learning with logical search, yet many systems default to a single pass that ignores deeper reasoning. This work reveals that such shortcuts are common in high‑clue domains and that the real value of learned components lies in efficiency rather than accuracy. The findings echo broader questions about sample efficiency and model calibration in reinforcement‑learning agents.

## Implications
For practitioners, the paper suggests designing models to calibrate early predictions and exploit symmetry to avoid unnecessary computation. It also warns against over‑optimizing search mechanisms that may mask fundamental learning gaps. These insights could guide both Sudoku solvers and general AI systems seeking cost‑effective reasoning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19635v1)
