---
title: SeDeM: Selective Decompression of Hidden-State Memories for Long-Context Question Answering
published: 2026-07-31T21:44:03Z
authors: Maryam Haghifam, Jason Cong, Yizhou Sun
url: http://arxiv.org/abs/2608.00311v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SeDeM: Selective Decompression of Hidden-State Memories for Long-Context Question Answering

## Abstract
Long-context inference with large language models (LLMs) is costly: self-attention during prefill scales quadratically with sequence length, and the key-value (KV) cache grows with the number of processed tokens. Larger context windows also do not ensure reliable evidence use. Context compression reduces this cost, but many soft-compression methods use LLMs as compressors and rely on compact memory tokens both to preserve information and to condition the decoder. We propose SeDeM, a selective decompression framework that decouples compact memory storage from decoder conditioning. An LLM extracts hidden states from a chosen intermediate Transformer layer, a lightweight compressor stores them as memory blocks, a query-conditioned selector selects relevant blocks, and a decompressor expands only the selected blocks into hidden states compatible with an intermediate decoder layer. Thus, the decoder avoids both full-context processing and direct generation from highly compressed memory slots. On four long-context QA benchmarks, SeDeM achieves higher QA scores than the evaluated compression baselines in both 1B and 3B same-backbone settings, and with the 3B backbone exceeds full-context fine-tuning on three datasets. The learned selector uses block-level evidence supervision during training. SeDeM also reduces online time-to-first-token and improves autoregressive decoding throughput relative to ICAE.

## Metadata
- **Published**: 2026-07-31T21:44:03Z
- **Authors**: Maryam Haghifam, Jason Cong, Yizhou Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00311v1)