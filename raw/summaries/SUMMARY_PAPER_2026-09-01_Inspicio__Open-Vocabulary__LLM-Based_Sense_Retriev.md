---
title: Inspicio: Open-Vocabulary, LLM-Based Sense Retrieval for Historical Languages
url: http://arxiv.org/abs/2609.00998v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_09-46-38Z_Inspicio_Open_Vocabulary_LLM_BasedSenseRetrievalfo.md
generated_at: 2026-09-01 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Inspicio, an open‑vocabulary retrieval system that uses instruction‑tuned large language models to link tokens in historical sentences to English synsets without needing a source‑language sense inventory. Evaluated on Latin and Ancient Greek perception verbs, the pipeline achieves 96% Recall@50 with a hybrid similarity approach.

## Key Takeaways
- Inspicio retrieves English word senses from Open English WordNet by generating two translations, candidate definitions, and lemmas for each token, enabling cross‑lingual sense retrieval.
- The system combines dense definition‑synset similarity, sparse lemma matching, and Maximal Marginal Relevance re‑ranking to improve recall across diverse LLMs and embeddings.
- Best configurations reach 96% Recall@50 on manually annotated perception verbs, showing strong performance in both diachronic Italian data and PREMOVE test set.

## Context
Word sense disambiguation remains challenging for low‑resource languages where traditional WordNet resources are absent. Recent advances leverage LLMs to generate candidate senses, but most pipelines still assume a pre‑existing mapping. Inspicio demonstrates that open‑vocabulary retrieval can be effective when combined with dense and sparse similarity mechanisms.

## Implications
This work opens a pathway for sense retrieval in historical scripts without costly lexical inventories, reducing reliance on manual annotation. Practitioners can integrate such pipelines into multilingual NLP systems to support translation, information extraction, and cross‑lingual reasoning tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00998v1)
