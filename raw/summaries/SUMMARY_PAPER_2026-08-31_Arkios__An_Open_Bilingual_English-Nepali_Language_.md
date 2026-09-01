---
title: Arkios: An Open Bilingual English-Nepali Language Model Trained From Scratch, with a Devanagari-Aware Tokenizer
url: http://arxiv.org/abs/2608.30092v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_23-39-44Z_Arkios_AnOpenBilingualEnglish_NepaliLanguageModelT.md
generated_at: 2026-08-31 21:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
Arkios is a 1.04B‑parameter dense transformer pretrained from scratch on 150 billion tokens of English‑Nepali bilingual text, using a custom Devanagari‑aware byte‑level BPE tokenizer and a single‑file C/CUDA training stack. The model outperforms three comparably sized open models (Pythia‑1.4B, TinyLlama‑1.1B, OLMo‑1B) despite having an order of magnitude fewer training tokens, indicating strong performance driven by data alignment rather than sheer scale.

## Key Takeaways
- Arkios achieves higher scores on English‑Nepali tasks than larger open models while using far less training data, suggesting that matching the pretraining corpus to the ARC grade‑school science format yields significant gains.  
- Standard multiple‑choice prompts place both English and Nepali performance at chance (≈0.24), masking genuine comprehension; only answer‑text evaluation reveals real ability, highlighting a limitation of common evaluation harnesses for low‑resource languages.  
- The instruction‑tuned model incorporates a manifest‑conditioned tool‑use contract that restricts tool calls to declared manifests, and the base and instruction‑tuned weights are released under Apache‑2.0 while training code is provided.

## Context
The paper contributes to the growing interest in open bilingual models for low‑resource languages, demonstrating that token efficiency and data relevance can surpass larger monolingual counterparts. It also underscores challenges in evaluating multilingual systems where evaluation formats may produce misleading results, especially when the language’s script influences tokenization and prompt design.

## Implications
For practitioners building multilingual AI systems, Arkios shows that careful alignment of pretraining corpora with downstream tasks can deliver strong performance without massive resources. It also calls for adopting more nuanced evaluation protocols to avoid false negatives in low‑resource languages and for using tool‑use contracts to improve safety and reliability in deployed models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30092v1)
