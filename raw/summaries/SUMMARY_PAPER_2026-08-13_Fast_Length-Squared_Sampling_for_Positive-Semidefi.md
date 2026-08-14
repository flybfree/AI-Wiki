---
title: Fast Length-Squared Sampling for Positive-Semidefinite Matrices
url: http://arxiv.org/abs/2608.12503v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_18-33-22Z_FastLength_SquaredSamplingforPositive_Semidefinite.md
generated_at: 2026-08-13 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a simple rejection-sampling algorithm that draws columns from an n×n positive‑semidefinite matrix with probability proportional to the square of their Euclidean norm. The method runs in expected O(n) time, which is optimal even for diagonal matrices, and it does not require precomputed column norms.

## Key Takeaways
- The algorithm achieves sublinear expected runtime by sampling directly from the matrix without needing auxiliary norm information.
- Its linear complexity is optimal because any algorithm must inspect at least one entry per row in the worst case.
- It enables asymptotically optimal Frobenius‑norm estimation for psd matrices and simplifies robust low‑rank approximation while matching existing complex methods.

## Context
In AI research, sublinear matrix algorithms are crucial for handling large data sets efficiently. This work contributes a theoretically tight sampling technique that can be integrated into downstream tasks such as low‑rank factorization and eigenvalue computation without sacrificing performance.

## Implications
Practitioners can use this O(n) sampler to accelerate machine‑learning pipelines that rely on psd matrices, reducing computational bottlenecks. The simplicity of the method also makes it easy to implement in real‑time systems where overhead matters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12503v1)
