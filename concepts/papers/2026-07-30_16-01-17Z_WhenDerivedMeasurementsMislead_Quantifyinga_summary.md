# Summary: 2026-07-30_16-01-17Z_WhenDerivedMeasurementsMislead_QuantifyingandMitig.md
Saved: 2026-07-30 22:18
Source: 2026-07-30_16-01-17Z_WhenDerivedMeasurementsMislead_QuantifyingandMitig.md
Model: None

---

## Summary  
The paper introduces a new metric for “derived‑feature over‑trust” (DFOT), which captures the phenomenon where large language models treat measurements that are derived from other data sources—as opposed to direct observations—as if they were equally reliable facts. By quantifying this misalignment, the authors develop a comprehensive framework of five estimands—conflict‑over‑trust rate, context‑induced error rate, correct‑repair rate, evidence‑specific repair margin, and utility‑harm rate—that together reveal how downstream LLMs misuse privileged‑modality data. Their work demonstrates that DFOT can be evaluated on real physiological sensor data (PPG‑ECG) and provides a common benchmark for improving LLM reliability.

## Key Contributions  
- [Finding 1] The authors define derived‑feature over‑trust (DFOT) as the failure of an LLM to respect the epistemic limits of measurements that are computed from other modalities.  
- [Finding 2] They introduce a set of five quantifiable estimands—COTR, CIR, CRR, ESRM, and UHR—that systematically measure conflict over‑trust, error propagation, repair effectiveness, evidence‑specific repair margins, and utility harm in high‑reliability cases.  
- [Finding 3] The study shows that DFOT can serve as a universal evaluation target for mitigating LLM over‑trust across different reliability generators.

## Methodology  
The research adopts physiological sensing (PPG and ECG) as the case study, pairing each PPG rhythm with an offline‑confirmed ECG measurement. Using 50 000 paired records, they construct a baseline “ECG‑to‑PPG privileged distillation” model that supplies training supervision without exposing the LLM to the ECG data. The downstream task is PPG‑only inference under protocol‑locked conditions for 187 patients. The framework does not rely on any specific reliability generator; it only requires paired reference data.

## Results  
On the test set, the baseline improves four repair and specificity endpoints by 1.82–6.69 percentage points (all 95 % confidence intervals exclude zero). The utility‑harm rate increases by 0.67 percentage points with a 95 % CI of –0.4 to +1.7, indicating that the LLM begins to use high‑reliability evidence without verification.

## Significance  
By quantifying DFOT and providing concrete metrics (COTR, CIR, CRR, ESRM, UHR), this work enables researchers to assess how LLMs mishandle derived measurements and to design mitigation strategies that respect the source of privileged data. The framework is agnostic to the reliability generator, making it a reusable tool for any domain where indirect measurements are incorporated into LLM pipelines.

## Related Concepts  
derived‑feature over‑trust (DFOT), epistemic status, downstream LLM inference, privileged modality, confidence intervals, repair rate, utility harm, evidence‑specific repair margin.
