---
title: AnchorKV: Anchor-Residual KV Cache Compression
published: 2026-08-03T21:38:30Z
authors: Malik Khalaf, Yara Shamshoum, Nitzan Hodos, Yuval Sieradzki, Assaf Schuster
url: http://arxiv.org/abs/2608.02901v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AnchorKV: Anchor-Residual KV Cache Compression

## Abstract
The key-value (KV) cache is the primary memory bottleneck in long-context LLM inference. Existing approaches attack it from opposite ends: eviction methods permanently discard tokens, degrading performance whenever a discarded token later proves essential, while quantization methods retain all tokens at low precision but offer limited compression. We propose AnchorKV, a compression scheme that shrinks the cache by $20\times$ without discarding a single token. AnchorKV represents the cache using a small set of anchors stored exactly, expresses every other token through its most similar anchor, and refines only those whose approximation most affects the model's output. AnchorKV consistently preserves accuracy across models and datasets, retaining 99% of the full-cache score at the 70B scale, while keeping the entire context at a fraction of its cost.

## Metadata
- **Published**: 2026-08-03T21:38:30Z
- **Authors**: Malik Khalaf, Yara Shamshoum, Nitzan Hodos, Yuval Sieradzki, Assaf Schuster
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02901v1)