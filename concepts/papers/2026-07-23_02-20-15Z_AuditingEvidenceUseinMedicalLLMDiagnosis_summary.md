# Summary: 2026-07-23_02-20-15Z_AuditingEvidenceUseinMedicalLLMDiagnosis.md
Saved: 2026-07-24 02:21
Source: 2026-07-23_02-20-15Z_AuditingEvidenceUseinMedicalLLMDiagnosis.md
Model: None

---

## Summary  
The paper proposes a behavioral audit to examine how medical large language models (LLMs) use patient evidence when generating diagnoses, arguing that diagnostic accuracy alone is insufficient. It introduces a method to decompose case information into evidence units, evaluate candidate diagnoses under subsets of evidence, and detect low‑order interactions in diagnostic margins. The study reveals that many interaction patterns are clinically plausible rather than failures, highlighting the need for role‑aware audits beyond standard accuracy metrics.  

## Key Contributions  
- [Finding 1] A systematic behavioral audit framework that separates evidence‑use interactions from failure assignments, distinguishing plausible differential diagnoses from suspicious evidence misuse.  
- [Finding 2] Empirical evidence that faithful support and differential conflict or cancellation dominate interaction strength across multiple medical LLMs on DDXPlus, CupCase, and MedCase datasets.  
- [Finding 3] In a blinded review sample, invalid or shortcut‑like cases concentrate in negated or absent findings and locally relevant clinical evidence, indicating where audits should focus.  

## Methodology  
The authors decompose each patient record into discrete evidence units (e.g., lab results, symptoms) and construct candidate diagnosis hypotheses. They then evaluate how the model’s output changes when only subsets of these evidence units are presented, measuring low‑order interactions in diagnostic margins. By comparing predictions under full vs. partial evidence, they identify whether a model relies on irrelevant or contradictory evidence. The audit is applied to five open‑weight LLMs across three benchmark datasets, and a subset of 130 enriched cases is reviewed blindly by five clinicians.  

## Results  
Across DDXPlus, CupCase, and MedCase, the majority of interaction strength arises from faithful support (e.g., “patient has fever → diagnosis: flu”) or differential conflict/cancellation (e.g., “fever but no cough → possible flu or pneumonia”). Low‑order interactions are rare and often reflect clinically plausible reasoning rather than outright failure. In the enriched blind review, 42 % of cases flagged as invalid were characterized by negated findings or absence of local evidence, suggesting systematic shortcuts. The overall diagnostic accuracy of the models remains high, but audit scores reveal a significant proportion of evidence‑use failures.  

## Significance  
This work demonstrates that standard evaluation metrics can mask evidence‑use errors in medical LLMs, potentially leading to unsafe clinical recommendations. By providing an objective framework for auditing evidence interactions, it enables developers and clinicians to target model improvements where they matter most—particularly in cases where evidence is negated or locally relevant. The findings motivate the integration of role‑aware audits into LLM evaluation pipelines.  

## Related Concepts  
- Medical Large Language Models (LLMs)  
- Diagnostic accuracy vs. evidence use  
- Evidence units and diagnostic margins  
- Low‑order interactions  
- Role‑aware audit  
- Shortcut detection in AI systems
