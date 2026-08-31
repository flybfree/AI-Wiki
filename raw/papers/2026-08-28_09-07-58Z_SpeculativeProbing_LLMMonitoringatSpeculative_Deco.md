---
title: Speculative Probing: LLM Monitoring at Speculative-Decoding Cost
published: 2026-08-28T09:07:58Z
authors: Collin Zhang, Tingwei Zhang, Vitaly Shmatikov
url: http://arxiv.org/abs/2608.28099v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Speculative Probing: LLM Monitoring at Speculative-Decoding Cost

## Abstract
Real-time classification during language model inference is valuable for safety filtering, behavioral analysis, and model monitoring, but current approaches force a trade-off between accuracy and efficiency. Hidden-state probes are fast but limited: they are either not context-aware: operating on a single vector and cannot model interactions across positions; or they are very costly: having dedicated classifier models (Llama Guard, Qwen Guard, LLM-as-judge) or performing computation on hidden states for all tokens and then pooling the results (MultiMax). This shows an intrinsic trade-off between efficiency and accuracy.   However, we find that the speculative-decoding module in recent LLMs can be repurposed for efficient high-quality classification. By appending a trained soft prompt at the end of the target sequence, we can repurpose the speculative-decoding module into a sequence classifier. At inference time in a speculative-decoding pipeline, the KV cache is already in GPU memory, so classification adds negligible overhead. We evaluate on four classification tasks across four models (Qwen3.5-4B, 9B, 27B, MiniCPM4.1-8B). Our small probes consistently outperform zero-shot GPT-5.4-mini and, on multilingual prompt safety, match or beat specialized 8B safety classifiers (Qwen3Guard-Gen-8B, Llama-Guard-3-8B) without running a full LLM.

## Metadata
- **Published**: 2026-08-28T09:07:58Z
- **Authors**: Collin Zhang, Tingwei Zhang, Vitaly Shmatikov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28099v1)