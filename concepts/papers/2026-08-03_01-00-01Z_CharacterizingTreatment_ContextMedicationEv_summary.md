# Summary: 2026-08-03_01-00-01Z_CharacterizingTreatment_ContextMedicationEvidenceA.md
Saved: 2026-08-03 23:34
Source: 2026-08-03_01-00-01Z_CharacterizingTreatment_ContextMedicationEvidenceA.md
Model: None

---

## Summary  
This paper investigates the discrepancy between medication information captured in clinician‑written clinic notes and the structured medication history stored in electronic health records (EHRs). By applying a note‑grounded framework that combines large‑language‑model assisted reference construction, targeted and random human review, deterministic normalization, and semantic/temporal comparisons with the EHR data, the authors quantify how often these two sources agree. Their analysis reveals substantial mismatches that stem from normalization errors, terminology variations, or timing differences in documentation.

## Key Contributions  
- The exact canonical agreement between note‑derived medication mentions and structured EHR entries rose from 0.7226 to 0.8429 after lexical cleanup and curated alias mapping on a held‑out test set of 5,403 rows.  
- A random audit of previously unaudited rows shows high canonical‑label agreement (0.9210) for valid medication mentions but lower treatment‑action attribution (0.5326).  
- Full‑cohort analysis demonstrates that only 16.44 % of note rows have same‑visit exact overlap with the EHR, yet 55.17 % share semantic overlap, 90.34 % fall within a same‑visit or ±30‑day window, and merely 3.97 % remain in the strict no‑overlap bucket under broad mapping.

## Methodology  
The authors built a note‑grounded pipeline that first extracts medication mentions from clinic notes using LLM‑assisted reference construction, then applies deterministic normalization to produce canonical labels. Targeted human reviewers address systematic errors while random reviewers assess residual cases. The normalized notes are compared semantically and temporally with the structured EHR medication history, producing a unified set of evidence rows for evaluation.

## Results  
Exact canonical agreement improved markedly after cleaning (0.7226 → 0.8429). Human‑reviewed rows exhibit near‑perfect label agreement but lower action attribution. On the held‑out test, only a minority of notes align exactly with EHR entries; however, most show semantic or temporal proximity within ±30 days. The strict OMOP‑backed no‑overlap rate dropped from 43.99 % to 36.68 % after adding development‑derived alias supplements.

## Significance  
Understanding these mismatches is crucial for improving medication evidence extraction, reducing downstream clinical errors, and ensuring reliable data integration across unstructured notes and structured EHRs. The findings highlight the need for robust normalization pipelines and ontology‑driven semantic matching to bridge documentation gaps.

## Related Concepts  
medication evidence, clinic notes, structured EHR medication history, note‑grounded approach, large language model assisted reference construction, deterministic medication normalization, semantic overlap, temporal comparison, OMOP ontology, alias mapping.
