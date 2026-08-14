---
title: When Local Variance Optimality Is Not Enough: RoPE-Aligned Q/K Rotations for Dynamic 4-Bit Quantisation
url: http://arxiv.org/abs/2608.13365v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_15-31-01Z_WhenLocalVarianceOptimalityIsNotEnough_RoPE_Aligne.md
generated_at: 2026-08-13 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether rotation‑based post‑training quantisation that respects RoPE’s frequency decomposition can outperform the conventional full‑head Hadamard transform. By analysing orthogonal maps that commute with RoPE, it derives a pairwise rotation that minimises channel variance under a pooled‑covariance surrogate and shows it reaches its analytical optimum. Experiments on four checkpoints reveal that this configuration does not improve perplexity in the dynamic W4A4KV4 setting compared to full‑head mixing. The study also demonstrates that the pairwise transform satisfies a ±0.05 PPL interval when composed with the Hadamard.

## Key Takeaways
- The paper proves that for distinct frequencies, only specific per‑pair rotations commute with RoPE, limiting orthogonal maps to two‑channel support.  
- Using a pooled‑covariance surrogate, the derived rotation achieves its analytic minimum in variance reduction, yet perplexity remains unchanged when compared to full‑head mixing.  
- Interpolating from two‑channel to full‑head mixing reduces quantisation error and perplexity degradation, indicating that matching the surrogate’s support to the quantiser’s scale‑setting improves outcomes.

## Context
RoPE (Rotary Position Embedding) is widely used in transformer models to inject positional information without altering attention weights. Post‑training quantisation often employs orthogonal transforms like Hadamard to compress weight magnitudes while preserving accuracy. This work extends that discussion by examining how RoPE‑aligned rotations can be integrated into quantisation pipelines.

## Implications
For practitioners, the findings suggest that optimality for a structured surrogate does not automatically translate to lower quantisation error when the surrogate’s support mismatches the quantiser’s scale metric. Aligning these components may yield modest gains in dynamic 4‑bit schemes. The research highlights a nuanced trade‑off between theoretical variance minimisation and practical model performance, guiding future design of efficient quantisation strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13365v1)
