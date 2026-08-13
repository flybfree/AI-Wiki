---
title: Gloss-Free Representation Learning for Cross-Dataset Sign Spotting
published: 2026-08-11T18:31:57Z
authors: Oğuz Akif Tüfekcioğlu, Ezgi Ekin, Mustafa Kaan Çevik, Hacer Yalim Keles
url: http://arxiv.org/abs/2608.11332v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gloss-Free Representation Learning for Cross-Dataset Sign Spotting

## Abstract
Sign-language research for resource-constrained languages is often limited by the cost of dense linguistic labels such as glosses, temporal boundaries, and sign order. Broadcast news offers a practical alternative by pairing continuous signing with spoken-language transcripts, but this supervision is weak since text and signing are loosely aligned. Morphologically rich languages such as Turkish add further difficulty, as the same lexical meaning can appear in many inflected forms while some derived forms should remain distinct. We study whether weak transcript-based supervision can pretrain a reusable sign encoder in this setting, where poor text normalization can fragment pseudo-gloss targets and weaken representation learning. Unlike prior pseudo-gloss pipelines designed mainly to improve translation, we test whether the pretrained encoder transfers as a reusable representation for cross-dataset sign spotting. We pretrain on TSL-News, a new Turkish broadcast corpus, using pseudo-gloss labels derived from transcripts rather than manual annotation, comparing rule-based morphological lemmatization with constrained LLM-assisted normalization over a fixed vocabulary. We evaluate the learned representations via cross-dataset sign spotting on a new TSL Spotting Benchmark built from the TSL Dictionary corpus. The LLM-assisted encoder raises top-5 temporal localization mean IoU from 0.235 to 0.465, with 56.2% of examples reaching an IoU of at least 0.50; a frequency analysis suggests this gain is not mainly driven by memorizing frequent pseudo-gloss labels. In a downstream translation check, the same pretraining improves BLEU-4 from 9.60 to 11.04 and ROUGE from 23.48 to 27.43. These results show that loosely aligned broadcast data can provide effective weak supervision for learning sign representations that capture both lexical content and temporal structure.

## Metadata
- **Published**: 2026-08-11T18:31:57Z
- **Authors**: Oğuz Akif Tüfekcioğlu, Ezgi Ekin, Mustafa Kaan Çevik, Hacer Yalim Keles
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11332v1)