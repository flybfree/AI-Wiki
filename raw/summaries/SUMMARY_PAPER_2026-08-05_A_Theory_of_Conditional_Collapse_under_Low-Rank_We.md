---
title: A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation
url: http://arxiv.org/abs/2608.03620v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_13-10-19Z_ATheoryofConditionalCollapseunderLow_RankWeight_Sp.md
generated_at: 2026-08-05 01:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a theoretical model of conditional collapse under low‑rank weight‑space ablations and proves three exact results about how deleting or patching carriers affects the readout, then validates these predictions with synthetic tasks and real models.

## Key Takeaways
- Deleting a subset of carriers collapses a matched input pair onto the same unconditional output if and only if the removal is symmetric on the pair and leaves no outside contrast; the resulting error is deterministic.  
- Patching a carrier moves the readout by its donor‑receiver contrast, whereas ablating it moves the readout by its absolute level; neither bound the other, so a single‑carrier patch can flip the decision while no single‑carrier ablation does.  
- For an attention head composed with its own layer’s normalization and MLP, an exact first‑order interaction formula holds with a provably second‑order remainder that vanishes when only the MLP is ablated but not in general when a whole head is.

## Context
This work bridges activation patching and weight‑space ablation by providing a unified theoretical framework that predicts their effects on model behavior, offering a principled way to interpret empirical observations across transformer architectures.

## Implications
The theory helps practitioners understand why certain interventions succeed or fail, guiding design of efficient regularization and ablation strategies in large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03620v1)
