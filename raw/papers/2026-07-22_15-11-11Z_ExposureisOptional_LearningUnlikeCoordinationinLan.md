---
title: Exposure is Optional: Learning Unlike Coordination in Language Models
published: 2026-07-22T15:11:11Z
authors: Jiamu Luo, Shane Steinert-Threlkeld
url: http://arxiv.org/abs/2607.20251v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Exposure is Optional: Learning Unlike Coordination in Language Models

## Abstract
Coordination, a fundamental linguistic structure, remains a subject of intense debate, and its exact nature continues to elude theoretical linguistics. A common view holds that only same-category constituents can be conjoined, which has been challenged by the many grammatical unlike coordinations found in natural language. Treating language models as a computational testbed, we investigate whether the acquisition of unlike coordination requires direct exposure in the training data, or whether it can emerge organically from general compositional abilities. Using Filtered-Corpus Training (FiCT), we train GPT-2 models on corpora from which all instances of unlike coordination have been removed. We find that direct exposure is not necessary: models trained on filtered data successfully generalize to unlike coordination, achieving perplexity and grammaticality judgments comparable to models trained on unfiltered text. Furthermore, our analyses of internal representations indicate that language models process unlike coordination by treating the conjoined elements as belonging to similar structural categories or through a mechanism akin to deletion, both of which appear learnable from exposure to alike coordination alone. This work contributes to the growing understanding of how language models internally represent linguistic structures, while also adding to the broader debate on coordination by showing how models generalize and process unlike coordination without direct exposure.

## Metadata
- **Published**: 2026-07-22T15:11:11Z
- **Authors**: Jiamu Luo, Shane Steinert-Threlkeld
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20251v1)