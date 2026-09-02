---
title: OCGQuant: Outlier-Companion Grouping for NVFP4 Quantization
url: http://arxiv.org/abs/2609.00066v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-30_16-00-11Z_OCGQuant_Outlier_CompanionGroupingforNVFP4Quantiza.md
generated_at: 2026-09-01 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces OCGQuant, a post‑training quantization method that reduces activation outliers in NVFP4 blocks by pairing large outlier channels with low‑magnitude companion channels. It defines collateral quantization error and shows that OCGQuant yields the lowest WikiText‑2 perplexity and highest downstream accuracy among evaluated PTQ methods while preserving near‑RTN prefill speedup.

## Key Takeaways
- The method defines collateral quantization error as the reducible error caused by remaining block values when a block’s scale is set by its maximum, highlighting how outliers dominate scaling.  
- OCGQuant adaptively pairs outlier channels with low‑magnitude companion channels to improve NVFP4 activation composition and reduce this error.  
- Experiments on Llama3 and Qwen3 demonstrate that OCGQuant achieves the best perplexity and accuracy while matching RTN’s peak decoding memory.

## Context
Low‑bit inference formats like NVFP4 are crucial for efficient AI deployment, yet outlier activations can degrade quantization performance without extra computation. Existing PTQ techniques either ignore this issue or add overhead, limiting their suitability for real‑world models.

## Implications
This work shows that channel‑level grouping can be a lightweight solution to outlier errors in low‑bit formats, encouraging more research into structured quantization strategies. Practitioners can adopt OCGQuant to improve model quality without sacrificing speed, supporting broader adoption of efficient inference pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00066v1)
