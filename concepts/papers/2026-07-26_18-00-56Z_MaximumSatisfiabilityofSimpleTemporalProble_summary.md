# Summary: 2026-07-26_18-00-56Z_MaximumSatisfiabilityofSimpleTemporalProblems.md
Saved: 2026-07-27 23:59
Source: 2026-07-26_18-00-56Z_MaximumSatisfiabilityofSimpleTemporalProblems.md
Model: None

---

## Summary  
The paper tackles the MAXSTP problem – finding a maximum‑cardinality subset of consistent Simple Temporal Problem constraints – and investigates its computational difficulty when various instance features are considered as parameters. By analyzing hardness under measures such as the number of variables \(n\), the maximum coefficient magnitude \(k\), treewidth \(tw\) and vertex‑cover size \(vc\), the authors determine which parameterizations render MAXSTP tractable or intractable, offering both theoretical insights and concrete algorithmic bounds.

## Key Contributions  
- [Finding 1] MAXSTP is W[1]-hard when parameterized by the number of variables \(n\); thus any algorithm that depends only on \(n\) (including treewidth \(tw\) and vertex‑cover size \(vc\)) cannot be fixed‑parameter tractable.  
- [Finding 2] For a fixed numeric range \(k\), an \(O^*(k^n)\)‑time algorithm exists, giving single‑exponential solvability in the worst case.  
- [Finding 3] When combined parameters such as \(k + tw\) are used, MAXSTP is solvable in XP time with an \(O^*((n\cdot k)^{tw})\) algorithm, and it becomes FPT when parameterized by \(n\) or \(tw\).

## Methodology  
The authors adopt a parameterized‑complexity framework, treating the instance size \(n\), numeric bound \(k\), treewidth \(tw\) and vertex‑cover size \(vc\) as distinct parameters. They first prove hardness results for each parameter set, then construct algorithms that exploit these parameters: a naïve exponential algorithm for fixed \(k\); an XP algorithm leveraging treewidth; and FPT reductions to known tractable problems when the appropriate parameter is small.

## Results  
Theoretical analysis yields W[1]-hardness for \(n\)‑parameterization, confirming that no FPT algorithm can exist under this measure. Algorithmic results include: (i) an \(O^*(k^n)\) algorithm for fixed \(k\); (ii) an XP bound of \(O^*((n\cdot k)^{tw})\) using treewidth; and (iii) FPT algorithms when the problem is parameterized by \(n\) or \(tw\). Empirical verification shows that many practical instances, such as RCC‑8 and Allen’s algebra, satisfy these tractability conditions.

## Significance  
MAXSTP often behaves like a hard optimization problem for qualitative CSPs, highlighting the need to consider both quantitative and structural features. The paper clarifies which parameter combinations enable efficient solutions, guiding researchers toward feasible parameterizations and informing practical algorithm design.

## Related Concepts  
Simple Temporal Problem (STP), MAXSTP, W[1]-hardness, fixed‑parameter tractability (FPT), exponential‑time parametrization (XP), treewidth, vertex cover size, coefficient magnitude \(k\), parameterized complexity.
