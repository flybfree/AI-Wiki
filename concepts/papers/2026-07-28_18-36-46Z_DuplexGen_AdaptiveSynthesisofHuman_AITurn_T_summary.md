# Summary: 2026-07-28_18-36-46Z_DuplexGen_AdaptiveSynthesisofHuman_AITurn_TakingDi.md
Saved: 2026-07-29 22:11
Source: 2026-07-28_18-36-46Z_DuplexGen_AdaptiveSynthesisofHuman_AITurn_TakingDi.md
Model: None

---

## Summary  
The paper addresses the limitation of current dialogue models that apply uniform turn‑taking norms regardless of scenario, and introduces DuplexGen which adapts turn‑taking to human preferences via calibration against slot‑level annotations. It demonstrates that human‑calibrated generation yields more natural, scenario‑specific turn‑taking than prompting or generic training on human‑human corpora. This work shows that explicit preference calibration—not just data scale or prompt design—enables adaptive full‑duplex dialogue.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- Human‑preference calibration of LLM‑generated dialogues improves alignment with real‑world turn‑taking norms.  
- DuplexGen generates scenario‑adaptive turn‑taking by calibrating predictions against slot‑level annotations rather than relying on generic human‑human corpora.  
- A model trained on DuplexGen data exhibits human‑preferred, context‑sensitive turn‑taking behaviors.

## Methodology  
The authors collect six cooperative and competitive tasks where human turn‑taking preferences vary systematically. For each task they annotate slots with preference labels indicating which participant should speak next. Using these slot‑level annotations, they fine‑tune a large language model to predict the appropriate speaker for each slot. The calibrated model is then employed to generate dialogues that respect the annotated preferences, creating a synthetic dataset that can be used to further train full‑duplex models.

## Results  
Experiments show DuplexGen’s generated dialogues align significantly more closely with human turn‑taking preferences than uncalibrated prompting or generic training. When a full‑duplex model is trained on these synthetic data, its turn‑taking behavior matches human norms across all tasks, indicating successful adaptation to the specific scenarios.

## Significance  
This work proves that incorporating explicit human preference signals into dialogue synthesis yields scenario‑specific, naturalistic interactions, highlighting the importance of calibration over sheer dataset size or prompt engineering. It opens a path for building truly adaptive conversational agents that respect real‑world interaction norms.

## Related Concepts  
- Turn‑taking norms  
- Full‑duplex interaction  
- Large language model fine‑tuning  
- Slot‑level annotation  
- Human preference calibration  
- Cooperative/competitive dialogue tasks
