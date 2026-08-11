---
title: PROSLEX: A Novel Dataset for Expert-Annotated Legal Statute Prediction for Indian Judiciary
url: http://arxiv.org/abs/2608.08830v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_17-24-09Z_PROSLEX_ANovelDatasetforExpert_AnnotatedLegalStatu.md
generated_at: 2026-08-10 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PROSLEX, a dataset of 1,623 expert‑annotated Indian legal documents that includes both statute predictions and detailed explanations for each prediction. The study evaluates multiple prompting strategies—zero‑shot, few‑shot, chain‑of‑thought, and tree‑of‑thoughts—to generate accurate statutes along with coherent legal rationales. Results show that while predictive performance improves with richer prompting, the quality of explanations remains a key challenge.

## Key Takeaways
- The dataset provides 7,450 expert explanations, highlighting the importance of capturing underlying legal reasoning for explainable AI in judicial settings.
- Evaluation demonstrates that tree‑of‑thoughts prompting yields the most coherent and legally valid rationales compared to simpler chain‑of‑thought methods.
- Current LLM approaches prioritize accuracy metrics but neglect the need for transparent, justifiable explanations, a gap PROSLEX addresses.

## Context
Legal Statute Prediction is a multi‑label classification problem within natural language processing that aims to match factual descriptions with relevant statutes. Recent work has leveraged Large Language Models to boost prediction rates, yet most evaluations focus solely on accuracy without assessing the interpretability of generated outputs. This paper fills that gap by integrating legal reasoning into both prediction and explanation generation.

## Implications
For AI researchers, PROSLEX offers a benchmark for building explainable systems that can support judges and lawyers with transparent reasoning. In practice, such tools could enhance decision‑making transparency in Indian courts and promote trust in automated legal assistance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08830v1)
