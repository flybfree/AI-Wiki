---
title: ASPIRE: Asynchronous Batched Self-Speculative Decoding for Long-Context LLM Inference
published: 2026-09-16T00:04:13Z
authors: Amir Ziashahabi, Hossein Entezari Zarch, Lei Gao, Murali Annavaram, Salman Avestimehr
url: http://arxiv.org/abs/2609.17943v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ASPIRE: Asynchronous Batched Self-Speculative Decoding for Long-Context LLM Inference

## Abstract
Long-context LLM inference is bottlenecked by attention, whose repeated KV-cache reads make decoding memory-bound. Self-speculative decoding alleviates this by drafting tokens with sparse attention and verifying them with full attention, but existing batched methods remain synchronized: all requests in a batch share a single draft-verify schedule, even though the optimal draft length varies widely across requests and changes dynamically within each request. We propose ASPIRE, a non-synchronized batched self-speculative decoding framework built on three components. First, a unified mixed forward allows drafting and verifying requests to coexist in the same batched forward pass, removing the need for global draft-verify phases. Second, a lightweight online speculation scheduler uses per-request acceptance-rate estimates and a batch-aware cost model to let each request independently choose when to verify. Third, an intra-draft refresh layer performs full attention at a single designated layer during drafting, updating the sparse context at every draft step to reduce staleness during drafting. Across three models and five reasoning and long-context benchmarks, ASPIRE achieves $1.70$-$4.58\times$ speedup in decoding throughput over autoregressive baselines and improves average speedup by approximately $27\%$ over the strongest prior self-speculative baselines.

## Metadata
- **Published**: 2026-09-16T00:04:13Z
- **Authors**: Amir Ziashahabi, Hossein Entezari Zarch, Lei Gao, Murali Annavaram, Salman Avestimehr
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.17943v1)