---
title: Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache
published: 2026-08-31T05:03:30Z
authors: Tong Yuan, Chengxi Liao, Zeyi Wen
url: http://arxiv.org/abs/2608.30252v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache

## Abstract
Long-context LLM applications such as document summarization and multi-turn agents require generation from prefixes spanning tens of thousands of tokens, making decoding latency a major bottleneck. Speculative decoding (SD) reduces latency without changing model outputs, but its speedup depends on both accepted draft tokens and draft-step latency: Lightweight drafts are fast but lack the capacity to capture long-range dependencies, whereas strong independent drafts recover acceptance but incur growing KV-access cost at long prefixes. We introduce memory-augmented drafting for long-context SD, equipping a strong independent draft with compressed draft-side KV memory: A lightweight adaptor constructs and incrementally updates this memory to retain distant information and exact recent context. The target verifier retains its full KV cache and applies the standard accept/reject rule, preserving SD's lossless guarantee. Experiments on Llama~3.1-8B and 70B targets at prefix lengths up to 32K show that our method reduces draft-side memory by over 70%. It achieves speedups of up to 2.08x and 3.33x , respectively, over autoregressive decoding.

## Metadata
- **Published**: 2026-08-31T05:03:30Z
- **Authors**: Tong Yuan, Chengxi Liao, Zeyi Wen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30252v1)