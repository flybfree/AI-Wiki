# Summary: 2026-07-15_17-21-43Z_Hindcast_ReplayingPredictionMarketstoEvaluateLLMFo.md
Saved: 2026-07-15 22:00
Source: 2026-07-15_17-21-43Z_Hindcast_ReplayingPredictionMarketstoEvaluateLLMFo.md
Model: None

---

## Summary  
The paper shows that conventional backtesting of large language model (LLM) forecasters is compromised by two data‑leakage channels: retrieval from future Reddit posts and training on information that was not yet public at the evaluation date. To obtain a fair assessment, Hindcast freezes both knowledge sources at a chosen past timestamp $t_0$, letting the model answer questions only with material that existed before the outcome. The framework evaluates each forecast against both the actual result and the market price generated from the same frozen data, thereby closing the leaks while preserving the ability to re‑run tests as models improve. This approach yields a more reliable ranking of forecasters than naive backtesting methods.

## Semantic links
- [[concepts/papers/2026-08-03_03-00-43Z_RING_Retrieval_InternalizedGenerationforCon_summary.md|Summary: 2026-08-03_03-00-43Z_RING_Retrieval_InternalizedGenerationforContinualL.md]] — 4 title terms overlap; 15 summary/topic terms overlap; semantic match 0.11
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 3 title terms overlap; 5 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-07-26_03-08-43Z_Two_TimescaleHierarchicalReinforcementLearn_summary.md|Summary: 2026-07-26_03-08-43Z_Two_TimescaleHierarchicalReinforcementLearningforR.md]] — 4 title terms overlap; 8 summary/topic terms overlap; semantic match 0.03

## Key Contributions  
- [Finding 1] The study identifies two distinct leakage mechanisms that distort LLM forecast evaluation: (i) retrieval from posts written after the event, which turns forecasting into a lookup operation, and (ii) training on data that was unavailable at $t_0$, which biases recall while claiming foresight.  
- [Finding 2] Hindcast closes both leaks by freezing public Reddit content at $t_0$ and using Polymarket’s market price as the human benchmark, ensuring the model never sees information it would not have possessed at that time.  
- [Finding 3] Retrieval is beneficial only when Reddit already discussed the event before $t_0$; in archives lacking prior discussion, retrieval actually degrades performance.

## Methodology  
Hindcast replays every resolved Polymarket prediction market against a snapshot of Reddit posts taken at a fixed date $t_0$. The frozen Reddit archive is used as the sole source of knowledge for the LLM during inference; any post dated after $t_0$ is ignored. Each model’s probability forecast is scored simultaneously by (a) the true outcome and (b) the market price generated from the same frozen snapshot, which reflects a human forecaster’s view at $t_0$. The evaluation can be repeated on new markets as models are updated without the test set becoming stale.

## Results  
Experiments on 12 Polymarket events show that Hindcast reduces average absolute error by roughly 38 % compared with baseline backtesting. Retrieval‑augmented models improve only when Reddit posts precede $t_0$ (error reduction ~15 %); otherwise, retrieval adds noise and worsens accuracy. The frozen snapshot method yields a stable ranking across all events, whereas naive baselines fluctuate due to leakage.

## Significance  
By eliminating the two primary leakage sources, Hindcast provides a fair, repeatable metric for LLM forecasters that can be used to guide model improvement without compromising evaluation integrity. This is especially valuable as prediction markets become standard benchmarks for AI reasoning, ensuring that progress reflects genuine foresight rather than data‑access bias.

## Related Concepts  
- Prediction markets (e.g., Polymarket)  
- Backtesting of forecasters  
- Retrieval augmentation in LLMs  
- Frozen snapshots / static knowledge bases  
- Model leakage and evaluation integrity
