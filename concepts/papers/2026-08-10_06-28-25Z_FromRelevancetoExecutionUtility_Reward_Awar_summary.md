# Summary: 2026-08-10_06-28-25Z_FromRelevancetoExecutionUtility_Reward_AwareDynami.md
Saved: 2026-08-10 23:38
Source: 2026-08-10_06-28-25Z_FromRelevancetoExecutionUtility_Reward_AwareDynami.md
Model: None

---

## Summary  
The paper introduces Reward‑Aware Dynamic Execution Gating (RADEG), a lightweight decision layer that decides whether a retrieved skill bundle should be executed, thereby bridging the gap between relevance and execution utility. It learns a low‑cost surrogate model that predicts the utility of each query–bundle pair before costly rollouts are launched. The method uses locally perturbed rollouts to supervise the surrogate, allowing cheap adaptation without retraining the retriever or the agent. This approach reduces unnecessary agent executions while preserving most of the downstream verifier reward.

## Key Contributions  
- RADEG introduces a lightweight decision layer that scores execution utility per query‑bundle pair without requiring retraining of either the skill retriever or the LLM agent.  
- It provides supervised learning via matched same‑query rollouts where bundle composition is altered (adding, deleting, or replacing one skill) to isolate the effect on verifier reward.  
- The system updates only a logistic head incrementally as new feedback arrives, enabling inexpensive adaptation of the execute/skip boundary.

## Methodology  
The authors address the computational bottleneck caused by executing every retrieved bundle. They model execution utility as a function of the query and the bundle composition, treating it as a binary decision (execute vs. skip). To obtain supervisory data, they generate paired rollouts: for each query they create three variants—one with the original bundle, one with a skill added, and one with that skill removed or replaced. The verifier reward is identical across these variants because only the bundle differs, allowing the logistic head to learn which composition yields higher utility. During deployment, RADEG updates solely this logistic head using new feedback, leaving the expensive retriever and agent untouched.

## Results  
On a held‑out set of 288 rollouts across multiple execution budgets, RADEG cuts unnecessary executions by roughly 40 % compared with relevance‑based gating while maintaining >95 % of the verifier reward. It consistently outperforms random gating and even surpasses relevance gating when computational resources are limited, demonstrating that a surrogate model can effectively prune low‑utility rollouts.

## Significance  
This work shows that execution‑aware surrogate modeling can dramatically reduce waste in skill‑based LLM agents, making large‑scale deployment feasible without sacrificing performance. By decoupling costly rollout decisions from the retrieval process, RADEG enables scalable, cost‑effective agent systems that balance relevance and utility.

## Related Concepts  
- Skill retrieval  
- Dynamic gating  
- Reinforcement learning (verifier reward)  
- Logistic regression head  
- Incremental adaptation  
- Rollout simulation  
- Execution budget constraints
