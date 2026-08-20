---
title: Improving Natural-Language Combinatorial-Optimization Accuracy in Resource-Constrained Language Models via Formal Abstractions
published: 2026-08-19T00:36:43Z
authors: Shrenil Shaun Sharma, Avi Sharma
url: http://arxiv.org/abs/2608.18409v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Improving Natural-Language Combinatorial-Optimization Accuracy in Resource-Constrained Language Models via Formal Abstractions

## Abstract
Combinatorial scheduling poses a significant challenge for language models, requiring them to identify feasible solutions within exponentially large search spaces while satisfying complex constraints. This challenge is especially pronounced in resource-constrained settings, where larger language models are impractical and selection is limited to smaller models which often fail to preserve feasibility when scheduling directly from natural language. To address these limitations, we introduce SDDL, a neuro-symbolic framework that translates natural-language scheduling problems into compact, solver-aligned representations of tasks, resources, constraints, and objectives, while delegating low-level modeling and search to a deterministic compiler and external solver. On a 300-instance, multi-family subset of scheduling problems, SDDL improves independently verified feasibility for every resource-constrained model tested. The two strongest SDDL configurations reach 55.3% and 28.3%, up from direct-generation baselines of 23.7% and 1.3% and solver-code baselines of 21.7% and 7.0%, with a 0.0% median optimality gap among feasible schedules. By expressing problem structure rather than generating solutions or solver code, SDDL enables smaller models to approach the strongest evaluated direct- and solver-code configurations, including substantially larger frontier models.

## Metadata
- **Published**: 2026-08-19T00:36:43Z
- **Authors**: Shrenil Shaun Sharma, Avi Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18409v1)