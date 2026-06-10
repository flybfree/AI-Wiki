---
title: 'Gender-Dependent Diagnostic Substitution in LLM Medical Triage: Same Symptoms, Unequal Urgency'
published: 2026-06-02T13:35:12Z
authors: Qi Han Wong
url: http://arxiv.org/abs/2606.03641v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gender-Dependent Diagnostic Substitution in LLM Medical Triage: Same Symptoms, Unequal Urgency

## Abstract
We investigate whether large language models produce different medical triage recommendations for identical neurological symptoms when only the patient's stated gender and age vary. Using three model families--Gemini 3.5 Flash, Claude Sonnet 4.6, and GPT-5.4-mini--we present a standardized symptom profile (persistent headache, blurred vision, morning nausea, visual disturbances) across seven demographic conditions: three age groups (25, 38, 65) x two genders (male, female), plus a gender-unspecified baseline (n = 30 per condition per model, 630 total trials). We find a stark, systemic gender-dependent triage disparity: young women receive significantly lower emergency room (ER) referral rates than age-matched men (Gemini: 0% vs. 23.3%; Claude: 6.7% vs. 96.7%; GPT: 6.7% vs. 66.7%, all p < 0.001). The disparity disappears at age 65 for all models. The primary mechanism is diagnostic substitution: the models anchor on a gender-associated diagnosis, preferentially classifying young women with Idiopathic Intracranial Hypertension (IIH)--a condition epidemiologically linked to women of childbearing age--while diagnosing men with generic increased intracranial pressure with space-occupying lesions in the differential. This diagnostic closure routes female patients to lower-urgency care (outpatient doctor appointments) despite comparable severity ratings (7-9/10). Our findings demonstrate that clinical LLMs replicate documented human clinical biases by using epidemiological priors to suppress triage urgency, suggesting that AI triage engines must decouple urgency assessment from probabilistic diagnostic priors. We release all code, prompts, and raw results.

## Metadata
- **Published**: 2026-06-02T13:35:12Z
- **Authors**: Qi Han Wong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.03641v1)