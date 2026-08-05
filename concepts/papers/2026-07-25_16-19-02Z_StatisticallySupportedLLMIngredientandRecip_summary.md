# Summary: 2026-07-25_16-19-02Z_StatisticallySupportedLLMIngredientandRecipeDataCo.md
Saved: 2026-07-27 20:13
Source: 2026-07-25_16-19-02Z_StatisticallySupportedLLMIngredientandRecipeDataCo.md
Model: None

---

## Summary  
The paper proposes a quality‑controlled LLM pipeline to collect ingredient data for computational nutrition, addressing the problem of incomplete and inconsistent databases that are built only for human reference. It combines statistical estimation, domain‑specific invariant checks, and a web‑fetch fallback to produce reliable nutrient records while quantifying uncertainty rather than discarding it. A Heap’s Law analysis shows that unique‑ingredient growth is sub‑linear and front‑loaded as recipes scale up. The framework treats repeated LLM queries as samples from an answer distribution and uses robust point estimators with normalized confidence scores.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 13 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- Statistical estimation of ingredient attributes using multiple LLM invocations treated as samples from a model‑induced answer distribution, yielding normalized confidence scores across numerical, Boolean, multiple‑choice, open categorical, and optional integer types.  
- An invariant guard layer that enforces nutritional and logical self‑consistency within each ingredient record; minor numeric inconsistencies are reconciled with a linear program minimizing worst‑case percentage deviation while preserving semantic zeros, and major violations trigger web‑evidence repair before human review.  
- A Heap’s Law fit to 233 recipes reveals sub‑linear growth of unique ingredients: the projected ratio drops from 1.74 at 100 recipes to 0.19 at 5 000, informing database scaling and resource planning.

## Methodology  
The authors built a pipeline that (1) issues repeated LLM queries for each ingredient attribute to generate an answer distribution; (2) applies robust point estimators with normalized confidence scores appropriate to the data type; (3) enforces invariants via a guard layer that checks nutritional and logical consistency; (4) resolves minor numeric discrepancies using linear programming to minimise worst‑case percentage deviation while keeping zeros intact; (5) escalates major violations to web‑evidence grounding, with human review as the final fallback. The pipeline is designed to be an API service costing roughly $1 per ingredient.

## Results  
On a curated 30‑ingredient reference set, the pipeline achieves 98.4 % exact match on nutrient flags and reduces median absolute percentage error from 31.9 % for the median‑aggregated baseline to 10.1 %, a reduction of 21.8 percentage points, at an estimated API cost of about $1 per ingredient.

## Significance  
By operationalising uncertainty rather than discarding it, this work provides a scalable, auditable method for building nutrition databases that can be integrated into computational models with transparent error handling and confidence quantification.

## Related Concepts  
LLM prompting, statistical inference, data engineering, invariant checking, linear programming, Heap’s Law, nutritional databases, uncertainty quantification.
