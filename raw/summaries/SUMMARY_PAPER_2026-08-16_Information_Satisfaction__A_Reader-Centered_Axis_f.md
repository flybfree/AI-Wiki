---
title: Information Satisfaction: A Reader-Centered Axis for Summarization Evaluation
url: http://arxiv.org/abs/2608.14457v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_16-41-23Z_InformationSatisfaction_AReader_CenteredAxisforSum.md
generated_at: 2026-08-16 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a reader‑centered evaluation framework for summarization that measures how well a summary satisfies the informational needs of a specific user persona rather than relying on generic metrics like ROUGE or BERTScore. Experiments show that many popular metrics, including LLM‑based judges, are insensitive to changes in content relevance and do not align with human judgments of information satisfaction.

## Key Takeaways
- Popular summarization metrics fail basic perturbation tests because they ignore differences between informational needs across user roles such as a biomedical researcher versus a family doctor.  
- The paper demonstrates that LLM‑as‑judge scores are similarly uninterested in persona‑specific relevance, leading to misleading performance estimates.  
- Human evaluations based on a defined background consistently rank summaries higher when they match the reader’s expertise and use case.

## Context
Current summarization evaluation largely treats all readers as equivalent, overlooking how domain expertise shapes information requirements. This oversight limits the usefulness of automated metrics in real‑world applications where personalized content delivery is crucial.

## Implications
For practitioners developing adaptive summarization systems, this research calls for incorporating persona awareness to improve relevance and user satisfaction. The field must move beyond generic quality scores toward assessments that reflect actual informational utility for diverse audiences.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14457v1)
