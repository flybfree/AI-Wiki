---
title: TSWAP: A Multilingual Retrieval-Augmented Thai Wellness Advisor
url: http://arxiv.org/abs/2608.22917v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_07-54-07Z_TSWAP_AMultilingualRetrieval_AugmentedThaiWellness.md
generated_at: 2026-08-24 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TSWAP, a multilingual conversational wellness advisor that leverages retrieval‑augmented generation to answer questions about Thai traditional medicine and certified wellness providers. The system demonstrates high recall performance on its benchmark and real‑world QA logs while incorporating safety mechanisms and zero‑shot support for eight languages.

## Key Takeaways
- The hybrid dense‑sparse retriever with cross‑encoder reranking achieves a Recall@5 of 0.88 on a 30.6K‑chunk Thai index, enabling reliable grounding of LLM responses to verified knowledge.
- Without the safety prompt the backend model would generate unsafe drug dosing schedules and ignore out‑of‑scope requests, highlighting the necessity of rule‑based constraints for medical scope enforcement.
- The system requires forced retrieval routing; without it English‑calibrated 4‑bit AWQ quantization corrupts Thai tone marks, showing that grounding mechanisms are essential for accurate multilingual service.

## Context
Retrieval‑augmented generation is becoming a standard approach to keep large language models grounded in factual knowledge while mitigating hallucinations. This work extends the concept to a culturally specific domain—Thai wellness—and integrates safety and zero‑shot multilingual support, illustrating how grounding can be both effective and adaptable across languages.

## Implications
For practitioners building medical or wellness chatbots, TSWAP shows that combining retrieval with safety layers yields reliable, ethically sound responses. The findings suggest that quantization strategies must respect language‑specific formatting to avoid degradation, and that forced retrieval is a non‑negotiable component for high‑quality grounding in multilingual AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22917v1)
