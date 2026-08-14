---
title: Algebraic Decomposition Theory for Transformer Length Generalization
url: http://arxiv.org/abs/2608.13433v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_16-20-56Z_AlgebraicDecompositionTheoryforTransformerLengthGe.md
generated_at: 2026-08-13 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper establishes the first complete characterization of which regular languages transformers can generalize to longer sequences, introducing a decision algorithm based on C-RASP and iterated wreath products. It provides a polynomial‑time method to test language membership that complements classical decomposition theory. Experiments validate the theory against transformer behavior.

## Key Takeaways
- The paper defines a formalism called C-RASP that captures exactly the regular languages transformers length‑generalize on, extending beyond finite semigroup tools.
- It shows that classical Krohn‑Rhodes decomposition cannot express flip‑flops or simple groups needed for C‑RASP, requiring an algebraic shift to infinite additive groups.
- The derived algorithm uses iterated wreath products of integers and runs in polynomial time relative to the syntactic monoid size.

## Context
Transformer length generalization remains a critical open problem in natural language processing, affecting model robustness. Classical finite decomposition theory is limited to bounded semigroups, leaving an algebraic gap that this work bridges.

## Implications
Researchers can now predict which regular languages will be handled by transformers without exhaustive simulation. Practitioners gain a principled test for model generalization, improving design of long‑context language models and reducing overfitting risks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13433v1)
