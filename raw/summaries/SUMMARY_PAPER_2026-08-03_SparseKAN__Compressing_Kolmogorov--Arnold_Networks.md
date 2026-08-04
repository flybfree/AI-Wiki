---
title: SparseKAN: Compressing Kolmogorov--Arnold Networks Across Basis Functions, Neurons, and Bits
url: http://arxiv.org/abs/2608.00859v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_20-42-41Z_SparseKAN_CompressingKolmogorov__ArnoldNetworksAcr.md
generated_at: 2026-08-03 20:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SparseKAN, a method that compresses Kolmogorov–Arnold Networks along three axes: basis functions, neurons/channels, and numerical precision. It uses hierarchical learnable gates to select important coefficients and then hardens the selection under budget constraints, achieving compact models with minimal accuracy loss.

## Key Takeaways
- SparseKAN learns a differentiable active‑cost importance structure that guides which basis coefficients are retained, enabling compression without explicit sparse masks.
- The method supports full or low‑precision recovery of selected terms while fitting strict width and basis budgets, resulting in physical compaction up to 73 % parameter reduction on MNIST.
- Quantization experiments show eight‑bit quantization works broadly, but four‑bit convolutional KANs need adaptation; the compressed models also cut CUDA latency to about half of dense execution.

## Context
Kolmogorov–Arnold Networks are a class of function‑based neural architectures that replace edge weights with learnable univariate functions, yet they suffer from redundancy across basis coefficients. Traditional compression techniques do not fully exploit this redundancy, leading to inefficient parameter usage and hardware inefficiency. SparseKAN addresses these gaps by integrating cost‑aware selection with explicit budget enforcement.

## Implications
For practitioners, SparseKAN offers a practical pathway to deploy high‑accuracy KANs on resource‑constrained devices such as FPGAs and edge GPUs, where latency and memory are critical. The approach’s ability to compress both model structure and precision translates into tangible gains in inference speed and energy efficiency, encouraging broader adoption of function‑based models in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00859v1)
