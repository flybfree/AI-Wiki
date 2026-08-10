---
title: Autonomy-of-Heads: Data-Free Sparse Attention from Frozen Query-Key Geometry
url: http://arxiv.org/abs/2608.06849v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_06-18-18Z_Autonomy_of_Heads_Data_FreeSparseAttentionfromFroz.md
generated_at: 2026-08-09 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Autonomy-of-Heads (AoH), a data‑free technique that selects which attention heads to retain based on the spectral geometry of query‑key projections, eliminating the need for runtime attention scores or calibration prompts. Experiments show that at 50 % sparsity AoH retains about 96.5 % of full‑attention performance while cutting prefill latency by up to 41.4 %, decode latency by 66.0 %, and KV‑cache memory by 50 % for 256K tokens.

## Key Takeaways
- AoH uses the effective rank of the kernel operator M_h = W_K^{hᵀ}W_Q^h to distinguish retrieval heads (concentrated spectra) from streaming heads (diffuse spectra), providing a data‑free head diagnosis.  
- The method computes attention in d_head dimensions, avoiding the full d_model × d_model matrix and enabling efficient sparse computation.  
- At 50 % sparsity AoH maintains near‑full performance with substantial reductions in latency and memory usage across models.

## Context
Current large language model inference is limited by quadratic attention complexity and growing KV‑cache costs, which hinder long‑context generation. Existing solutions rely on runtime decisions that require additional data or prompts, complicating deployment. This work offers a principled, model‑agnostic approach to sparsify attention without external signals.

## Implications
AoH enables scalable inference for massive language models by reducing computational load and memory footprint, making high‑capacity LLMs more practical for real‑world applications. Practitioners can adopt this method to improve latency and cost efficiency while preserving most of the model’s performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06849v1)
