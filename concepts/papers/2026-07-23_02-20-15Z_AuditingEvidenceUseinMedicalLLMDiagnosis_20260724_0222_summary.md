# Summary: 2026-07-23_02-20-15Z_AuditingEvidenceUseinMedicalLLMDiagnosis.md
Saved: 2026-07-24 02:22
Source: 2026-07-23_02-20-15Z_AuditingEvidenceUseinMedicalLLMDiagnosis.md
Model: None

---

## Summary  
The paper proposes a behavioral audit to examine how medical large language models (LLMs) use patient evidence when generating diagnoses, arguing that diagnostic accuracy alone is insufficient because it does not reveal whether the model’s reasoning relies on appropriate evidence. By decomposing clinical cases into evidence units and scoring candidate diagnoses under controlled subsets of those units, the authors identify low‑order interactions in diagnostic margins that may be clinically plausible or indicative of failures. Their analysis reveals that many “interactions” are actually valid differential diagnoses rather than outright errors, prompting a shift toward role‑aware audit frameworks for LLM evaluation. The contribution is both methodological (a systematic audit protocol) and empirical (empirical evidence across multiple datasets).

## Key Contributions  
- [Finding 1] A behavioral audit framework that separates interaction discovery from failure assignment in medical diagnosis.  
- [Finding 2] Empirical evidence that faithful support and differential conflicts dominate interaction strength, indicating many interactions are clinically plausible.  
- [Finding 3] In a blinded review of 130 enriched cases, invalid or shortcut‑like diagnoses concentrate on negated findings and locally relevant evidence.

## Methodology  
The authors decompose each patient record into discrete evidence units (e.g., lab results, symptoms). They then evaluate five open‑weight LLMs by presenting subsets of these units to the models and scoring candidate diagnoses. Interaction strength is measured as the magnitude of disagreement between diagnoses when different evidence subsets are used. The audit isolates “large” or “negative” interactions—potentially indicating robust reasoning—or “suspicious” ones that may signal shortcutting. To validate findings, they conduct a blinded five‑reviewer analysis on an enriched 130‑item sample from DDXPlus, CupCase, and MedCase.

## Results  
Across the three datasets, the majority of interaction strength is accounted for by faithful support (positive evidence reinforcing the correct diagnosis) or differential conflict/cancellation (evidence that could justify alternative diagnoses). The audit uncovers that invalid or shortcut‑like cases are not uniformly distributed; they tend to appear when negated findings are absent and when only locally relevant evidence is present. In the enriched review, 23% of cases were flagged as potentially problematic, highlighting a systematic bias toward missing negative evidence.

## Significance  
This work demonstrates that diagnostic accuracy metrics can mask evidence‑use failures in LLMs, leading to overconfidence in models that may not truly understand their reasoning. By providing a role‑aware audit protocol, the study motivates future evaluation frameworks that prioritize how and why diagnoses are generated rather than only whether they are correct.

## Related Concepts  
- Medical Large Language Models (LLMs)  
- Evidence units / diagnostic evidence decomposition  
- Interaction strength in diagnostic margins  
- Role‑aware audit frameworks  
- Differential diagnosis and clinical plausibility
