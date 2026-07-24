---
title: BaseRT: Advancing Best-in-Class LLM Inference with Apple M5 Neural Accelerators
published: 2026-07-21T06:42:18Z
authors: Fabian Waschkowski, Prabod Rathnayaka, Lukas Wesemann
url: http://arxiv.org/abs/2607.19438v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BaseRT: Advancing Best-in-Class LLM Inference with Apple M5 Neural Accelerators

## Abstract
Apple's M5 generation introduces a redesigned GPU architecture in which every core carries a dedicated Neural Accelerator: on-die matrix units exposed through the Metal~4 tensor API. We show that BaseRT, our native Metal inference runtime for large language models on Apple Silicon, exploits these units to push inference throughput on Apple hardware substantially beyond both llama.cpp and MLX. Building on BaseRT's framework-free design, we add a family of hand-written Metal~4 tensor-core kernels (including dense and mixture-of-experts GEMM and flash-attention prefill kernels) that route the compute-bound matrix multiplications of inference through the M5 Neural Accelerators while leaving the memory-bound decode path on our existing specialised kernels. On an Apple M5 Pro, across fifteen model configurations spanning the Qwen3, Qwen3.5/3.6, Llama~3.2, and Gemma~4 families from sub-1B to 35B parameters, BaseRT delivers up to $6.4\times$ higher prompt-processing throughput than llama.cpp and $3.9\times$ higher than MLX, with the largest margins on the mixture-of-experts models where matrix multiplication dominates, while maintaining its lead on decode of up to $1.75\times$ over llama.cpp and $1.33\times$ over MLX. These results establish a new performance ceiling for on-device LLM inference and show that the M5's tensor cores are the decisive lever for prompt processing on Apple Silicon. BaseRT is publicly available at https://github.com/basecompute/baseRT.

## Metadata
- **Published**: 2026-07-21T06:42:18Z
- **Authors**: Fabian Waschkowski, Prabod Rathnayaka, Lukas Wesemann
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19438v1)