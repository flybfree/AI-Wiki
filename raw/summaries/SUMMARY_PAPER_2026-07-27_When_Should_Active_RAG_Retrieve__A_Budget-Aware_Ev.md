---
title: When Should Active RAG Retrieve? A Budget-Aware Evaluation of Utility, Calibration, and Cost
url: http://arxiv.org/abs/2607.24010v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_05-17-06Z_WhenShouldActiveRAGRetrieve_ABudget_AwareEvaluatio.md
generated_at: 2026-07-27 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a budget‑aware evaluation framework for active retrieval‑augmented generation (Active RAG) that measures the true value of retrieving information as marginal correctness gain rather than raw accuracy. It demonstrates that existing single‑point metrics can misrepresent performance, leading to misleading comparisons between different retrieval policies.

## Key Takeaways
- Retrieval is valuable only when it improves a no‑retrieval answer, so utility frontiers are defined by exact top‑k gains across the budget.
- Thresholds calibrated on past data may not meet future budgets, causing threshold‑transfer error that inflates or deflates reported usage.
- Simple uncertainty or score baselines can rival learned utility routers, highlighting the need for conservative budget frontiers and cost decompositions.

## Context
Active RAG systems operate under limited retrieval budgets, making them a practical concern in large language model deployment. Current evaluation practices often ignore these constraints, conflating accuracy with effective information use.

## Implications
For practitioners, reporting frontiers, realized usage, threshold errors, harm rates, and cost breakdowns will align research with real‑world budget limits. This shift encourages more transparent and actionable Active RAG studies across industry and academia.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24010v1)
