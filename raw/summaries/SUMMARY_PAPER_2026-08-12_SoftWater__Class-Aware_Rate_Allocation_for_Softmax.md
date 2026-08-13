---
title: SoftWater: Class-Aware Rate Allocation for Softmax Quantization
url: http://arxiv.org/abs/2608.12026v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_13-06-50Z_SoftWater_Class_AwareRateAllocationforSoftmaxQuant.md
generated_at: 2026-08-12 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes SoftWater, a class‑aware rate allocation scheme for softmax quantization that treats the problem as a KL divergence minimization under 2‑bit constraints. It replaces the full Cholesky factorization with a per‑class scaled factorization and achieves lower head‑induced KL error than prior methods while preserving model performance.

## Key Takeaways
- SoftWater quantizes each class of softmax outputs using its own covariance‑weighted grid, giving fine grids to frequent low‑variance classes and coarse grids to rare high‑variance ones. - The method computes all necessary statistics in a single forward pass by reusing the Cholesky factorization across classes, enabling efficient lattice encoding via successive interference cancellation. - On Llama‑3.2‑1B‑Instruct, a 2‑bit head reduces stored bytes by 45–60 % with only a 2.9–3.7 % perplexity increase.

## Context
Quantization of softmax layers is critical because these heads dominate parameter count in small LLMs and directly affect model size without impacting inference quality. Prior approaches either ignore class‑specific variance or rely on expensive per‑class factorizations that hinder pipeline efficiency. SoftWater addresses both by providing a scalable, single‑pass solution.

## Implications
For practitioners, SoftWater enables practical head quantization even at 2 bits, preserving most of the original model size and only modestly degrading perplexity. This reduces deployment costs for large models where memory is scarce, encouraging wider adoption of quantized inference in edge devices and cloud services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12026v1)
