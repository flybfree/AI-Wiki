---
title: PulseInfer: I/O-Centric Sparse KV Cache Offloading for Efficient Long-Context LLM Decoding
published: 2026-09-28T08:12:39Z
authors: Qiuyang Zhang, Kai Zhou, Kai Lu, Haocheng Lu, Jian Zhou, Yuanpeng Su, Kun Bao, Jiguang Wan, Fei Wu
url: http://arxiv.org/abs/2609.34555v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PulseInfer: I/O-Centric Sparse KV Cache Offloading for Efficient Long-Context LLM Decoding

## Abstract
Long-context LLM serving is increasingly bottlenecked by decode, where large KV caches limit batch size and underutilize GPUs. Sparse KV cache offloading expands effective capacity by storing most historical KV blocks in CPU DRAM and recalling only selected blocks on demand. However, we find that existing offloading systems shift the bottleneck to CPU-GPU recall I/O: recall volume varies widely across layers, decode steps and requests, while headwise sparse selection fragments recalls into many small PCIe transfers.   This paper presents PulseInfer, an I/O-centric sparse KV cache offloading system. PulseInfer hides variable recall latency with interruptible layer-wise scheduling, adapts offloading decisions with IO-Adaptive Offloading Admission, and coalesces fragmented transfers using SoloHead sparse selection and a gather-scatter I/O engine. Implemented on SGLang, PulseInfer improves decode throughput by up to 4.7x over SGLang and 2.6x over the best existing offloading baseline, while reducing TPOT by up to 76% and preserving near-lossless accuracy.

## Metadata
- **Published**: 2026-09-28T08:12:39Z
- **Authors**: Qiuyang Zhang, Kai Zhou, Kai Lu, Haocheng Lu, Jian Zhou, Yuanpeng Su, Kun Bao, Jiguang Wan, Fei Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34555v1)