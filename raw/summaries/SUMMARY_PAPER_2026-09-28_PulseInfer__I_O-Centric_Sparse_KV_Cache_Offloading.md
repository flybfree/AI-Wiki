---
title: PulseInfer: I/O-Centric Sparse KV Cache Offloading for Efficient Long-Context LLM Decoding
url: http://arxiv.org/abs/2609.34555v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_08-12-39Z_PulseInfer_I_O_CentricSparseKVCacheOffloadingforEf.md
generated_at: 2026-09-28 23:24
model: qwen3.6-35b-a3b
---

## Summary
PulseInfer addresses the I/O bottlenecks inherent in sparse KV cache offloading for long-context LLM decoding by introducing an I/O-centric architecture that optimizes CPU-GPU data transfers. The system employs interruptible layer-wise scheduling, IO-adaptive admission control, and a gather-scatter engine to coalesce fragmented recalls, significantly improving throughput and reducing latency without sacrificing accuracy.

## Key Takeaways
- Existing sparse offloading systems shift the performance bottleneck to CPU-GPU recall I/O due to highly variable recall volumes across layers and requests, as well as fragmented PCIe transfers caused by headwise sparse selection; PulseInfer resolves this via a gather-scatter I/O engine and SoloHead sparse selection that coalesce small transfers into efficient bulk operations.
- The system utilizes interruptible layer-wise scheduling to hide the latency of variable recall operations and implements IO-Adaptive Offloading Admission to dynamically adjust offloading decisions based on real-time I/O conditions, ensuring robust performance under fluctuating workloads.
- Implemented on SGLang, PulseInfer delivers up to a 4.7x increase in decode throughput over the base framework and a 2.6x improvement over the best existing offloading baseline, while reducing Time Per Output Token (TPOT) by up to 76% and preserving near-lossless model accuracy.

## Context
As large language models increasingly handle extended contexts, the memory footprint of KV caches grows exponentially, straining GPU resources and limiting batch processing capabilities in production serving environments. While sparse offloading offers a path to expand effective capacity by leveraging CPU DRAM, prior approaches have struggled with inefficient data movement that negates the benefits of reduced memory pressure.

## Implications
This work demonstrates that optimizing the I/O pipeline is as critical as algorithmic sparsity for realizing the full potential of

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34555v1)
