# Summary: 2026-07-24_23-20-59Z_BuildingAIThatWorks_ESnet_sPragmaticApproachtoAI_D.md
Saved: 2026-07-27 23:29
Source: 2026-07-24_23-20-59Z_BuildingAIThatWorks_ESnet_sPragmaticApproachtoAI_D.md
Model: None

---

## Summary  
The paper presents ORBIT, an agentic AI system integrated into ServiceNow to automate routine Network Operations Center (NOC) tasks and deliver actionable insights, addressing persistent pain points such as slow retrieval from siloed data sources, lengthy and hard‑to‑parse incident tickets, and context loss across shift handoffs. It introduces a modular skill‑based architecture that enables reliable, bounded AI execution within the operators’ existing tooling, thereby reducing cognitive load and shortening resolution times.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- The ORBIT project successfully automated six initial operational tasks, demonstrating feasibility of agentic AI in NOC workflows and showing measurable gains in efficiency.  
- A layered modular architecture with versioned “skills” improves reliability and predictability compared to fully unconstrained agents, providing a structured way to manage stochasticity.  
- Rapid organic adoption of components such as the chat interface and LiteLLM model gateway indicates that the solution scales beyond the pilot and can be reused by other teams.

## Methodology  
The authors designed ORBIT as a centralized reasoning hub that accesses ESnet data via Multi‑Channel Pipes (MCPs), employs a semantic search layer to locate relevant information, and presents synthesized results through an operator‑facing chat interface. Skill development follows industry best practices: each bounded responsibility is defined as a testable, versioned function that guides the system’s behavior without unrestricted autonomy.

## Results  
All six initial tasks were completed with high success rates, and two additional tasks proposed by NOC engineers were also delivered on schedule. Experiments with the skill framework show a reduction in the number of steps required to resolve incidents and an elimination of previously observed error modes, indicating both speed improvements and higher reliability.

## Significance  
By embedding agentic AI directly into ServiceNow, ORBIT offers a pragmatic pathway to operational excellence for large‑scale networks: it lowers human workload, accelerates incident resolution, and scales across shifts without requiring extensive re‑engineering of legacy systems. The approach validates that modular, skill‑based AI can be safely integrated into existing infrastructure.

## Related Concepts  
Agentic AI, modular skill architecture, semantic search, service integration (ServiceNow), cross‑source synthesis, shift handoff context management, operational excellence, bounded autonomy, LiteLLM model gateway, MCPs.
