# Summary: 2026-07-31_13-42-51Z_AgenticRepair_Multi_FacetedProgramContextEngineeri.md
Saved: 2026-08-03 10:14
Source: 2026-07-31_13-42-51Z_AgenticRepair_Multi_FacetedProgramContextEngineeri.md
Model: None

---

## Summary
Automated vulnerability repair seeks to minimize the manual effort required by security engineers to patch critical security flaws identified in triage reports. While recent agentic AI models have demonstrated success in general program repair, they often fail to capture the rich, specialized context necessary for secure code modification. This paper introduces AgenticRepair, a novel framework that addresses this limitation by engineering three distinct facets of program context: code structure, runtime execution, and commit history. By orchestrating specialized Large Language Model (LLM) subagents to gather and embed this information, AgenticRepair significantly outperforms existing baselines in patching real-world vulnerabilities.

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 4 title terms overlap; 29 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 6 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 6 summary/topic terms overlap

## Key Contributions
- The identification of three critical gaps in current agentic vulnerability repair approaches: the lack of code-structure context for cross-file data flows, insufficient runtime-execution context for crash semantics, and missing commit-history context for understanding fragile code patterns.
- The development of AgenticRepair, a multi-agent framework that engineers these specific contexts and integrates them into the memory of a dedicated repair subagent to synthesize precise, context-conditioned patches.
- Empirical validation on the SEC-Bench dataset demonstrating that the three identified context facets are mutually complementary and that both multi-agent scaffolding and base-model capacity are essential for achieving high success rates in vulnerability repair.

## Methodology
The authors approached the problem by first analyzing the workflow of security engineers to identify necessary contextual information that automated tools typically miss. They defined three specific context dimensions: code-structure context, which captures cross-file data flows and memory operation patterns; runtime-execution context, which reveals crash semantics and memory origins through sanitizer-based analysis; and commit-history context, which recovers the historical introduction of fragile code patterns. AgenticRepair orchestrates three specialized LLM subagents to autonomously engineer these contexts. These engineered contexts are then embedded into the working memory of a dedicated repair subagent, which uses this enriched information to generate and verify patches. The framework employs sanitizer-based patch verification to ensure the correctness and security of the generated solutions.

## Results
Evaluated on SEC-Bench, a dataset comprising 300 real-world vulnerability instances, AgenticRepair achieved a 73% success rate in repairing vulnerabilities. This performance substantially outperforms the strongest existing baseline by 29 percentage points. The authors conducted an ablation study which confirmed that removing any of the three context facets (code-structure, runtime-execution, or commit-history) significantly degraded performance, proving their mutual complementarity. Furthermore, the results highlighted that both the multi-agent scaffolding architecture and the capacity of the base LLM are critical components for the framework's effectiveness.

## Significance
This research establishes multi-faceted program context engineering as a vital design direction for future agentic vulnerability repair systems. By demonstrating that richer, engineer-simulated context leads to superior patching outcomes, it provides a roadmap for closing the gap between automated tools and professional security practices. The significant performance gain over baselines suggests that current LLMs require explicit structural and historical guidance to handle complex security flaws effectively.

## Related Concepts
- Agentic AI
- Automated Program Repair (APR)
- Vulnerability Triage and Patching
- Large Language Models (LLMs) in Software Engineering
- Multi-Agent Systems
- SEC-Bench Dataset
- Sanitizer-Based Verification
- Context-Aware Code Generation
