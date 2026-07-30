---
title: Automorphism-Induced Non-Canonicity in Top-k Explanations of Graph Neural Networks
url: http://arxiv.org/abs/2607.26344v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_23-36-05Z_Automorphism_InducedNon_CanonicityinTop_kExplanati.md
generated_at: 2026-07-29 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why gradient‑based graph neural network explainers sometimes produce non‑canonical top‑k attribution reports when the input graph possesses automorphisms. It proves that such symmetry is a structural limitation of message passing rather than an implementation flaw and shows how to detect it algorithmically.

## Key Takeaways
- Gradient‑based GNN explanations are forced to assign equal scores to chemically equivalent nitro groups because message passing is permutation equivariant, leaving attribution invariant under any automorphism.
- When no minimal valid explanation can be fixed by the input's automorphism group, a single‑valued rule cannot simultaneously be minimal, symmetry‑respecting and score‑optimal.
- A parameter‑free criterion implemented in Lean 4 decides whether every optimal report of a given size must split an orbit, matching mechanical model‑equivalence checks across thousands of instances.

## Context
This work addresses a fundamental issue in interpretable machine learning: the arbitrariness introduced by symmetric inputs that break canonical explanations. The findings highlight how group theory and automorphism groups can limit the expressiveness of explanation methods beyond what is captured by gradient analysis alone.

## Implications
For practitioners, the paper provides a principled way to detect and mitigate symmetry‑induced non‑canonicality without relying on external assumptions about model parameters. It also suggests that reporting orbits can remove arbitrary ordering bias at negligible computational cost, improving both fairness and reproducibility in chemical and other graph‑based AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26344v1)
