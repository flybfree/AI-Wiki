---
title: TaskPress: Query-Agnostic KV Cache Compression via Task-Guided Pruning
published: 2026-08-04T07:51:37Z
authors: Wonpyo Park, Seung-won Hwang
url: http://arxiv.org/abs/2608.03276v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TaskPress: Query-Agnostic KV Cache Compression via Task-Guided Pruning

## Abstract
Long-context inference with large language models is constrained by the linear growth of the key-value cache to sequence length. While pruning offers mitigation, prevailing methods determine query-specific token importance that cannot be reused across unseen queries. In contrast, we introduce TaskPress, a framework for task-guided, query-agnostic KV cache eviction. Instead of optimizing the cache for a single query, TaskPress constructs a reusable memory representation conditioned on a high-level task guide. The guide functions as a meta-query during prefill to filter irrelevant tokens before downstream queries are issued. In addition, TaskPress leverages quantization scale factors as a zero-cost signal for detecting influential representation outliers, providing an efficient proxy for token importance. Experiments on conducted on various tasks with long context input demonstrate that TaskPress efficiently creates a compact, reusable cache across diverse queries.

## Metadata
- **Published**: 2026-08-04T07:51:37Z
- **Authors**: Wonpyo Park, Seung-won Hwang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03276v1)