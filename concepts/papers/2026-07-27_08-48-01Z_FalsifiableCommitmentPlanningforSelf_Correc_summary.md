# Summary: 2026-07-27_08-48-01Z_FalsifiableCommitmentPlanningforSelf_CorrectingWeb.md
Saved: 2026-07-27 22:55
Source: 2026-07-27_08-48-01Z_FalsifiableCommitmentPlanningforSelf_CorrectingWeb.md
Model: None

---

## Summary  
The paper introduces FCPAgent, a falsifiable commitment planning framework for long‑horizon web agents that prevents them from deviating from user goals by explicitly modeling evidence supporting or contradicting plan steps. By representing each step as a Falsifiable Commitment Unit (FCU), the system can detect when observations falsify a commitment and trigger localized repairs. This approach enables robust self‑correction without catastrophic failure.

## Key Contributions  
- [Finding 1] The concept of Falsifiable Commitment Units (FCUs) decomposes each plan step into a subgoal grounded in a reusable skill, together with confirming evidence, falsifying evidence, and a confidence score.  
- [Finding 2] A hybrid testing module performs pre‑action checks using lightweight evidence matching and post‑execution verification via LLM‑based diagnostic verification to flag contradictions early.  
- [Finding 3] Scope‑aware repair isolates the source of a contradiction—whether it lies in execution, skill usage, or planning—and revises only the smallest adequate component.

## Methodology  
The authors approach the problem by constructing a hierarchical planning process where commitments are tied to reusable skills and evidence. They then iterate through a plan‑test‑repair loop: first, candidate actions are filtered with lightweight evidence matching; second, after each action they verify observations using LLM diagnostics that can explain why an observation falsifies a commitment. When a falsification occurs, the repair system determines whether the contradiction originates from the execution step, the underlying skill, or the planning assumption and updates only that part.

## Results  
Experimental evaluation on WebArena shows that FCPAgent achieves a 13.8 % relative increase in average success compared with the strongest baseline, and the gains are most pronounced for tasks requiring several sequential steps. The improvement persists across both short‑ and long‑horizon challenges, indicating scalability.

## Significance  
This work matters because it provides a principled mechanism for self‑correction that scales to long‑horizon interactions, reducing the risk of agents becoming stuck or producing nonsensical outputs. By grounding commitments in evidence and enabling precise, localized repairs, FCPAgent makes web agents more reliable and trustworthy.

## Related Concepts  
- Falsifiable Commitment Unit (FCU)  
- Plan‑test‑repair loop  
- Evidence matching  
- LLM diagnostic verification  
- Scope‑aware repair
