---
title: BHARATI: Morphology-Aware Tokenizers for Classical Indian Languages with Subword Fertility Analysis
url: http://arxiv.org/abs/2607.23319v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_18-23-06Z_BHARATI_Morphology_AwareTokenizersforClassicalIndi.md
generated_at: 2026-07-27 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces BHARATI, a set of SentencePiece BPE tokenizers tailored for classical Indian languages, addressing inefficiencies caused by agglutinative morphology and phonological sandhi. The authors evaluate three tokenizer versions (v1‑v3) on a balanced corpus and show that v3 reduces token usage per technical term to 2.6 compared with GPT‑2’s 5.25 tokens. On test sentences, v3 cuts sequence length by about 90% relative to GPT‑2.

## Key Takeaways
- BHARATI’s tokenizer architecture is language‑specific and includes native script support for all seven Indian languages, eliminating byte‑fallback for Tamil in later versions.
- Subword fertility analysis reveals that v3 achieves a 61 % reduction in tokens per IKS technical term versus GPT‑2, directly improving effective context length.
- The released tokenizer models (32 000 vocabulary) and evaluation scripts are open‑licensed, enabling reproducible research on classical language processing.

## Context
Classical Indian languages have long been under‑represented in modern subword tokenization datasets, which are built from contemporary corpora. This gap leads to poor segmentation for agglutinative morphology and phonological sandhi, limiting performance of downstream models. BHARATI bridges this gap by providing linguistically informed tokenizers that respect native script structures.

## Implications
For AI practitioners working with multilingual or domain‑specific language models, BHARATI offers a practical solution to reduce sequence length and improve efficiency without sacrificing linguistic fidelity. The open release encourages community adoption and further research on classical language NLP, potentially lowering computational costs for large‑scale inference pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23319v1)
