# Summary: 2026-08-09_16-34-38Z_IDRAAK_FromMulti_AgentNLPtoFew_ShotPromptingforSem.md
Saved: 2026-08-10 23:25
Source: 2026-08-09_16-34-38Z_IDRAAK_FromMulti_AgentNLPtoFew_ShotPromptingforSem.md
Model: None

---

## Summary  
The paper introduces IDRAAK, an interpretable framework that detects semantic drift in technical requirements across languages without relying on language‑specific models. By representing each requirement with a language‑independent Semantic Requirement Representation (SRR), the authors evaluate six detection workflows—from deterministic SRR comparison to multi‑agent verification and few‑shot prompting—to show that a single LLM call with six examples can achieve high accuracy. The study demonstrates that simple few‑shot prompting outperforms complex, structured alternatives on both technical and general‑domain data.

## Key Contributions  
- [Finding 1] A language‑independent SRR enables semantic drift detection across engineering domains, providing a unified representation for all requirements.  
- [Finding 2] Few‑shot prompting with six examples yields MCC = 0.888 and F1 = 0.983, surpassing deterministic comparison (F1 ≈ 0.898) and multi‑agent methods on synthetic perturbations.  
- [Finding 3] Deterministic SRR comparison excels on technical requirements but fails on general text, highlighting domain‑specific performance differences.

## Methodology  
The authors constructed 890 synthetic perturbed requirements from 300 original specifications across ten engineering fields and measured drift using six workflows. Each workflow was implemented as a single LLM call: (1) deterministic SRR comparison, (2) structured evidence aggregation, (3) multi‑agent verification with pairwise reasoning, (4) few‑shot prompting with six examples, (5) post‑hoc Platt scaling for confidence calibration, and (6) hybrid approaches. Experiments were conducted on synthetic data, PAWS‑X (805 pairs across five languages), and XNLI (700 pairs across seven languages).

## Results  
On the synthetic dataset, few‑shot prompting achieved the best metrics (MCC = 0.888, F1 = 0.983). Deterministic SRR comparison performed well on technical requirements (F1 ≈ 0.898) but collapsed to near zero on general text (F1 ≈ 0.012). Multi‑agent verification showed modest gains over deterministic methods, while structured evidence helped with adversarial paraphrases. Platt scaling improved confidence calibration without sacrificing detection accuracy.

## Significance  
IDRAAK reveals that increasing agentic complexity does not guarantee better semantic drift detection; instead, minimal few‑shot prompting can deliver state‑of‑the‑art performance efficiently. This insight guides researchers toward lightweight, interpretable solutions for cross‑lingual requirement verification in engineering and other technical fields.

## Related Concepts  
Semantic Requirement Representation (SRR), few‑shot prompting, MCC/F1 metrics, multi‑agent verification, deterministic comparison, post‑hoc Platt scaling.
