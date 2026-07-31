---
title: Shapes from Examples: Foundations of Shape Learning in Recursive SHACL
url: http://arxiv.org/abs/2607.27934v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_09-45-22Z_ShapesfromExamples_FoundationsofShapeLearninginRec.md
generated_at: 2026-07-30 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the fitting problem in SHACL shape learning, where a shape expression must validate nodes in a positive set P and reject those in a negative set N. The authors focus on using ELI‑based core fragments with well‑founded, stable, supported semantics to compute such expressions. They prove existence of solutions within exponential time and provide polynomial bounds for special cases.

## Key Takeaways
- Fitting existence is guaranteed under the given semantics, but the computation can be exponential in the worst case.  
- The most specific fitting problem also admits an exponential‑time algorithm, with tighter bounds than generic methods.  
- Specialized subproblems enjoy polynomial time solutions thanks to structural properties of ELI shapes.

## Context
Shape learning is a core challenge for knowledge graph validation, enabling automated checks that enforce domain semantics without manual schema design. This work contributes theoretical guarantees that bridge practical fitting algorithms with the expressive power of SHACL’s ELI fragment.

## Implications
For practitioners building large graphs, these bounds suggest when to expect tractable solutions versus costly exponential searches. The insights help optimize validation pipelines and guide the selection of shape expressions for real‑world data integrity tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27934v1)
