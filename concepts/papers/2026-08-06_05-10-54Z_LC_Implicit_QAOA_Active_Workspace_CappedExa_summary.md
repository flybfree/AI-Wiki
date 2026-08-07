# Summary: 2026-08-06_05-10-54Z_LC_Implicit_QAOA_Active_Workspace_CappedExactObjec.md
Saved: 2026-08-06 22:05
Source: 2026-08-06_05-10-54Z_LC_Implicit_QAOA_Active_Workspace_CappedExactObjec.md
Model: None

---

## Summary  
The paper introduces LC‑Implicit‑QAOA, a framework that enables exact evaluation of both the objective and all shared gradients for QAOA training while respecting the causal‑cone structure of bounded QUBO problems. By profiling cone geometry and induced edge counts before allocating local amplitudes and workspace resources, it jointly schedules microbatches and checkpoint evaluations under a strict active‑evaluator budget, rejecting infeasible requests early. The method is fully “implicit”: no global state or cost table is stored, and the evaluation proceeds solely through dense complex128/float64 adjoints that match the reference implementation to within 1.56 × 10⁻¹³ relative error. Experiments on a p=2 bounded‑cone grid complete all target requests with memory usage capped at 79.7 % of the budget, and on a 3‑regular n=512 instance it reaches the finite‑budget endpoint in only 101 objective‑equivalent calls versus 909 for central differences.

## Key Contributions  
- [Finding 1] LC‑Implicit‑QAOA provides exact objective‑and‑gradient evaluation without storing global state or a full cost table, leveraging the causal‑cone structure to allocate resources only when needed.  
- [Finding 2] The framework enforces a named active‑evaluator workspace budget, jointly selecting microbatches and checkpoint schedules while rejecting infeasible requests before allocation.  
- [Finding 3] A dense complex128/float64 adjoint matches the reference implementation over 1,800 graph‑angle comparisons with a worst relative gradient error of 1.56 × 10⁻¹³.

## Methodology  
The authors first compute the cone structure and induced edge counts for the QUBO problem, which determines how many local amplitudes can be stored locally. This information guides the allocation of microbatches—equal‑size subsets of basis states—and checkpoint schedules that respect a pre‑specified active‑evaluator memory budget. Any request that would exceed this budget is rejected immediately, ensuring “implicit” evaluation proceeds without global state or cost table materialization. The dense complex128/float64 adjoint is then constructed to compute gradients analytically, matching the reference implementation across all tested angles.

## Results  
On a p=2 bounded‑cone grid, LC‑Implicit‑QAOA completes all 104 target requests; the matched state‑plus‑cost reference is executed for 28 of them and deliberately omitted for 76. The allocated evaluator memory never exceeds 0.797 of the budget. For a 3‑regular n=512 instance, the adjoint reaches the finite‑budget endpoint in 101 objective‑equivalent calls and 189 s, compared with 909 calls and 1,565 s for central differences.

## Significance  
LC‑Implicit‑QAOA dramatically reduces the cost of training over bounded QUBO light cones by eliminating the need for costly global state updates and hardware‑specific optimizations. Its near‑exact gradients enable reliable optimization within a strict memory budget, offering a hardware‑independent baseline that can be scaled to larger problems while preserving theoretical guarantees.

## Related Concepts  
causal cone restriction, adjoint differentiation, active‑evaluator workspace budget, microbatch checkpointing, QAOA training, QUBO light cones, dense complex128/float64 adjoints.
