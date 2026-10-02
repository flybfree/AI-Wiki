---
title: Legal Research Bench: Measuring End-to-End Reliability in Long-Horizon Legal Research Agents
url: http://arxiv.org/abs/2610.00609v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-09-30_19-13-16Z_LegalResearchBench_MeasuringEnd_to_EndReliabilityi.md
generated_at: 2026-10-01 21:14
model: qwen3.6-35b-a3b
---

## Summary
Legal Research Bench introduces a benchmark of 413 open-ended U.S. legal research questions to evaluate the end-to-end reliability of AI agents in complex, retrieval-intensive workflows. The study assesses thirteen frontier models using tools for web and case-law search, revealing that even the strongest model achieves full correctness on only 42.9% of tasks, underscoring significant challenges with missing authorities, stale citations, and conflicting information.

## Key Takeaways
- The Legal Research Bench comprises 413 expert-authored questions paired with gold answers, supporting authorities, and binary grading rubrics, utilizing an all-pass grading mechanism where responses are deemed correct only if every criterion is satisfied and cited sources are verified against the ground truth.
- Model performance exhibits substantial variance across different legal domains and task types; specifically, tasks requiring the reconciliation of conflicting authorities demonstrate significantly lower success rates compared to other question categories, indicating difficulty in synthesizing contradictory information.
- Analysis shows that increasing agent complexity does not yield proportional gains in accuracy; metrics such as the number of interaction turns, frequency of tool calls, and inference costs fail to predict higher correctness across models, suggesting current scaling approaches may be inefficient for legal reliability.

## Context
This research addresses a critical gap in evaluating AI agents for professional domains where high stakes demand rigorous verification beyond superficial plausibility. By focusing on

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.00609v1)
