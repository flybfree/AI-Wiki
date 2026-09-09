---
title: MOAE: Multi-Objective Agent Evolution with Pareto-Preserving Search
published: 2026-09-05T09:31:34Z
authors: Hengle Jiang, Qijun Cai, Ziying Luo, Ke Tang
url: http://arxiv.org/abs/2609.05992v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MOAE: Multi-Objective Agent Evolution with Pareto-Preserving Search

## Abstract
As LLM-based agents continue to advance, their evaluation has become increasingly multifaceted: a capable agent must not only achieve high task completion accuracy but also perform well in interaction quality, safety, and efficiency, raising a central question: can these objectives be optimized simultaneously? Existing methods have considered multiple objectives, but many collapse heterogeneous measurements into a fixed scalar score. Such scalarization depends on metric normalization and preference weights and may discard candidates that represent useful deployment trade-offs. We introduce Multi-Objective Agent Evolution (MOAE), which organizes iterative in-context refinement as a Pareto-preserving evolutionary search over complete agent rollouts. Given a limited rollout budget, MOAE maintains an empirical archive of non-dominated candidates, uses objective-specific diagnostics to guide offspring generation, and applies constraint-aware selection only at deployment. This separates candidate preservation during search from the preference used to return a final solution. The procedure requires no parameter updates and allows each objective to be replaced by any measurable property, which we instantiate as task performance, trajectory quality, and safety. Experiments on TravelPlanner and AgentDojo show that MOAE consistently improves task performance and trajectory quality while maintaining strong safety under matched rollout budgets. Search-behavior analysis further shows that Pareto preservation expands the attainable objective region and increases the frequency of joint improvement. These results demonstrate the potential of Pareto-preserving in-context evolution for optimizing multiple agent properties without committing to a fixed scalarization during search.

## Metadata
- **Published**: 2026-09-05T09:31:34Z
- **Authors**: Hengle Jiang, Qijun Cai, Ziying Luo, Ke Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05992v1)