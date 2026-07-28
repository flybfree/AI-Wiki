# Summary: 2026-07-27_13-31-24Z_FailuresRevealWhatMetricsMiss_AnEvidence_DrivenAge.md
Saved: 2026-07-27 22:57
Source: 2026-07-27_13-31-24Z_FailuresRevealWhatMetricsMiss_AnEvidence_DrivenAge.md
Model: None

---

## Summary  
RecursiveECG proposes an evidence‑driven LLM‑as‑Designer framework that refines 12‑lead ECG classifiers by grounding each improvement in concrete failure cases and deterministic measurements rather than relying on aggregate performance metrics. The pipeline converts curated ECG criteria into reproducible functions, evaluates failures through a joint analysis of raw waveforms, measurements, and model outputs, and only retains revisions supported by this evidence. This approach yields consistent improvements across benchmark datasets while providing an auditable trail linking every accepted change to its supporting data.

## Key Contributions  
- Introduces an evidence‑driven LLM‑as‑Designer framework (RecursiveECG) for recursive refinement of ECG classifiers.  
- Develops Criteria‑to‑Measurement Compilation: converting curated ECG criteria into deterministic functions that produce reproducible, reference‑backed measurements for individual ECGs.  
- Implements Evidence‑Grounded Failure Review that jointly analyzes raw waveforms, measurement outputs, and model predictions to diagnose classifier limitations and formulate targeted revisions.

## Methodology  
The authors built an offline pipeline where the LLM operates as a designer rather than an inference engine. Curated ECG criteria are compiled into deterministic functions (Criteria‑to‑Measurement Compilation) that generate reproducible measurements for each ECG sample. When a failure is identified, Evidence‑Grounded Failure Review examines the raw waveform, the measurement output of the function, and the classifier’s prediction to pinpoint the root cause. Candidate revisions are executed under a fixed problem contract, re‑evaluated on the same evidence set, and only those that improve performance while preserving evidence support are retained. The refined model is then frozen for deployment, with an audit trail linking each accepted revision to its supporting measurements.

## Results  
Across PTB‑XL, Georgia, and CPSC2018, RecursiveECG consistently outperforms strong baselines, achieving an average relative improvement of 10.0 %. Ablation studies confirm that only evidence‑grounded updates matter for performance gains, and transfer experiments show the framework’s adaptability to other ECG domains.

## Significance  
By anchoring model refinement in concrete failures and reproducible measurements, RecursiveECG reduces dependence on manual expert inspection, enables fully automated iterative design, and supplies an auditable record that each revision is justified by empirical evidence. This advances explainable AI for medical ECG classification and demonstrates a scalable path toward robust, continuously improving classifiers.

## Related Concepts  
- LLM‑as‑Designer  
- Recursive refinement of classifiers  
- Evidence‑based learning  
- Deterministic measurement functions  
- Failure diagnosis in deep models  
- Explainable AI (XAI) for medical imaging  
- ECG classifier optimization
