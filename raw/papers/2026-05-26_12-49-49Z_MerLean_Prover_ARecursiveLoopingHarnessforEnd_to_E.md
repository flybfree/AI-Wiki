---
title: MerLean-Prover: A Recursive Looping Harness for End-to-End Lean 4 Theorem Proving
published: 2026-05-26T12:49:49Z
authors: Jinzheng Li, Zeru Zhu, Yuanjie Ren
url: http://arxiv.org/abs/2605.26959v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MerLean-Prover: A Recursive Looping Harness for End-to-End Lean 4 Theorem Proving

## Abstract
MerLean-Prover is an end-to-end Lean4 theorem prover that replaces sorry declarations with kernel-checkable proofs. It is built from three agent types (Planning, Check, and Lean) composed by a recursive outer loop whose unit of revision is the proof plan itself, and uses no fine-tuning, no custom RL objective, and no theorem-specific scaffolding. On FormalQualBench, a benchmark of 23 PhD-qualifying-exam theorems, MerLean-Prover solves 10/23, surpassing the strongest published open-source baseline (OpenGauss, 8/23). On Putnam2025, the same harness closes 12/12 with substantially lower total wall-clock than the next-best system that closes the full set. The harness also transfers to smaller models: Sonnet closes all four tested FormalQualBench problems, and Haiku closes the two short ones. These results suggest that harness design is a central factor in end-to-end Lean4 theorem proving, alongside raw model capability, and that a relatively simple harness can already be effective.

## Metadata
- **Published**: 2026-05-26T12:49:49Z
- **Authors**: Jinzheng Li, Zeru Zhu, Yuanjie Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.26959v1)