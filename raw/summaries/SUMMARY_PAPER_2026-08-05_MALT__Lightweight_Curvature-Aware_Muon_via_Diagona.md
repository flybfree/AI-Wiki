---
title: MALT: Lightweight Curvature-Aware Muon via Diagonal Preconditioning
url: http://arxiv.org/abs/2608.05088v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_17-26-47Z_MALT_LightweightCurvature_AwareMuonviaDiagonalPrec.md
generated_at: 2026-08-05 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MALT, a lightweight curvature‑aware variant of Muon that uses diagonal preconditioners to reduce sensitivity to loss‑landscape anisotropy while keeping memory and compute costs low. Experiments on GPT‑2 variants show MALT outperforms the original Muon method without sacrificing efficiency. The authors also present MALTER, an adaptive step‑size rescaling extension.

## Key Takeaways
- MALT employs two‑sided diagonal preconditioners that approximate curvature geometry with minimal memory and computation overhead.
- The preconditioned momentum is orthogonalized via Newton‑Schulz iterations and mapped back to define the update direction, using norm grafting for magnitude control.
- MALTER adds adaptive step‑size rescaling to improve robustness against stochastic gradient noise, and convergence guarantees are provided in a stochastic non‑convex setting.

## Context
Muon has become popular as an AdamW alternative by orthogonalizing momentum matrices through Newton‑Schulz iterations. However, its performance can degrade when the loss landscape exhibits strong curvature anisotropy, which is common in large language model training. Recent work seeks methods that explicitly incorporate curvature information without heavy computational cost.

## Implications
Incorporating curvature awareness directly into optimizer design could lead to more stable and faster pretraining for massive models. Practitioners will benefit from MALT’s near‑identical memory footprint, allowing adoption on existing hardware while achieving better convergence. This research may inspire future lightweight preconditioning techniques across deep learning training pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05088v1)
