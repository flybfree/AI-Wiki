---
title: Structured Output Collapses Answer Diversity Across 44 Language Models
url: http://arxiv.org/abs/2607.18476v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_19-47-16Z_StructuredOutputCollapsesAnswerDiversityAcross44La.md
generated_at: 2026-07-23 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how a simple instruction to reply in JSON only reduces answer diversity across 44 language models, revealing that the model’s response is shaped more by its training on structured formats than by any decoder constraints. The modal answer becomes dominant in many prompts, while distinct alternatives decline sharply, indicating a systematic collapse of diversity.

## Key Takeaways
- The presence of a JSON‑only format clause causes six out of forty‑four models to shift their answers toward the most frequent option, with the most distinctive models moving first and the least diverse ones remaining static.  
- A within‑run re‑sample shows that 53 % of a model’s stable chat defaults revert to crowd‑sourced choices when JSON is required, while some models adopt completely new defaults absent from normal conversation.  
- The compression effect is format‑specific: JSON and XML incur measurable surprisal reduction (≈0.2 bits), whereas YAML and CSV show none, suggesting the collapse is tied to the model’s learned response style rather than decoder enforcement.

## Context
This work highlights a subtle but significant divergence between how language models behave in conversational settings versus when their output is constrained to structured data formats. It underscores that evaluation benchmarks often compare chat‑style outputs with artificially imposed JSON responses, potentially skewing fairness assessments of model diversity and performance.

## Implications
For developers, the findings suggest that relying solely on response format specifications may unintentionally homogenize model behavior, reducing the richness of generated answers. Practitioners should consider whether such constraints are necessary or if alternative evaluation metrics better capture genuine capability across diverse output styles.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18476v1)
