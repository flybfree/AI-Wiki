# Summary: 2026-07-01_21-20-57Z_ProceduralMemoryDistillation_OnlineReflectionforSe.md
Saved: 2026-07-23 23:36
Source: 2026-07-01_21-20-57Z_ProceduralMemoryDistillation_OnlineReflectionforSe.md
Model: None

---

## Summary  
The paper introduces Procedural Memory Distillation (PMD), a technique that captures cross‑episode procedural signals from reinforcement learning with verifiable rewards and converts them into reusable memory that is distilled directly into the model’s weights, enabling self‑improving language models without explicit storage. By extracting raw trajectories, self‑reflected strategies, and higher‑level patterns online, PMD creates a memory scaffold that co‑evolves with the policy, allowing the model to internalize procedural knowledge within its parameters.

## Key Contributions  
- **Memory abstraction**: PMD organizes experience into three levels—raw trajectories, self‑reflected strategies, and recurring behavioral patterns—all extracted online from the model’s own rollouts.  
- **Co‑evolution design**: The method simultaneously updates a memory that conditions supervision for the student teacher and uses those updates to refine the policy, forming a feedback loop between generation and memory refinement.  
- **Empirical gains**: Across Qwen3‑8B and OLMo3‑Instruct‑7B, PMD improves over SDPO by 3.8–5.5% on SCIKNOWEVAL and 7.9–13.6% on LIVECODEBENCH, with freezing either component reducing gains by more than 10%.

## Methodology  
The authors first generate rollouts under a current policy and use the verifier to identify strategies that consistently pass verification (self‑reflected strategies). These strategies are stored as procedural memory at the three abstraction levels. A memory‑conditioned self‑teacher then supervises its own rollouts using this accumulated experience, producing supervision signals that drive weight updates. The process repeats online, with each iteration refining both the policy and the memory.

## Results  
Across multiple benchmarks, PMD consistently outperforms SDPO: SCIKNOWEVAL gains of 3.8–5.5% and LIVECODEBENCH gains of 7.9–13.6%. The authors also demonstrate that freezing either the memory or the policy alone reduces performance by >10%, confirming that the co‑evolutional interaction is essential for the observed improvements.

## Significance  
PMD demonstrates that procedural knowledge can be internalized directly into a language model’s parameters, yielding a memory‑free inference system while boosting task performance. This approach offers a scalable pathway to self‑improving models that retain cross‑task experience without external storage, addressing a limitation of current distillation methods.

## Related Concepts  
- Reinforcement learning with verifiable rewards (RLVR)  
- Self‑distillation (SDPO)  
- Procedural memory  
- Co‑evolution between policy and memory  
- Memory‑conditioned teacher student framework
