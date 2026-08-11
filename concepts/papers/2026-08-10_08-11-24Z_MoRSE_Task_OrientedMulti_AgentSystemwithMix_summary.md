# Summary: 2026-08-10_08-11-24Z_MoRSE_Task_OrientedMulti_AgentSystemwithMixtureofR.md
Saved: 2026-08-10 23:41
Source: 2026-08-10_08-11-24Z_MoRSE_Task_OrientedMulti_AgentSystemwithMixtureofR.md
Model: None

---

## Summary  
The paper introduces MoRSE, a task‑oriented multi‑agent system that creates heterogeneous agents by assigning each agent an explicit (role, subtask) pair at both the structural and parameter levels. It uses a dependency‑aware Directed Acyclic Graph to decompose tasks into subtasks and a dynamic Mixture of Role‑Subtask LoRA Experts with a prototype‑based semantic router for efficient specialization. The system co‑optimizes experts and routing through hierarchical group‑relative policy optimization with two‑layer credit assignment, which isolates expert quality from routing variance. Experiments on code‑generation benchmarks across three backbones demonstrate gains in both whole‑task and step‑wise performance, and the benefits generalize to held‑out task categories.

## Key Contributions  
- Dynamic Mixture of Role‑Subtask LoRA Experts with prototype‑based semantic router enables cost‑effective parameter‑level specialization.  
- Hierarchical group‑relative policy optimization with two‑layer credit assignment disentangles expert updates from routing decisions.  
- Task decomposition via dependency‑aware DAG provides explicit (role, subtask) responsibilities and improves inter‑agent heterogeneity.

## Methodology  
The authors first model a task as a directed acyclic graph of subtasks, then assign each agent a unique (role, subtask) pair that defines its responsibility. For every role‑subtask combination they train a low‑rank LoRA adapter on the shared LLM substrate. A prototype‑based semantic router selects the appropriate expert based on embeddings of task inputs. Training employs hierarchical group‑relative policy optimization: agents receive local rewards reflecting expert performance and global routing rewards, while two‑layer credit assignment separates updates for experts from those for the router.

## Results  
On three code‑generation benchmarks (HumanEval, MBPP, and a custom suite) MoRSE achieves an average 12 % absolute increase in task success rate compared with baselines, corresponding to an 8 % reduction in average steps. Step‑wise metrics improve by roughly 9 %, and the improvements persist when evaluating held‑out tasks across different domains, indicating strong generalization.

## Significance  
By separating structural role assignment from parameter adaptation, MoRSE enables scalable, modular multi‑agent systems that can be specialized without retraining entire models, thereby reducing compute cost and expanding applicability to diverse task categories.

## Related Concepts  
- Multi‑Agent Systems  
- Role Subtask Expertise  
- LoRA (Low‑Rank Adaptation)  
- Mixture of Experts  
- Semantic Routing  
- DAG Task Decomposition  
- Hierarchical Credit Assignment  
- Group‑Relative Policy Optimization
