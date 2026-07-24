---
title: A New Well-Supported Semantics for Description Logic Programs
url: http://arxiv.org/abs/2607.21203v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_11-20-31Z_ANewWell_SupportedSemanticsforDescriptionLogicProg.md
generated_at: 2026-07-23 22:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a new semantics for description logic programs that evaluates ontological atoms more strictly than the existing well‑supported semantics. The approach preserves NP‑complete consistency while eliminating higher‑level polynomial hierarchy complexity, and it defines a syntactic class where the new semantics matches the old one.

## Key Takeaways
- The new semantics enforces stricter evaluation of ontological atoms, which keeps the consistency problem at NP‑complete rather than moving to the second level of the polynomial hierarchy.
- It provides a reduct transformation characterization for a specific syntactic subclass of description logic programs where the new and old semantics are equivalent.
- The semantics is defined using a fixpoint operator and a reduct‑based transformation, making it a strict subset of the current well‑supported semantics.

## Context
Description logic programs are widely used in knowledge representation to combine logical rules with ontological constraints. Their semantics must guarantee that answer sets do not depend on cyclic dependencies, which is crucial for reliable reasoning systems. This work contributes to that goal by refining the complexity profile and offering a more precise operational model.

## Implications
For AI practitioners, this refinement reduces computational overhead in consistency checking without sacrificing correctness, enabling faster deployment of DL‑based applications. The formal characterization also supports automated tools that generate or verify DSL programs, improving toolchain reliability and maintainability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21203v1)
