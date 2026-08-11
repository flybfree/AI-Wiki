# Summary: 2026-08-10_02-48-16Z_DualCert_ASolverfortheTravelingSalesmanProblemwith.md
Saved: 2026-08-10 23:33
Source: 2026-08-10_02-48-16Z_DualCert_ASolverfortheTravelingSalesmanProblemwith.md
Model: None

---

## Summary  
The paper proposes DualCert, a solver for large traveling salesman problems that integrates constraint‑coupled learning to guarantee feasible tours while minimizing computational cost. By linking learned transition probabilities directly to degree equations and dynamically selected subtour‑elimination constraints (SECs), the method enforces validity at each refinement step. The approach uses an iterate‑dependent Karush–Kuhn–Tucker manifold to map finite states onto a positive state, ensuring that only strictly satisfied constraints influence learning. Deterministic verification then recomputes original costs and accepts only lower‑bounded candidate graphs, preserving output correctness.

## Key Contributions  
- [Finding 1] DualCert introduces constraint‑coupled learning where the KKT manifold is defined by current degree equations and strictly satisfied SEC rows with positive slacks.  
- [Finding 2] The solver performs an exact constrained mirror‑descent step that maps each finite state to a positive state on this manifold, updating dual variables locally.  
- [Finding 3] DualCert achieves a mean tour‑cost gap of 0.0573 % over LKH‑3 on TSP1000 instances in 9.55 batch‑amortized seconds per instance while delivering an 81.46 % edge‑decision coverage.

## Methodology  
The authors treat the TSP as a constrained optimization problem and embed learning within a dual‑variable framework. At each iteration, they compute the KKT manifold using degree equations and selected SEC rows that have positive slack; violated rows generate a local cost field. Implicit differentiation maps parameter perturbations into the tangent space of this manifold, allowing reuse of the forward constraint operator for derivatives. The terminal edge state allocates computation across Held–Karp ascent, candidate‑graph edge tests, and tour construction under a fixed budget, while deterministic verification recomputes original costs to accept only verified lower bounds.

## Results  
On 1,000 held‑out TSP1000 instances, DualCert’s mean gap is 0.0573 % compared with the LKH‑3 reference tour, which is a 67.1 % improvement over NeuroLKH’s reported mean gap. The method returns a verified candidate‑graph lower bound for every instance and achieves an edge‑decision coverage of 81.46 %. These results demonstrate that constraint‑coupled learning can produce near‑optimal tours with far less computational overhead than traditional OR hybrids.

## Significance  
DualCert bridges the gap between learned guidance and hard constraints, offering a principled way to enforce TSP feasibility without sacrificing performance. By guaranteeing that only strictly satisfied constraints shape the solution space, it avoids invalid subtours while preserving the efficiency of neural‑based heuristics. This work advances the design of constraint‑aware OR solvers for large combinatorial problems.

## Related Concepts  
- Traveling Salesman Problem (TSP)  
- Neural Operations Research (OR) hybrids  
- Constraint‑coupled learning  
- KKT manifold and mirror descent  
- Subtour‑elimination constraints (SECs)  
- Dual variables and slack management  
- Deterministic verification of candidate graphs
