# Summary: 2026-08-09_21-15-12Z_ADomain_StructuredEnsembleFrameworkforPerioperativ.md
Saved: 2026-08-10 23:30
Source: 2026-08-09_21-15-12Z_ADomain_StructuredEnsembleFrameworkforPerioperativ.md
Model: None

---

## Summary  
The paper proposes a domain‑structured ensemble framework to predict postoperative delirium (POD) using routinely collected electronic health record (EHR) data, addressing the limitations of conventional risk models that rely on narrow surgical cohorts or lack calibration. By organizing predictors into patient‑related, surgery‑related, and anesthetics‑related domains, each domain is modeled with gradient boosting, and a logistic regression meta‑learner combines these estimates to produce a calibrated risk score. The framework demonstrates superior discrimination (AUROC 0.899) and excellent calibration compared with the best single‑stage model, while also providing interpretable decision thresholds for clinical use.

## Key Contributions  
- A domain‑structured ensemble that integrates patient, surgical, and anesthetic predictors improves AUROC to 0.899 (vs. 0.849 for a single model).  
- The logistic regression meta‑learner yields a calibrated risk estimate with intercept −0.006 and slope 1.035, outperforming the surgery‑only ensemble (AUROC 0.879).  
- Temporal validation on post‑2017 data achieves AUROC 0.915, confirming robustness over time.

## Methodology  
The authors extracted EHR records from a statewide health information exchange containing 5,386 surgical encounters (2,693 cases with POD and 2,693 controls). Predictors were classified into three domains: patient‑related (e.g., age, comorbidities), surgery‑related (e.g., procedure type, length), and anesthetics‑related (e.g., induction agents). Each domain was trained using gradient boosting machines to generate independent risk predictions. These domain‑specific outputs were combined via a logistic regression meta‑learner that produces the final POD probability. Domain ablation experiments removed one or more domains to assess impact on discrimination and calibration.

## Results  
The stacked model achieved AUROC 0.899 (95% CI: 0.891–0.906), precision‑recall AUC 0.881, and Brier score 0.126, surpassing the best single‑stage model’s AUROC of 0.849. Ablation studies showed that incorporating all three domains improves discrimination (AUROC 0.879) and calibration (Brier 0.140 vs. 0.126). Temporal validation on post‑2017 data retained AUROC 0.915, indicating stability. Calibration was excellent: intercept −0.006 (95% CI: −0.083 to 0.070) and slope 1.035 (95% CI: 0.982 to 1.088). Decision‑curve analysis, corrected for case‑control sampling, revealed positive net benefit across clinically plausible thresholds.

## Significance  
This framework offers a scalable, interpretable, and calibration‑aware tool for peri‑operative risk prediction that can be adapted to other outcomes or extended with additional domains, thereby enhancing clinical decision support without sacrificing model performance. The modular design facilitates ongoing updates as new EHR data become available.

## Related Concepts  
perioperative outcome prediction; electronic health records (EHR); domain‑structured ensemble; gradient boosting machines; logistic regression meta‑learner; calibration; decision curve analysis; ICD codes; Confusion Assessment Method (CAM).
