---
title: ECA-BLS: An Efficient Complex-Augmented Broad Learning System
url: http://arxiv.org/abs/2608.29763v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_12-50-13Z_ECA_BLS_AnEfficientComplex_AugmentedBroadLearningS.md
generated_at: 2026-08-31 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ECA‑BLS, a real‑domain variant of complex augmented BLS that cuts computational cost while preserving the exact decision function of CA‑BLS. By reformulating the model entirely in the real domain, it achieves up to 75 % fewer multiplications and over 60 % fewer additions compared with the original complex version. Experiments on 26 benchmark datasets show that ECA‑BLS consistently outperforms classical BLS and recent state‑of‑the‑art randomized neural networks in accuracy, average rank, and statistical significance.

## Key Takeaways
- The complex augmentation transforms real inputs into phase‑encoded complex representations to capture second‑order statistics that conventional BLS cannot model.  
- ECA‑BLS reformulates the entire architecture in the real domain without losing theoretical equivalence, delivering massive computational savings while maintaining exact decision function performance.  
- Benchmark results demonstrate consistent outperformance across accuracy, average rank, and statistical significance on 26 UCI and KEEL datasets.

## Context
Broad Learning Systems provide fast training and strong generalization with limited data, yet they are confined to real‑valued representations that cannot fully exploit second‑order dependencies in complex domains. This work fills a critical gap by introducing augmented modeling of latent nonlinearities and coherence structures that were previously inaccessible to BLS formulations.

## Implications
Practitioners can deploy ECA‑BLS for real‑time applications where inference efficiency is paramount, such as signal processing or quantum‑inspired machine learning. The approach demonstrates that complex second‑order modeling can be achieved with minimal computational overhead, opening new research directions and practical implementations in AI research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29763v1)
