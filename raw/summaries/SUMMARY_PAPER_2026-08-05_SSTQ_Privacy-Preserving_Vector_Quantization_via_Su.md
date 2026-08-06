---
title: SSTQ:Privacy-Preserving Vector Quantization via Subsampled Stochastic TurboQuant
url: http://arxiv.org/abs/2608.05127v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_17-51-25Z_SSTQ_Privacy_PreservingVectorQuantizationviaSubsam.md
generated_at: 2026-08-05 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SSTQ, a privacy-preserving vector quantization method that reduces communication overhead in federated learning by using subsampled stochastic turboquantization. It achieves optimal mean squared error scaling while limiting codebook bits to ceil(log2 N)+b where N is frame size. The framework includes two variants: flat randomized response and metric-aware Laplace, with the latter better for high bit-width regimes.

## Key Takeaways
- SSTQ reduces codebook-dependent MSE scaling from O(4^b) to O(2^b) by using a surrogate privacy-aware objective.
- Communication cost is limited to ceil(log2 N)+b bits per client, where N = Θ(d).
- The metric-aware Laplace variant outperforms the flat randomized response in higher codebook bit-width regimes.

## Context
Vector quantization remains challenging for federated settings because high-dimensional embeddings increase communication and variance. Existing methods like vqSGD suffer from dimension-dependent performance that hampers scalability. SSTQ addresses these issues by decoupling error scaling from codebook size through subsampling and privacy-aware quantization.

## Implications
This work enables efficient, low‑communication federated optimization without sacrificing utility, making it suitable for real‑world deployments where data privacy is paramount. Practitioners can adopt SSTQ to build robust models while meeting differential privacy constraints, accelerating research in decentralized machine learning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05127v1)
