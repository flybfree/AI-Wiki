# Summary: 2026-08-10_08-11-24Z_MoRSE_Task_OrientedMulti_AgentSystemwithMixtureofR.md
Saved: 2026-08-10 23:58
Source: 2026-08-10_08-11-24Z_MoRSE_Task_OrientedMulti_AgentSystemwithMixtureofR.md
Model: None

---

## Summary  
The paper introduces MoRSE, a task‑oriented multi‑agent system that creates explicit role‑subtask specialization at both the structural and parameter levels to overcome the coarse prompt‑level differentiation used in existing LLM agents. By decomposing tasks into a dependency‑aware DAG of subtasks and assigning each agent a specific (role, subtask) responsibility, MoRSE generates richer inter‑agent heterogeneity. A dynamic Mixture of Role‑Subtask LoRA Experts with a prototype‑based semantic router enables cost‑effective parameter adaptation. The system stabilizes learning through hierarchical group‑relative policy optimization with two‑layer credit assignment that isolates expert updates from routing variance.

## Key Contributions  
- [Finding 1] Task decomposition into a dependency‑aware DAG and explicit (role, subtask) agent assignment.  
- [Finding 2] Dynamic Mixture of Role‑Subtask LoRA Experts with prototype‑based semantic router for parameter‑level specialization.  
- [Finding 3] Hierarchical group‑relative policy optimization with two‑layer credit assignment to decouple expert updates from routing decisions.

## Methodology  
The authors address the limitation of coarse prompt differentiation by first defining a task structure that maps subtasks to agents, thereby making responsibilities explicit. MoRSE then builds each agent as a shared LLM augmented with LoRA modules whose weights are tuned per (role, subtask). A semantic router selects the appropriate expert based on prototype‑based similarity to the current subtask. Training employs hierarchical reinforcement learning: a top‑level policy updates group‑level actions while a bottom‑level policy fine‑tunes individual expert weights. This two‑layer credit assignment scheme stabilizes convergence under sparse task rewards and prevents interference between routing decisions and expert quality.

## Results  
Experiments on three code‑generation benchmarks using different LLM backbones demonstrate that MoRSE improves both whole‑task and step‑wise performance compared with baseline prompt‑only methods. The gains persist when transferred to held‑out task categories and domains, indicating generalization of the learned specialization.

## Significance  
MoRSE provides a scalable framework for multi‑agent systems where each agent can be specialized without retraining the entire model, enabling more robust, long‑horizon tasks with complex requirements. By separating structural role assignment from parameter adaptation, it mitigates bottlenecks that limit performance in existing approaches.

## Related Concepts  
Multi‑agent system, role‑subtask specialization, LoRA (Low‑Rank Adaptation), Mixture‑of‑Experts, DAG decomposition, credit assignment, hierarchical RL, prototype‑based routing.
