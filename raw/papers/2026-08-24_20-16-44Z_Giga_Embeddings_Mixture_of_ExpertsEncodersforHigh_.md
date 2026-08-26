---
title: Giga-Embeddings: Mixture-of-Experts Encoders for High-Throughput Text Embeddings
published: 2026-08-24T20:16:44Z
authors: Egor Kolodin, Egor Krasnoperov, Evgeniy Kosarev, Fyodor Minkin
url: http://arxiv.org/abs/2608.23806v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Giga-Embeddings: Mixture-of-Experts Encoders for High-Throughput Text Embeddings

## Abstract
We introduce Giga-Embeddings, a family of text embedding models designed to combine strong retrieval quality with efficient serving. Its largest member is a sparse 10B-parameter Mixture-of-Experts encoder with approximately 1.8B active parameters per token. Across English, Russian, multilingual, and code MTEB benchmarks, this model achieves the strongest aggregate performance within the family on all four evaluated suites. In our vLLM benchmark with 1024-token inputs, it processes 114.5k tokens per second, providing 25 percent higher throughput than the dense 3B model and 1.56-2.65x the throughput of the evaluated external systems. The family also includes a dense 3B encoder and a distilled 480M encoder for tighter compute and memory budgets. We train the compact model using a dimension-agnostic objective that aligns teacher and student similarity distributions. The resulting 480M model scores 70.98 on Russian MTEB, surpassing FRIDA while using 42 percent fewer parameters. We release all three model checkpoints.

## Metadata
- **Published**: 2026-08-24T20:16:44Z
- **Authors**: Egor Kolodin, Egor Krasnoperov, Evgeniy Kosarev, Fyodor Minkin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23806v1)