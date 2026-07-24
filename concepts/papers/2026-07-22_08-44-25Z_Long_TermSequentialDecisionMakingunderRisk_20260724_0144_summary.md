# Summary: 2026-07-22_08-44-25Z_Long_TermSequentialDecisionMakingunderRisk.md
Saved: 2026-07-24 01:44
Source: 2026-07-22_08-44-25Z_Long_TermSequentialDecisionMakingunderRisk.md
Model: None

---

## Summary  
The paper tackles finite‑horizon Markov decision process planning under root‑based (resolute) risk objectives that are non‑linear and therefore violate Bellman optimality, making scenario‑tree enumeration intractable. It introduces ERQDP—a deterministic, enumeration‑free, sampling‑free algorithm—that solves the rank‑quantile surrogate exactly via dynamic programming over a discretized return probability mass function and provides certified upper‑lower gaps for any discretization budget.

## Key Contributions  
- **ERQDP** is presented as an exact DP method that computes the root‑based risk objective without enumerating scenario trees.  
- The algorithm yields **certified upper‑lower gaps** for any discretization budget, enabling anytime reporting of solution quality.  
- ERQDP enables fast risk‑parameter sweeps and supports both risk‑averse (convex) and risk‑seeking (concave) policies.

## Methodology  
The authors discretize the return distribution on a fixed grid with an explicit rounding bound, constructing a probability mass function (PMF). Using exact DP over this PMF they evaluate each candidate policy’s root‑based risk exactly. The rank‑quantile surrogate is obtained from these evaluations, and an anytime loop refines the surrogate by re‑applying DP to improve estimates while delivering explicit residual gaps that bound the true objective.

## Results  
Across a suite of benchmark MDP instances, ERQDP either returns certified optimal policies or provides precise upper‑lower certificates, achieving substantial runtime gains compared with traditional scenario‑tree approaches. The method works for both risk‑averse and risk‑seeking objectives, demonstrating its flexibility across diverse applications.

## Significance  
ERQDP bridges the gap between exact MDP planning under non‑linear risk measures and practical computation by offering certified guarantees without sampling or enumeration. This makes robust long‑term sequential decision making feasible in finance, operations research, and other domains where risk is a central constraint.

## Related Concepts  
- Finite‑horizon Markov Decision Processes (MDPs)  
- Root‑based (resolute) risk objectives  
- Rank‑quantile surrogate  
- Dynamic programming over probability mass functions  
- Anytime algorithms with upper‑lower certificates  
- Discretization budgets and rounding bounds
