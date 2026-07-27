---
title: Unified Static-Dynamic Pruning for Efficient LLM Inference
url: http://arxiv.org/abs/2607.21985v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_05-19-41Z_UnifiedStatic_DynamicPruningforEfficientLLMInferen.md
generated_at: 2026-07-26 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SPDP a unified static-dynamic pruning framework for large language model inference that combines unstructured weight removal with input‑adaptive runtime skipping to reduce GPU compute and memory usage. Experiments on inference‑optimized GPUs show average speedups of 1.24x–1.37x compared with state‑of‑the‑art sparse frameworks while preserving perplexity up to 25% higher sparsity.

## Key Takeaways
- SPDP integrates unstructured static pruning that permanently removes redundant weights with dynamic pruning that adapts to each input’s activation pattern, eliminating the trade‑off between adaptivity and runtime irregularity.  
- The Tiled‑Columnwise Bitmap Compressed format enables bandwidth‑efficient memory access and supports fine‑grained activation skipping via a CUDA‑core spMspV kernel with Hybrid Activation‑aware Dynamic Shared‑Memory Bitmap Decoding.  
- Tensor‑Core SpMM kernels compute prefill efficiently, delivering up to 2.51x speedup while matching perplexity despite higher sparsity.

## Context
Large language models dominate inference workloads where memory bandwidth and compute intensity are critical bottlenecks. Existing sparse inference methods either sacrifice adaptivity or incur overhead, limiting their practical deployment in real‑time serving environments.

## Implications
Unified static-dynamic pruning can be integrated into existing LLM pipelines without redesigning model architecture, offering practitioners a path to higher throughput and better performance‑per‑watt on GPUs. This research accelerates the adoption of sparsity for scalable inference systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21985v1)
