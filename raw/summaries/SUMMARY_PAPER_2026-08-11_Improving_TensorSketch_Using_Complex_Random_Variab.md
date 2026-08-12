---
title: Improving TensorSketch Using Complex Random Variables
url: http://arxiv.org/abs/2608.10523v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_05-59-25Z_ImprovingTensorSketchUsingComplexRandomVariables.md
generated_at: 2026-08-11 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a modified version of TensorSketch that retains the input‑sparsity advantage while achieving variance bounds comparable to those obtained by using complex random variables. The authors demonstrate that their variant reduces the exponential growth of estimator variance with polynomial degree, matching prior work on complex distributions.

## Key Takeaways
- The variance of both existing estimators grows exponentially as 3^p/D, which can be mitigated to 2^p/D through complex‑valued random variables.  
- The new TensorSketch variant applies this variance reduction without sacrificing the O(p( nnz(x) + D log D)) runtime for sparse inputs.  
- Experiments on synthetic and real datasets confirm that the improved estimator maintains low bias while offering faster computation than dense JL‑type projections.

## Context
In machine learning, accurate polynomial kernel estimation is essential for tasks such as classification and regression in high‑dimensional spaces. Efficient sketching algorithms are crucial because they enable scalable training on massive data sets without full feature expansion. This work addresses a longstanding challenge of balancing variance control with computational efficiency.

## Implications
The findings provide a practical tool for practitioners seeking robust kernel methods that scale to sparse, high‑degree features. By integrating complex random variables into TensorSketch, the method can be adopted in real‑time pipelines where both accuracy and speed are paramount, potentially accelerating model training in large‑scale AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10523v1)
