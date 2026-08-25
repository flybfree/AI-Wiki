---
title: Beyond Fixed Directions: Adaptive Representation Analysis of Reasoning and Memorization in LLMs
url: http://arxiv.org/abs/2608.21919v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_11-15-43Z_BeyondFixedDirections_AdaptiveRepresentationAnalys.md
generated_at: 2026-08-24 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether reasoning and memorization tasks can be captured by a single representation direction, testing this hypothesis after reinforcement learning using GRPO on the Qwen3-0.6B model. It finds that a one-dimensional projection matches a full 1024‑dimensional linear probe with AUROC = 1.00 but that the underlying direction is substantially reorganized following GRPO.

## Key Takeaways
- A one‑dimensional projection can achieve AUROC = 1.00, indicating single‑direction decodability for the studied task groups.  
- After GRPO, mean‑direction cosine averages 0.453 and probe‑direction cosine is 0.445, showing a geometric reorganization of the representation space.  
- Direct representation drift reaches 0.511 at the final layer yet the probe AUROC remains 1.00.

## Context
This work challenges the assumption that a fixed linear embedding captures all task information, highlighting how reinforcement learning can reshape model behavior without affecting performance metrics. It contributes to understanding dynamic geometry in neural representations and informs future research on adaptive versus static embeddings.

## Implications
Practitioners should consider representation stability when applying RL methods, as geometry may shift even if predictions stay optimal. The findings suggest a move toward adaptive representations rather than relying on fixed directions for reasoning or memorization tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21919v1)
