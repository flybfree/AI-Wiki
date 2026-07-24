---
title: Auditing Evidence Use in Medical LLM Diagnosis
url: http://arxiv.org/abs/2607.20848v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_02-20-15Z_AuditingEvidenceUseinMedicalLLMDiagnosis.md
generated_at: 2026-07-23 22:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
Medical LLMs are evaluated on diagnostic accuracy but this does not reveal how evidence is used. The paper introduces a behavioral audit that decomposes patient data into evidence units and scores diagnoses under controlled subsets, revealing low-order interactions in diagnostic margins. Experiments on five open-weight models show that most interaction strength stems from plausible differential diagnosis rather than outright failures.

## Key Takeaways
- Faithful support and differential conflict or cancellation account for most interaction strength, indicating many evidence interactions are clinically plausible rather than errors.
- Invalid or shortcut-like cases concentrate in negated or absent findings and locally relevant clinical evidence, suggesting accuracy can hide candidate evidence‑use failures.
- The audit separates interaction discovery from failure assignment, allowing robust checks on suspicious interactions.

## Context
Medical language models face a gap between reported performance and the quality of reasoning they perform. This work addresses that gap by providing a systematic method to audit how evidence drives diagnostic decisions, which is essential for trustworthy AI in healthcare.

## Implications
Clinicians and developers must move beyond accuracy metrics to evaluate evidence‑driven reasoning. Role‑aware audits can guide model improvement and ensure that LLM outputs are both correct and justified, fostering safer clinical decision support systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20848v1)
