---
title: WeaveMark: Robust and Scalable Multi-bit LLM Watermarking via Coded Payload Spreading
published: 2026-09-02T06:39:43Z
authors: Gang-Hyun Park, Ju-Hyeong Lee, Hee-Youl Kwak, Dae-Young Yun
url: http://arxiv.org/abs/2609.02177v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WeaveMark: Robust and Scalable Multi-bit LLM Watermarking via Coded Payload Spreading

## Abstract
Multi-bit watermarking for large language models (LLMs) enables content source tracing by embedding user-identifiable messages into generated text. Existing methods face a fundamental trade-off among extraction accuracy, text quality, and payload capacity. We propose WeaveMark, a robust and scalable multi-bit LLM watermarking scheme based on coded payload spreading. WeaveMark shifts this trade-off frontier by improving payload capacity through multi-bit-per-token spreading, improving extraction accuracy through soft-decision error-correcting code, and preserving text quality through unbiased multilayer reweighting. It further introduces dedicated zero-bit layers for reliable watermark presence detection. Experiments show large gains, especially for long messages and edited text. WeaveMark achieves 89.8% match rate for 32-bit messages at 200 tokens, compared with 20.8% for BiMark. Under 10% substitution attacks on 16-bit messages at 200 tokens, it maintains 86.0% versus 30.7%, while preserving text quality. Our code is available at https://github.com/qkrrkd90-source/WeaveMark.

## Metadata
- **Published**: 2026-09-02T06:39:43Z
- **Authors**: Gang-Hyun Park, Ju-Hyeong Lee, Hee-Youl Kwak, Dae-Young Yun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02177v1)