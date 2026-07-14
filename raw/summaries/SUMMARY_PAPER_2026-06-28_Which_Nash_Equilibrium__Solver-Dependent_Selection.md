---
title: "Summary: Which Nash Equilibrium? Solver-Dependent Selection on Zero-Sum Nash Polytopes"
url: http://arxiv.org/abs/2606.28308v1
type: paper-summary
date: 2026-06-28
source_paper: 2026-06-26_17-53-30Z_WhichNashEquilibrium_Solver_DependentSelectiononZe.md
generated_at: 2026-06-28 22:00
model: nvidia/nemotron-3-nano-4b
---
# Summary: 2026-06-28 Which Nash Equilibrium  Solver-Dependent Selection

## Summary
This paper investigates how different Nash equilibrium solvers converge on the set of optimal strategies in zero‑sum games that have a polytope of equilibria rather than a single point. Using analytically known Nash sets, it shows that solver choice influences which member of this set is selected, not merely the random seed.

## Key Takeaways
- selection depends on the algorithm and its regularization rather than the initial seed, producing systematic differences across families of solvers  
- regularized last‑iterate methods such as R‑NaD converge to the maximum‑entropy equilibrium, which corresponds to projecting a uniform reference onto the Nash polytope, while regret‑averaging approaches drift toward lower‑entropy faces  
- the chosen equilibrium has measurable downstream effects on performance against sub‑optimal opponents, especially when sequential or hidden‑information structures are present  

## Context
Zero‑sum games with multiple equilibria challenge the assumption that solvers produce interchangeable outcomes. In AI and game theory, the choice of equilibrium can affect strategic decisions, making it important to understand how solver behavior varies across algorithmic families.

## Implications
For practitioners selecting a solver for zero‑sum environments, this research suggests that regularized last‑iterate methods may yield more robust strategies by targeting high‑entropy equilibria. However, reliance on any single solver without accounting for its selection bias could lead to suboptimal performance in complex strategic settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.28308v1)
