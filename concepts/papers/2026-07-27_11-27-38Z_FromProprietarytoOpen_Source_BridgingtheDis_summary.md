# Summary: 2026-07-27_11-27-38Z_FromProprietarytoOpen_Source_BridgingtheDistributi.md
Saved: 2026-07-27 22:56
Source: 2026-07-27_11-27-38Z_FromProprietarytoOpen_Source_BridgingtheDistributi.md
Model: None

---

## Summary  
The paper tackles the challenge of transferring reasoning competence from large proprietary language models to more efficient student agents using knowledge distillation, while also solving knowledge-intensive tasks via agentic search. Conventional logit‑matching fails because of hidden logits and tokenizer mismatches, and raw trajectory imitation only captures surface style. The authors introduce Multi‑Agent Protocol Distillation (MAPD), a joint framework that creates a structured protocol as an intermediate representation to provide dense distillation signals. MAPD combines this protocol with outcome‑based reinforcement learning to bridge the distribution gap between teacher and student agents.

## Key Contributions  
- [Finding 1] A novel protocol‑level distillation method that normalizes style and aligns token distributions across heterogeneous teachers.  
- [Finding 2] An offline multi‑agent system (MAS) that decomposes queries, retrieves evidence, repairs failed searches, and emits a JSON protocol containing task type, reasoning plan, and grounding facts.  
- [Finding 3] Demonstrated consistent performance gains across seven QA benchmarks, achieving average success rates of 39.4 % on Qwen3‑1.7B and 44.4 % on Qwen3‑4B.

## Methodology  
MAPD operates in two phases: first, an offline multi‑agent system generates a protocol for each query that encodes the task type, a step‑by‑step reasoning plan, and extractive grounding facts; second, during training only a privileged branch of the student policy receives this protocol, allowing it to learn dense token distributions while simultaneously optimizing a sparse RL objective. The protocol serves as a shared representation that mitigates style drift and verbosity degeneration.

## Results  
Extensive experiments across seven QA benchmarks show MAPD outperforms both conventional distillation baselines and pure RL approaches, delivering the highest average success rates observed in prior work. The framework also generalizes robustly to diverse proprietary teacher models, confirming its flexibility beyond a single source model.

## Significance  
By decoupling style from reasoning and providing a structured protocol as a dense supervision signal, MAPD addresses long‑standing limitations of distillation in agentic search. This enables more efficient training of student agents that retain strong reasoning abilities while reducing reliance on proprietary teacher models, fostering broader adoption and interoperability.

## Related Concepts  
knowledge distillation; multi‑agent protocol; distillation signal; outcome‑based reinforcement learning; style drift mitigation
