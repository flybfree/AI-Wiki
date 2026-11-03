---
title: Integer-Exact Microscaling: Running MXFP4 Language Models on INT8 Matrix Units
url: http://arxiv.org/abs/2611.00486v1
type: paper-summary
date: 2026-11-02
source_paper: 2026-10-31_00-18-06Z_Integer_ExactMicroscaling_RunningMXFP4LanguageMode.md
generated_at: 2026-11-02 21:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper demonstrates that MXFP4 (4-bit floating-point) quantized language models can be executed as a single INT8 GEMM on hardware with INT8 matrix datapaths, such as Apple's M5 Neural Accelerators, provided a simple structural condition on block exponents is met. The authors show this condition is naturally satisfied by 97.9–99.997% of weight rows across seven real models, enabling a practical W4A8 pipeline that is both faster than existing MXFP4 implementations and more accurate than competing 4-bit formats like NVFP4.

## Key Takeaways
- A row of MXFP4 weights is exactly representable as one INT8 vector multiplied by a single power-of-two scale whenever its 32-element block exponents span at most three distinct values. Enforcing this constraint adds at most 1/16 of a row's largest rounding error to affected blocks, and real model weights already satisfy it in 97.9–99.997% of rows, including 99.93% of the 95 million rows in Qwen3.8-Flash-Next, a 125-billion-parameter MoE model.
- The authors introduce an "integer-exact" quantization format using 16-wide blocks with integer multipliers from 1 to 10 at 4.26 bits per weight. This format runs as a single exact INT8 GEMM without any per-block rescaling inside the reduction loop, outperforms NVFP4 (4.5 bits) in perplexity on five small models, and on Qwen3.8-Flash-Next's routed experts achieves KL divergence of 0.0557 versus 0.0553 for NVFP4 with scale search, while surpassing MLX's MXFP4 and affine INT4 quantization.
- A complete W4A8 system on the Apple M5 produces outputs bit-identical to the quantized reference and delivers 1.34–1.74× prefill speedup over MLX on a dense model, 1.10–1.57× on two MoE models up to 35B parameters, and 1.22–1.29× on Qwen3.8-Flash-Next, where shared non-GEMM overhead bounds further gains.

## Context
Large language model inference increasingly relies on hardware-specific quantization formats to fit models into consumer and edge accelerators. Apple's M-series Neural Accelerators expose INT8×INT8 as the fastest matrix datapath, creating a mismatch with the FP4-based microscaling formats (MXFP4, NVFP4) that the broader industry is standardizing for 4-bit inference. This paper bridges that gap by proving that the FP4-to-INT8 conversion can be made exact under a mild structural constraint, eliminating the per-block rescaling overhead that existing MXFP4 kernels impose inside the reduction loop.

## Implications
For practitioners deploying quantized LLMs on Apple silicon, this work provides a path to near-lossless 4-bit inference with measurable speedups over current MXFP4 toolchains, making large MoE models like Qwen3.8-Flash-Next practical on consumer hardware. For the quantization research community, the finding that real weight matrices overwhelmingly satisfy the three-exponent-span condition suggests that microscaling formats can be designed around integer-exact representations, potentially simplifying hardware kernels and reducing accuracy loss compared to formats requiring per-block scale search.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.00486v1)
