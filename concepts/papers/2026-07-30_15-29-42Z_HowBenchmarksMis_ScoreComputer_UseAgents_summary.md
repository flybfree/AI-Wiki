# Summary: 2026-07-30_15-29-42Z_HowBenchmarksMis_ScoreComputer_UseAgents.md
Saved: 2026-07-30 22:16
Source: 2026-07-30_15-29-42Z_HowBenchmarksMis_ScoreComputer_UseAgents.md
Model: None

---

## Summary  
The paper argues that current benchmarks for computer‑use agents (CUAs) generate unreliable scores because the evaluation pipelines are brittle, often relying on scripted oracles and ignoring visual evidence. By auditing 150 public failure‑scored trajectories from five benchmark suites—web browsing, enterprise workflows, and desktop control—the authors reveal systematic errors that inflate false failures and underestimate genuine ones. Their work introduces a reliability framework that separates task construction, trajectory observation, scoring, and reporting, and proposes stage‑specific design rules to improve evaluation.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 3 title terms overlap; 29 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 10 summary/topic terms overlap

## Key Contributions  
- 15.3 % of FAIL verdicts are wrong: 10.7 % are evaluator false negatives and 4.7 % stem from broken tasks.  
- A three‑tier diagnostic taxonomy shows that verification/feedback and planning failures dominate execution/grounding errors, while execution/grounding errors are less frequent.  
- A single scalar success rate cannot explain the tiered nature of failures; stage‑specific evaluation rules are required.

## Methodology  
The authors organized the problem into a reliability framework covering four stages: task construction (defining what the agent must achieve), trajectory observation (capturing visual and interactive evidence), scoring (applying verdicts), and reporting (aggregating results). They collected 150 public failure‑scored trajectories from five benchmarks, applied the taxonomy to each trajectory, and quantified false negatives versus broken tasks. The analysis was performed by programmatically parsing the trajectories and classifying them according to the diagnostic tiers.

## Results  
The audit shows that 15.3 % of FAIL verdicts are incorrect: 10.7 % are evaluator false negatives (the agent succeeded but was marked as failed) and 4.7 % arise from broken or undefined tasks. When failures are genuine, the taxonomy reveals that verification/feedback errors account for roughly half of all failure cases, followed by planning failures; execution/grounding errors constitute a smaller share. A single success rate fails to capture this tiered distribution, underscoring the need for multi‑dimensional evaluation.

## Significance  
These findings demonstrate that current benchmark scores misrepresent CUA performance, potentially leading to overestimation of agent capabilities and misguided deployment decisions. By exposing the sources of false failures and proposing a more nuanced diagnostic taxonomy, the paper calls for a shift toward reliable, stage‑specific evaluation methods in AI research.

## Related Concepts  
Computer-use agents, benchmark reliability, failure taxonomy, verification feedback, planning, execution/grounding errors, scalar success rate, stage-specific design rules.
