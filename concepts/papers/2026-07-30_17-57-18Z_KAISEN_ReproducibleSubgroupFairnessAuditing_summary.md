# Summary: 2026-07-30_17-57-18Z_KAISEN_ReproducibleSubgroupFairnessAuditingforClin.md
Saved: 2026-07-30 22:23
Source: 2026-07-30_17-57-18Z_KAISEN_ReproducibleSubgroupFairnessAuditingforClin.md
Model: None

---

## Summary  
KAISEN is a five‑phase audit pipeline designed to evaluate the reliability of subgroup fairness assessments in clinical risk models, where aggregate performance can mask material disparities across patient groups. The authors stress‑test each phase—subgroup stratification, disparity measurement, mechanism diagnostics, post‑hoc mitigation, and drift monitoring—on a synthetic benchmark that spans 16 disease tasks, 15 social‑determinant axes from Healthy People 2030, and three predefined intersections. By quantifying how often each component correctly identifies fairness gaps and how robust those findings are to model‑driven noise, KAISEN provides a systematic way to report audit outcomes that go beyond simple pass/fail metrics. The work demonstrates that many fairness audits can be misleading if only average effects are reported or if thresholds are tuned on one cohort without regard for drift.

## Key Contributions  
- **Finding 1:** Significance tracks each axis’s gap against its minimum detectable effect with a rank correlation ρ = 0.56 (rising to 0.78 when EOD is standardized by that floor), indicating moderate alignment between audit significance counts and raw equalized‑odds differences across the 15 axes.  
- **Finding 2:** Per‑group threshold optimization reduces EOD in all 48 held‑out runs (paired delta = –0.285, 95% CI [–0.313, –0.252]), whereas group‑wise Platt scaling—generally the better calibrator—exhibits near‑zero mean effect with a variance of 0.47; thus auditors should report variance rather than average improvement.  
- **Finding 3:** The mechanism diagnostic correctly classifies all 144 controlled cases but recovers none of the 48 model‑driven cases under proxy misspecification, and CUSUM failures and false alarms track cohort realization more than disease (χ² p = 0.002), showing that threshold tuning on one cohort does not transfer.

## Methodology  
KAISEN follows a five‑phase audit pipeline: (1) subgroup stratification to isolate patient groups, (2) disparity measurement using equalized‑odds difference (EOD), (3) mechanism diagnostics to assess whether observed gaps stem from model bias or data artifacts, (4) post‑hoc mitigation strategies such as threshold optimization and Platt scaling, and (5) drift monitoring to track performance over time. The pipeline was evaluated on a synthetic benchmark comprising 16 disease tasks, 15 social‑determinant axes, and three intersections, with known ground truth provided for each run.

## Results  
The empirical results show that significance correlates moderately with EOD across axes (ρ = 0.56), that per‑group threshold optimization consistently lowers EOD without bias, while Platt scaling’s effect is highly variable (mean ≈ 0, variance 0.47). The mechanism diagnostic achieves perfect recall on controlled cases but fails entirely on model‑driven cases when proxies are misspecified. CUSUM failure rates and false alarms are more sensitive to cohort realization than disease prevalence, with a significant χ² test indicating non‑transferability of thresholds.

## Significance  
KAISEN highlights that fairness audits in clinical risk models must be evaluated for internal consistency and external transferability; otherwise reported improvements can be artifacts. By emphasizing variance over average gains and documenting CUSUM drift, the pipeline enables more honest communication of audit outcomes to clinicians and regulators.

## Related Concepts  
subgroup fairness, equalized‑odds difference (EOD), post‑hoc mitigation, mechanism diagnostics, CUSUM monitoring, drift detection, Healthy People 2030 axes.
