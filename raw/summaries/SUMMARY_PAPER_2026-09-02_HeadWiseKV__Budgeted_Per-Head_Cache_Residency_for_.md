---
title: HeadWiseKV: Budgeted Per-Head Cache Residency for Hybrid Long-Context Language Models
url: http://arxiv.org/abs/2609.02029v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_02-59-11Z_HeadWiseKV_BudgetedPer_HeadCacheResidencyforHybrid.md
generated_at: 2026-09-02 20:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HeadWiseKV, a training‑free method that allocates a fixed KV cache budget across heads of hybrid long‑context language models to reduce GPU memory usage. Experiments on four hybrid models and Qwen3.6‑27B show it preserves generation quality while cutting peak memory by 8.59% at 112K context length and extending the maximum verifiable context from 114K to 161K.

## Key Takeaways
- HeadWiseKV assigns each physical KV head a static, multilevel history window that makes cache demand predictable before serving.  
- The allocation is modeled as a restricted operational rate‑distortion problem solved by SeqCalib, which processes layers in execution order and conditions decisions on lower‑layer policies.  
- A grouped‑cache runtime materializes the selected policy as actual per‑head residency rather than a mask over the full cache.

## Context
Hybrid language models combine global attention with local recurrent paths, creating unpredictable KV cache growth that limits inference throughput. Efficient memory management is critical for scaling to long contexts without sacrificing performance or quality.

## Implications
This work provides a practical framework for deploying hybrid models at longer lengths while keeping GPU usage low, enabling broader accessibility and cost‑effective deployment in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02029v1)
