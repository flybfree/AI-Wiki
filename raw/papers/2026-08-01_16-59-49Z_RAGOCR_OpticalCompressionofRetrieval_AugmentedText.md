---
title: RAGOCR: Optical Compression of Retrieval-Augmented Text via Visual Representation
published: 2026-08-01T16:59:49Z
authors: Jiayang Yu, Jialun Zhong, Lei Zou
url: http://arxiv.org/abs/2608.00765v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RAGOCR: Optical Compression of Retrieval-Augmented Text via Visual Representation

## Abstract
Retrieval-Augmented Generation (RAG) has become essential for knowledge-intensive question answering, yet scaling RAG pipelines remains challenging due to the prohibitive computational cost of processing lengthy retrieved contexts. Existing compression approaches face a fundamental trade-off: hard compression methods operate online in a query-aware fashion but achieve only modest compression rates and typically require fine-tuning the generative model, while soft compression methods attain higher ratios but rely on costly offline encoding that is entirely agnostic to the input query. To bridge this gap, we introduce RAGOCR, a novel framework that compresses retrieved documents into compact visual representations conditioned on the input query. To further balance compression rate and information fidelity, we introduce a query-aware dynamic resolution mechanism that adaptively allocates visual granularity based on each document's estimated relevance and complexity: highly relevant passages are rendered at higher resolution to preserve fine-grained details, while peripheral documents are aggressively compressed at lower resolution. Experiments on five QA benchmarks using the MedOmniKB retrieval corpus demonstrate that RAGOCR surpasses naive RAG by over 15\% in accuracy while requiring only one-eighth the number of input tokens, and consistently outperforms both hard and soft compression baselines across varying retrieval depths.

## Metadata
- **Published**: 2026-08-01T16:59:49Z
- **Authors**: Jiayang Yu, Jialun Zhong, Lei Zou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00765v1)