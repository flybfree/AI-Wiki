# Summary: 2026-08-16_18-38-00Z_BoundedAgents_DelegationSecurityforMulti_AgentAISy.md
Saved: 2026-08-17 23:21
Source: 2026-08-16_18-38-00Z_BoundedAgents_DelegationSecurityforMulti_AgentAISy.md
Model: None

---

## Summary  
This paper addresses the security vulnerability of LLM‑driven multi‑agent systems where an agent may perform actions beyond a user’s delegated intent, combine permitted operations into prohibited outcomes, or hand authority to sub‑agents unchecked. The authors introduce the Agentic Principal Chain (APC), a formal authorization architecture that tracks and evaluates each request against accumulated session state using six checks, thereby preventing unauthorized combinations and enforcing decisions outside the model. Their work proves two key properties—Blast Radius Monotonicity and Composition Soundness—and demonstrates that APC can neutralize prompt‑injection attacks without degrading utility. The contribution lies in a complete theoretical analysis plus extensive empirical validation across real‑world agent implementations.

## Key Contributions  
- **APC Framework**: A six‑check authorization pipeline that accumulates delegated authority, evaluates each request against prior actions, and enforces decisions externally to the model.  
- **Theoretical Guarantees**: Proof of Blast Radius Monotonicity (security never worsens with more checks) and Composition Soundness (no prohibited combination can be formed under a complete restriction set).  
- **Empirical Impact**: Empirical testing shows AgentDojo’s data‑stealing success rate drops from 75–100 % to 0 %, all 544 InjecAgent cases are blocked, and latency at the 99th percentile is 0.24 ms with utility reduced by 8.6 and 13.9 percentage points.

## Methodology  
The authors approached the problem by modeling delegation as a chain of principals where each principal delegates authority to the next. APC maintains a session‑state log that records granted permissions, budgets, and prior actions. For every incoming request, the system performs six authorization checks: (1) scope validation, (2) budget check, (3) prohibited‑combination test via composition closure, (4) sub‑agent delegation limit, (5) intent binding verification, and (6) external decision enforcement. The model is never consulted to decide whether a request is allowed; instead, APC’s policy engine blocks or permits the action. To evaluate, the authors inserted ground‑truth attack calls after legitimate tool use in 3,154 instances across InjecAgent, AgentDojo, and ASB.

## Results  
Experimentally, APC reduced exfiltration rates dramatically: AgentDojo’s data‑stealing fell from 75–100 % to 0 % across four domains. All 544 InjecAgent attempts were blocked, confirming Composition Soundness in practice. Authorization latency measured at the 99th percentile is 0.24 ms on an idle host. Utility scores for AgentDojo dropped by 8.6 and 13.9 percentage points compared with baseline implementations without APC. The theoretical proofs hold: Blast Radius Monotonicity ensures adding more checks never harms security, while Composition Soundness guarantees no prohibited combination can be formed under a complete restriction set.

## Significance  
This research demonstrates that multi‑agent AI security is fundamentally an issue of authorization architecture rather than model behavior alone. By separating policy enforcement from the language model, APC mitigates prompt injection and other delegation attacks, offering a scalable solution for real‑world deployments. The empirical results prove that robust authorization can eliminate high‑impact exploits while incurring negligible latency.

## Original Paper

**Original paper**: [arXiv:2608.15888](https://arxiv.org/abs/2608.15888)

## Related Concepts  
- Authorization Architecture  
- Permission Stack / Delegation Security  
- Prompt Injection  
- Blast Radius Monotonicity  
- Composition Soundness  
- Agentic Principal Chain (APC)
