---
title: Characterizing Treatment-Context Medication Evidence Across Clinic Notes and Structured EHR Medication History
url: http://arxiv.org/abs/2608.01570v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_01-00-01Z_CharacterizingTreatment_ContextMedicationEvidenceA.md
generated_at: 2026-08-03 23:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the mismatch between medication mentions in clinic notes and structured EHR histories, proposing a note-grounded approach that combines LLM-assisted reference building, human review, deterministic normalization, and semantic-temporal comparisons to improve alignment. On a held-out test set of 5,403 mention rows, exact canonical agreement rose from 72% to 84%, while random audit revealed high agreement on valid mentions (92%) but lower treatment-action attribution (53%). Overall, only 16% of note-derived rows matched structured history exactly, yet 55% had semantic overlap and 90% had same‑ or +/-30‑day overlap.

## Key Takeaways
- The exact canonical agreement improved from 0.7226 to 0.8429 after lexical cleanup and alias mapping, showing that normalization errors are a major source of mismatch.
- Random audit found high agreement on valid medication mentions (0.9210) but lower treatment-action attribution (0.5326), indicating that while the medication labels align, linking them to actions is less reliable.
- Only 16.44% of rows had same‑visit exact overlap with structured history, yet 55.17% showed semantic overlap and 90.34% had same‑ or +/-30‑day overlap, highlighting the importance of temporal flexibility.

## Context
This work contributes to AI‑driven health data integration by demonstrating that large language models can be combined with deterministic normalization pipelines to resolve noisy clinical documentation. It underscores a persistent gap between unstructured notes and structured EHR records, which remains a challenge for downstream analytics and decision support systems.

## Implications
Clinicians and developers must adopt robust normalization strategies and temporal awareness when merging note‑based data with EHR histories. The findings suggest that AI tools should prioritize semantic alignment over strict exact matching to improve patient safety and clinical decision making.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01570v1)
