---
title: Find Before You Fine-Tune: A Diagnostic Study of Small LLMs for Cybersecurity QA
url: http://arxiv.org/abs/2607.18725v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_05-32-40Z_FindBeforeYouFine_Tune_ADiagnosticStudyofSmallLLMs.md
generated_at: 2026-07-23 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FiT, a diagnostic framework for small LLMs in cybersecurity QA, and finds fine‑tuning harms vocabulary recognition and parametric knowledge while affecting instruction following differently under two regimes.

## Key Takeaways
- Fine‑tuning consistently degrades vocabulary recognition and parametric knowledge in 7‑billion‑parameter models regardless of regime. - Knowledge‑focused tuning causes moderate degradation that preserves ranking, whereas instruction‑focused tuning induces abstention, collapsing measured knowledge and reversing the ranking while leaving retrieval‑grounded contextualization unchanged.

## Context
Cybersecurity QA demands reliable small LLMs that retain domain vocabulary and up‑to‑date parametric facts. Current practice often fine‑tunes models without diagnostic checks, risking performance loss. This study offers a systematic way to assess suitability before adaptation.

## Implications
Practitioners can use FiT scores to screen models, avoid unnecessary training, and reduce hallucination risks. The framework supports safer deployment of small LLMs in high‑stakes security pipelines where knowledge integrity is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18725v1)
