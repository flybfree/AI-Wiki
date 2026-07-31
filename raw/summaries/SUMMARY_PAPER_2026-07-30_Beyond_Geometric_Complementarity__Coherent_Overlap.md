---
title: Beyond Geometric Complementarity: Coherent Overlap in Sparse Mixture-of-Experts Routing
url: http://arxiv.org/abs/2607.28308v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_14-45-39Z_BeyondGeometricComplementarity_CoherentOverlapinSp.md
generated_at: 2026-07-30 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how sparse mixture-of-experts models route tokens and whether geometric overlap between expert subspaces correlates with routing quality. It introduces the Expert Subspace Separation Index (ESSI) to separate route coherence from candidate quality, showing that experts can be geometrically similar yet still provide better representation than matched alternatives.

## Key Takeaways
- Across six MoE architectures, expert subspaces overlap significantly but actual routes improve token representations more than matched alternatives, indicating that geometric similarity does not guarantee routing effectiveness.
- In the 39 factorial cells of Mixtral and DeepSeek, selected candidates explain more residual representation than strongest unselected rivals, yet all interactions are negative with confidence intervals below zero, suggesting a narrowing advantage over time.
- Adding later experts improves next‑token prediction in 24 out of 39 frozen‑route comparisons, while the remaining 15 remain inconclusive, and controlled training favors Top‑2 over Top‑1 across three seeds.

## Context
Mixture-of-experts models aim to balance model capacity with parameter efficiency by routing tokens to a subset of experts. Understanding whether routing decisions are driven by geometric alignment or functional relevance is crucial for designing scalable AI systems.

## Implications
This work clarifies that redundancy can persist without disjoint linear coverage, guiding practitioners to prioritize functional value over simple geometric separation in MoE design and pruning strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28308v1)
