# Summary: 2026-07-28_06-43-39Z_Cardiologent_Multi_AgentClinicalDecisionSupportfor.md
Saved: 2026-07-28 22:33
Source: 2026-07-28_06-43-39Z_Cardiologent_Multi_AgentClinicalDecisionSupportfor.md
Model: None

---

## Summary  
The paper introduces **Cardiologent**, a multi‑agent clinical decision support system that moves beyond single‑record arrhythmia detection to produce patient‑level assessments of urgency and management. It integrates ECG leads and photoplethysmogram (PPG) signals into a unified rhythm profile, then reasons against evidence‑based cardiology guidelines using an audit‑trail critic agent. Each conclusion is traceable to a specific guideline, enabling clinicians to evaluate rather than blindly act on AI output. The system is evaluated across diagnostic accuracy, clinical significance, and urgency scoring.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 10 summary/topic terms overlap

## Key Contributions  
- [Finding 1] A multi‑agent architecture that spans detection through decision across both ECG leads and PPG signals.  
- [Finding 2] Integration of a patient‑level rhythm profile with retrieved clinical guidelines, validated by a critic agent that checks each conclusion against the guideline it cites.  
- [Finding 3] Superior performance on all three evaluation axes—diagnostic accuracy, clinical significance, and urgency scoring—matching inter‑rater agreement.

## Methodology  
The authors designed three agents: (1) Signal agents compute quantitative features from individual ECG leads and PPG recordings; (2) an Assembly agent merges these signals into a patient rhythm profile; (3) a Decision agent reasons about the profile using retrieved clinical guidelines, while a Critic agent audits each recommendation for guideline compliance. Training leverages annotated cardiology cases with human‑in‑the‑loop feedback to refine the agents.

## Results  
Across 150 patient‑level arrhythmia episodes, Cardiologent achieved an intraclass correlation coefficient (ICC) of 0.74 against expert cardiologists and 0.66 versus a large language model judge, matching the inter‑rater ICC of 0.67 between cardiologists themselves. It outperformed single‑agent LLMs by +23 % in diagnostic accuracy, +18 % in clinical significance, and +31 % in urgency scoring. Each recommendation is accompanied by a citation to a specific guideline.

## Significance  
By delivering auditable, patient‑level decisions that are directly linked to evidence‑based guidelines, Cardiologent reduces reliance on blind alerts and supports continuous monitoring. Its multi‑agent design enables scalability across diverse data sources, fostering trust in AI‑driven arrhythmia management for both routine care and real‑time interventions.

## Related Concepts  
- Multi‑agent reinforcement learning  
- Clinical guideline integration  
- Patient‑level decision support (PLDS)  
- Large language model evaluation (ICC)
