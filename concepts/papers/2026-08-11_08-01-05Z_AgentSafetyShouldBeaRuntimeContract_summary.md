# Summary: 2026-08-11_08-01-05Z_AgentSafetyShouldBeaRuntimeContract.md
Saved: 2026-08-12 22:20
Source: 2026-08-11_08-01-05Z_AgentSafetyShouldBeaRuntimeContract.md
Model: None

---

## Summary  
The authors argue that AI safety cannot be achieved solely by training‑time techniques such as RLHF or DPO, especially for autonomous agents that can execute code, modify files, send messages, and alter databases. They propose treating safety as a runtime contract enforced by the agent’s harness, consisting of two complementary faces: a preventive face that blocks dangerous actions through sandboxes, permission gates, output filters, and trajectory monitors; and an evidential face that requires verifiable proof—such as test runs, log captures, file diffs, or citation grounding—that gating task submission on hard evidence. The paper grounds this claim in four publicly released datasets: a survey of 52 AI‑agent safety incidents, a false‑completion audit with 31 non‑contested cases plus one illustrative case, a trajectory‑schema audit of 12 public agent systems and harnesses, and a title‑level audit of 28,560 papers from NeurIPS, ICML, ICLR (2023‑2025) showing an 8–12× imbalance between training‑time and deployment‑time publications. The authors formalize the “Agent Trajectory Schema” and “Evidence Chain,” state a compositional gating proposition based on standard monitor composition, and outline a research agenda.

## Key Contributions  
- [Finding 1] Safety should be enforced as a runtime contract with both preventive and evidential components rather than only during training.  
- [Finding 2] The Agent Trajectory Schema formalizes the structure of an agent’s execution path together with checkable evidence, providing a unified unit of safety.  
- [Finding 3] Empirical audits reveal a stark gap between published safety work and actual deployment incidents, underscoring the need for runtime enforcement.

## Methodology  
The authors approached the problem by synthesizing existing literature on AI‑agent safety with insights from computer security and experimental sciences, which both rely on runtime contracts. They compiled four datasets (incident survey, false‑completion audit, trajectory‑schema audit, title‑level audit) to empirically quantify how often safety is addressed at training versus deployment stages. Using these data they derived the 8–12× imbalance, formulated the Agent Trajectory Schema and Evidence Chain, and applied standard monitor composition theory to derive a compositional gating proposition.

## Results  
The empirical audits confirm that most AI‑agent safety failures are not caught by training‑time methods; instead, they manifest at runtime. The trajectory‑schema audit identifies 12 public systems where preventive safeguards exist but evidential checks are absent, leading to undetected harmful actions. The false‑completion audit shows 31 cases where the model produced plausible but incorrect outputs that could be exploited without verification.

## Significance  
This work shifts the unit of safety from a static model property to a dynamic trajectory with checkable evidence, aligning agentic AI with established practices in security and experimental science. It provides a concrete framework for building trustworthy autonomous agents and highlights a critical research gap: the lack of runtime enforcement mechanisms despite extensive training‑time safety literature.

## Related Concepts  
- Runtime contract  
- Agent Trajectory Schema  
- Evidence Chain  
- Preventive face (sandboxes, permission gates)  
- Evidential face (test runs, log captures, file diffs)  
- Monitor composition  
- Compositional gating proposition

## Original Paper Reference

- [Read the original paper](http://arxiv.org/abs/2608.11274v1)
