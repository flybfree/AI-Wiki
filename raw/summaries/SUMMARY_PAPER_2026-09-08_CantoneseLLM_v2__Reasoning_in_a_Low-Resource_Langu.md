---
title: CantoneseLLM v2: Reasoning in a Low-Resource Language
url: http://arxiv.org/abs/2609.06970v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_03-08-43Z_CantoneseLLMv2_ReasoninginaLow_ResourceLanguage.md
generated_at: 2026-09-08 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CantoneseLLM v2, a series of large language models built on Qwen3 8B and 30B‑A3B that are trained to generate reasoning traces in the low‑resource Cantonese language. The authors demonstrate that techniques such as chat‑vector merging, supervised fine‑tuning (SFT), directed policy optimization (DPO) and reinforcement learning from language vectors (RLVR) can restore or enhance performance on Hong Kong‑focused evaluation benchmarks while preserving native Cantonese reasoning behavior.

## Key Takeaways
- Chat‑vector merging transfers instruction following to the model but keeps the donor model’s reasoning language intact, showing a balance between utility and linguistic fidelity.  
- SFT with limited Cantonese reasoning data tends to erase or shorten reasoning traces, leading to a noticeable drop in benchmark scores compared to the merged checkpoint.  
- RLVR training using Cantonese language and Traditional Chinese scripts as multiplicative constraints re‑aligns the model’s language and recovers most of the performance lost during SFT.

## Context
The study addresses a well‑known challenge in multilingual AI: limited data for low‑resource languages like Cantonese, which hampers the development of models that can reason fluently. By integrating diverse training strategies and releasing both model checkpoints and a large Traditional Chinese Common Crawl corpus, the work contributes to the broader effort of building inclusive language models.

## Implications
For practitioners, CantoneseLLM v2 shows that hybrid fine‑tuning pipelines can mitigate data scarcity without sacrificing linguistic authenticity. This approach could be replicated for other under‑represented languages, fostering more equitable AI systems and opening new markets where Cantonese is the primary user language.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.06970v1)
