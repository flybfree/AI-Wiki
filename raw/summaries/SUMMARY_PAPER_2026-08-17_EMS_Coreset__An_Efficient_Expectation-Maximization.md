---
title: EMS Coreset: An Efficient Expectation-Maximization Algorithm for Sinkhorn Coreset
url: http://arxiv.org/abs/2608.16101v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_04-46-34Z_EMSCoreset_AnEfficientExpectation_MaximizationAlgo.md
generated_at: 2026-08-17 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes EMS Coreset, a scalable Expectation‑Maximization algorithm for constructing Sinkhorn coresets that reduces the computational cost of Optimal Transport selection while preserving approximation quality. The method yields centroids that generalize k‑means through soft assignments and provides asymptotic consistency with Lipschitz stability guarantees.

## Key Takeaways
- EMS Coreset introduces non‑uniform weights to enable closed‑form updates of entropically regularized OT couplings, eliminating the need for iterative transport plan computation.  
- The resulting coresets maintain asymptotic consistency with the original data distribution and exhibit Lipschitz stability, meaning small perturbations in the dataset produce only modest changes in the selected measure.  
- Benchmarks show that EMS Coreset achieves competitive or improved approximation quality compared to Wasserstein‑based and standard Sinkhorn coresets while cutting runtime substantially at large scale.

## Context
The need for efficient data representation remains a bottleneck as machine learning pipelines process massive datasets. Traditional OT‑based coreset selection is computationally prohibitive, limiting its use in real‑time applications. This work addresses that bottleneck by offering a method that balances accuracy with speed.

## Implications
For practitioners, EMS Coreset enables faster downstream training without sacrificing performance, making large‑scale learning feasible. In industry, the reduced runtime translates to lower hardware costs and higher throughput for data‑driven products.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16101v1)
