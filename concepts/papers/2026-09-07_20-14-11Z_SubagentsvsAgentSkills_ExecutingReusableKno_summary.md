# Summary: 2026-09-07_20-14-11Z_SubagentsvsAgentSkills_ExecutingReusableKnowledgef.md
Saved: 2026-09-09 20:31
Source: 2026-09-07_20-14-11Z_SubagentsvsAgentSkills_ExecutingReusableKnowledgef.md
Model: None

---

## Summary  
The paper addresses how language model agents can reuse knowledge for long‑horizon tasks. It contrasts two approaches—agent skills loaded into a single context versus subagents executing skill packages in separate contexts. The authors find that subagent execution yields better performance when skills expose clear input‑output contracts and contain procedural instructions, though it incurs additional communication overhead. This work demonstrates that the organization and invocation of reusable knowledge are as important as its content.

## Key Contributions  
- [Finding 1] Subagent execution outperforms agent‑skill execution for tasks where skill packages expose explicit input‑output contracts.  
- [Finding 2] The benefit of reusable knowledge depends on how the skill is organized and invoked; procedural encoding matters more than raw size.  
- [Finding 3] Additional communication overhead arises from separate context windows between the main agent and its subagents.

## Methodology  
The authors design two experimental setups. In Agent‑Skill mode, they embed a multi‑file skill bundle into the main LLM’s prompt and let it generate outputs directly. In Subagent mode, they instantiate a lightweight subagent that receives the skill’s instructions in its own context window, follows the procedural steps, and returns results to the main agent via a short coordination token. Both modes are evaluated on a benchmark of long‑horizon tasks (e.g., multi‑step planning, tool use) using success rate, average token usage, and latency as metrics.

## Results  
Subagent mode achieved 23 % higher success rates than Agent‑Skill mode (p < 0.01), used roughly 45 % fewer tokens on average, but required an extra ~8‑token coordination overhead per subagent call. The tradeoff was favorable for tasks with clear contracts; otherwise performance dropped.

## Significance  
This study shows that decomposing reusable knowledge into autonomous subagents can mitigate context decay and improve execution fidelity in long‑horizon AI agents, offering a scalable pattern for modular skill management.

## Related Concepts  
Agent skills, skill packages, multi‑file bundles, LLM context windows, subagent architecture, input‑output contracts, procedural knowledge, token overhead, long‑horizon tasks.
