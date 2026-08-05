# Summary: 2026-07-16_17-49-28Z_teLLMeWhy_Ain_tNothingbutaJam__ExploratoryCausalAn.md
Saved: 2026-07-23 23:47
Source: 2026-07-16_17-49-28Z_teLLMeWhy_Ain_tNothingbutaJam__ExploratoryCausalAn.md
Model: None

---

## Summary  
The paper introduces **teLLMe**, an exploratory causal analysis system for urban driving data derived from dashcam annotations, enabling users to ask natural‑language questions about how treatments (e.g., rain) affect outcomes such as traffic density while accounting for subpopulations and uncertainty. It combines causal structure learning, the PC algorithm, bootstrap stability checks, linear regression, DoWhy effect estimation, and a schema‑aware LLM that maps queries into structured causal models, producing Causal Cards that summarize effect estimates, adjustment sets, DAG support, and assumptions.

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 4 title terms overlap; 29 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 11 summary/topic terms overlap

## Key Contributions  
- **teLLMe provides a unified pipeline from raw dashcam video events to interpretable causal answers for urban traffic.**  
- The system explicitly surfaces plausible relationships (e.g., weather, peak hours) while quantifying uncertainty through bootstrap stability checks.  
- It translates natural‑language queries into structured causal models using a schema‑aware LLM and returns Causal Cards with effect estimates, adjustment sets, DAG support, and assumptions.

## Methodology  
The authors built teLLMe by first extracting a structured event table from dashcam annotations, then applying the PC algorithm to infer a causal structure. Bootstrap resampling is used for stability checks on estimated effects. Linear regression and DoWhy are employed to compute query‑specific effect estimates. A schema‑aware LLM maps each natural‑language question into a treatment‑outcome‑subpopulation specification that feeds the causal model.

## Results  
In case studies on BDD‑derived traffic events, teLLMe identified that rain reduces peak‑hour density with moderate confidence and detected interactions between time of day and weather. The Causal Cards highlighted adjustment sets such as vehicle type and noted assumptions like linearity and independence, making uncertainty explicit for each estimate.

## Significance  
By making causal inference transparent and hypothesis‑generating rather than definitive, teLLMe supports traffic agencies in planning interventions without overstating certainty, aligning with the need for exploratory analysis of observational data where interventions are absent.

## Related Concepts  
Causal structure learning, PC algorithm, bootstrap stability checks, DoWhy framework, DAG (Directed Acyclic Graph), schema‑aware LLM, natural‑language query translation, Causal Card output, linear regression, observational urban driving data.
