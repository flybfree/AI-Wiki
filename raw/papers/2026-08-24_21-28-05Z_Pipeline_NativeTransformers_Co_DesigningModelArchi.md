---
title: Pipeline-Native Transformers: Co-Designing Model Architecture and CPU Inference for Bandwidth-Efficient Autoregressive Decode
published: 2026-08-24T21:28:05Z
authors: Tom Poperszky
url: http://arxiv.org/abs/2608.23841v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pipeline-Native Transformers: Co-Designing Model Architecture and CPU Inference for Bandwidth-Efficient Autoregressive Decode

## Abstract
Single-token autoregressive decode on CPUs is bound by memory bandwidth, not arithmetic: a modern CPU sustains roughly 1 TFLOP/s of compute but only about 50 GB/s from main memory, and each generated token must stream every active weight once. This report argues that the most effective response is to co-design the model architecture and the inference runtime together. It presents cflow, a CPU-first streaming engine, alongside a family of pipeline-native transformer architectures whose inter-layer dependency graphs are constructed to permit a vertical, stage-major execution schedule.   cflow stores weights as L2-sized tiles in compute-consumption order, reads only the top-k experts of each mixture-of-experts layer, fuses projections, and executes a delay-aware schedule from per-model dependency parameters. Across five architectures trained on TinyStories, one (arch2_4_combined) achieves a 2.00x reduction in critical-path weight bandwidth (9.00 to 4.50 MB/token) within 0.24 perplexity of the best candidate, and the tile layout incurs 7.29x fewer L1-data read misses than a row-major baseline. On a 30.9-billion-parameter pipeline-native MoE, cflow decodes at 5.94 tokens/s (tok/s) on a 32-vCPU Ice Lake server, ahead of llama.cpp (4.75) and the vLLM CPU backend (1.65) on comparably sized dense models. Realizing the expert-delay window as asynchronous I/O overlap on a disk-resident expert tier yields a further net win of up to 1.68x, matching the overlap model within 1%. Measurement refutes one of the eight design claims and leaves a second inconclusive; both are reported in full, with the conditions under which they would hold.

## Metadata
- **Published**: 2026-08-24T21:28:05Z
- **Authors**: Tom Poperszky
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23841v1)