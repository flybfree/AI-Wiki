# Summary: 2026-07-21_11-32-41Z_MedDDC_Eval_Diagnosis_DecoupledEvaluationofMulti_T.md
Saved: 2026-07-24 01:05
Source: 2026-07-21_11-32-41Z_MedDDC_Eval_Diagnosis_DecoupledEvaluationofMulti_T.md
Model: None

---

## Summary  
The paper introduces MedDDC‑Eval, a diagnosis‑decoupled evaluation framework for multi‑turn medical consultation agents that separates the quality of the elicited patient history from the policy‑generated terminal diagnosis to enable fair assessment. It treats the history as a fixed reference and measures diagnostic usefulness independently of how diagnoses are produced.

## Key Contributions  
- [Finding 1] MedDDC‑Eval provides a diagnosis‑decoupled testbed where only the diagnostic reader is varied while the patient history remains constant, isolating its impact on diagnostic performance.  
- [Finding 2] The framework yields precise precision‑recall counts for open‑ended items with at most one credit per prediction or reference, and shows that fixing histories but varying readers can shift F1 scores by up to 19 points and reverse many pairwise orderings.  
- [Finding 3] Applying Group Relative Policy Optimization (GRPO) over interactive rollouts improves Qwen3‑32B’s total‑score on held‑out splits by 9.7 (Record) and 4.6 (Dialogue), demonstrating that feedback from diagnosis results can guide policy optimization.

## Methodology  
The authors construct MedDDC‑Eval by freezing a shared reader to generate consistent histories, then varying the diagnostic reader across two sources: a grounded interface and an auditable D/T/E harness. They compute diagnostic usefulness via information‑acquisition metrics, efficiency through the D/T/E scores, and precision‑recall using directional semantic coverage combined with deterministic one‑to‑one assignment.

## Results  
On held‑out splits (100 cases Record, 70 Dialogue), the trained policy improves over initialization by 9.7 and 4.6 total‑score points respectively; removing either primary signal degrades joint performance. Changing only the diagnostic reader alters F1 scores between 2.2–19.0 points and flips 18%–36% of pairwise orderings, confirming diagnosis‑decoupling.

## Significance  
This work enables interpretable measurement of elicited histories and guides evidence‑acquisition policies without confounding them with terminal diagnoses, advancing trustworthy AI in medical consultations.

## Related Concepts  
- Diagnosis‑decoupled evaluation  
- Multi‑turn medical consultation agents  
- Grounded interface  
- Auditable D/T/E harness  
- Group Relative Policy Optimization (GRPO)  
- Fixed reader vs. variable diagnostic reader
