---
title: AxQM: A Textbook-Scale Benchmark for Formal Proof Synthesis in a Library of Finite-Dimensional Quantum Mechanics
published: 2026-09-04T13:58:19Z
authors: Weichen Winston Yin, Jacob M. Taylor, Dirk R. Englund, Frank H. L. Koppens
url: http://arxiv.org/abs/2609.05157v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AxQM: A Textbook-Scale Benchmark for Formal Proof Synthesis in a Library of Finite-Dimensional Quantum Mechanics

## Abstract
Formalizing mathematics in a proof assistant, where a machine checks every definition, statement and proof, has set a new standard of rigor. Large language models are now capable of formalizing autonomously, even at the scale of whole textbooks. We bring this standard of rigor to physics, where theoretical arguments carry idealizations that are rarely stated fully, and any logical gaps could have a cascading effect on interdependent results. Recognizing the need to evaluate autoformalization systems for physics, we release AxQM, 1,019 kernel-checkable proof-synthesis tasks over 479 items drawn from the textbook Quantum Computation and Quantum Information by Nielsen and Chuang. The tasks are stated in a custom Lean library of finite-dimensional quantum mechanics. By task count, it is the largest proof-synthesis benchmark in physics by a factor of four. AxQM is derived from a near-complete formalization of the formal portions of the textbook, so every task is guaranteed a solution, which we keep private. Grading of the benchmark is done deterministically by the Lean kernel, which checks that the proof compiles, that no sorry appears in it or in any declaration it depends on, and that it introduces no new axioms.

## Metadata
- **Published**: 2026-09-04T13:58:19Z
- **Authors**: Weichen Winston Yin, Jacob M. Taylor, Dirk R. Englund, Frank H. L. Koppens
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05157v1)