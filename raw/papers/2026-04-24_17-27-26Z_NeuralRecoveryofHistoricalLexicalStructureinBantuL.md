---
title: Neural Recovery of Historical Lexical Structure in Bantu Languages from Modern Data
published: 2026-04-24T17:27:26Z
authors: Hillary Mutisya, John Mugane
url: http://arxiv.org/abs/2604.22730v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neural Recovery of Historical Lexical Structure in Bantu Languages from Modern Data

## Abstract
We investigate whether neural models trained exclusively on modern morphological data can recover cross-lingual lexical structure consistent with historical reconstruction. Using BantuMorph v7, a transformer over Bantu morphological paradigms, we analyze 14 Eastern and Southern Bantu languages, extract encoder embeddings for their noun and verb lemmas, and identify 728 noun and 1,525 verb cognate candidates shared across 5+ languages. Evaluating these candidates against established historical resources-the Bantu Lexical Reconstructions database (BLR3; 4,786 reconstructed Proto-Bantu forms) and the ASJP basic vocabulary-we confirm 10 of the top 11 noun candidates (90.9%) align with previously reconstructed Proto-Bantu forms, including *-ntU 'person' (8 languages), *gombe 'cow' (9 languages), and *mUn (9 languages). Extending to verbs, 12 verb cognates align with reconstructed Proto-Bantu roots, including *-bon- 'see' and *-jIm- 'stand', each attested across wide geographic ranges. Cross-model validation using an independent translation model (NLLB-600M) confirms these patterns: both models recover cognate clusters and phylogenetic groupings consistent with established Guthrie-zone classifications (p < 0.01). Cross-lingual noun class analysis reveals that all 13 productive classes maintain >0.83 cosine similarity across languages (within-class > between-class, p < 10^-9). Our dataset is restricted to Eastern and Southern Bantu, so we interpret these results as recovering shared Bantu lexical structure consistent with Proto-Bantu rather than definitively distinguishing Proto-Bantu retentions from later regional innovations.

## Metadata
- **Published**: 2026-04-24T17:27:26Z
- **Authors**: Hillary Mutisya, John Mugane
- **Source**: [ArXiv Link](http://arxiv.org/abs/2604.22730v1)