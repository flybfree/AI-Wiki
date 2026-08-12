---
title: How Robust Are LLMs to Vietnamese Dialects?
url: http://arxiv.org/abs/2608.10414v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_03-02-57Z_HowRobustAreLLMstoVietnameseDialects.md
generated_at: 2026-08-11 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces VialectBench, a benchmark that tests how large language models handle Vietnamese dialectal variations across four natural‑language tasks. The study finds that all ten instruction‑tuned models degrade on average by 2.82 % when given dialect inputs, with no model fully invariant, and QA suffers the most severe drop.

## Key Takeaways
- Dialect rewrites cause a measurable shift in model relative likelihoods while keeping text length comparable to standard forms.  
- The largest performance drops occur for PNT3 (6.17 %) and PNT2 (4.73 %), whereas PNB slightly improves average scores by 0.42 %.  
- Central dialect group (PNT1‑PNT4) yields the highest harmful‑flip rate across all models, at 6.54 %.

## Context
The results highlight a gap between standard‑language model training and real‑world usage where regional dialects are common. Existing work normalizes dialects rather than measuring robustness, so this evaluation fills that void.

## Implications
For developers, the paper warns against assuming dialect invariance and suggests designing models to handle linguistic variation explicitly. For industry practitioners, it underscores the need for diverse test sets to ensure equitable performance across all user groups.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10414v1)
