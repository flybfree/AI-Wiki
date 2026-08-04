---
title: Optimal Unambiguous DNFs and Alon-Saks-Seymour
url: http://arxiv.org/abs/2608.02533v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_17-26-54Z_OptimalUnambiguousDNFsandAlon_Saks_Seymour.md
generated_at: 2026-08-03 23:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper constructs unbounded DNFs of linear width whose 0‑certificate complexity is quadratic, then lifts this structure to a communication problem via a constant gadget, establishing an optimal refutation of the Alon‑Saks‑Seymour conjecture and improving Clique vs Independent Set lower bounds. It also shows functions with quartic separation between certificate complexity and approximate degree, and a sample compression bound for multiclass learning.

## Key Takeaways
- The constructed DNFs have width O(n) but 0‑certificate complexity Ω(n^2), demonstrating a gap that cannot be closed by any constant‑size gadget.
- Lifting the structure to communication yields an optimal separation, refuting Alon‑Saks‑Seymour and improving Clique vs Independent Set lower bounds by doubly logarithmic factors.
- The same construction provides functions with quartic certificate‑approximate degree gap and a sample compression bound Ω(√log c) for multiclass concept classes.

## Context
This work advances theoretical computer science by linking algebraic DNF properties to communication complexity, offering new tools for analyzing non‑transitive problems. It fills gaps in longstanding conjectures that have resisted progress for decades.

## Implications
For practitioners, the results provide tighter lower bounds for combinatorial games and learning algorithms, guiding more efficient implementations of Clique detection and multiclass classifiers. The theoretical insights also inspire future research into gadget‑based complexity transfers across domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02533v1)
