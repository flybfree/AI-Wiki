---
title: Giga-Embeddings: Mixture-of-Experts Encoders for High-Throughput Text Embeddings
url: http://arxiv.org/abs/2608.23806v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_20-16-44Z_Giga_Embeddings_Mixture_of_ExpertsEncodersforHigh_.md
generated_at: 2026-08-25 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents Giga-Embeddings, a family of Mixture-of-Experts encoders that balance retrieval quality with serving efficiency. The largest model is a sparse 10B‑parameter encoder that activates only about 1.8B parameters per token and delivers the highest performance across English, Russian, multilingual, and code MTEB benchmarks.

## Key Takeaways
- A sparse Mixture-of-Experts encoder with 10B total parameters uses roughly 1.8B active parameters per token, achieving strong retrieval scores while keeping memory usage low.
- The dense 3B model processes 114.5k tokens per second in vLLM, offering 25% higher throughput than the previous dense baseline and up to 2.65x faster than external systems.
- A distilled 480M encoder reaches a Russian MTEB score of 70.98, outperforming FRIDA while using only 42% fewer parameters thanks to a dimension‑agnostic alignment objective.

## Context
Mixture-of-Experts models are increasingly used to scale language embeddings without proportionally increasing compute or memory demands. This work demonstrates that sparsity can be applied effectively even at the billion‑parameter level, offering a practical path toward high‑throughput text embedding services.

## Implications
For industry practitioners, Giga‑Embeddings suggests that sparse architectures can replace dense models in production pipelines, reducing latency and cost while maintaining or improving performance. Researchers should explore similar alignment techniques to further compress large Mixture-of-Experts systems for broader deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23806v1)
