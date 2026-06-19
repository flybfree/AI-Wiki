---

title: "DECO: Sparse Mixture-of-Experts with Dense-Comparable Performance on End-Side Devices"
url: http://arxiv.org/abs/2605.10933v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-11_17-58-28Z_DECO_SparseMixture_of_ExpertswithDense_ComparableP.md
generated_at: "2026-06-11 10:38"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces DECO, a sparse Mixture-of-Experts architecture that matches the performance of dense Transformers while using only 20% of experts and achieving three times faster inference on real hardware. The authors demonstrate that DECO’s learnable scaling and NormSiLU activation enable high sparsity without sacrificing quality.

## Key Takeaways
- DECO activates only a fraction (20%) of its expert modules, yet delivers dense‑level performance under the same total parameter budget.
- The ReLU‑based routing combined with learnable expert‑wise scaling stabilizes activation ratios and improves intrinsic sparsity.
- Non‑gated MLP experts with ReLU routing provide an architectural simplification that yields comparable results to gated designs.

## Context
Mixture-of-Experts models have become a standard way to scale deep neural networks, but their dense parameter count limits deployment on resource‑constrained devices. Recent work shows that sparsity can reduce both storage and memory access while preserving accuracy, yet many solutions still suffer from high computational overhead.

## Implications
For industry practitioners, DECO offers a practical path to deploy large language models in edge environments where bandwidth and power are limited. Researchers gain a template for designing efficient MoE variants that balance capacity, cost, and storage constraints without compromising performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.10933v1)
