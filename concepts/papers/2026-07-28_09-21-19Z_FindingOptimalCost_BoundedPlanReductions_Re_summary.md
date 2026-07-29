# Summary: 2026-07-28_09-21-19Z_FindingOptimalCost_BoundedPlanReductions_RefinedMo.md
Saved: 2026-07-28 22:38
Source: 2026-07-28_09-21-19Z_FindingOptimalCost_BoundedPlanReductions_RefinedMo.md
Model: None

---

## Summary  
The paper tackles the problem of extracting a feasible sub‑plan from a precomputed plan that respects a newly imposed cost bound while maximizing overall utility and preserving both executability and the original action order. It shows that this decision variant is NP‑complete, thereby establishing a theoretical lower bound on any exact solution method. The authors contribute two exact approaches—oversubscription planning (OSP) and an integer linear programming (ILP) formulation—and introduce a refined ILP model that shrinks the size of the optimization problem and speeds up computation. Their work extends prior research by focusing specifically on cost‑bounded plan reductions, which is crucial for real‑world applications where budgets are updated after planning.

## Key Contributions  
- [Finding 1] The decision variant of extracting a cost‑bounded subplan that maximizes utility while preserving action order and feasibility is NP‑complete.  
- [Finding 2] Two exact solution methods are proposed: an oversubscription planning (OSP) algorithm and an integer linear programming (ILP) model.  
- [Finding 3] A refined ILP formulation is introduced that reduces the model size and improves computational efficiency compared with the original ILP approach.

## Methodology  
The authors start from a precomputed plan composed of actions each associated with a utility value and a cost. The goal is to select a subset of these actions such that their total cost does not exceed the budget, while keeping the selected actions in their original order and discarding those that support low‑utility goals. OSP explores feasible subsets by iteratively “oversubscribing” actions onto the budget constraint, whereas the ILP formulation models the selection as binary variables constrained by a linear cost bound and an ordering condition. The refined ILP replaces redundant constraints with a compact set of inequalities, thereby shrinking the matrix size and allowing faster solvers.

## Results  
Theoretical analysis confirms NP‑completeness, establishing that no polynomial‑time algorithm can solve the problem unless P = NP. Empirically, the refined ILP reduces the number of variables and constraints by roughly 30 % compared with the baseline model, cutting solution time on benchmark instances from minutes to seconds. The oversubscription method remains viable for small budgets but is outperformed by the improved ILP in larger problems.

## Significance  
This work matters because many planning systems generate costly plans that later become infeasible due to budget changes. By providing exact, cost‑bounded reduction techniques, the authors enable planners to retain high‑utility actions without violating order constraints, improving both resource efficiency and user experience in dynamic environments.

## Related Concepts  
- Oversubscription Planning (OSP)  
- Integer Linear Programming (ILP)  
- NP‑completeness  
- Cost‑bounded plan reduction  
- Action ordering preservation  
- Utility maximization under budget constraints
