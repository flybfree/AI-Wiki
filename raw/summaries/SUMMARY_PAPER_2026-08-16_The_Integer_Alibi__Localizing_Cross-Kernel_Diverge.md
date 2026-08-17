---
title: The Integer Alibi: Localizing Cross-Kernel Divergence in INT8-Quantized LLM Inference
url: http://arxiv.org/abs/2608.13756v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_20-34-36Z_TheIntegerAlibi_LocalizingCross_KernelDivergencein.md
generated_at: 2026-08-16 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates why two GPU kernels implementing the same scaled INT8 GEMM interface in vLLM produce divergent outputs despite identical checkpoints, prompts, and quantization settings. By swapping only the linear kernel (CUTLASS versus Triton) across Qwen3-1.7B and 8B models, the authors demonstrate that end‑to‑end predictions differ on every sequence tested. The investigation reveals an “integer alibi”: while INT32 dot products remain exact and order‑independent under a no‑overflow bound, differences arise from scale application and output rounding after the accumulator, causing at most one bfloat16 spacing variance.

## Key Takeaways
- Localizing the divergence to scale application and output rounding shows that the accumulator cannot explain kernel‑swap discrepancies.  
- Bit‑identical outputs are observed under power‑of‑two scales, confirming a pinned prediction list for 196/196 and 252/252 layers respectively.  
- Cross‑implementation FP8 GEMM exhibits growing divergence with reduction depth, whereas INT8 differences stay within parts per million and one spacing over a wide range of K.

## Context
The work addresses a longstanding concern in quantized large language model inference: whether kernel interchangeability guarantees identical results. As models grow larger and quantization schemes become more common, subtle numerical differences can affect performance and reliability without being visible to users. This study provides empirical evidence that such differences are often confined to specific arithmetic stages rather than the entire pipeline.

## Implications
For practitioners deploying quantized LLMs, this research offers a concrete check for kernel interchangeability by exposing where rounding errors may propagate. It also suggests that monitoring per‑layer predictions can serve as a safeguard against hidden discrepancies in inference pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13756v1)
