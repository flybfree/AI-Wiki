# Summary: 2026-07-28_18-50-39Z_Position_EvaluationScoresArePerishableKnowledgeCla.md
Saved: 2026-07-29 21:29
Source: 2026-07-28_18-50-39Z_Position_EvaluationScoresArePerishableKnowledgeCla.md
Model: None

---

## Summary  
The paper argues that evaluation scores from language models are perishable knowledge claims and should not be aggregated blindly, leading to trust inflation. It proposes treating scores as epistemic statements with formality, scope, and validity windows, and suggests adding metadata to convey this status. The authors demonstrate via the HELM leaderboard that mean aggregation inflates rankings while weakest‑link yields a more reliable ordering. They also introduce a framework for explicit score metadata. By framing scores as claims with measurable uncertainty, the work encourages systematic handling of their temporal decay.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 3 title terms overlap; 29 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- Finding 1: Evaluation scores exhibit trust inflation when averaged across heterogeneous signals.  
- Finding 2: Scores should be annotated with formality tier, scope declaration, and expiration date to reflect their epistemic reliability.  
- Finding 3: Weakest‑link aggregation yields a more conservative and accurate ranking than mean aggregation.

## Methodology  
The authors analyze the composition of evaluation signals (automated metrics, LLM judgments, human scores) and benchmark results. They model these as epistemic claims governed by three properties—formality, scope, validity window—and derive that weakest‑link is the conservative endpoint of a parameterized operator family controlled by pessimism. Their experimental harness for agentic AI collects metadata and evaluates it on HELM. This analytical approach links philosophical logic to practical evaluation design.

## Results  
Across 54 frontier models on ten scenarios, mean scores rank top models differently from those ranked by weakest‑link; the two rankings are completely disjoint. The metadata‑annotated approach improves interpretability without changing raw scores. Additionally, the study quantifies trust inflation as a 30 % average increase in confidence when using mean aggregation.

## Significance  
This work highlights a systemic flaw in current evaluation practices and offers a practical solution to make score reliability transparent, which is crucial for trustworthy AI deployment. It also suggests that future research should adopt perishable‑knowledge principles to avoid overconfidence in static metrics.

## Related Concepts  
- Trust inflation  
- Weakest‑link aggregation  
- Formality tier  
- Scope declaration  
- Validity window (expiration date)  
- HELM leaderboard
