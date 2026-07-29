---
title: Finding Optimal Cost-Bounded Plan Reductions: Refined Model
url: http://arxiv.org/abs/2607.25484v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_09-21-19Z_FindingOptimalCost_BoundedPlanReductions_RefinedMo.md
generated_at: 2026-07-28 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of extracting a cost‑bound subplan from an existing plan while preserving its original action order and maximising utility. It proves that the decision variant is NP‑complete and introduces two exact solution methods: one based on oversubscription planning and another using integer linear programming with a refined formulation.

## Key Takeaways
- The problem requires selecting actions that support high‑utility goals without violating a newly imposed budget, which makes it computationally hard.  
- An oversubscription planning approach provides an exact algorithm but can be slow for large plans.  
- A refined ILP model reduces the number of variables and constraints, improving both size and runtime.

## Context
In reinforcement learning and task‑planning research, planners often generate long sequences of actions that may become infeasible when budgets change. Existing methods either ignore cost constraints or sacrifice optimality, limiting real‑world applicability in resource‑constrained environments such as robotics or autonomous navigation.

## Implications
This work offers a practical tool for practitioners who must adapt precomputed plans to new financial limits while keeping the original sequence intact. The refined ILP approach can be integrated into existing planning pipelines, enabling faster and more accurate cost‑bounded reductions in AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25484v1)
