---
title: MIRA-Ev:A Benchmark for Granular Evidence Detection and Relational Reasoning in Clinical Exams
url: http://arxiv.org/abs/2607.19201v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_15-34-44Z_MIRA_Ev_ABenchmarkforGranularEvidenceDetectionandR.md
generated_at: 2026-07-23 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
MIRA‑Ev is a new benchmark for detecting granular evidence in clinical exams and classifying the relational links between premises, claims, and support or attack statements. The dataset consists of re‑annotated cases from Spanish, English, and Basque versions of the MIR exam, organized into three tasks: sentence retrieval, argumentative component extraction, and relation classification.

## Key Takeaways
- MIRA‑Ev introduces a clinical argument mining benchmark that evaluates models not only on final answer accuracy but also on how well they ground diagnoses in relevant evidence.  
- The dataset is built from licensed exam cases annotated by expert clinicians with span‑level premises, claims, and directed support/attack relations, making it the first clinical argumentation resource available in Basque.  
- Evaluation is structured into a three‑tier hierarchy: retrieving supporting sentences, extracting argumentative components, and classifying the type of relation between them.

## Context
Current AI research in medical natural language processing focuses on end‑to‑end question answering that ignores intermediate reasoning steps, limiting diagnostic transparency. MIRA‑Ev addresses this gap by providing a fine‑grained, multilingual resource that forces models to reason about evidence rather than just produce correct answers.

## Implications
For clinicians and AI developers, MIRA‑Ev highlights the need for explainable models that can trace decisions to specific textual evidence, improving trust in clinical decision support systems. The benchmark’s inclusion of Basque also underscores the importance of multilingual argument mining for diverse healthcare populations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19201v1)
