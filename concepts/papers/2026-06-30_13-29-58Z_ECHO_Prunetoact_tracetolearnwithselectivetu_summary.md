# Summary: 2026-06-30_13-29-58Z_ECHO_Prunetoact_tracetolearnwithselectiveturnmemor.md
Saved: 2026-06-30 21:01
Source: 2026-06-30_13-29-58Z_ECHO_Prunetoact_tracetolearnwithselectiveturnmemor.md
Model: None

---


## Summary  
The paper tackles the problem of long‑horizon language agents that must retain and reuse fine‑grained evidence across many turns while operating within a bounded context window. Existing methods either truncate distant history or collapse it into summaries, which both limit policy reuse and obscure the causal path to successful outcomes. The authors introduce ECHO, a selective turn‑memory framework that compresses each completed environment turn into a compact memory record, reconstructs bounded contexts by selecting from these records, and routes positive outcome credit back to the evidence and selection actions via source indices. This dual focus on compression without loss of traceability aims to improve both efficiency and learning in agentic reinforcement learning.

## Key Contributions  
- [Finding 1] ECHO compresses each completed environment turn into a compact memory record, preserving fine‑grained observations while reducing trajectory volume.  
- [Finding 2] The framework reconstructs bounded policy contexts by selecting from these records, enabling the agent to reuse evidence across turns without explicit rollout truncation.  
- [Finding 3] Positive outcome credit is routed through selected source indices, allowing traceable learning and clear attribution of successful answers.

## Methodology  
ECHO operates on a per‑turn basis: after each environment step, the system creates a memory record that includes the observation, action, and a unique source index. The agent’s policy context window is then built by sampling these records according to a lightweight selection mechanism (e.g., a sliding‑window with priority). When an answer is generated, the algorithm identifies which selected indices contributed positively and updates their associated credit scores. This source‑indexed reconstruction ensures that each piece of evidence remains addressable, enabling precise alignment between policy updates and the supporting data.

## Results  
On the BrowseComp‑Plus benchmark, ECHO achieves 43.4 % held‑out accuracy, significantly outperforming GRPO (28.9 %) and the rolling‑summary baseline SUPO (36.1 %). The model also uses fewer turns and generates lower trajectory volumes than SUPO, as shown in Figure 1. Moreover, the trained policy generalizes to zero‑shot tasks across multi‑objective QA, code generation, and deep information‑seeking benchmarks, performing well on both dense and MoE backbones.

## Significance  
By decoupling compression from traceability, ECHO solves two longstanding limitations of context management in agentic RL: loss of fine‑grained evidence and opaque credit assignment. The approach reduces memory footprint while preserving the ability to learn from specific turns, which is crucial for scalable, long‑horizon language agents that must balance efficiency with performance.

## Related Concepts  
- Context‑management techniques (rollout truncation, rolling summaries)  
- Gradient‑proportional policy optimization (GRPO)  
- Selective memory or selective turn memory  
- Source‑indexed reconstruction for traceable learning  
- Agentic reinforcement learning with long horizons
