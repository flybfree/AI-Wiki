---
title: Grammar Concept Annotation at Scale: Deployed Fine-Tuned Small Language Models Outperform Prompted Frontier Models
published: 2026-10-07T19:31:24Z
authors: Marjan Celikik, Ana Peleteiro Ramallo, Javier Morales
url: http://arxiv.org/abs/2610.10827v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Grammar Concept Annotation at Scale: Deployed Fine-Tuned Small Language Models Outperform Prompted Frontier Models

## Abstract
Corrective feedback is among the best-evidenced drivers of second-language acquisition, yet corrections delivered during lessons rarely accumulate into an actionable view of grammar mastery. Prompted frontier models can provide such a view from learner--tutor lesson transcripts, but they are costly at scale. We close this gap by fine-tuning Qwen3.5 small language models (SLMs) on filtered and rebalanced teacher-generated supervision, then deploying an efficient 0.8B model in an end-to-end grammar mastery tracker for all English learners on our platform. Internalizing the annotation contract into adapter weights enables pairing the 0.8B model with a compact matched prompt rather than verbose instructions. On two human-curated benchmarks, both the deployed 0.8B model and a 4B reference comparator outperform prompted GPT-5.4 and GPT-5.6 Sol in precision and recall under nested matching criteria of increasing strictness: concept, evidence span, and correctness. The deployed 0.8B SLM reduces serving cost by approximately 16$\times$. A feature-level online experiment shows significant gains in learner engagement ($+15.8\%$) and key business metrics, including scheduled hours ($+2.1\%$) and GMV from new lessons ($+13.2\%$).

## Metadata
- **Published**: 2026-10-07T19:31:24Z
- **Authors**: Marjan Celikik, Ana Peleteiro Ramallo, Javier Morales
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.10827v1)