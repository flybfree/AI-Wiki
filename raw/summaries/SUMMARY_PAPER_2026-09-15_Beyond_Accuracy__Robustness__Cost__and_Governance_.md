---
title: Beyond Accuracy: Robustness, Cost, and Governance Trade-offs for Vision-Language Models in Templated Document Extraction
url: http://arxiv.org/abs/2609.15706v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-14_15-10-33Z_BeyondAccuracy_Robustness_Cost_andGovernanceTrade_.md
generated_at: 2026-09-15 00:25
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This study addresses the lack of practical guidance for selecting vision-language models in business document extraction by evaluating eleven distinct systems across quality, latency, governance, and cost dimensions. The researchers demonstrate that fine-tuning open-source VLMs on a modest dataset can surpass zero-shot commercial models in F1 score, while also introducing an open-source decision framework to help practitioners navigate these operational trade-offs based on specific task requirements.

## Key Takeaways
- Fine-tuning five open-source VLMs on just 3,000 samples elevates their performance beyond an F1 of 0.98, outperforming every zero-shot commercial system tested on a held-out set of synthetic checks.
- Commercial models show significant variance in robustness, with GPT-5 achieving the highest overall F1 score while Claude Sonnet 4.5 exhibits severe failures specifically on date extraction tasks.
- The authors provide a practitioner-oriented selection framework that translates task profiles—encompassing quality thresholds, latency constraints, governance policies, and processing volume—into optimized model recommendations through filtering and total-cost minimization.

## Context
As organizations increasingly automate document processing pipelines, the reliance on vision-language models has grown alongside concerns about benchmark inflation and real-world reliability. This paper shifts focus from isolated accuracy metrics to a holistic evaluation that accounts for operational constraints like latency, data governance, and inference costs, reflecting a broader industry trend toward pragmatic AI deployment over theoretical performance peaks.

## Implications
Practitioners can leverage the proposed framework to make cost-aware model selections tailored to their specific compliance and throughput requirements rather than defaulting to the most expensive commercial APIs. The findings suggest that carefully fine-tuned open-source models may offer superior reliability and economic efficiency for high-volume document extraction, prompting enterprises to reconsider vendor lock-in strategies and internal ML infrastructure investments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.15706v1)
