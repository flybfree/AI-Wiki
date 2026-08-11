# Summary: 2026-08-08_18-26-25Z_StatefulCARS_ExactCross_HistoryReuseforPolicy_Cons.md
Saved: 2026-08-10 23:06
Source: 2026-08-08_18-26-25Z_StatefulCARS_ExactCross_HistoryReuseforPolicy_Cons.md
Model: None

---

## Summary  
The paper proposes **Stateful CARS**, an exact sampling framework that reuses invalidity certificates across multiple attempts of a policy‑constrained language‑model agent. By freezing a bank of sound state‑continuation schemas and discarding any trajectory that contains a certified continuation at a matching abstract state, the method yields an exact conditional distribution while preserving i.i.d. outputs, almost‑sure termination, and monotone acceptance. The authors prove schema soundness, compression invariance, and provide a checkable future‑validity bisimulation condition, demonstrating that the approach matches empirical validity probabilities to within \(10^{-16}\) on enumerable workflows.

## Key Contributions  
- [Finding 1] **Exact Sampling with Cross‑History Reuse** – Stateful CARS constructs an exact residual Doob transform conditioned on a hard validator, eliminating trajectories that violate abstract state continuity and thus achieving exact sampling without re‑evaluation of the full history.  
- [Finding 2] **Analytical Guarantees** – The authors prove schema soundness, adaptive exactness, monotone acceptance, almost‑sure termination, compression invariance, and provide a bisimulation condition that can be checked in polynomial time relative to reachable full‑history product states.  
- [Finding 3] **Empirical Superiority over Local Decoding** – Experiments show that Stateful CARS achieves an empirical validity error of \(6 \times 10^{-8}\) (matching the target), whereas state‑aware local decoding can be off by up to 0.97, and it outperforms official CARS in sampler steps with a root/Stateful ratio of 0.942.

## Methodology  
The authors treat policy constraints as a validator that produces certificates for each abstract state. During an attempt, they maintain a set of sound schemas that describe permissible continuations. Any trajectory that triggers a certificate is frozen and removed from the proposal space; the remaining proposals are sampled exactly via a Doob transform. This process repeats across attempts, reusing the same schemas, which reduces computational overhead compared to recomputing validators for each sample.

## Results  
Theoretical analysis yields an exact conditional distribution whose acceptance probability equals the validator’s validity measure up to \(10^{-16}\). On a benchmark of enumerable workflows, the method reaches a validity probability of \(6 \times 10^{-8}\) with an error margin below \(10^{-16}\), while local decoding methods deviate by up to 0.97. Comparative sampling step counts show that Stateful CARS uses fewer steps than official CARS (ratio 0.942, 95 % CI [0.934, 0.951]) and matches Qwen’s performance within a narrow confidence interval (0.99). Cross‑history transfer only yields modest gains in an internal matched‑key ablation (1.27×), indicating that the primary advantage lies in exact schema conditioning rather than system efficiency.

## Significance  
Stateful CARS bridges the gap between exact conditional sampling and practical agent use, offering provable guarantees while maintaining i.i.d. output generation. The ability to reuse certificates across attempts reduces computational cost dramatically, making high‑precision policy‑constrained sampling feasible for language‑model agents that must respect evolving constraints.

## Related Concepts  
- **CARS (Conditional Acceptance Rejection Sampling)** – a prior exact sampling technique for constrained models.  
- **Doob Transform** – an exact resampling method preserving the conditional distribution.  
- **Abstract State Continuation Schemas** – formalizations of state‑continuing policies that can be frozen and reused.  
- **Bisimulation Condition** – a checkable property ensuring two states are equivalent under the validator’s rules.
