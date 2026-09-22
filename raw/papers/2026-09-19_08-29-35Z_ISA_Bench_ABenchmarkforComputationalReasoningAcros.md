---
title: ISA-Bench: A Benchmark for Computational Reasoning Across Instruction Set Architectures
published: 2026-09-19T08:29:35Z
authors: Aditya Pola, Arkaprava Majumdar, Vineeth N. Balasubramanian
url: http://arxiv.org/abs/2609.22878v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ISA-Bench: A Benchmark for Computational Reasoning Across Instruction Set Architectures

## Abstract
Large language model code generation benchmarks primarily evaluate well-resourced languages like Python and Java, where models benefit from abundant training data. They provide limited evidence about reasoning in unfamiliar computational models: deriving arithmetic from a single subtract instruction, coordinating parallel programs across communicating nodes, or wiring logic gates into circuits. We present ISA-Bench, a benchmark of programming games with constrained instruction sets. For each game we provide a full execution stack (parser, VM, and verifier), enabling automated evaluation with structured feedback for iterative refinement. Reasoning models achieve higher average solve rates than code-specialized and general-purpose models, but unfamiliar syntax remains a major source of failure. Models solve more tasks with iterative feedback, though the gains vary substantially across architectures. We introduce a reasoning--execution gap (REG) analysis that reveals a recurring disconnect between identifying a plausible computational strategy and expressing it as a correct program in the target ISA. Code is open-sourced.

## Metadata
- **Published**: 2026-09-19T08:29:35Z
- **Authors**: Aditya Pola, Arkaprava Majumdar, Vineeth N. Balasubramanian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.22878v1)