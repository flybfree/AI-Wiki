---
title: Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM
url: http://arxiv.org/abs/2609.04098v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_17-04-26Z_WhyGatedDeltaNetSurvives4_BitQuantization_NVFP4W4A.md
generated_at: 2026-09-03 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the performance of a 4‑bit quantized hybrid large language model that includes Gated DeltaNet recurrent layers alongside linear attention. By applying NVFP4 W4A4 quantization to all 496 linear and GDN blocks, the authors demonstrate that perplexity at long contexts remains within seed noise of BF16 while achieving a smaller footprint and faster prefill speed than comparable methods.

## Key Takeaways
- NVFP4’s 16‑element block scaling localizes extreme activations in the residual stream, preventing error accumulation across many GDN layers and keeping activation errors balanced throughout the network.  
- The gate projections are less sensitive to quantization because softplus, exponential, or sigmoid parameterizations compress GEMM errors from ~11 % down to only ~2 % of the output error.  
- The delta‑rule recurrence injects noise at a flat plateau over 32 K tokens and forgets state impulses within hundreds of steps because each write overwrites the current key direction, so per‑token quantization cost does not compound.

## Context
Hybrid LLMs combine softmax attention with linear‑attention layers that maintain compact recurrent states. Early 4‑bit quantization efforts often left these recurrent components in higher precision, fearing error buildup over long contexts. This work shows that those fears are unfounded when a uniform low‑precision scheme is applied and when the recurrence’s write mechanism resets quickly.

## Implications
The findings provide a practical recipe for fully quantizing hybrid models without sacrificing performance or speed, encouraging developers to adopt NVFP4 W4A4 as a standard. It also clarifies that the recurrent half of such architectures is inherently more tolerant to quantization than the attention half, guiding future research on mixed‑precision training and deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04098v1)
