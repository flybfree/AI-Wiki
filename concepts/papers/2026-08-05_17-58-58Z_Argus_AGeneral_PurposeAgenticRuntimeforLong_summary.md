# Summary: 2026-08-05_17-58-58Z_Argus_AGeneral_PurposeAgenticRuntimeforLong_Horizo.md
Saved: 2026-08-05 22:36
Source: 2026-08-05_17-58-58Z_Argus_AGeneral_PurposeAgenticRuntimeforLong_Horizo.md
Model: None

---

## Summary  
The paper introduces Argus, a persistent agentic runtime designed to support long‑horizon reasoning by allowing an agent to persist when its current approach is validated and pivot only after evidence indicates failure or constraint violation. Argus separates the stable user intent from operational objectives, constraints, and verification criteria, enabling bounded missions executed by four roles—Manager, Planner, Engineer, and Reviewer—that share a durable project state. Self‑evolution occurs through persistent runtime state rather than retraining model weights, with autonomous execution occurring only between operator‑owned escalation points. The system produces structured trajectories that can be leveraged for future supervised or reinforcement learning.  

## Key Contributions  
- [Finding 1] Argus provides a general‑purpose agentic runtime capable of persistent self‑evolution without retraining model weights, preserving verified approaches across long tasks.  
- [Finding 2] The runtime achieves higher benchmark performance (≈78 % on SWE‑Bench Pro versus 59 % for Direct Copilot) while using only 1.41× the token budget and improving efficiency by 21 % fewer solve‑input tokens and 15 % less active workflow time per task after verification‑gated evolution.  
- [Finding 3] Argus generates structured, verified trajectories that reduce false routes (34 verifier recoveries) and enable strict review‑loop rescues (22 rescues), facilitating future supervised or reinforcement learning.  

## Methodology  
Argus is built as a persistent runtime where the user intent remains stable while operational objectives, constraints, and verification criteria are dynamically managed. Bounded missions are assigned to four roles—Manager (high‑level oversight), Planner (task decomposition), Engineer (implementation), and Reviewer (verification)—each operating on a shared project state that includes memories, skills, procedures, routing decisions, and rejected routes. Model weights stay fixed; self‑evolution is driven by persistent runtime state and control policies. Autonomous execution proceeds only between operator‑owned escalation points, ensuring safety and traceability.  

## Results  
Across seven GPT‑5.5 benchmark arenas, Argus scores 78 % on SWE‑Bench Pro compared with 59 % for Direct Copilot, using 1.41× the aggregate tokens. After verification‑gated self‑evolution, mature waves use 21 % fewer solve‑input tokens and 15 % less active workflow time per task than startup waves, recording 34 verifier recoveries and 22 strict review‑loop rescues. Argus also reaches 76.8 % on AARRI‑Bench and a 28.0‑point gap on mathematical data synthesis, with competitive GPU‑kernel and language‑model‑training results. An optimized RWKV6 kernel was merged upstream; a six‑paper mathematics campaign retained falsified routes while updating proof‑backed frontiers, completing 254 missions with 16 stage rollbacks.  

## Significance  
Argus demonstrates that a fixed‑weight, self‑evolving harness can revise, recover, and accumulate verified approaches, producing structured trajectories suitable for downstream supervised or reinforcement learning. By minimizing token waste and enabling robust recovery mechanisms, it addresses long‑horizon reasoning challenges where agents must persist through validated paths yet adapt when constraints emerge. This work paves the way for more reliable, efficient AI agents that can operate autonomously over extended periods without costly retraining.  

## Related Concepts  
- Agentic runtime  
- Persistent state  
- Verification‑gated evolution  
- Bounded missions  
- Role‑based execution (Manager/Planner/Engineer/Reviewer)  
- Memory and skill acquisition  
- Structured trajectories for future RL
