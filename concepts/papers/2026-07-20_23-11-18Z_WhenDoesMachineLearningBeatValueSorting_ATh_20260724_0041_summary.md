# Summary: 2026-07-20_23-11-18Z_WhenDoesMachineLearningBeatValueSorting_AThree_Dat.md
Saved: 2026-07-24 00:41
Source: 2026-07-20_23-11-18Z_WhenDoesMachineLearningBeatValueSorting_AThree_Dat.md
Model: None

---

## Summary  
The paper investigates whether machine‑learning (ML) ranking can outperform a simple no‑model baseline that inspects the highest‑value shipments first, given limited managerial review capacity in supply‑chain operations. It evaluates ML across three real‑world datasets—SCMS procurement, DataCo logistics, and Olist e‑commerce—using leakage‑controlled rolling‑origin evaluation with paired bootstrap confidence intervals to assess ranking performance. The study finds that ML (predicted delay severity multiplied by known value) beats the severity‑only ranking in all cases but does not consistently beat pure value sorting. A diagnostic protocol is proposed rather than a new learning algorithm.

## Key Contributions  
- [Finding 1] Machine‑learning ranking (M1 = predicted delay severity × known value) outperforms severity‑only ranking across all three datasets.  
- [Finding 2] ML does not generally beat pure value sorting; at a 10 % review budget, M1 minus VALUE_ONLY is –5.5 pp for SCMS, +10.1 pp for DataCo, and –4.9 pp for Olist.  
- [Finding 3] The performance gap correlates with severity learnability (R²) and calibration bias; only DataCo shows a positive R² (0.27) and slight positive bias (+0.01 days), while SCMS and Olist have near‑zero or negative R².

## Methodology  
The authors employ leakage‑controlled rolling‑origin evaluation on three real supply‑chain datasets: SCMS procurement, DataCo logistics, and Olist e‑commerce. For each dataset they compute paired bootstrap confidence intervals for ranking performance. The baseline is “VALUE_ONLY,” which inspects the highest‑value shipments first. A cost‑sensitive nested‑cross‑validation (CV) retraining procedure is applied to a machine‑learning model M1, but its improvement over M1 is not stable.

## Results  
Across all datasets, M1 beats severity‑only ranking, yet it only marginally improves over VALUE_ONLY in DataCo (+10.1 pp) and slightly worsens in SCMS (‑5.5 pp) and Olist (‑4.9 pp). R² values are: DataCo ≈ 0.27 with a calibration bias of +0.01 days; SCMS and Olist have R² ≈ –0.02 and negative calibration biases. Nested‑CV retraining does not deliver a stable advantage over M1.

## Significance  
The diagnostic shows that ML is only beneficial when it can accurately learn severity and be properly calibrated; otherwise value sorting remains superior. The paper provides a practical evaluation protocol for deploying prioritization models in supply chains, guiding managers to audit model learnability before committing resources.

## Related Concepts  
Delay‑risk models, exposure‑weighted shipment prioritization, leakage‑controlled rolling‑origin evaluation, paired bootstrap confidence intervals, R² (coefficient of determination), calibration bias, cost‑sensitive nested‑CV retraining, M1 ranking (severity × value), VALUE_ONLY baseline.
