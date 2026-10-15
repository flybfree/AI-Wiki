---
title: MemCode: Discrete Semantic Representations for Long-Term Agent Memory
published: 2026-10-14T02:51:29Z
authors: Xin Li, Liang Hu, Duoqian Miao, Ming Peng, Qi Zhang
url: http://arxiv.org/abs/2610.19472v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemCode: Discrete Semantic Representations for Long-Term Agent Memory

## Abstract
Long-term memory remains a fundamental bottleneck for large language model (LLM) agents across sessions. Existing systems typically adopt a write-then-retrieve paradigm, storing context-dependent dialogue fragments and retrieving them via nearest-neighbor search in a continuous embedding space. This design yields unstable access units and systematically misses logically related but lexically distant evidence. We propose MemCode, a long-term agent memory framework that couples retrieval-oriented writing with discrete associative retrieval. MemCode rewrites dialogue into self-contained atomic memory units (AMUs), maps AMUs into a learnable codebook with isomorphic semantic quantization (ISQ), and uses codebook co-occurrence topology as a retrieval path complementary to vector search. For long-term memory stores, MemCode separates online atomic writes from asynchronous offline consolidation. On LongMemEval-S and LoCoMo with GPT-4o-mini and Qwen3-30B-A3B-Instruct-2507 backbones, MemCode achieves the best overall accuracy while keeping per-dialogue memory construction within roughly 40~130 seconds, making it 3~21 times faster than LightMem and over an order of magnitude faster than A-MEM and MemoryOS.

## Metadata
- **Published**: 2026-10-14T02:51:29Z
- **Authors**: Xin Li, Liang Hu, Duoqian Miao, Ming Peng, Qi Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19472v1)