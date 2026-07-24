# Summary: 2026-07-21_20-13-40Z_OnlineOptimizationofDifference_of_ConvexCompositio.md
Saved: 2026-07-24 01:14
Source: 2026-07-21_20-13-40Z_OnlineOptimizationofDifference_of_ConvexCompositio.md
Model: None

---

## Summary  
The paper tackles the online optimization of a broad class of structured non‑convex problems where each loss is a composition of a difference‑of‑convex (DC) function with a smooth mapping and where feasibility is governed by composite DC constraints.  It introduces a time‑smoothed proximal linear algorithm that leverages a proximal residual mapping to guide updates, establishing this residual as a proper stationarity measure whose fixed point implies first‑order optimality.  The analysis exploits a tangent‑cone characterization of the feasible region, enabling each update to be solved via a convex subproblem despite the overall non‑convexity.  

## Key Contributions  
- Finding 1: The paper proposes a time‑smoothed proximal linear algorithm for online optimization of difference‑of‑convex compositions with smooth mappings.  
- Finding 2: It introduces a local‑regret measure based on a proximal residual mapping that is a proper stationarity measure, implying first‑order optimality when the fixed point is reached.  
- Finding 3: The analysis provides a bound on the total number of inner convex subproblems and an error bound linking the proximal residual to the distance to stationarity, yielding a quantitative certificate of approximate stationarity.  

## Methodology  
The authors approach the problem by first formulating the feasible set using a tangent‑cone characterization for composite DC constraints; this yields a convex description that can be solved with a standard convex optimization oracle.  The online algorithm then computes each update as a proximal step with respect to a residual mapping, which is derived from the original loss and its gradient.  Because the residual satisfies a fixed‑point condition equivalent to first‑order stationarity, the updates are guaranteed to converge toward optimal solutions while maintaining tractable computational complexity through the convex subproblems.  

## Results  
The theoretical analysis establishes a local‑regret bound that decays at a rate proportional to the number of iterations and inversely proportional to the step size, demonstrating efficient convergence.  It also shows that the total number of inner convex subproblems required over the entire algorithm is bounded by a constant depending only on the smoothness parameters of the mappings and the Lipschitz constants of the DC components.  Moreover, an error bound is derived connecting the magnitude of the proximal residual to the distance between the current point and the true stationary point, providing a concrete measure of approximation quality.  

## Significance  
These results extend online optimization techniques to structured non‑convex problems where both loss functions and constraints are DC compositions with smooth mappings—a challenging class that often defies standard convex relaxations.  By guaranteeing convergence via a proper stationarity residual and bounding computational effort, the method offers practical algorithms for large‑scale applications such as machine learning, control, and combinatorial optimization.  

## Related Concepts  
- Difference‑of‑convex functions (DC)  
- Smooth mappings  
- Proximal mapping and proximal residual  
- Tangent cone characterization of feasible sets  
- Local regret minimization  
- Proper stationarity measure
