---
title: FuTransformer: FP8 prefill and INT4 decode for Llama-style inference on Hopper
url: http://arxiv.org/abs/2610.23796v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_17-22-01Z_FuTransformer_FP8prefillandINT4decodeforLlama_styl.md
generated_at: 2026-10-18 23:39
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
FuTransformer presents a highly optimized CUDA implementation of a Llama-style Transformer inference block targeting NVIDIA Hopper GPUs, combining FP8 precision for the prefill phase with INT4 quantized weights and KV-cache for the decode phase. The work achieves substantial speedups over existing PyTorch and CODA baselines—up to 1.48x for prefill and 1.3–6.3x for decode—while maintaining acceptable perplexity degradation, demonstrating that aggressive quantization and hardware-aware kernel design can coexist with practical inference quality.

## Key Takeaways
- The prefill path leverages CODA's GEMM-plus-epilogue methodology but extends it with direct KV-cache placement, folding the fixed RMSNorm gain into weight matrices, and writing FP8 outputs with delayed scaling to avoid intermediate buffer overhead. This yields 1.29 PFLOP/s throughput and up to 1.48x speedup over compiled PyTorch FP8, with the FP8 path being 2.02–2.18x faster than the evaluated BF16 CODA path for gate/up projections with SwiGLU at the 8B shape.
- The decode path introduces INT4 projection weights and an INT4 KV-cache copy, with weights and keys stored in Tensor Core fragment layouts so they can be dequantized directly into MMA operands without materializing full intermediate tiles. A block-diagonal Hadamard transform is applied to reduce cache quantization error from outlier channels. Across 8B and 70B model shapes at batch sizes 1–32, INT4 decode is 1.3–2.4x faster than the best of PyTorch's BF16 and INT4 blocks, 2.1–3.3x faster than compiled CUDA-graphed BF16, and 31–51% faster than the paper's own FP8 path.
- End-to-end quality is characterized: complete Llama-3.1-8B decode runs at 2.8 ms per step at batch one versus 8.1 ms for the compiled transformers implementation. Decoding every WikiText-2 token through the INT4 weight path raises perplexity from 6.24 to 7.23 with round-to-nearest weights or 6.99 with GPTQ, while the rotated INT4 cache adds 0.20 perplexity. The custom kernels match a quantized reference computation within 0.001 perplexity, confirming implementation correctness.

## Context
This paper sits at the intersection of low-precision quantization research and GPU kernel engineering for large language model serving. As Llama-family models dominate open-weight deployment, the community has been actively exploring FP8 and INT4 quantization to reduce memory bandwidth and compute costs on modern accelerators like NVIDIA H100. FuTransformer advances this line by integrating quantization-aware kernel design—Tensor Core fragment layouts, epilogue fusion, and Hadamard-based outlier mitigation—into a single coherent inference pipeline rather than treating quantization as a separate preprocessing step.

## Implications
For practitioners deploying Llama-style models on Hopper hardware, FuTransformer demonstrates that a single hand-tuned CUDA kernel can outperform compiled PyTorch and existing quantization frameworks by large margins, potentially reducing serving costs and latency in production inference stacks. The explicit perplexity accounting for INT4 weight and cache paths gives deployment teams concrete quality-versus-speed tradeoff data, while the Hadamard transform technique offers a reusable strategy for mitigating quantization error in KV-cache compression, a bottleneck that grows with context length in long-context serving workloads.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23796v1)
