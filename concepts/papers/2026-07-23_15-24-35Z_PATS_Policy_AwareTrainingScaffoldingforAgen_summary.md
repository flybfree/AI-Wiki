# Summary: 2026-07-23_15-24-35Z_PATS_Policy_AwareTrainingScaffoldingforAgenticRein.md
Saved: 2026-07-24 02:49
Source: 2026-07-23_15-24-35Z_PATS_Policy_AwareTrainingScaffoldingforAgenticRein.md
Model: None

---

## Summary  
The paper proposes PATS, a policy‑aware training scaffolding that treats skills as dynamic support for long‑horizon LLM agents in reinforcement learning. It reframes skill‑centric methods into an adaptive training‑time scaffold that supplies task‑specific context and guidance to improve weak policies. By converting rollout groups into evidence cards and using evaluation‑driven adjustments, PATS reduces redundant guidance as the policy improves. Experiments on ALFWorld and WebShop show up to 18.6 % higher reward than strong baselines while using fewer prompt tokens.

## Key Contributions  
- [Finding 1] PATS introduces a policy‑centric training paradigm that views skills as an adaptive scaffold rather than static components.  
- [Finding 2] The framework converts rollout groups into evidence cards and uses task‑specific evaluation to dynamically adjust context for subsequent rollouts.  
- [Finding 3] As the policy improves, redundant guidance is removed, preserving useful variation while minimizing prompt token usage.

## Methodology  
The authors approached the problem by analyzing how weak policies generate repetitive failures in long‑horizon tasks. They designed PATS as a scaffolding that provides evidence cards derived from the latest policy’s rollouts, which are evaluated task‑specifically to inform future context. The training loop uses standard RLVR for optimization while discarding the scaffold at deployment.

## Results  
On ALFWorld and WebShop benchmarks, PATS achieved up to 18.6 % higher reward than strong baselines. Across seven search‑augmented QA tasks, it remained competitive with 32.1 % fewer prompt tokens than baseline methods, indicating efficiency gains without sacrificing performance.

## Significance  
This work matters because it shifts the focus from static skill optimization to adaptive, policy‑driven scaffolding that enhances sample efficiency and reduces unnecessary guidance, offering a scalable approach for LLM agents in complex environments.

## Related Concepts  
- Reinforcement Learning (RL)  
- Long‑horizon tasks  
- Skill‑centric methods  
- Evidence cards  
- Prompt token usage  
- RLVR
