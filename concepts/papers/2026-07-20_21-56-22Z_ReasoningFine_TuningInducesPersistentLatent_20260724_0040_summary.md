# Summary: 2026-07-20_21-56-22Z_ReasoningFine_TuningInducesPersistentLatentPolicyS.md
Saved: 2026-07-24 00:40
Source: 2026-07-20_21-56-22Z_ReasoningFine_TuningInducesPersistentLatentPolicyS.md
Model: None

---

## Summary  
The paper investigates how reasoning fine‑tuning changes the internal dynamics of language models, proposing that such fine‑tuning reorganizes latent policy states into a structured dynamical system. By modeling Chain‑of‑Thought (CoT) reasoning as a switching dynamical system (SDS), they recover discrete latent policies from activation trajectories across multiple model sizes and benchmarks. Their analysis reveals that fine‑tuned models develop richer, more specialized regimes of state utilization that persist beyond training. This work bridges performance gains with mechanistic understanding.  

## Key Contributions  
- Finding 1: Reasoning fine‑tuning reorganizes the internal representation into a switching dynamical system where latent policy states evolve over time.  
- Finding 2: The recovered regimes exhibit functional specialization aligned with distinct reasoning stages, showing model‑dependent changes in state persistence and mixing.  
- Finding 3: Causal interventions (state‑swap ablations, transplanting dynamics) show that the new structures improve performance on challenging problems.  

## Methodology  
The authors treat CoT reasoning as a discrete dynamical system where each token’s activation trajectory corresponds to a latent policy state. They employ time‑aware contrastive learning to align trajectories across different reasoning steps and use regression‑based regime discovery to infer the underlying policy schedule. The framework is applied to four benchmark suites (e.g., MATH, GSM8K) across models from 1.5B to 32B parameters.  

## Results  
Across all settings, fine‑tuned models exhibit a higher number of distinct latent policies and smoother transitions compared with base models. Ablation studies demonstrate that swapping states reduces one‑step predictive fit by ~0.8 points, while transferring the reasoning dynamics into a base model boosts performance on hard problems by up to 12.5 percentage points. SDS‑guided pruning of failure‑prone prefixes outperforms self‑consistency in 11/12 settings.  

## Significance  
Understanding that fine‑tuning creates persistent latent policy states provides a mechanistic explanation for why reasoning models improve, moving beyond empirical performance to process‑level control. This insight enables targeted interventions such as pruning or state swapping without sacrificing accuracy.  

## Related Concepts  
- Switching dynamical system (SDS)  
- Latent policy states  
- Time‑aware contrastive representation learning  
- Discrete regime discovery  
- Causal intervention  
- SDS‑guided pruning
