---
title: Q-Strata: Hierarchical Bit Allocation for Mixed-Precision Quantization of Mixture-of-Experts LLMs
url: http://arxiv.org/abs/2608.30564v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_10-39-01Z_Q_Strata_HierarchicalBitAllocationforMixed_Precisi.md
generated_at: 2026-08-31 21:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Q‑Strata, a hierarchical bit allocation algorithm for Mixture‑of‑Experts large language models that optimizes mixed‑precision quantization under a fixed budget. By separating within‑block assignments from across‑block decisions and using a model‑level objective on the assembled quantized model, Q‑Strata outperforms uniform‑bitwidth GPTQ and state‑of‑the‑art MoE MPQ methods in low‑bit regimes.

## Key Takeaways
- The inner stage creates a Pareto frontier of candidate assignments per block for finely spaced budgets, allowing cheap ranking without evaluating the full model.  
- The outer stage selects one budget per block instead of allocating bitwidths to every linear layer, directly optimizing the assembled model’s objective and capturing inter‑block coupling missed by additive proxies.  
- On Mixtral‑8x7B‑Instruct, Qwen1.5‑MoE‑A2.7B, and DeepSeek‑V2‑Lite, Q‑Strata consistently reduces WikiText2 perplexity compared to uniform GPTQ and the best MoE MPQ baselines.

## Context
Mixture‑of‑Experts models replicate dense architectures across many experts, inflating the search space for bit allocation. Traditional approaches either treat each block uniformly or use additive proxies that ignore cross‑block interactions, limiting quantization quality. This work addresses the scalability and coupling challenges inherent to MoE systems.

## Implications
For practitioners deploying large, modular LLMs, Q‑Strata offers a practical path to high‑quality mixed‑precision inference without exhaustive search. The method’s efficiency could lower hardware costs while maintaining performance, encouraging broader adoption of quantized MoE models in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30564v1)
