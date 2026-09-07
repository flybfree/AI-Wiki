---
title: Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving
url: http://arxiv.org/abs/2609.04748v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_05-27-34Z_SameRequest_DifferentAnswer_QuantizationAmplifiesC.md
generated_at: 2026-09-06 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how prefix caching in LLM serving introduces nondeterministic behavior when model weights are quantized, causing repeated requests to diverge in outcomes.  

## Key Takeaways
- Prefix caching amplifies divergence from 0% to 36.2% at 16-bit precision and 75.0% at four-bit, indicating cache state influences results beyond model parameters.  
- The server-level prompt-cache setting is the primary driver of run-to-run differences, moving divergence by 37.5 percentage points when active.  
- Re-computing paths still differ on 14 items despite identical cache state, showing cached and recompute branches are not fully deterministic.  

## Context
This work highlights a hidden source of nondeterminism in large language model deployment that can affect reproducibility studies.  

## Implications
For practitioners, it means caching must be treated as a non‑deterministic factor when benchmarking or debugging AI agents. The findings urge explicit cache reset mechanisms to ensure consistent results across runs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04748v1)
