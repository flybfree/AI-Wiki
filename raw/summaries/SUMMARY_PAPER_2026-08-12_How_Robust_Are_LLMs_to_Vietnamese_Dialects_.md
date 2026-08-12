---
title: How Robust Are LLMs to Vietnamese Dialects?
url: http://arxiv.org/abs/2608.10414v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_03-02-57Z_HowRobustAreLLMstoVietnameseDialects.md
generated_at: 2026-08-12 08:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces VialectBench, a benchmark that tests how large language models handle six Vietnamese dialect groups alongside standard written Vietnamese. The study shows that all evaluated instruction‑tuned LLMs degrade on average by 2.82 % when given dialectal inputs, with no model fully invariant to dialect variation. Performance drops are highest for PNT3 and PNT2 dialects (6.17 % and 4.73 %) while the Central dialect group causes a harmful‑flip rate of 6.54 %.

## Key Takeaways
- Dialectal rewrites induce a measurable model‑relative likelihood shift, indicating that models are sensitive to surface form changes even when meaning is preserved.
- The average performance reduction across ten models is 2.82 %, and the largest individual drops occur for PNT3 (6.17 %) and PNT2 (4.73 %).
- No model achieves full dialect invariance; central dialects (PNT1‑PNT4) consistently produce the highest harmful‑flip rates.

## Context
The research highlights a gap between standard benchmarking practices that ignore regional linguistic variation and real‑world usage where meaning is conveyed through dialectal forms. By quantifying performance degradation under dialect inputs, this work contributes to more realistic assessments of model robustness in multilingual and multicultural settings.

## Implications
For developers and practitioners, the findings suggest that relying solely on standard Vietnamese benchmarks may overestimate a model’s reliability across diverse user bases. Industry adoption should incorporate dialect‑aware evaluation metrics to ensure equitable performance and avoid unintended bias amplification in regional communities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10414v1)
