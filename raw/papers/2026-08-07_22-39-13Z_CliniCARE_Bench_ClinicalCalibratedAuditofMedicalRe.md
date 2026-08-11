---
title: CliniCARE-Bench: Clinical Calibrated Audit of Medical Reasoning in EHR
published: 2026-08-07T22:39:13Z
authors: Veronica Chatrath, Bryan Zhu, George Pu, Jingxuan Fan, Apaar Shanker, Varun Ursekar, Anahita Sharma, Jason Qin, Keqi Han, Soham Dinesh Tiwari, Soham Dan, Vijay Kalmath, Yuan Li, Daniel Yue Zhang, Chenguang Wang, Zainab Doctor, Zhijun Yin, Nigam H. Shah, Yuan Xue
url: http://arxiv.org/abs/2608.07796v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CliniCARE-Bench: Clinical Calibrated Audit of Medical Reasoning in EHR

## Abstract
Large language models perform strongly on medical knowledge benchmarks, but reliable clinical deployment requires agents to conduct defensible investigations over heterogeneous, longitudinal records: determining what evidence is needed, retrieving and reconciling structured and free-text data, grounding conclusions in verifiable evidence, and deferring cases that cannot be resolved reliably. We introduce CliniCARE-Bench (Clinical Calibrated Audit of Medical Reasoning in EHR), a benchmark for retrospective clinical audit: 25 clinician-validated scenarios instantiated as 750 patient-specific cases over real-patient-derived MIMIC-IV data. Systems investigate each case through a governed, logged tool environment for record retrieval, computation, and policy access, and return one of four verdicts---Yes, No, Indeterminate: Lack of Data, or Indeterminate: Medically Ambiguous---the last two separating missing evidence from residual medical ambiguity. Beyond verdict accuracy, we score patient-evidence and policy grounding, process adherence, calibrated abstention, reliability, and efficiency against case-level reference verdicts produced by independent multi-model adjudication and calibrated against Clinical Board review. Every retrieval, computation, and report is replayable, so the investigation trace is inspectable and scorable. To our knowledge, CliniCARE-Bench is the first deployment-oriented clinical-agent benchmark to jointly evaluate real longitudinal EHR investigation, claim-level evidence grounding, governing-policy use, process adherence, and calibrated abstention within a common patient-level adjudication framework. Across 16 agentic systems, four-way accuracy spans 65.3-76.1%, but raw accuracy overstates investigation quality. Defect-free accuracy, which credits a verdict only when correct and free of prohibited shortcuts, is 4.8-14.8 points lower and reorders the leaderboard.

## Metadata
- **Published**: 2026-08-07T22:39:13Z
- **Authors**: Veronica Chatrath, Bryan Zhu, George Pu, Jingxuan Fan, Apaar Shanker, Varun Ursekar, Anahita Sharma, Jason Qin, Keqi Han, Soham Dinesh Tiwari, Soham Dan, Vijay Kalmath, Yuan Li, Daniel Yue Zhang, Chenguang Wang, Zainab Doctor, Zhijun Yin, Nigam H. Shah, Yuan Xue
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07796v1)