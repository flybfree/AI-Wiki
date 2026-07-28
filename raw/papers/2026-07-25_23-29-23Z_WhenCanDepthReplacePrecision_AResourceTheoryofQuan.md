---
title: When Can Depth Replace Precision? A Resource Theory of Quantized Neural Computation
published: 2026-07-25T23:29:23Z
authors: Mojtaba Soltanalian
url: http://arxiv.org/abs/2607.23390v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Can Depth Replace Precision? A Resource Theory of Quantized Neural Computation

## Abstract
When can additional low-bit residual computation replace missing numerical precision for a fixed input-output map? We model a quantized residual system over a fixed horizon as a pure schedule selecting fields from a declared low-bit operation library, and use relaxed controls to characterize its infinite-depth limit. The distance from the target to the closed relaxed reachable set is the exact structural floor: no increase in depth can remove it for that library. Pure schedules approach the relaxed class at rate $O(D^{-1})$ under bounded-variation time dependence and $O(D^{-\vartheta}+D^{-1})$ under Holder dependence of exponent $\vartheta$. Execution arithmetic can reverse this conclusion: full-state write-back introduces a $Dρ_z$ penalty and can freeze residual updates, whereas increment error feedback replaces this growth by a bounded carry term and obeys an exact common-lattice conservation law. A fixed-teacher converse makes this rate sharp: for coherent depth-$L$ first-order high-precision comparators, accuracy matching requires $D=Θ(L)$. Learned codebooks add a metadata resource, while state-dependent routing introduces hybrid event conditions. Verified primal and dual bounds yield feasible, impossible, or unresolved decisions before training. Companion software implements the workflow, and Lean 4 machine-checks the exact discrete core. Depth replaces precision only relative to a declared library, horizon, execution semantics, and routing model.

## Metadata
- **Published**: 2026-07-25T23:29:23Z
- **Authors**: Mojtaba Soltanalian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23390v1)