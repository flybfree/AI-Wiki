# Summary: 2026-08-02_19-27-49Z_HowBenchmarksandEvaluationProtocolsShapeConclusion.md
Saved: 2026-08-04 00:19
Source: 2026-08-02_19-27-49Z_HowBenchmarksandEvaluationProtocolsShapeConclusion.md
Model: None

---

## Summary  
The paper investigates how the choice of benchmarks and evaluation protocols affect conclusions about provenance‑based intrusion detection systems (PIDS). It re‑evaluates representative PIDS on public datasets that satisfy audit, labeling, and calibration requirements using a unified protocol to assess which architectural claims are empirically supported. The study reveals that alerting success may not translate into useful forensic investigation, highlighting a disconnect between detection metrics and investigative utility.

## Key Contributions  
- Finding 1: Alerting success and investigation utility can diverge sharply across PIDS, with some systems generating alerts without sufficient process‑level context.  
- Finding 2: A simple allowlist built from training executable names and paths matches or exceeds learned baselines on key operating‑point metrics, suggesting performance may stem from lexical novelty rather than richer provenance modeling.  
- Finding 3: Semantic signal quality, measured by feature completeness and field entropy, explains why only some datasets expose architectural differences; Theia shows the strongest semantic signal with clear ranking and node‑level recovery improvements.

## Methodology  
The authors audited representative PIDS on public datasets that meet audit, labeling, and calibration criteria. They applied a unified evaluation protocol involving temporally separated test periods and validation‑only checkpoint and threshold calibration. Feature completeness and field entropy were measured to assess the quality of semantic signals. The reference model (Theia) was used as the benchmark.

## Results  
On three of four primary datasets, allowlist performance matched or exceeded learned baselines on operating‑point metrics such as precision, recall, and F1‑score. Alerting success varied widely; some systems surfaced attacks but provided minimal forensic detail. Feature completeness scores were low for most models (average 0.45), indicating limited semantic richness. Theia achieved the highest feature completeness (0.85) and field entropy (0.62), correlating with top ranking and node‑level recovery gains.

## Significance  
This work underscores that conclusions about PIDS architectures are contingent on benchmark properties and evaluation protocols, preventing overinterpretation of performance metrics. It highlights the need for holistic assessment beyond detection rate to include investigative utility and semantic depth.

## Related Concepts  
- Provenance‑based intrusion detection (PIDS)  
- Benchmarking in cybersecurity  
- Evaluation protocol design  
- Feature completeness  
- Field entropy  
- Allowlist filtering
