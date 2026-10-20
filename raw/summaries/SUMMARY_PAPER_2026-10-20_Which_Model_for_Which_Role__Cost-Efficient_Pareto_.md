---
title: Which Model for Which Role? Cost-Efficient Pareto Recommendation for LLM Agentic Workflows
url: http://arxiv.org/abs/2610.26676v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_16-25-07Z_WhichModelforWhichRole_Cost_EfficientParetoRecomme.md
generated_at: 2026-10-20 00:03
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Cost-Coupled Gittins (CC-Gittins), a multi-objective search algorithm designed to efficiently recommend optimal model-to-role assignments in LLM agentic workflows where users face trade-offs between task quality, deployment cost, and latency. The method exploits the coupling between evaluation and deployment costs to reduce the search overhead, achieving substantial recovery of the true Pareto frontier at roughly 10% of exhaustive evaluation cost, with most of the frontier recovered by 30% of the search budget.

## Key Takeaways
- CC-Gittins extends the single-objective cost-aware Gittins index framework into a multi-objective Pareto recommendation setting, alternating between seeking higher quality and lower deployment cost while reusing each evaluation to inform both search directions simultaneously, thereby halving the effective search cost compared to independent searches.
- The algorithm exploits a critical coupling insight: assignments that are more expensive to deploy are also more expensive to evaluate, meaning the search budget spent on evaluation is inherently proportional to deployment cost, allowing the algorithm to prioritize exploration of cheaper candidates first and build uncertainty-adjusted estimates incrementally.
- Evaluation across eight quality-cost matrices spanning workflows with two to five roles and up to 1,681 candidate assignments demonstrates that CC-Gittins recovers a substantial fraction of the true Pareto frontier at approximately 10% of exhaustive-evaluation cost, and recovers most of the frontier with few false positives by 30%, including experiments incorporating latency as a third objective.

## Context
As LLM agentic workflows mature into production systems, practitioners increasingly compose pipelines using heterogeneous models assigned to specialized roles such as planning, retrieval, reasoning, and output generation. The combinatorial space of model-role assignments grows rapidly with the number of roles and available candidates, making exhaustive evaluation infeasible. This paper addresses a practical gap in the literature: while prior work on model selection and routing focuses on single-objective optimization, real users need Pareto-optimal recommendations across quality, cost, and latency simultaneously, and the search itself carries non-trivial evaluation costs that must be accounted for in the algorithm design.

## Implications
For practitioners deploying multi-model agentic systems, CC-Gittins provides a principled, budget-aware method to identify viable model assignments without exhaustively benchmarking every candidate, reducing both experimentation cost and time-to-deployment. For the broader research community, the coupling-based search strategy offers a template for multi-objective optimization problems where evaluation and deployment costs are correlated, potentially applicable to hardware selection, data pipeline design, and other resource-constrained allocation tasks in AI systems engineering.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26676v1)
