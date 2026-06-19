---

title: 'Dimensionality Reduction for Robust Federated Learning: A Theoretical Analysis and Convergence Guarantee'
published: "2026-05-27T11:39:47Z"
authors: Shiyuan Zuo, Jiashuo Li, Rongfei Fan, Han Hu, Jie Xu
url: http://arxiv.org/abs/2605.28335v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Dimensionality Reduction for Robust Federated Learning: A Theoretical Analysis and Convergence Guarantee



**Source**: [Original Paper](http://arxiv.org/abs/2605.28335v1)
## Abstract
Federated Learning (FL) enables multiple clients to collaboratively train models without sharing raw data, but it is highly vulnerable to Byzantine attacks. Existing robust approaches can neutralize these threats but incur substantial computational overhead during high-dimensional gradient aggregation, an overhead that scales poorly with model size and increasingly dominates the training cost as modern models grow larger. To address this computational bottleneck, we propose Projected Dimensionality Reduction (PDR), a universal acceleration framework for vector-level distance-based robust aggregators, which performs robust aggregation by compressing gradients into a drastically smaller subspace via sparse random projection to efficiently compute reliability weights. This approach reduces the server computational complexity to an optimal $ \mathcal{O}(Mp) $, where $ M $ is the number of clients and $ p $ is the model dimension, matching the theoretical lower bound required merely to read the gradients. We establish convergence guarantees under standard FL assumptions in prior Byzantine-robust FL analyses. By leveraging the Subspace Embedding Theorem, we show that PDR achieves optimal convergence rates of $ \mathcal{O}(1/\sqrt{T}) $ for non-convex functions and $ \mathcal{O}(1/T) $ for strongly convex functions, where $ T $ denotes the number of iterations. Crucially, we mathematically demonstrate that this massive acceleration comes almost for free, merely inflating the inherent Byzantine error floor by a bounded, tunable factor of $ \frac{1+ε}{1-ε} $. Experimental results on benchmark datasets confirm that integrating PDR with existing aggregators yields orders of magnitude speedups in time efficiency while maintaining highly competitive convergence performance.

## Metadata
- **Published**: 2026-05-27T11:39:47Z
- **Authors**: Shiyuan Zuo, Jiashuo Li, Rongfei Fan, Han Hu, Jie Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.28335v1)