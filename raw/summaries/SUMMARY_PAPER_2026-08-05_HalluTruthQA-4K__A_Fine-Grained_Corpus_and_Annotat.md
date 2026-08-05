---
title: HalluTruthQA-4K: A Fine-Grained Corpus and Annotation Process for Arabic Hallucination Detection and Truth Verification
url: http://arxiv.org/abs/2608.03966v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_17-33-38Z_HalluTruthQA_4K_AFine_GrainedCorpusandAnnotationPr.md
generated_at: 2026-08-05 01:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces HalluTruthQA-4K, a fine‑grained Arabic hallucination detection dataset that expands the original HalluTruthQA resource to 4,000 expert‑curated question‑answer pairs across Islamic knowledge, history, science, and geography. The corpus provides model responses, reference answers, distractors, character‑level erroneous spans, human explanations, and hierarchical hallucination types, enabling detailed error analysis beyond binary labeling.

## Key Takeaways
- 1643 hallucinated responses are annotated with precise character‑level erroneous spans and accompanying human explanations.
- The dataset contains 1843 annotated erroneous spans, allowing researchers to locate exact mistakes in generated text.
- There are 2357 non‑hallucinated responses, providing a balanced reference for evaluating model reliability.

## Context
Large language models generate fluent Arabic answers but often embed factual errors that are hard to detect automatically. Existing resources typically label entire responses as hallucinated or not, limiting the ability to pinpoint erroneous content and correct it. This work addresses that gap by creating a richly annotated dataset that supports span‑level error localization.

## Implications
For AI researchers, HalluTruthQA-4K offers a reusable benchmark for evaluating factual reliability in Arabic language models. Practitioners can leverage its detailed annotations to improve hallucination detection pipelines and generate human explanations, thereby enhancing trustworthiness of model outputs in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03966v1)
