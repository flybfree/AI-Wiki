# Summary: 2026-08-02_16-59-29Z_WhenMayaModelReplacetheExperiment_Audits_Licenses_.md
Saved: 2026-08-04 00:17
Source: 2026-08-02_16-59-29Z_WhenMayaModelReplacetheExperiment_Audits_Licenses_.md
Model: None

---

## Summary  
The paper investigates when machine‑learning surrogates can safely replace costly experiments in design optimization across chemistry and materials science. It shows that surrogate predictions alone cannot certify quality because they may produce misleading rankings, yet a rigorous audit framework can substitute evaluations at a quantified cost. The authors derive theoretical bounds on the “selection tax” and prove when audits are optimal. Their work provides a decision rule for when models may act as oracles without compromising safety.  

## Semantic links
- [[concepts/training-optimization/training-optimization-hub.md|Training and Optimization Hub]] — 2 title terms overlap; 505 backlinks; 4 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 4 title terms overlap; 7 summary/topic terms overlap; semantic match 0.02
- [[concepts/ai-foundations/ai-ml-foundations-lesson-01-ai-machine-learning-and-deep-learning.md|AI/ML Foundations Lesson 01 - AI, Machine Learning, and Deep Learning]] — 3 title terms overlap; 5 backlinks; 4 summary/topic terms overlap

## Key Contributions  
- Finding 1: Surrogate predictions cannot be trusted to certify quality; any certification must rest on true experiments, leading to a selection‑tax bound.  
- Finding 2: Trust can be purchased via optimal query‑complexity audits that preserve rank over accuracy and reduce oracle cost by up to 25%.  
- Finding 3: A dichotomy exists between audit‑driven surrogate use and full model replacement; the latter is safe only when predictions are validated against experiments.  

## Methodology  
The authors conduct a mathematical analysis on three exhaustively ground‑truthed design tasks, comparing surrogate‑only screening with audited surrogate evaluation. They derive upper and lower bounds for the over‑prediction of selected candidates (selection tax) and formulate an architectural rule: predictions may propose and train freely, but certified conclusions require true evaluations.  

## Results  
Across 432 surrogate fits under six task regimes, the audit statistic correlates with deployed search performance at Spearman rank correlation 0.80–0.99, while R²‑based regret correlation drops to as low as 0.33. Audited screening cuts certified oracle cost by a factor of 25 compared with un‑audited use.  

## Significance  
This work clarifies the trade‑offs between trust in surrogate models and experimental validation, offering a principled cost model for when audits are justified. It helps researchers avoid deterministic self‑confirmation failures and reduces expensive evaluation budgets without sacrificing design quality.  

## Related Concepts  
- Surrogate modeling  
- Experimental audit  
- Selection tax  
- Oracle vs. experiment  
- Spearman rank correlation  
- Query complexity optimization
