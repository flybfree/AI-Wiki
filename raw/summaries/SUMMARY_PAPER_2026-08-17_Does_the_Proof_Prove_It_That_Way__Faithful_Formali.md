---
title: Does the Proof Prove It That Way? Faithful Formalization of Elements Proofs
url: http://arxiv.org/abs/2608.15432v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_22-20-08Z_DoestheProofProveItThatWay_FaithfulFormalizationof.md
generated_at: 2026-08-17 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Pistis, a proof search system that generates Lean formalizations of proofs while preserving faithfulness—the alignment between natural‑language reasoning and the resulting formal proof. By applying OrderDecompose, it produces high‑quality artifacts for Euclid’s first three books, which outperform existing baselines in both speed and human/LLM evaluation.

## Key Takeaways
- Faithful formal proofs must satisfy five necessary conditions that ensure their reasoning mirrors the original argument.
- The OrderDecompose divide‑and‑conquer search tracks citation dependencies and blocks unfaithful shortcuts, enabling completion within a 12‑hour budget.
- Human reviewers and LLM judges favor Pistis‑generated proofs, achieving 2.89× and 5.2× higher acceptance rates than prior methods.

## Context
Formal verification relies on autoformalization and proof search, yet the gap between human intuition and machine output remains a challenge. This work bridges that gap by formalizing proofs in a way that retains their logical structure, offering tools for both mathematicians and AI systems to verify reasoning.

## Implications
Faithful formalization can serve as a reliable proof‑checking tool, catching gaps or errors before they propagate. For industry, it enables automated verification of complex mathematical models, accelerating research and reducing manual oversight costs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15432v1)
