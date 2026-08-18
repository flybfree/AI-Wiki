---
title: SchurQuant: Groupwise Discrete Optimization for Layer-Wise LLM Quantization
url: http://arxiv.org/abs/2608.15567v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_06-29-10Z_SchurQuant_GroupwiseDiscreteOptimizationforLayer_W.md
generated_at: 2026-08-17 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes SCHURQUANT, a groupwise discrete optimization framework that improves post‑training quantization accuracy for large language models at low bit depths without backpropagation. On the 2‑bit Qwen3‑4B model it raises zero‑shot mean accuracy by 11.88 pp compared with GPTQ and exceeds the strongest baseline by 9.65 pp across eight Llama and Qwen variants.

## Key Takeaways
- Group decisions ignore correction that the remaining continuous suffix can absorb; SCHUROPT analytically eliminates this optimal response using Schur‑complement curvature.
- Discrete refinements typically keep the affine quantization grid fixed; SCHURQUANT alternates closed‑form row‑wise scale/zero‑point refitting with coordinate descent over integer codes.
- At higher precision, tighter reconstruction does not consistently improve end‑model metrics; SCHURQUANT therefore combines quantized‑prefix teacher reconstruction, reference‑weight regularization, residual‑add targets, and teacher‑decision token weighting.

## Context
Post‑training quantization is essential for deploying massive language models under tight memory budgets, yet existing backpropagation‑free optimizers suffer from limited accuracy gains. This work advances discrete optimization by providing exact groupwise quadratic solutions that respect both continuous and integer components of the quantization process.

## Implications
The results demonstrate that high‑quality 2‑bit models are achievable without gradient computation, reducing hardware costs for inference services. Practitioners can leverage SCHURQUANT to push accuracy while maintaining low memory footprints, encouraging wider adoption of quantized LLMs in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15567v1)
