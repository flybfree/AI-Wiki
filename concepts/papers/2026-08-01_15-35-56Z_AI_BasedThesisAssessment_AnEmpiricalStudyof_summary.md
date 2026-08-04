# Summary: 2026-08-01_15-35-56Z_AI_BasedThesisAssessment_AnEmpiricalStudyofHumanEv.md
Saved: 2026-08-03 21:28
Source: 2026-08-01_15-35-56Z_AI_BasedThesisAssessment_AnEmpiricalStudyofHumanEv.md
Model: None

---

## Summary  
This paper investigates how thesis supervisors actually prioritize evaluation criteria in human‑based thesis assessment and examines the consequences of using those supervisor‑derived weights for an AI‑driven rubric system called RubiSCoT. By comparing the weight distributions supplied by 84 supervisors across four disciplines with the default weights built into the AI, the authors show that simple calibration does not substantially improve alignment between automated scores and human judgments.  

## Key Contributions  
- Survey of 84 thesis supervisors yields a divergent set of criterion‑weight patterns that differ markedly from the default RubiSCoT configuration.  
- Integrating supervisor‑derived weights into calibrated RubiSCoT configurations reduces the mean relative deviation between AI and human scores from 11.18 % to 10.85 %, although this improvement is not statistically significant.  
- Human supervisors exhibit strong inter‑supervisor agreement, with a mean inter‑supervisor relative deviation of 4.44 %.  

## Methodology  
The authors conducted an empirical study that first surveyed 84 thesis supervisors from four academic disciplines to collect weighting data for 35 evaluation criteria. They then compared these supervisor weights against the default weight matrix used by RubiSCoT. After establishing a baseline, they implemented multiple calibration configurations using the supervisor‑derived weights and evaluated each configuration on a corpus of 80 German‑language theses to measure alignment with human assessments.  

## Results  
The best‑performing calibration reduced the mean relative deviation between AI‑generated evaluations and supervisor assignments from 11.18 % to 10.85 %. However, statistical testing did not reveal a significant difference, indicating that the gain is marginal. Human supervisors themselves showed high agreement, with an average inter‑supervisor relative deviation of only 4.44 %, suggesting that subjective weighting decisions are already fairly consistent across experts.  

## Significance  
The findings challenge the assumption that merely swapping supervisor weights into a pre‑trained AI rubric will markedly improve its performance. They highlight the limited impact of criterion‑weight calibration on aligning automated assessments with human judgments and underscore the need for more holistic approaches to thesis evaluation, such as incorporating additional contextual factors or using ensemble methods.  

## Related Concepts  
Rubric‑based AI assessment; criterion weighting; expert judgment; inter‑rater reliability; calibration; mean relative deviation; rubric systems (e.g., RubiSCoT).
