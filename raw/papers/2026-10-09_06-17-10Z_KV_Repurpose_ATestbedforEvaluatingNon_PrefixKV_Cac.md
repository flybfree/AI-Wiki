---
title: KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse
published: 2026-10-09T06:17:10Z
authors: Taiga Ikeda, Daisuke Miyashita, Jun Deguchi
url: http://arxiv.org/abs/2610.13060v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse

## Abstract
KV-cache reuse in large language model serving is commonly limited to exact prompt prefixes, preventing reuse when the same retrieved document appears after different system prompts, conversation histories, or dynamic metadata. We present KV-Repurpose, an open-source, vLLM-based system for developing and evaluating segment-wise KV-cache reuse beyond exact prefixes. The system combines cache-aware segment scheduling, prompt construction, capacity management, workload generation, and runtime monitoring. Experiments on long-context benchmarks show that naive segment reuse largely preserves output quality for single-document question answering and summarization, while exposing clear limitations in cross-document reasoning. Under a Zipfian RAG-style workload in which 20% of requests share a fixed prefix, KV-Repurpose achieves a substantially higher token-level cache hit rate than prefix caching at the same 30 GB cache capacity, 63.9% versus 3.3%, resulting in lower TTFT. Even with 1 TB of cache capacity, prefix caching reaches only a 17.9% hit rate in this workload. Source code is available under the Apache-2.0 license at https://github.com/taiga333/eval-kv-repurpose.

## Metadata
- **Published**: 2026-10-09T06:17:10Z
- **Authors**: Taiga Ikeda, Daisuke Miyashita, Jun Deguchi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13060v1)