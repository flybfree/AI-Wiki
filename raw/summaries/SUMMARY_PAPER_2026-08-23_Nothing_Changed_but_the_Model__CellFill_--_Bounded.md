---
title: Nothing Changed but the Model: CellFill -- Bounded In-Cell Learning for Bit-Identical, Revocable Updates to Quantized LLMs
url: http://arxiv.org/abs/2608.20873v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_08-49-07Z_NothingChangedbuttheModel_CellFill__BoundedIn_Cell.md
generated_at: 2026-08-23 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CellFill, a method that enables revocable, bounded in‑cell learning inside quantized language models without altering the released checkpoint. By writing updates only into per‑weight residuals within each quantization decision cell, the model can be re‑quantized to produce an artifact that is bit‑identical to the original release. The authors demonstrate that exact invariance is nearly free and that cross‑domain forgetting is reduced compared with adapter merging.

## Key Takeaways
- CellFill writes new knowledge into frozen integer codes and scales, keeping the released 4‑bit checkpoint unchanged while updating only the per‑weight residual inside each cell.  
- The method provides a machine‑checkable guarantee: reverting to the original residual restores the exact artifact, and drift is bounded by construction.  
- Across three paired seeds, constrained dense training matches an unconstrained reference within 0.5 points of fact recall (95% CI [-5.0,+4.0]), showing that updating only residuals does not degrade performance.

## Context
Quantized LLMs are widely deployed because they reduce storage and inference cost, yet any fine‑tuning typically requires a new checkpoint, breaking compatibility with existing caches and evaluations. CellFill offers a way to augment knowledge without sacrificing the immutable artifact that users rely on for reproducibility and cache integrity.

## Implications
For practitioners, CellFill means that model updates can be applied in production without forcing clients to reload checkpoints or re‑run benchmarks, preserving trust in cached results. The bounded revocability also mitigates risk of unintended drift, making it a practical solution as organizations scale AI services with strict data governance requirements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20873v1)
