# Summary: 2026-07-23_02-20-15Z_AuditingEvidenceUseinMedicalLLMDiagnosis.md
Saved: 2026-07-24 02:35
Source: 2026-07-23_02-20-15Z_AuditingEvidenceUseinMedicalLLMDiagnosis.md
Model: None

---

## Summary  
Medical LLMs are evaluated for diagnostic accuracy, but this metric does not reveal whether the model appropriately uses patient evidence. This paper introduces a behavioral audit that isolates how evidence units influence candidate diagnoses and detects low‑order interactions in diagnostic margins. By decomposing cases into evidence subsets and scoring diagnoses under controlled evidence, the authors uncover interactions that may be clinically plausible or indicative of failures. The study evaluates five open‑weight LLMs on DDXPlus, CupCase, and MedCase to show that many interaction strengths reflect legitimate differential diagnosis rather than outright errors.  

## Key Contributions  
- Finding 1: Faithful support and differential conflict or cancellation dominate interaction strength across datasets, indicating that most evidence interactions are clinically plausible.  
- Finding 2: Invalid or shortcut‑like cases concentrate in negated findings and locally relevant clinical evidence, suggesting a systematic bias toward false negatives.  
- Finding 3: A blinded five‑reviewer review of an enriched sample reveals that accuracy can hide candidate evidence‑use failures, motivating role‑aware audit frameworks.  

## Methodology  
The authors decompose each patient record into discrete evidence units, then evaluate multiple open‑weight LLMs on a set of diagnostic candidates using controlled subsets of those evidence units. By measuring the strength and direction of interactions between evidence and diagnosis (positive, negative, or cancellation), they isolate low‑order interactions that may not be captured by overall accuracy scores.  

## Results  
Across DDXPlus, CupCase, and MedCase, the majority of interaction strengths arise from faithful support or differential conflict/cancellation. The enriched blind review shows that cases flagged as invalid are predominantly those where negated findings or locally relevant evidence are missing, indicating a pattern of shortcut behavior. These results demonstrate that standard accuracy metrics can mask evidence‑use failures.  

## Significance  
Understanding which evidence interactions are genuine versus erroneous is crucial for trustworthy medical AI. This audit provides a framework to detect subtle diagnostic errors that could lead to harmful misdiagnoses, guiding future model evaluation and clinical deployment.  

## Related Concepts  
- Diagnostic accuracy  
- Evidence units  
- Interaction strength  
- Differential diagnosis  
- Role‑aware auditing
