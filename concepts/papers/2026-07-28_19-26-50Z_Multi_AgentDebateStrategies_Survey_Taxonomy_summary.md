# Summary: 2026-07-28_19-26-50Z_Multi_AgentDebateStrategies_Survey_Taxonomy_andCha.md
Saved: 2026-07-29 21:29
Source: 2026-07-28_19-26-50Z_Multi_AgentDebateStrategies_Survey_Taxonomy_andCha.md
Model: None

---

## Summary  
This paper conducts a systematic literature review of 141 primary studies on Multi‑Agent Debate (MAD) to address the fragmented state of research in improving LLM‑based agentic systems through structured argument exchange. The authors introduce a three‑dimensional taxonomy that formalizes debate participants, interaction mechanisms, and agreement protocols, providing notation for MAD configurations and highlighting the prevalence of static, fully connected topologies with verbatim exchange and voting resolution. By exposing this narrow design pattern and its implications for cross‑study comparison, the work aims to serve as a descriptive map, benchmarking framework, and potential schema for machine‑readable MAD specifications.

## Semantic links
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 5 title terms overlap; 2 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-20_12-38-50Z_AClassifierThatTeachesItself_Self_Improving_summary.md|Summary: 2026-07-20_12-38-50Z_AClassifierThatTeachesItself_Self_Improving_Frozen.md]] — 4 title terms overlap; 9 summary/topic terms overlap; semantic match 0.04
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 4 title terms overlap; 8 summary/topic terms overlap; semantic match 0.02

## Key Contributions  
- [Finding 1] The taxonomy isolates three core dimensions—participants, interaction mechanisms, agreement protocols—to systematically characterize MAD studies.  
- [Finding 2] Empirical analysis shows that static fully connected topologies with verbatim exchange and short‑term memory voting dominate the literature, rendering cross‑study comparisons unreliable when these choices are implicit.  
- [Finding 3] The framework enables a machine‑readable specification of MAD configurations, facilitating cost‑aware benchmarking and automated tuning.

## Methodology  
The authors performed a comprehensive survey of primary research articles indexed in arXiv up to July 2026, selecting 141 papers that explicitly describe an MAD system. They extracted metadata on debate participants (e.g., number, roles), interaction mechanisms (topology, message format), and agreement protocols (resolution rule). Using a three‑dimensional taxonomy, they encoded each study as a tuple (participants, mechanism, protocol) with formal notation, then aggregated findings to identify common patterns.

## Results  
Statistical clustering revealed that 87 % of studies adopt static fully connected topologies where agents exchange verbatim arguments and resolve via majority voting. Alternative designs—dynamic graphs, paraphrased exchanges, or long‑term memory—account for only 13 % and are rarely compared across papers. The taxonomy thus maps the research landscape onto a narrow design pattern, suggesting that future work should formalize these configurations to enable rigorous benchmarking.

## Significance  
By exposing the implicit assumptions of existing MAD studies, this framework improves reproducibility and allows developers to evaluate trade‑offs between engagement depth, computational cost, and resolution accuracy. A machine‑readable specification can automate configuration generation, supporting scalable experiments that align with specific performance goals.

## Related Concepts  
Multi‑Agent Debate (MAD), Large Language Model agentic systems, debate participants, interaction mechanisms, agreement protocols, static fully connected topologies, verbatim exchange, short‑term memory, voting resolution.
