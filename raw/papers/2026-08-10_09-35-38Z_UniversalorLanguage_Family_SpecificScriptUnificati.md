---
title: Universal or Language-Family-Specific Script Unification for Cross-Lingual Transfer? A Case Study on Turkic Languages
published: 2026-08-10T09:35:38Z
authors: Zijie Zhang
url: http://arxiv.org/abs/2608.09356v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Universal or Language-Family-Specific Script Unification for Cross-Lingual Transfer? A Case Study on Turkic Languages

## Abstract
Closely related languages written in different scripts expose little surface overlap to multilingual models, limiting cross-lingual transfer. We compare two approaches to script unification: the general-purpose uroman romanizer and the family-specific Common Turkic Script (CTS). We train matched fastText models on transliterated Wikipedia corpora from 11 Turkic languages and evaluate them on WikiANN named entity recognition and Universal Dependencies part-of-speech tagging. CTS and uroman show no significant difference on NER, while both substantially outperform the official monolingual fastText baselines. POS results reveal no universal winner: language-specific differences are associated with the cross-lingual character n-gram coverage induced by each representation, while within-language coverage becomes more important when target-language supervision is available. Although CANINE-c achieves higher overall POS averages, the substantially simpler fastText-based systems remain competitive on several treebanks. Overall, the effectiveness of script unification depends on the language, the induced subword overlap, and the available supervision.

## Metadata
- **Published**: 2026-08-10T09:35:38Z
- **Authors**: Zijie Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09356v1)