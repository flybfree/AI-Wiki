---
title: Cardiologent: Multi-Agent Clinical Decision Support for Patient-Level Arrhythmia Assessment, Urgency, and Management
published: 2026-07-28T06:43:39Z
authors: Sukju Oh, Moo-Yong Rhee, Jae-Sik Jang, Sukkyu Sun
url: http://arxiv.org/abs/2607.25340v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cardiologent: Multi-Agent Clinical Decision Support for Patient-Level Arrhythmia Assessment, Urgency, and Management

## Abstract
The same episode of atrial fibrillation is a minor finding in a healthy adult and grounds for anticoagulation in an elderly patient with hypertension: identical signal, opposite decision. Naming the rhythm is only the start; what determines a patient's outcome is the judgement that follows -- what the arrhythmia is across the whole record, what it means for this patient, and what should be done about it. Recent work pairing large language models with the ECG stops short of this, reading one recording without assembling a patient-level finding; and agentic systems built around it either receive the arrhythmia a device has already detected or target a different diagnostic task, stopping before the decision this task requires. We formulate patient-level arrhythmia decision support as a task and present Cardiologent, a multi-agent system that spans it from detection to decision. An agent for each signal -- a single ECG lead and the photoplethysmogram a wearable acquires -- grounds its window reading in measured features rather than a bare label; the readings are assembled into the patient's rhythm profile and, with the patient's own data, reasoned against clinical guidelines retrieved for the case, with a critic checking each conclusion against the guideline it cites. We evaluate the clinical decision rather than the report, across integrated diagnosis, clinical significance, and urgency and management. Cardiologent scores highest on every axis, first on every patient-level task under both cardiologists and an at-scale LLM judge -- whose agreement with the cardiologists (ICC 0.74, 0.66) matches theirs with each other (0.67). Because each conclusion traces to a cited guideline and is validated against expert cardiologists, it yields decisions a clinician can audit rather than act on blindly -- a step toward use in continuous monitoring.

## Metadata
- **Published**: 2026-07-28T06:43:39Z
- **Authors**: Sukju Oh, Moo-Yong Rhee, Jae-Sik Jang, Sukkyu Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25340v1)