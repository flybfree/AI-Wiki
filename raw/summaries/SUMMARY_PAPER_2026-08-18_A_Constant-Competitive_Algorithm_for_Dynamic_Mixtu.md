---
title: A Constant-Competitive Algorithm for Dynamic Mixture-of-Experts Serving
url: http://arxiv.org/abs/2608.16947v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-15_03-51-27Z_AConstant_CompetitiveAlgorithmforDynamicMixture_of.md
generated_at: 2026-08-18 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a constant‑competitive algorithm for serving dynamic mixture‑of‑experts models and proves that its randomized primal competitive ratio is Theta(1) regardless of the number of experts. It also tightens the upper bound by converting service costs into movement using fractional paths, rounding composition, and machine‑checked formal proofs.

## Key Takeaways
- The algorithm achieves a constant competitive factor for any k, eliminating the earlier O(sqrt(log k)) dependence on extra GPU replicas.
- Positive‑body chasing with covering row sparsity two is reduced to a finite tangent envelope that approximates reciprocal epigraphs within a constant factor.
- Lazy threshold rounding combined with deterministic rational controls yields an explicit bound E[ALG] ≤ 10 C_PB OPT + (5 C_PB + 2) k + 16, verified in Lean 4.

## Context
Mixture‑of‑experts models scale to many GPUs by routing queries to the most relevant subnetwork. Existing competitive guarantees degrade with more experts or replicas, limiting practical deployment. This work provides a uniform constant bound that is independent of model size.

## Implications
Practitioners can now design scalable expert servers without fearing exponential performance loss as expertise grows. The formal verification ensures reliability for production systems where theoretical guarantees are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16947v1)
