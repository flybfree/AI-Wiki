---
title: Sparse Weight Decomposition for Efficient Circuit Extraction
url: http://arxiv.org/abs/2608.03913v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_16-40-48Z_SparseWeightDecompositionforEfficientCircuitExtrac.md
generated_at: 2026-08-05 01:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Sparse Weight Decomposition (SWD), a method that reparameterizes pretrained linear projection matrices into two sparse factors without training an auxiliary model. This allows circuit extraction to reuse the same scoring, selection, and ablation workflows as existing sparse feature methods while preserving high fidelity. Experiments on GPT‑2, Qwen2.5, and Qwen3.5 show that SWD matches or exceeds baseline replacement performance with far less data usage.

## Key Takeaways
- SWD factors each weight matrix into two sparse components whose shared coordinates act as addressable circuit units, enabling interpretable unit discovery without extra training.
- The method achieves the same held‑out fidelity as Transcoder and other strong baselines while using less than 1% of the data they require for replacement training.
- Full‑model replacement of attention and MLP matrices is possible by fine‑tuning only the nonzero factor values, supporting comprehensive mechanistic analysis.

## Context
Understanding how neural networks compute predictions remains a bottleneck in AI research. Current circuit extraction techniques often require costly auxiliary models or large datasets to learn sparse representations, limiting their practicality. SWD offers a lightweight alternative that integrates seamlessly with existing interpretability pipelines.

## Implications
For researchers and practitioners, SWD reduces the computational burden of mechanistic analysis while maintaining high accuracy, making large‑scale model interpretation more feasible. The zero‑data variant broadens applicability to any fine‑tuned transformer, encouraging systematic study of neural circuit behavior across diverse tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03913v1)
