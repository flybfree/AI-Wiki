---
title: Solver-Aware Decompositions for Programming-by-Example: When Dividing Requires Knowing how to Conquer
url: http://arxiv.org/abs/2608.03461v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_10-57-31Z_Solver_AwareDecompositionsforProgramming_by_Exampl.md
generated_at: 2026-08-05 01:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Solver-Aware Decomposition (SAD) to address limitations of decomposition-based programming-by-example where ground-truth subgoals may be intractable for bounded solvers. It shows that matching GT decompositions does not improve synthesis, while SAD learns solver-friendly subgoals and yields better end-to-end performance. The study empirically compares SAD with standard GT‑based decomposers across two domains.

## Key Takeaways
- A decomposer trained solely on ground-truth subgoals can generate logically valid but unsolvable subtasks because it ignores the solver's inductive biases.
- The synthesizer provides direct feedback through its loss, rewarding subgoals that keep the synthesis loss low and are actually solvable by the frozen model.
- Higher GT alignment does not translate into better synthesis accuracy; SAD instead trades GT match for solver tractability.

## Context
Current PBE methods assume decomposition quality is intrinsic to a task, but bounded solvers have fixed search dynamics. This paper challenges that assumption and demonstrates that optimal decompositions depend on the solver's capabilities rather than human annotations alone.

## Implications
For practitioners developing automated synthesis tools, this work suggests designing decomposers with solver constraints rather than relying solely on GT data. It may lead to more robust PBE systems that generalize across solvers and improve real-world task completion rates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03461v1)
