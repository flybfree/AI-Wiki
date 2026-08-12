---
title: Batch Size or Negatives? A Selection Rule for Memory-Constrained Recommender Training
url: http://arxiv.org/abs/2608.11061v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_15-29-01Z_BatchSizeorNegatives_ASelectionRuleforMemory_Const.md
generated_at: 2026-08-11 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how to allocate memory between batch size and the number of negative items when training large‑scale recommender models under a fixed computational budget. The authors show that, given smoothness and variance assumptions, the optimal strategy is to use many examples with only one sampled negative per example. Experiments on synthetic data and four real datasets confirm faster convergence and higher final quality compared with other allocations.

## Key Takeaways
- With a fixed memory budget B = n k, the fastest convergence occurs when batch size n equals B and k ≈ 1, meaning each example sees only one candidate negative item.  
- The theoretical analysis assumes standard smoothness and variance properties of softmax loss, which hold for typical recommender models.  
- Empirical results across multiple benchmarks demonstrate that this allocation yields better final recommendation quality than imbalanced choices such as large k with small n.

## Context
The memory bottleneck in training neural recommenders stems from storing logits and gradients for the full item vocabulary, which scales linearly with K. Prior work has explored sampled softmax to mitigate this cost, but the trade‑off between batch size and negative sampling remains underexplored under a strict budget constraint.

## Implications
Practitioners can now set training configurations that maximize convergence speed without sacrificing model quality by prioritizing large batches over many negatives. This guideline simplifies resource planning for memory‑constrained environments such as edge devices or limited cloud instances, encouraging smarter utilization of available compute.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11061v1)
