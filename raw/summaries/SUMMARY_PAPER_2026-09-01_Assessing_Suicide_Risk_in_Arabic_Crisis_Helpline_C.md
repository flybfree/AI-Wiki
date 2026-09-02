---
title: Assessing Suicide Risk in Arabic Crisis Helpline Calls: A Comparison of Arabic and English Large Language Models
url: http://arxiv.org/abs/2609.00191v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_18-11-36Z_AssessingSuicideRiskinArabicCrisisHelplineCalls_AC.md
generated_at: 2026-09-01 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This study evaluates Arabic and English large language models for suicide risk classification using de‑identified transcripts from Lebanon’s National Lifeline, achieving high performance on both tasks. The best model reached macro‑F1 81.19 and ROC‑AUC 90.61 in Arabic and 85.00/92.59 in English. Translation to English did not degrade results.

## Key Takeaways
- De‑identified transcripts were processed locally, keeping audio within the helpline privacy constraints while enabling LLM fine‑tuning.
- High‑risk suicidal ideation was classified more accurately than low‑severity cases across both languages.
- Model performance remained strong after translating Arabic transcripts to English, indicating robust cross‑lingual capability.

## Context
Natural language processing for mental health crisis triage is emerging as a way to reduce manual workload and improve consistency. This work demonstrates that LLMs can operate on sensitive data without violating privacy policies, offering a scalable alternative to human operators.

## Implications
Operators could integrate these models into existing workflows to flag high‑risk calls quickly, freeing staff for higher‑severity cases. The findings suggest that AI‑driven risk assessment is feasible even in resource‑limited settings where audio data cannot leave the call center.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00191v1)
