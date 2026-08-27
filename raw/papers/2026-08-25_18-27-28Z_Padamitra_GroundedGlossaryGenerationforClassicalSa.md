---
title: Padamitra: Grounded Glossary Generation for Classical Sanskrit
published: 2026-08-25T18:27:28Z
authors: Manoj Balaji Jagadeeshan, Sai Pragnaan Marala, Pawan Goyal
url: http://arxiv.org/abs/2608.25038v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Padamitra: Grounded Glossary Generation for Classical Sanskrit

## Abstract
We introduce grounded glossary generation, a structured task requiring models to recover semantically meaningful Sanskrit phrases and produce translation-grounded meanings from a sloka-translation pair, formalizing the traditional patha commentary practice as an evaluable NLP objective. We construct a benchmark of 31,316 sloka-translation-glossary triples from the Valmiki Ramayana and Srimad Bhagavatam, paired with two metrics: Jaccard for phrase recovery and Meaning Faithfulness for semantic consistency. Across zero-shot, few-shot, and instruction fine-tuned variants of Gemma-3n-E4B, Gemma-3-12B, Phi-4, and Qwen3.5-9B, instruction fine-tuning substantially outperforms prompting, while explicit segmentation yields gains. Error analysis identifies over-segmentation of sandhi and samasa compounds as the dominant failure mode, pointing to morphological modeling as the key bottleneck for faithful Sanskrit lexical decomposition.

## Metadata
- **Published**: 2026-08-25T18:27:28Z
- **Authors**: Manoj Balaji Jagadeeshan, Sai Pragnaan Marala, Pawan Goyal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25038v1)