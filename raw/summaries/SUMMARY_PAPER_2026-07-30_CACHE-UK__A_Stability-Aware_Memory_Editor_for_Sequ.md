---
title: CACHE-UK: A Stability-Aware Memory Editor for Sequentially Updated Quantized LLMs in Finance
url: http://arxiv.org/abs/2607.28292v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_14-36-11Z_CACHE_UK_AStability_AwareMemoryEditorforSequential.md
generated_at: 2026-07-30 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CACHE‑UK, a stability‑aware memory editing framework for quantized LLMs in finance. Evaluated on a 4‑bit OpenLLaMA‑3B model with UK financial data, it reduces knowledge degradation by 11–17% and improves test success from 22% to 28%, outperforming adapted baselines.

## Key Takeaways
- CACHE‑UK uses a rank‑1 LoRA perturbation that limits edits to the low‑rank adapter subspace, preserving most of the model’s original weights.  
- The financial domain prioritization module dynamically adjusts edit strength based on content relevance, ensuring only critical facts are updated.  
- A closed‑loop Stability Controller monitors “degradation debt” across sequential updates, preventing catastrophic forgetting.

## Context
Quantized LLMs are increasingly deployed in resource‑constrained settings such as finance, where memory is limited but factual accuracy is paramount. Existing editing methods often cause severe performance drops when models are updated repeatedly, highlighting a stability crisis that this work addresses.

## Implications
Stability‑aware editing can enable cost‑effective deployment of financial LLMs without sacrificing too much accuracy. Practitioners may adopt CACHE‑UK’s components to maintain up‑to‑date knowledge in quantized systems while keeping training overhead low.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28292v1)
