# Summary: 2026-07-29_08-34-29Z_FewerClarifications_BetterCode_BenchmarkingCross_S.md
Saved: 2026-07-29 20:30
Source: 2026-07-29_08-34-29Z_FewerClarifications_BetterCode_BenchmarkingCross_S.md
Model: None

---

## Summary  
The paper tackles the recurring problem that AI‑assisted coding assistants frequently require users to provide clarification for ambiguous requests, even when the same ambiguity appears across multiple sessions. It proposes a new task called *personalized ambiguity adaptation*, where an assistant should recognize a previously resolved ambiguity pattern from the user’s history and generate the correct executable code without asking additional questions. To study this problem, the authors introduce CAPA, a benchmark that injects six distinct mechanisms of personalized coding ambiguity into unambiguous tasks using a controlled three‑stage generation pipeline.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Personalized ambiguity adaptation is a distinct task that benefits from remembering how users resolved ambiguities in earlier sessions.  
- [Finding 2] CAPA provides a systematic benchmark with 600 coding sessions across 60 balanced user‑ambiguity cells, quantifying six mechanisms of recurring ambiguity.  
- [Finding 3] A lightweight “same‑user history gating” mechanism improves first‑turn success and reduces the number of clarification turns compared to baselines that ignore session history.

## Methodology  
The authors construct CAPA by creating a controlled three‑stage generation pipeline: (1) generate an unambiguous executable task, (2) inject one of six personalized ambiguity mechanisms into the prompt, and (3) produce a coding assistant response. This yields 600 sessions distributed across 60 user–ambiguity cells, with 300 held out for evaluation. To assess model performance, they evaluate twelve recent large language models under two conditions: (a) no‑history (ignoring previous sessions) and (b) same‑user history (using resolved session data). Success is measured by three executable metrics: overall task success, first‑turn success (correct code on the initial turn), and turns‑to‑completion (how many assistant turns are needed to finish).

## Results  
Experiments show that models employing same‑user history gating achieve a ~12 % higher first‑turn success rate and reduce average clarification turns from 3.4 to 2.1 compared with the no‑history baseline. The benefit scales with task difficulty: high‑difficulty tasks see larger gains, while low‑difficulty tasks show modest improvement. User identity also matters; users who have resolved many ambiguities in prior sessions benefit more than those with sparse history.

## Significance  
These findings demonstrate that long‑term coding assistants can align generated code more closely to user intent by leveraging session memory, thereby minimizing repetitive clarification requests and improving productivity. The CAPA benchmark offers a reusable framework for evaluating personalized ambiguity adaptation across diverse LLMs.

## Related Concepts  
- Cross‑session personalization  
- Ambiguity adaptation in AI coding assistants  
- LLM evaluation with executable success metrics (overall success, first‑turn success, turns‑to‑completion)  
- Gating mechanisms for memory use at inference time
