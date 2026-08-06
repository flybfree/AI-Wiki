---
title: Causal Evidence Extraction and Triangulation in Crisis Reports using Large Language Models: A ReliefWeb-based Study
url: http://arxiv.org/abs/2608.04576v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_08-07-15Z_CausalEvidenceExtractionandTriangulationinCrisisRe.md
generated_at: 2026-08-05 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This study proposes a two‑stage Large Language Model pipeline for extracting structured causal evidence from humanitarian crisis reports on ReliefWeb, focusing on cash assistance and food outcomes between 2000 and 2024. The pipeline combines query‑conditioned extraction to limit results to specific intervention classes with snippet grounding for auditability, achieving high precision in an expert‑annotated dataset where the best closed‑source LLM reached a weighted F1 of 90.73% and Llama‑3.1‑8B fine‑tuned to 94.15%.

## Key Takeaways
- The query‑conditioned extraction reduces retrieval‑induced over‑extraction by restricting output to a defined intervention class, improving relevance and efficiency.
- Snippet grounding links each extracted relation to its supporting text, providing transparency and enabling reliable classification within the disaster × source cell framework.
- Context‑preserving triangulation aggregates strength‑weighted evidence across cells, using Laplace smoothing and equal weighting to compute a Level‑of‑Evidence score that quantifies cross‑context convergence.

## Context
The work addresses a growing need for automated, interpretable causal inference in long, noisy humanitarian texts where manual coding is costly. By leveraging LLMs with structured output and grounding mechanisms, the approach aligns well with current trends toward explainable AI and evidence‑based decision support in crisis management.

## Implications
Practitioners can rely on this pipeline to quickly surface actionable causal links for interventions such as cash assistance or food aid, reducing bias and increasing confidence in policy decisions. The Level‑of‑Evidence score offers a quantitative metric that can be integrated into larger monitoring systems, enhancing transparency and accountability across humanitarian operations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04576v1)
