---
title: Polish Medical Visual Question Answering: Vision-Language Models Underutilize Visual Evidence
url: http://arxiv.org/abs/2608.12928v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_08-07-22Z_PolishMedicalVisualQuestionAnswering_Vision_Langua.md
generated_at: 2026-08-13 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a Polish-language medical VQA benchmark using Board Certification Examination questions and evaluates open-weight and commercial vision‑language models. Results show the best model reaches 79% accuracy, which is close to but not exceeding human reference scores on a subset of tasks. The study also finds that models rely more on question text than from the accompanying medical image and perform worse on questions where visual cues dominate.

## Key Takeaways
- The benchmark demonstrates that Polish medical VQA tasks remain challenging with top‑performing models achieving 79% accuracy, which is close to but not exceeding human reference scores.
- Models extract more useful information from the textual part of an input than from the accompanying medical image and perform worse on questions where visual cues dominate.
- Even when images or questions are omitted, models still answer above chance by leveraging answer choices alone.

## Context
Medical VQA is a rapidly growing subfield that aims to integrate visual data with clinical knowledge for decision support. This Polish‑specific benchmark highlights the gap between generic vision‑language systems and domain‑tailored medical queries, underscoring the need for culturally and linguistically adapted datasets.

## Implications
Clinicians and developers must recognize that current models underperform when visual evidence is critical, suggesting a shift toward multimodal architectures that weight image information appropriately. The findings also imply that relying solely on textual cues may lead to suboptimal clinical decisions in Polish medical contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12928v1)
