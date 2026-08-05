# Summary: 2026-07-27_18-05-46Z_AmortisingTrajectoryOptimisationforResidualMPCviaI.md
Saved: 2026-07-28 20:19
Source: 2026-07-27_18-05-46Z_AmortisingTrajectoryOptimisationforResidualMPCviaI.md
Model: None

---

## Summary  
The paper proposes an amortised trajectory‑optimisation framework for residual model predictive control that leverages the Implicit Function Theorem to compute implicit contact sensitivities without resorting to costly finite‑difference approximations or unrolled automatic differentiation. By differentiating the stationarity residual at a tolerance‑converged solution, the method eliminates the need for solver‑specific KKT systems and keeps computational traces short. A second contribution is an optimiser‑distillation scheme that replaces full‑horizon iLQR with a short‑horizon residual iLQR policy to guide planning. Experiments on three manipulators show that this approach can raise six‑step success probability by 28–98 percentage points compared with standard iLQR.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Memory usage of the implicit differentiation method grows negligibly with iteration count, staying within ~4% increase versus a 10.6× explosion for unrolled automatic differentiation.]  
- [IFT‑based implicit differentiation yields a memory footprint that scales far more gently than unrolled AD, requiring only ~4% extra memory per iteration and using 20× less memory at 256 contacts compared with the exponential growth observed in unrolled methods.]  
- [Distillation of full‑horizon iLQR into a short‑horizon residual iLQR policy yields substantial performance gains, raising six‑step success by 28–98 percentage points across Finger, Franka, and Unitree robots.]

## Methodology  
The authors employ the Implicit Function Theorem to obtain implicit contact sensitivities from the stationarity residual of a regularised smooth contact model. Instead of unrolling the full contact solver or performing finite‑difference approximations, they differentiate the residual at the tolerance‑converged solution, thereby avoiding both solver unrolling and hand‑crafted KKT systems. The optimiser‑distillation step trains a short‑horizon iLQR policy to approximate the output of a full‑horizon iLQR, which is then used as a control law for residual MPC.

## Results  
The implicit differentiation technique reduces temporary memory growth to less than 4 % per iteration, whereas unrolled AD would increase memory by over tenfold. At 256 active contacts the method consumes roughly 20 times less memory than the exponential scaling of unrolled AD, and at 16 contacts it is about six times lighter. Moreover, optimiser distillation improves six‑step success probability on three robotic platforms by 28–98 percentage points relative to standard iLQR, demonstrating both theoretical and practical benefits.

## Significance  
By decoupling sensitivity computation from solver unrolling, the method enables real‑time trajectory planning with modest memory overhead. The amortised approach is especially valuable for high‑contact scenarios where full‑horizon optimisation would be prohibitive. The distillation framework further reduces computational load, making residual MPC feasible on embedded hardware while preserving high performance.

## Related Concepts  
Implicit Function Theorem, automatic differentiation, residual model predictive control (residual MPC), iLQR distillation, KKT sensitivity derivation, contact solvers, trajectory optimisation, temporary memory management.
