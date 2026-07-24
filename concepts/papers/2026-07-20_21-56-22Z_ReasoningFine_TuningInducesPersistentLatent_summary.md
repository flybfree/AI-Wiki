# Summary: 2026-07-20_21-56-22Z_ReasoningFine_TuningInducesPersistentLatentPolicyS.md
Saved: 2026-07-24 00:26
Source: 2026-07-20_21-56-22Z_ReasoningFine_TuningInducesPersistentLatentPolicyS.md
Model: None

---

## Summary  
The paper investigates whether reasoning fine‑tuning merely enhances token‑level competence or reorganizes the internal latent dynamics that govern multi‑step Chain‑of‑Thought (CoT) inference. By treating CoT as a switching dynamical system, it discovers persistent latent policy states that survive fine‑tuning and can be recovered from activation trajectories across multiple model scales and benchmarks. The framework shows that these regimes are functionally specialized at distinct reasoning stages and enable causal interventions such as state‑swap ablations and dynamic transplantation.

## Key Contributions  
- [Finding 1] Reasoning fine‑tuning reorganizes latent dynamics into discrete policy states rather than just improving local token competence.  
- [Finding 2] The identified regimes correspond to functional specialization at distinct reasoning stages, with measurable persistence and mixing patterns across model sizes.  
- [Finding 3] Causal interventions (state‑swap ablations, transplanting reasoning dynamics) demonstrate that the structure is not a by‑product of correctness but stems from coherent temporal organization.

## Methodology  
The authors model Chain‑of‑Thought reasoning as a switching dynamical system (SDS), employing time‑aware contrastive representation learning to capture how internal representations evolve under discrete latent policies. Discrete regime discovery extracts these policies directly from activation trajectories across four benchmark suites and models ranging from 1.5 B to 32 B parameters. Causal analyses then test the functional relevance of each state.

## Results  
Fine‑tuned models exhibit richer transition structures, more differentiated state utilization, and improved performance on challenging reasoning tasks compared with base models. SDS‑guided pruning of failure‑prone prefixes outperforms self‑consistency in 11 of 12 model‑dataset settings, delivering gains up to 12.5 percentage points.

## Significance  
These findings reveal that fine‑tuning globally reorganizes latent dynamics, providing a mechanistic lens for analyzing and controlling reasoning models at the process level. The ability to isolate and manipulate policy states opens new avenues for improving reliability and enabling targeted interventions in large language systems.

## Related Concepts  
Switching dynamical system (SDS), latent policy states, time‑aware contrastive learning, discrete regime discovery, causal intervention, chain‑of‑thought reasoning, model pruning, self‑consistency.
