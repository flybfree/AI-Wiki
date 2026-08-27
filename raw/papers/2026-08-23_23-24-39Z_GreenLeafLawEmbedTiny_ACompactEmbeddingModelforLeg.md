---
title: GreenLeaf Law Embed Tiny: A Compact Embedding Model for Legal Domain Retrieval
published: 2026-08-23T23:24:39Z
authors: Surya Saka
url: http://arxiv.org/abs/2608.24936v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GreenLeaf Law Embed Tiny: A Compact Embedding Model for Legal Domain Retrieval

## Abstract
We present GreenLeaf Law Embed Tiny, a 0.6B parameter embedding model for legal domain retrieval. GreenLeaf-Tiny achieves 75.11% on the Massive Legal Embedding Benchmark (MLEB) and 64.38% on MTEB(Law, v1),demonstrating competitive performance among models under 1B parameters. Our approach combines a two-stage training pipeline that first distills knowledge from a larger teacher model into a compact student architecture, then applies domain-specific fine-tuning with hard negative mining; a carefully curated dataset of 3.4 million query-passage pairs, including 150,000 human-curated samples across diverse legal jurisdictions; and an efficient inference architecture supporting multiple quantization levels (BF16, INT8, binary) enabling deployment in resource-constrained environments. We provide detailed analysis of our training methodology, architectural choices, and comprehensive evaluation across legal retrieval tasks. Our results demonstrate that domain-specific training with high-quality data can improve performance for specialized domain applications

## Metadata
- **Published**: 2026-08-23T23:24:39Z
- **Authors**: Surya Saka
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24936v1)