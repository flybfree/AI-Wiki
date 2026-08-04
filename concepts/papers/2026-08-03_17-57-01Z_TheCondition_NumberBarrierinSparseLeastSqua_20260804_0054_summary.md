# Summary: 2026-08-03_17-57-01Z_TheCondition_NumberBarrierinSparseLeastSquares.md
Saved: 2026-08-04 00:54
Source: 2026-08-03_17-57-01Z_TheCondition_NumberBarrierinSparseLeastSquares.md
Model: None

---

## Summary  
This paper addresses a long‑standing conjecture in sparse convex optimization that the linear dependence on the restricted condition number cannot be improved beyond a certain threshold. The authors prove a tight lower bound for randomized algorithms solving least‑squares problems, showing that achieving a small error while maintaining sparsity incurs a cost proportional to the condition number raised to a power less than one. Their result is conditional on the Small-Set Expansion Hypothesis (SSSH) in the weighted regular‑graph formulation of Raghavendra et al., and it holds even for rational instances with full column rank. The proof leverages an internal Gemini‑based agentic system that automates the combinatorial analysis, and the authors have manually verified and polished the exposition.

## Key Contributions  
- [Finding 1] A rigorous randomized lower bound on the performance of sparse least‑squares algorithms: for any fixed γ∈(0,1], no algorithm with probability ≥2/3 can achieve error ε while keeping sparsity s = O(k κ_{s+k}^{1−γ}).  
- [Finding 2] The bound is tight under the Small‑Set Expansion Hypothesis (SSSH) and applies to rational matrices of full column rank, confirming that the conjecture holds in a broad class of instances.  
- [Finding 3] The proof was derived using an automated Gemini agentic system, which systematically explores combinatorial configurations, and this approach provides a reproducible pathway for future conditional results.

## Methodology  
The authors tackled the problem by reformulating least‑squares as a weighted regular‑graph sparsity optimization. They then invoked the SSSH, which asserts that the volume of small subsets of vertices in such graphs expands at most polynomially with respect to the condition number. Using this hypothesis, they derived combinatorial constraints on feasible sparse solutions and encoded them into an automated Gemini agentic workflow that enumerates relevant graph structures, verifies feasibility, and computes the associated condition‑number exponent. The verification step was performed manually to ensure correctness before publication.

## Results  
The main theoretical result is the existence of a constant c(γ) such that any randomized polynomial‑time algorithm must incur an additive term proportional to κ_{s+k}^{1−γ}. This establishes the “condition‑number barrier” for sparse least squares, confirming Axiotis and Sviridenko’s conjecture. The proof holds for all γ≤1 and is unconditional on the SSSH except for its verification, which the authors have completed.

## Significance  
This work resolves a fundamental open problem in approximation theory for sparse convex problems, influencing algorithm design and theoretical guarantees. It also demonstrates how automated reasoning tools can complement human insight in deriving sharp bounds, paving the way for conditional results that may become unconditional with further progress on SSSH.

## Related Concepts  
- Condition number (κ_r) – restricted condition at sparsity level r.  
- Sparsity s = ‖x‖_0 – number of non‑zero entries in the solution vector.  
- Small‑Set Expansion Hypothesis (SSSH) – bound on volume growth for small subsets in weighted regular graphs.  
- Randomized exact‑volume SSSH – probabilistic version used to condition the barrier proof.
