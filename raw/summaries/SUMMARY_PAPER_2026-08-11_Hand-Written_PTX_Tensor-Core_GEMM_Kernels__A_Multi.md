---
title: Hand-Written PTX Tensor-Core GEMM Kernels: A Multi-Precision Study on NVIDIA L4
url: http://arxiv.org/abs/2608.10103v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_18-13-00Z_Hand_WrittenPTXTensor_CoreGEMMKernels_AMulti_Preci.md
generated_at: 2026-08-11 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates when hand‑written PTX Tensor Core GEMM kernels outperform the WMMA C++ API on an NVIDIA L4 GPU across FP16, INT8 and INT4 precisions. It finds that PTX yields speedups only for low‑precision integer arithmetic, while FP16 gains are negated by packing overhead.

## Key Takeaways
- Hand‑written PTX provides no end‑to‑end speedup for FP16 because instruction‑level benefits are offset by operand‑packing overhead. 
- PTX kernels achieve consistent 1.4×–1.8× speedups for INT8 due to lower instruction counts and better global‑memory coalescing. 
- The best quantized kernels reach up to 98.7× at N=8192, driven by native mma.sync.m16n8k64.s4 execution that avoids software emulation.

## Context
The study highlights a gap between high‑level abstraction and low‑level performance on modern Tensor Cores, where quantization and memory bandwidth dominate throughput. This research informs developers seeking to maximize throughput beyond the WMMA API’s convenience.

## Implications
For AI practitioners, the findings suggest targeting INT4 or INT8 workloads for hand‑written PTX kernels rather than relying on FP16 WMMA abstractions. Industry adoption may focus on quantization pipelines that exploit these speedups in large‑scale inference tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10103v1)
