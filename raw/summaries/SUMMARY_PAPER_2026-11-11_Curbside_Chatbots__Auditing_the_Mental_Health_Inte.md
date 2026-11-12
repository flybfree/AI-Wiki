---
title: Curbside Chatbots: Auditing the Mental Health Interventions Large Language Models Recommend to Clinicians, Caregivers, and Patients
url: http://arxiv.org/abs/2611.12814v1
type: paper-summary
date: 2026-11-11
source_paper: 2026-11-09_18-19-30Z_CurbsideChatbots_AuditingtheMentalHealthInterventi.md
generated_at: 2026-11-11 22:08
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper audits the mental health interventions that 41 large language models recommend when the same clinical vignette is presented from three different perspectives: a clinician describing a patient, a caregiver describing a loved one, or a person describing their own symptoms. Across 19 case vignettes and five questions, the authors collected 35,055 free-text responses and used a validated judge to extract every intervention named, while also having 29 models rate full option lists on a seven-point Likert scale. The central finding is that models largely recommend what they themselves rate highly, but recommendation behavior shifts significantly depending on who is asking, with clinicians receiving consultation-style responses and lay users receiving hedged, simplified advice.

## Key Takeaways
- Models produce systematically different recommendations based on the "footing" of the questioner: when a clinician asks, models generate consultation-style, technically detailed responses, whereas when a caregiver or patient asks, models produce hedged, simplified advice that may omit critical interventions or soften urgency, raising concerns about whether lay users receive adequate clinical guidance.
- When models are asked to recommend a specific intervention type, they more frequently name options they themselves rated below zero on the Likert scale as initial choices, typically attaching conditions or caveats, suggesting a disconnect between models' internal quality assessments and their outward recommendations.
- The study collected 35,055 free-text responses across 41 models and 19 vignettes, and the authors plan to release the instrument, code, and full corpus as a "living audit," making this a reproducible and extensible benchmark for ongoing evaluation of LLM mental health guidance.

## Context
As large language models increasingly serve as informal mental health information sources for patients, caregivers, and even clinicians, there is limited systematic evidence about whether these models provide clinically appropriate, audience-appropriate, and internally consistent recommendations. This paper addresses a critical gap in AI safety and clinical AI evaluation by auditing model behavior across multiple stakeholder perspectives rather than treating all users as a single audience, reflecting the real-world diversity of how people interact with AI for health questions.

## Implications
For clinicians and mental health practitioners, the finding that models tailor advice differently depending on who asks suggests that patients and caregivers may receive materially less rigorous or less complete guidance than professionals, potentially affecting treatment-seeking behavior and informed consent. For AI developers and regulators, the disconnect between models' internal quality ratings and their outward recommendations highlights the need for transparent auditing frameworks and standardized evaluation instruments before LLM-based mental health tools are deployed at scale. The authors' commitment to releasing a living audit instrument provides a reusable resource for the field to track model behavior over time as models evolve.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.12814v1)
