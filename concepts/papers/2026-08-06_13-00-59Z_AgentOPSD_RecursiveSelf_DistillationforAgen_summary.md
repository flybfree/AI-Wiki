# Summary: 2026-08-06_13-00-59Z_AgentOPSD_RecursiveSelf_DistillationforAgenticRein.md
Saved: 2026-08-06 20:44
Source: 2026-08-06_13-00-59Z_AgentOPSD_RecursiveSelf_DistillationforAgenticRein.md
Model: None

---

## Summary  
The paper proposes AgentOPSD, a critic‑free recursive self‑distillation method for turn‑level credit assignment in agentic reinforcement learning. It addresses the challenge of sparse outcome supervision by aggregating token‑level teacher‑student log‑probability gaps into turn‑level evidence and updating a Bayesian belief state recursively. This yields dense, pivotal turn signals without requiring an additional critic or extra rollouts.

## Key Contributions  
- [Finding 1] AgentOPSD provides dense, turn‑level credit signals without requiring an additional critic.  
- [Finding 2] The method uses recursive Bayesian belief updates in log‑odds space to convert sparse outcomes into pivotal turn identification.  
- [Finding 3] Empirical results show AgentOPSD outperforms GRPO and strong self‑distillation baselines, achieving 89.1% success on ALFWorld with Qwen2.5‑7B.

## Methodology  
The authors treat each token’s log‑probability gap between teacher and student as evidence for a turn. These evidences are aggregated to form turn‑level evidence vectors that update a cumulative Bayesian belief state stored in log‑odds space. The belief is recursively refined across turns, allowing the system to reweight past decisions based on how much the posterior changes when moving from one turn to the next. This reweighting yields credit assignments that highlight pivotal turns while preserving compatibility with standard policy optimization.

## Results  
AgentOPSD was evaluated on three benchmark tasks—ALFWorld, WebShop, and Search‑QA—using Qwen2.5 models at 3B and 7B parameter scales. It achieved a success rate of 89.1% on ALFWorld, surpassing GRPO (≈84%) and strong self‑distillation baselines. Ablation studies confirm that turn‑level aggregation and history‑dependent recursive belief updates are the primary drivers of performance gains. The method also reduces variance of credit assignment by focusing on marginal belief revisions between consecutive states.

## Significance  
By enabling precise credit assignment at the turn level without extra components, AgentOPSD improves long‑horizon agentic RL where outcomes depend on few critical decisions. The method’s compatibility with existing policy optimization pipelines makes it a practical enhancement for scalable, verifiable reward systems.

## Related Concepts  
- Reinforcement learning with verifiable rewards  
- Privileged self‑distillation  
- Bayesian belief state in log‑odds space  
- Recursive credit assignment
