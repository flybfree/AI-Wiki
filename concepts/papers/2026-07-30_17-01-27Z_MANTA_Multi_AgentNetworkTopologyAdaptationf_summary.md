# Summary: 2026-07-30_17-01-27Z_MANTA_Multi_AgentNetworkTopologyAdaptationforSelf_.md
Saved: 2026-07-30 22:21
Source: 2026-07-30_17-01-27Z_MANTA_Multi_AgentNetworkTopologyAdaptationforSelf_.md
Model: None

---

## Summary  
The paper proposes MANTA, a framework that allows communication topologies in multi‑agent systems to evolve during inference rather than being fixed offline. It enables self‑adaptive collaboration structures that respond to task conditions while maintaining the same agent budget and interface. By monitoring interaction traces, MANTA performs bounded structural updates to roles, links, order, visibility, and validation pathways. The framework demonstrates superior performance across diverse benchmarks compared to single‑agent and multi‑agent baselines.

## Key Contributions  
- Introduces inference‑time self‑evolving network topology adaptation for multi‑agent systems.  
- Provides a task‑conditioned initialization and bounded update mechanism that preserves the interface and agent budget.  
- Achieves state‑of‑the‑art performance on five benchmarks, notably PlanCraft, outperforming baselines by up to 5.8 percentage points.

## Methodology  
The authors address the limitation of static communication designs in large language model based multi‑agent systems by treating topology as a dynamic variable. They first collect structural experience from prior tasks to initialize a task‑conditioned topology. During deployment, they record collaboration traces and detect when the current organization is insufficient; then apply updates that modify agent roles, communication links, execution order, information visibility, or validation pathways while keeping the interface unchanged.

## Results  
MANTA was evaluated on five benchmarks covering information seeking, tool use, planning, workflow execution, and mathematical reasoning. It achieved an average score of 74.0, which is 5.8 points higher than the strongest baseline. The best result was obtained on PlanCraft, where MANTA outperformed all other methods.

## Significance  
This work demonstrates that collaboration architecture can be optimized at inference time, extending self‑improvement beyond task‑specific learning to system‑level design. It opens avenues for more flexible and resilient multi‑agent systems in complex problem solving.

## Related Concepts  
- Multi‑Agent Systems (MAS)  
- Communication Topology  
- Self‑Evolution / Self‑Adaptation  
- Task Conditioning  
- Bounded Updates  
- Large Language Model Inference
