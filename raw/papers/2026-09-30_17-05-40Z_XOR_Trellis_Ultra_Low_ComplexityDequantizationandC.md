---
title: XOR-Trellis: Ultra-Low-Complexity Dequantization and Curvature-Aware Hadamard-Free LLM Quantization
published: 2026-09-30T17:05:40Z
authors: Xiaofan Que, Nir Elkayam, Spandan Pyakurel, Shuokai Pan, Dibakar Gope
url: http://arxiv.org/abs/2610.00432v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# XOR-Trellis: Ultra-Low-Complexity Dequantization and Curvature-Aware Hadamard-Free LLM Quantization

## Abstract
Trellis-coded quantization enables high-dimensional compression of large language model (LLM) weights at ultra-low bit widths without the exponentially large codebooks required by conventional vector quantization. Practical deployment, however, presents two challenges: reconstructing compressed weights at sufficient parallel throughput to avoid making dequantization an inference bottleneck, and maintaining quantization accuracy without costly incoherence transformations. We address these challenges with two complementary techniques. First, we introduce an ultra-low-complexity trellis dequantizer that uses a structured, hardware-efficient state-to-value mapping while preserving diverse reconstruction choices for trellis search. Second, we reformulate discrete trellis path optimization with a curvature-aware objective that reflects model sensitivity directly in the original coordinate space. Together, these techniques enable high-quality ultra-low-bit trellis quantization with inexpensive, highly parallel runtime reconstruction and without relying on Hadamard-based incoherence processing.

## Metadata
- **Published**: 2026-09-30T17:05:40Z
- **Authors**: Xiaofan Que, Nir Elkayam, Spandan Pyakurel, Shuokai Pan, Dibakar Gope
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00432v1)