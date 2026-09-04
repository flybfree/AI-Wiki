---
title: Synthetic Semantic Supervision for Contrastive Code Representation Learning in Small Transformers: An Empirical Study
published: 2026-09-03T11:41:09Z
authors: Kenneth Paulsen, Florian Tambon, Mike Papadakis, Shin Yoo
url: http://arxiv.org/abs/2609.03702v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Synthetic Semantic Supervision for Contrastive Code Representation Learning in Small Transformers: An Empirical Study

## Abstract
General-purpose code embeddings power tools for code search, classification, and retrieval. Compact transformer encoders for code typically rely on either human-written docstrings (labor-intensive and inconsistent) or mined structural signals such as execution traces (setting-specific and costly to collect). We empirically study an alternative: contrastive pretraining of small encoders with synthetically generated natural-language descriptions emphasizing code functionality and intent, paired with code in a dual-encoder framework at training and discarded at inference. We benchmark this approach against pretraining-based baselines, generalist LLMs, and embedding-specific models on eight retrieval, classification, and generation tasks across C, C++, and Java. Synthetic semantic supervision yields statistically significant gains over pretraining baselines of the same inference-time size on five of eight tasks, with parity on two more; once fine-tuned, it matches or exceeds zero-shot models two orders of magnitude larger on classification, and it stays on par with execution-aware supervision at matched pretraining data, suggesting a scalable, effective alternative to existing code-representation paradigms.

## Metadata
- **Published**: 2026-09-03T11:41:09Z
- **Authors**: Kenneth Paulsen, Florian Tambon, Mike Papadakis, Shin Yoo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03702v1)