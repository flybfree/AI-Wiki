---
title: Extreme Compression of Per-Layer Embeddings via Cross-Layer Latent Vector Quantization
url: http://arxiv.org/abs/2610.31309v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_14-07-01Z_ExtremeCompressionofPer_LayerEmbeddingsviaCross_La.md
generated_at: 2026-10-22 22:19
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces OPTIC (Output-Path-fitted, Token-shared Indexed Codes), a novel quantization framework designed for extreme compression of Per-Layer Embeddings (PLE) in modern language models such as Gemma 4 E4B, where PLE constitutes 35.2% of total parameters. Rather than assigning each token-layer vector its own short code as conventional quantizers do, OPTIC stores a single quantized code tuple per token and reconstructs layer-specific embeddings via affine decoders fitted to the PLE output path. The method achieves approximately 97.8% retention of the uncompressed model's benchmark performance at roughly 100× compression, dramatically outperforming six conventional baselines including product quantization.

## Key Takeaways
- OPTIC fundamentally restructures the quantization paradigm for PLE by sharing a single code tuple across all layers for a given token, then applying layer-specific affine decoders to reconstruct the per-layer embeddings. This token-shared indexing approach avoids the information bottleneck of per-vector quantization, which limits each code to only a few bytes and severely degrades quality at extreme compression rates.
- At approximately 100× compression of bfloat16 E4B, OPTIC retains 97.8% aggregate performance across seven benchmarks, while product quantization, the strongest of six conventional baselines, retains only 66.3%. Even at extreme compression ratios of 594× and 1,002×, OPTIC preserves 90.5% and 84.1% of performance respectively, demonstrating remarkable robustness. On the official E4B release with 4-bit linear weights and 16-bit activations (W4A16), OPTIC still retains 96.9% at ~100× PLE compression.
- During inference at ~100× PLE compression, the compressed model uses 29.7% less GPU memory than the uncompressed-PLE variant at the same key-value cache size, while introducing at most 0.40% slowdown. This makes the compression practically deployable without meaningful latency penalties, addressing a critical bottleneck for serving large embedding-heavy models on constrained hardware.

## Context
The scaling of embedding capacity alongside Transformer computation represents a growing architectural trend in language model design, with Per-Layer Embeddings becoming a substantial fraction of model parameters. As models grow in both parameter count and embedding dimensionality, the memory footprint of embeddings becomes a dominant constraint for deployment on consumer GPUs, edge devices, and cost-sensitive inference infrastructure. Existing quantization techniques such as product quantization were designed for weight compression and struggle at the extreme ratios required for PLE, motivating the need for purpose-built compression methods that respect the multi-layer, token-indexed structure of these embeddings.

## Implications
For practitioners deploying large language models on memory-constrained hardware, OPTIC offers a path to compressing the single largest non-Transformer component of models like Gemma 4 E4B without sacrificing more than a few percentage points of task performance, enabling broader access to high-capability models on smaller GPUs. For the research community, the output-path-fitting principle—optimizing quantization codes against the downstream decoding path rather than the stored vectors themselves—suggests a generalizable strategy for compressing any structured, multi-stage embedding or lookup system in neural architectures. Industry deployments of embedding-heavy models for retrieval-augmented generation, recommendation systems, and on-device inference stand to benefit directly from the near-20% GPU memory reduction at negligible latency cost.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.31309v1)
