# Summary: 2026-07-31_13-42-51Z_AgenticRepair_Multi_FacetedProgramContextEngineeri.md
Saved: 2026-08-03 10:18
Source: 2026-07-31_13-42-51Z_AgenticRepair_Multi_FacetedProgramContextEngineeri.md
Model: None

---

## Summary
Automated vulnerability repair seeks to minimize the manual effort required by security engineers to patch critical security flaws, yet existing agentic AI approaches often fail due to insufficient program context. This paper introduces AgenticRepair, a novel framework that addresses this limitation by engineering three specific types of program context: code-structure, runtime-execution, and commit-history. By orchestrating specialized Large Language Model (LLM) subagents to gather and embed this rich contextual data into the memory of a dedicated repair agent, the system enables more accurate and robust patch synthesis. The authors demonstrate that this multi-faceted approach significantly outperforms current baselines in repairing real-world vulnerabilities.

## Key Contributions
- **Identification of Context Gaps**: The authors identify three critical deficiencies in existing agentic vulnerability repair systems: the lack of code-structure context for cross-file data flows, the absence of runtime-execution context for crash semantics, and the missing commit-history context for understanding fragile code patterns.
- **AgenticRepair Framework**: They propose AgenticRepair, a multi-agent architecture that uses specialized LLM subagents to engineer these specific contexts, which are then utilized by a repair subagent to condition patch generation effectively.
- **Empirical Validation of Complementarity**: Through extensive evaluation and ablation studies, the paper confirms that the three context facets are mutually complementary and that both the multi-agent scaffolding and base-model capacity are essential for achieving high success rates in vulnerability repair.

## Methodology
The authors developed AgenticRepair to overcome the limitations of general bug repair by focusing on the specific needs of security triage reports. The framework operates by orchestrating three specialized LLM subagents, each tasked with engineering a distinct facet of program context. First, the code-structure agent analyzes cross-file data flows and memory operation patterns. Second, the runtime-execution agent captures crash semantics and memory origins through execution traces. Third, the commit-history agent investigates how fragile code patterns were introduced over time. These engineered contexts are then embedded into the working memory of a dedicated repair subagent, which synthesizes patches conditioned on this comprehensive information. The system was evaluated on SEC-Bench, a dataset containing 300 real-world vulnerability instances, using sanitizer-based verification to ensure patch correctness.

## Results
AgenticRepair achieved a remarkable 73% success rate in repairing vulnerabilities on the SEC-Bench dataset. This performance substantially outperforms the strongest existing baseline by a margin of 29%, demonstrating the efficacy of multi-faceted context engineering. The ablation study further revealed that removing any single context facet significantly degraded performance, confirming their mutual complementarity. Additionally, the results highlighted that the combination of sophisticated multi-agent scaffolding and high-capacity base models is crucial for maximizing repair accuracy.

## Significance
This research establishes multi-faceted program context engineering as a vital design direction for future agentic vulnerability repair systems. By demonstrating that richer, security-specific context leads to dramatically improved patching outcomes, the work provides a practical pathway for reducing the burden on security engineers and enhancing software security posture through automation.

## Related Concepts
- Agentic AI
- Automated Program Repair (APR)
- Vulnerability Triage
- Large Language Models (LLMs)
- Multi-Agent Systems
- Context Engineering
- SEC-Bench
- Sanitizer-based Verification
