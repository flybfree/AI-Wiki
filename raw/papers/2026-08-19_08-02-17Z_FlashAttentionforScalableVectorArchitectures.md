---
title: FlashAttention for Scalable Vector Architectures
published: 2026-08-19T08:02:17Z
authors: Sonia Rani Gupta, Nikela Papadopoulou, Miquel Pericàs
url: http://arxiv.org/abs/2608.18656v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FlashAttention for Scalable Vector Architectures

## Abstract
Inference with transformer models on CPUs is increasingly important, especially for Small Language Models (SLMs), where vector architectures are emerging as a promising execution substrate. The attention module is a major bottleneck due to high memory bandwidth requirements; FlashAttention mitigates this by fusing operations to improve data locality and reduce intermediate memory traffic. In this paper, we present FlashAttention-V, a blocked FlashAttention for scalable vector architectures that adapts efficiently from short to very long vectors by exploiting parallelism across attention heads, inter-head packing to enable efficient utilization of vector lengths beyond the head dimension, and improving vector register utilization and memory access locality. We integrate FlashAttention-V into ggml within llama.cpp and evaluate it on TinyLlama, Llama 3.2, Qwen2.5, and Pythia-410M using gem5 and a Banana Pi BPI-F3. On the Banana Pi BPI-F3, we confirm that loop reordering and loop unrolling across attention heads are effective optimization principles, scaling performance gains with larger models and most pronounced with short contexts and during decoding. Simulation-based analysis shows that FlashAttention-V achieves 22x-42x speedup over scalar FlashAttention at 512-bit VL in prefill, with an additional 2x-2.5x gain scaling to 64 lanes and 4096-bit VL. During decode, FlashAttention-V achieves 8x-11x speedup using 512-bit vector lengths over scalar FlashAttention, with performance showing diminishing sensitivity to vector width and lane count due to single-token, memory-bound execution. We further identify structural bottlenecks in Q8_0 quantized linear layers that limit arithmetic amortization under long-vector execution, consistent across RVV and Arm SVE, indicating that current quantization formats pose a fundamental challenge to long-vector scalability.

## Metadata
- **Published**: 2026-08-19T08:02:17Z
- **Authors**: Sonia Rani Gupta, Nikela Papadopoulou, Miquel Pericàs
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18656v1)