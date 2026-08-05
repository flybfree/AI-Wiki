---
title: Solver-Aware Decompositions for Programming-by-Example: When Dividing Requires Knowing how to Conquer
published: 2026-08-04T10:57:31Z
authors: Janis Zenkner, Tobias Sesterhenn, Tim Grams, Christian Bartelt
url: http://arxiv.org/abs/2608.03461v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Solver-Aware Decompositions for Programming-by-Example: When Dividing Requires Knowing how to Conquer

## Abstract
Decomposition-based Programming-by-example (PBE) scales performance by splitting tasks into subtasks that a learned synthesizer solves: a decomposer predicts intermediate subgoals, and a synthesizer generates programs conditioned on them. Current approaches train the decomposer to imitate ground-truth ( GT) subgoals, implicitly treating decomposition quality as intrinsic to the task. We challenge this assumption: for bounded solvers with fixed inductive biases, GT decompositions reflect the annotator's factorization choices - not the solver's search dynamics. A decomposer trained to match GT decompositions may therefore propose subgoals that are logically valid yet intractable for the solver. We propose Solver-Aware Decomposition (SAD), a training framework that retains supervised training on GT subgoals as a structural scaffold, while additionally optimizing the decomposer via direct feedback from a frozen synthesizer. Subgoals are rewarded based on the synthesizer's loss on the target program - a signal of subtask difficulty that encourages decompositions the solver can act on. Our experiments reveal an accuracy paradox: higher agreement with GT decompositions does not improve synthesis success - even though the synthesizer was trained on the very same GT data the decomposer is optimized to mimic. SAD instead learns decompositions that trade GT alignment for solver tractability, yielding consistent gains in synthesis and end-to-end task accuracy across two PBE domains. Moreover, SAD solves tasks that a GT decomposition oracle fails - empirical evidence that GT decompositions are not universally optimal for bounded solvers, and that decomposition quality is solver-relative, not intrinsic.

## Metadata
- **Published**: 2026-08-04T10:57:31Z
- **Authors**: Janis Zenkner, Tobias Sesterhenn, Tim Grams, Christian Bartelt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03461v1)