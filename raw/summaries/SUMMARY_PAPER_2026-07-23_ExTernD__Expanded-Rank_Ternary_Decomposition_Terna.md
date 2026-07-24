---
title: ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM PTQ with Accuracy Approaching Any Quantization Level
url: http://arxiv.org/abs/2607.13511v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-15_07-04-32Z_ExTernD_Expanded_RankTernaryDecompositionTernaryLL.md
generated_at: 2026-07-23 23:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
ExTernD proposes a post‑training factorization of LLM weight matrices using ternary factors B and C with values in {‑1,0,+1} and a real scale vector D. By expanding the inner rank beyond full rank (μ > 1) the method corrects quantization errors from lower‑rank components, enabling accuracy to approach bf16 levels arbitrarily closely.

## Key Takeaways
- The expanded‑rank ternary decomposition lets residual error decrease monotonically with k and can be driven below any ε > 0, achieving bf16‑level precision.  
- Memory and compute scale continuously depend on μ while sparsity follows a threshold τ, so an exact accuracy target is met rather than rounded to the next bit width.  
- On Gemma‑4‑E2B and Qwen3.5‑4B models ExTernD reaches 5.2–5.5 effective bpw per matrix, matching Q4_K performance and a full conversion at μ = 3 yields 10.10 wikitext‑2 perplexity versus 9.78 for bf16, placing it near the Q4_K/Q5_K band.

## Context
LLM inference is increasingly constrained by memory and compute budgets, making quantization a critical bottleneck. Existing ternary schemes are limited to fixed plane counts that cannot fully resolve quantization error, leading to performance gaps at lower bit widths. ExTernD addresses this gap with a flexible rank‑expansion strategy.

## Implications
For practitioners, ExTernD offers a practical path to high‑fidelity inference without sacrificing memory efficiency, potentially enabling deployment of larger models on edge devices. Industry adoption could accelerate the transition from coarse quantization to near‑bf16 accuracy, reshaping hardware design and optimization priorities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.13511v1)
