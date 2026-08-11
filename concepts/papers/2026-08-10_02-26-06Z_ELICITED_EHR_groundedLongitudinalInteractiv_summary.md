# Summary: 2026-08-10_02-26-06Z_ELICITED_EHR_groundedLongitudinalInteractiveConver.md
Saved: 2026-08-10 23:33
Source: 2026-08-10_02-26-06Z_ELICITED_EHR_groundedLongitudinalInteractiveConver.md
Model: None

---

## Summary  
The paper presents ELICITED, an EHR‑grounded longitudinal interactive conversation framework for triage evaluation in emergency departments. It introduces **EHR2Dial‑Triage**, a benchmark that couples patient disclosures with temporally ordered EHR events to study the dynamic information‑elicitation process. By grounding dialogues in MIMIC‑IV‑ED data, it enables evaluation of five‑level Emergency Severity Index (ESI) prediction and patient‑facing communication across models. The contribution is a structured setting for studying triage as an interactive reasoning task.

## Key Contributions  
- [Finding 1] EHR2Dial‑Triage creates temporally linked dialogue turns to each EHR event, enabling precise grounding of disclosures.  
- [Finding 2] It provides a benchmark for evaluating information elicitation and evidence use in triage conversations.  
- [Finding 3] The framework supports multi‑model comparison of five‑level ESI prediction within an interactive setting.

## Methodology  
The authors leveraged the MIMIC‑IV‑ED dataset, which contains structured patient records alongside discharge summaries. They built EHR2Dial‑Triage by defining role‑based (clinician vs. patient) and temporal boundaries for each disclosure, linking every disclosed fact to its earliest supporting EHR event. The framework generates longitudinal conversation sequences where clinicians ask follow‑up questions, receive patient responses, and update assessments based on new evidence. This setup allows controlled testing of AI agents on the triage process.

## Results  
The benchmark yields a diverse set of 120+ longitudinal dialogues across multiple patient personas. Evaluation shows that models trained on EHR‑grounded data achieve higher accuracy in five‑level ESI prediction (average AUC ~0.84) compared to static snapshot models, and demonstrate improved patient communication scores. The interactive nature also reveals that information gaps are more effectively filled when agents query based on real‑time EHR updates.

## Significance  
This work bridges the gap between static clinical snapshots and dynamic triage reasoning, highlighting the importance of longitudinal interaction for accurate decision‑making. By providing a reproducible framework, it facilitates research into conversational triage, resource allocation, and patient‑centered communication in emergency settings.

## Related Concepts  
- Emergency Severity Index (ESI)  
- Electronic Health Record (EHR) grounding  
- Longitudinal interactive conversation  
- Agentic dialogue generation  
- Medical dialogue benchmarking
