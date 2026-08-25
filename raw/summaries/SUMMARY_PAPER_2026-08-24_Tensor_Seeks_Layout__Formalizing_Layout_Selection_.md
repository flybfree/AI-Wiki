---
title: Tensor Seeks Layout: Formalizing Layout Selection for ML Compilers
url: http://arxiv.org/abs/2608.21555v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-21_18-44-48Z_TensorSeeksLayout_FormalizingLayoutSelectionforMLC.md
generated_at: 2026-08-24 21:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a formal model for selecting tensor memory layouts in machine‑learning compilers, treating the problem as combinatorial optimization over dataflow graphs. It proves that optimal layout selection is computationally hard even for simple matrix‑multiplication programs and proposes an exact algorithm for bounded treewidth instances while providing a weighted MaxSAT encoding for general cases. Empirical results show that the solver can reduce execution time by up to five times compared with greedy heuristics when the cost model is accurate.

## Key Takeaways
- Optimal layout selection over dataflow graphs is NP‑hard, establishing a theoretical lower bound on compiler complexity.  
- An optimal polynomial‑time algorithm exists for programs with bounded treewidth, offering exact solutions in practical scenarios.  
- A weighted MaxSAT formulation enables off‑the‑shelf solvers to handle general instances, achieving near‑optimal results where the cost model is reliable.

## Context
Machine learning compilers must balance operator performance with data movement costs, a challenge that scales with increasingly complex neural networks and specialized hardware. Existing heuristics often rely on local decisions without a unified theoretical foundation, leading to suboptimal or inconsistent layout assignments across operators.

## Implications
The formalization provides a principled basis for layout selection, enabling more reliable compiler strategies that can be tuned to specific cost models. Practitioners can leverage exact solvers where beneficial and fall back to heuristics when computational limits arise, improving model performance on AI accelerators.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21555v1)
