# Summary: 2026-08-10_02-48-16Z_DualCert_ASolverfortheTravelingSalesmanProblemwith.md
Saved: 2026-08-10 23:37
Source: 2026-08-10_02-48-16Z_DualCert_ASolverfortheTravelingSalesmanProblemwith.md
Model: None

---

## Summary  
The paper aims to develop a solver for large traveling salesman problems that combines learning with constraint enforcement. It introduces constraint‑coupled learning where degree equations and subtour‑elimination constraints directly shape learned transitions. The method uses an exact constrained mirror‑descent step on a KKT manifold to map finite states to positive ones while respecting computational budgets.  

## Key Contributions  
- [Finding 1] Introduces constraint‑coupled learning that ties each learned transition to current degree equations and dynamically selected subtour‑elimination constraints.  
- [Finding 2] Achieves a mean tour‑cost gap of 0.0573% on TSP1000 instances, which is 67.1 % smaller than the NeuroLKH mean gap.  
- [Finding 3] Provides verified candidate‑graph lower bounds for all instances and attains 81.46 % edge‑decision coverage.  

## Methodology  
The authors formulate a constrained optimization problem in which each iteration defines a primal‑slack KKT manifold using the active degree equations and strictly satisfied SEC rows with positive slacks. A local cost field is derived from repaired dual variables and violated SEC constraints, and an exact mirror‑descent step maps finite states onto this manifold while preserving the budget for Held–Karp ascent, candidate‑graph edge tests, and tour construction. Deterministic verification recomputes original costs to accept only lower bounds that satisfy all constraints, ensuring output validity without stochastic sampling.  

## Results  
On 1,000 held‑out TSP1000 instances the solver attains a mean tour‑cost gap of 0.0573 % compared with LKH‑3 reference tours in 9.55 batch‑amortized seconds per instance. It returns a verified candidate‑graph lower bound for every instance and achieves 81.46 % edge‑decision coverage, yielding a gap that is 67.1 % smaller than the reported NeuroLKH mean gap.  

## Significance  
By enforcing constraints directly on learning, DualCert eliminates invalid tours while dramatically reducing computational overhead relative to neuro‑based hybrids. The deterministic verification guarantees correctness, and the tight budget allocation enables near‑optimal performance on very large instances, making it a practical alternative for real‑world TSP applications where both speed and optimality are critical.  

## Related Concepts  
- Constraint‑coupled learning  
- KKT manifold  
- Exact constrained mirror‑descent  
- Subtour‑elimination constraints (SECs)  
- Candidate‑graph lower bound  
- Deterministic verification  
- Held–Karp ascent  
- Neuro‑OR hybrids
