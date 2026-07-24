# Summary: 2026-07-20_23-11-18Z_WhenDoesMachineLearningBeatValueSorting_AThree_Dat.md
Saved: 2026-07-24 00:28
Source: 2026-07-20_23-11-18Z_WhenDoesMachineLearningBeatValueSorting_AThree_Dat.md
Model: None

---

## Summary  
The paper investigates whether machine‑learning (ML) can outperform a simple value‑based sorting rule for prioritizing shipments when managers have limited review capacity. It introduces a diagnostic framework that compares ML predictions against the baseline of selecting highest‑value shipments first across three real supply‑chain datasets. The study evaluates this competition using leakage‑controlled rolling‑origin evaluation and paired bootstrap confidence intervals, and it reports whether ML beats the no‑model benchmark.  

## Key Contributions  
- [Finding 1] Ranking by predicted delay severity multiplied by known value (M1) consistently outperforms severity‑only ranking but does not generally surpass pure value sorting across all three domains.  
- [Finding 2] The performance gap is quantified via percentage point differences at a 10 % review budget; M1 minus VALUE_ONLY yields -5.5 pp for SCMS, +10.1 pp for DataCo, and -4.9 pp for Olist, showing mixed outcomes.  
- [Finding 3] Model learnability (R²) and calibration bias differ by dataset: DataCo shows moderate R²=0.27 but positive calibration bias (+0.01 days), whereas SCMS/Olist have near‑zero or negative R² and negative calibration bias.  

## Methodology  
The authors employed a leakage‑controlled rolling‑origin evaluation where each shipment’s true delay is observed only after its origin is known, preventing look‑ahead bias. They used 1000‑sample paired bootstrap confidence intervals to assess ranking stability. A cost‑sensitive nested cross‑validation was applied to retrain models under a fixed review budget, and the results were compared against the baseline value sorting.  

## Results  
M1 beats severity‑only ranking in all three datasets (p < 0.05). However, M1’s advantage over value sorting is only positive for DataCo; for SCMS and Olist it is negative. The confidence intervals do not cross zero for any dataset, confirming the observed directionality.  

## Significance  
The study provides a practical diagnostic: ML should be deployed only after verifying learnability (R² > 0) and acceptable calibration (bias below a threshold). It underscores that value sorting remains a reliable baseline and that ML gains are context‑specific rather than universal.  

## Related Concepts  
- Delay‑risk models  
- Exposure‑weighted shipment prioritization  
- Leakage‑controlled rolling‑origin evaluation  
- Pairwise bootstrap confidence intervals  
- R² (coefficient of determination) for model fit  
- Calibration bias in delay prediction  
- Cost‑sensitive nested cross‑validation
