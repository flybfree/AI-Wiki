---
title: Sign Language Question Answering: A New Task, Benchmark, and Baseline for Sign Language Understanding
url: http://arxiv.org/abs/2607.27826v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_08-05-26Z_SignLanguageQuestionAnswering_ANewTask_Benchmark_a.md
generated_at: 2026-07-30 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Sign Language Question Answering (SLQA) as a new task to evaluate sign language understanding beyond fixed recognition and translation tasks. It creates two benchmarks from PHOENIX14T and CSL-Daily that generate question-answer pairs across five reasoning categories. Their baseline model with a question-conditioned temporal downsampling outperforms vision-language models.

## Key Takeaways
- The proposed SLQA task requires models to answer arbitrary natural language questions about sign videos, assessing reasoning beyond fixed mappings.
- Two benchmarks are built using templates that automatically generate QA pairs from existing gloss and sentence annotations covering position reasoning, structural reasoning, visual search, gloss recognition, and translation understanding.
- Their baseline model incorporates a question-conditioned temporal downsampling module and in-domain knowledge transfer, achieving consistent gains across all categories.

## Context
This work addresses the limitation of SLU benchmarks that focus on specific tasks like continuous recognition or translation. By introducing a flexible QA framework, it provides a more holistic assessment of semantic understanding in sign language. The approach aligns with broader efforts to evaluate multimodal models using reasoning tasks rather than task-specific metrics.

## Implications
Practitioners can use SLQA as a benchmark to compare new SLU systems, guiding development toward richer understanding. Industry interest may arise for assistive technologies that require comprehension of diverse sign inputs beyond simple translation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27826v1)
