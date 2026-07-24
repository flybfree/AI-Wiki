---
title: Unlearning Under Imbalance: Benchmarking Fairness in Multimodal LLM Unlearning
url: http://arxiv.org/abs/2607.21300v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_13-24-34Z_UnlearningUnderImbalance_BenchmarkingFairnessinMul.md
generated_at: 2026-07-23 22:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces FAIRGET, a benchmark for evaluating fairness in multimodal large language model unlearning under realistic, imbalanced request patterns, and FAUN, an algorithm that unlearns identities while preserving fairness. Experiments on the new benchmark show that standard unlearning methods can introduce bias when forget data is skewed, whereas FAUN maintains both high unlearning quality and equitable performance across demographic groups.

## Key Takeaways
- Unlearning in multimodal LLMs often fails to account for uneven request frequencies, causing biased internal representations of certain demographic identities.  
- The proposed benchmark FAIRGET creates diverse, realistic forget scenarios that expose these fairness issues, allowing systematic comparison with existing methods.  
- FAUN’s bias‑aware activation steering successfully removes identity information without degrading model fairness or unlearning accuracy.

## Context
Machine unlearning is essential for compliance with data privacy regulations and ethical AI deployment. However, most prior evaluations assume uniform request distribution, which does not reflect real‑world usage where some groups are over‑represented in removal requests. This gap limits the reliability of unlearning techniques in diverse settings.

## Implications
For practitioners, FAIRGET provides a practical tool to stress‑test fairness during model updates, ensuring that personal data removal does not inadvertently harm protected groups. Industry adoption could lead to more equitable AI systems that respect both privacy and non‑discriminatory behavior.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21300v1)
