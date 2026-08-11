---
title: Explicit Boundary Markers for Subword Vocabularies
published: 2026-08-09T18:16:51Z
authors: Sander Land, Clara Meister
url: http://arxiv.org/abs/2608.08847v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Explicit Boundary Markers for Subword Vocabularies

## Abstract
Subword tokenizers represent many common words twice in space-using writing systems, once with a leading space and once without. The two entries have separate embeddings in models, so occurrences of one word are divided across rows that are trained independently, and the two forms need not even segment the string the same way: " together" may be a single entry while the same word without a preceding space is tokenized as "to|gether". Capitalization divides a word further, into as many as six forms. We introduce an alternative to standard whitespace conventions using an explicit word boundary marker, which prevents such duplication. Words are delimited by the boundary markers, and spaces between words are represented as pairs of such markers. Two shift codes do the same for title case and upper case, allowing one internal representation of a word to be re-used across different settings. Switching to this convention mitigates the duplicate-entry issue, but does not improve tokenization compression: for both vocabulary-learning algorithms, the best marker scheme stays within one percent of the baseline in characters per token, averaged across six languages. It does result in better language modeling performance. Every marker scheme tested downstream reaches lower bits per byte than the baseline, suggesting that duplication carries a cost that compression does not capture.

## Metadata
- **Published**: 2026-08-09T18:16:51Z
- **Authors**: Sander Land, Clara Meister
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08847v1)