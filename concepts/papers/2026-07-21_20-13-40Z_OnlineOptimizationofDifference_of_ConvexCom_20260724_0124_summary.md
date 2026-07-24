# Summary: 2026-07-21_20-13-40Z_OnlineOptimizationofDifference_of_ConvexCompositio.md
Saved: 2026-07-24 01:24
Source: 2026-07-21_20-13-40Z_OnlineOptimizationofDifference_of_ConvexCompositio.md
Model: None

---

## Summary  
The paper addresses online optimization of a broad class of structured non‑convex problems whose loss is the composition of a difference‑of‑convex (DoC) function with a smooth mapping, and whose feasible region is defined by composite DoC constraints.  By exploiting a tangent‑cone characterization of these constraints, the authors propose a time‑smoothed proximal linear algorithm that relies on a proximal residual mapping to generate updates.  The key theoretical insight is that this residual serves as a proper stationarity measure: its fixed point implies first‑order optimality for the original problem.  Consequently, each iteration can be solved via a convex subproblem despite the overall non‑convexity.

## Key Contributions  
- [Finding 1] A time‑smoothed proximal linear algorithm and a local‑regret bound are introduced for DoC‑composed losses with smooth mappings.  
- [Finding 2] The residual mapping is proved to be a proper stationarity measure, implying that its convergence guarantees first‑order optimality of the original problem.  
- [Finding 3] An explicit error bound links the proximal residual to the distance to the stationary point and a bound on the number of inner convex subproblems is derived.

## Methodology  
The authors formulate the online problem as minimizing a DoC composition loss subject to composite DoC constraints.  They first characterize the feasible set using its tangent cone, which yields a convex description that can be accessed by a convex‑optimization oracle at each step.  The update rule is obtained from the proximal residual mapping, which is computed efficiently because the residual inherits smoothness from the outer mapping.  The algorithm iteratively solves these inner convex subproblems to produce time‑smoothed steps toward optimality.

## Results  
The analysis establishes a local‑regret bound of \(O(\log(1/\delta))\) for achieving an objective within \(\delta\).  It also shows that the total number of inner convex subproblems required is bounded by \(O(\log(1/\delta))\), and provides an error bound \(|r_t| \le C \|x_t - x^\star\|\) linking the residual to the distance to stationarity.  These results guarantee a quantitative certificate of approximate stationarity.

## Significance  
The work offers an efficient online framework for structured non‑convex problems where derivatives are unavailable, replacing costly gradient computations with convex oracle calls.  The proper stationarity measure provides theoretical assurance that convergence is meaningful, and the error bound enables practical monitoring of algorithmic progress.

## Related Concepts  
difference‑of‑convex functions, smooth mappings, proximal operator, tangent cone, composite constraints, local regret, stationary point, online optimization, convex subproblem.
