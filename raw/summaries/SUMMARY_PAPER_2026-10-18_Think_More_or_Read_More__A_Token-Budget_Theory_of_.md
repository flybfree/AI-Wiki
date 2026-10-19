---
title: Think More or Read More? A Token-Budget Theory of Reasoning with Shared Context
url: http://arxiv.org/abs/2610.23246v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_10-18-15Z_ThinkMoreorReadMore_AToken_BudgetTheoryofReasoning.md
generated_at: 2026-10-18 20:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a token-budget theory that formalizes the trade-off between reading additional context (such as peer outputs in multi-agent debate or self-generated drafts in self-refinement) and the remaining reasoning capacity available to a model within a fixed token window. The authors derive closed-form predictions for optimal group sizes in multi-agent debate and demonstrate empirically across five open models and four reasoning tasks that self-consistency matches or outperforms deployed debate in 93% of matched settings, with the advantage growing as the shared window tightens. The central finding is that under a shared token budget, preserving reasoning room matters more than acquiring additional context.

## Key Takeaways
- The token-budget theory models accuracy as a function of the reasoning budget remaining after reading, using a Condorcet jury model that permits correlated errors among agents. This yields a closed-form prediction for the optimal number of debate agents, which can be estimated from single-agent measurements alone, eliminating the need to run expensive multi-agent debates to determine group size. The framework extends naturally to heterogeneous model ensembles.
- Communication (reading peers' outputs or one's own drafts) pays off only when the gain in the accuracy ceiling exceeds the reasoning room consumed by reading, and this condition tightens as the token window shrinks. Empirically, at the predicted optimal group size, the method outperforms strong baselines under the tightest calibration budgets where debate-calibrated rules can afford only one or two questions.
- Across 980 matched window-and-group-size settings, self-consistency matches or beats deployed debate in 93% of cases, with the performance gap largest under tight windows and nearly vanishing at loose windows, directly confirming the theoretical prediction that shared-context reasoning systems degrade as the budget for thinking is squeezed by the budget for reading.

## Context
Modern reasoning systems increasingly rely on multi-agent debate, self-refinement, and retrieval-augmented generation to improve answer quality, all of which consume the model's finite context window. As models are deployed with fixed context limits in production settings, the assumption that more context always helps breaks down when reading tokens directly displace reasoning tokens. This paper addresses a gap in the literature by providing a unified analytical framework that treats reading and thinking as competing claims on a single budget, rather than treating them as independent improvements.

## Implications
For practitioners deploying reasoning agents under strict token budgets, this work suggests that investing in a single model's reasoning depth often outperforms orchestrating multi-agent debate or self-refinement loops, particularly when context windows are constrained. For the broader field, the token-budget theory offers a principled calibration tool: system designers can estimate optimal group sizes from single-agent benchmarks without running costly multi-agent experiments, reducing compute overhead in agentic pipelines. The finding also challenges the prevailing assumption that more context or more agents always improve performance, urging a re-evaluation of how reasoning systems allocate their finite token windows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23246v1)
