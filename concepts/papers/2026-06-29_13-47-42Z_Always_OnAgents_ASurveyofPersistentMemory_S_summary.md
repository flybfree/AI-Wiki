title: "Summary: 2026-06-29_13-47-42Z_Always_OnAgents_ASurveyofPersistentMemory_State_an.md"
# Summary: 2026-06-29_13-47-42Z_Always_OnAgents_ASurveyofPersistentMemory_State_an.md
Saved: 2026-06-29 22:01
Source: 2026-06-29_13-47-42Z_Always_OnAgents_ASurveyofPersistentMemory_State_an.md
Model: None

---


## Summary  
This paper surveys the emerging field of always‑on agents—systems that retain durable state across interactions and whose future behavior depends on accumulated memories, ledgers, permissions, and audit trails. The authors frame these agents as persistent‑state systems and introduce a six‑axis diagnostic framework to evaluate memory, authority, scope, mutability, provenance, recoverability, and actionability. By analyzing 435 works coded as a scoped map rather than an exhaustive census, they highlight that literature emphasizes state accumulation and retrieval over governance mechanisms. Their contribution is the Always‑On Evaluation Protocol (AOEP‑v0), which quantifies state mutation and recovery obligations rather than solely answer quality.

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Persistent agents are modeled as persistent‑state systems encompassing memories, task ledgers, credentials, commitments, provenance, shared state, trigger conditions, and externally committed effects.  
- [Finding 2] The literature is organized through six diagnostic axes (authority, scope, mutability, provenance, recoverability, actionability) to systematically assess each state item.  
- [Finding 3] AOEP‑v0 provides a concrete governance scoring mechanism that evaluates state mutation and recovery obligations as primary evaluation criteria.

## Methodology  
The authors conducted a literature survey of 435 works, coding each entry against the six diagnostic axes and a lifecycle of state handling (write → validate → organize → retrieve → act upon → update → forget → audit → roll back). This approach allowed them to map the current research landscape as a “scoped map” rather than an exhaustive census. They then designed AOEP‑v0 as a pilot evaluation contract that operationalizes governance requirements by scoring state mutation and recovery obligations.

## Results  
The survey reveals that most works focus on accumulating and retrieving state, with only a minority addressing governing, recovering, or relinquishing it. The AOEP‑v0 protocol demonstrates that explicit scoring of state mutation and recovery can make governance concrete, linking agents to databases, distributed systems, formal methods, capability security, and machine unlearning.

## Significance  
This work bridges the gap between persistent memory and governance in LLMAgents, offering a practical evaluation framework that ensures agents maintain integrity across interactions. By connecting these concepts to broader system architectures, it advances research on secure, accountable, and reusable AI systems.

## Related Concepts  
Persistent memory, state, governance, LLMAgents, AOEP‑v0, capability security, machine unlearning, distributed systems, formal methods, audit trails, provenance, shared state.
