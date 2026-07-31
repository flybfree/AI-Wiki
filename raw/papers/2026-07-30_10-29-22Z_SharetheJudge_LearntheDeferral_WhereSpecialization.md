---
title: Share the Judge, Learn the Deferral: Where Specialization Helps LLM Evaluation
published: 2026-07-30T10:29:22Z
authors: Weining Zhang
url: http://arxiv.org/abs/2607.27984v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Share the Judge, Learn the Deferral: Where Specialization Helps LLM Evaluation

## Abstract
Agentic systems have widened the gap between producing candidate outputs and reviewing them. This paper asks a practical architectural question: should domain specialization be built into an evaluator's weights, or into the rule that decides when its judgment can be trusted? We study 99,952 public, rubric-conditioned examples. Supplying the correct rubric improves locked-test accuracy by 2.11 points over a response-only control; replacing it with an unrelated rubric costs 2.66 points. Dividing the same training corpus among eight criterion-family LoRA judges, however, loses 10.05 points and cuts audited coverage at a 5% risk target from 24.44% to 5.43%. Matching the bank's stored capacity with one rank-64 adapter does not reproduce this loss. Nor is the result explained by learning rate or optimizer steps. Initializing the family adapters from a shared, trained judge recovers test accuracy to 76.85%, 19.94 points above scratch training at the same learning rate (95% interval 18.88-21.02). The result changes when specialization governs deferral rather than judgment. On RewardBench 2, learned correctness heads route examples through a 0.6B-4B-8B cascade without changing any reward score. Across 20 locked repartitions, the cascade attains 89.40% accuracy, compared with 84.75% for 8B alone, at 0.415 normalized parameter compute. Every run passes an exact one-sided 95% risk audit; margin-based rules remain near 84.8% accuracy while using at least 0.94 compute. These results suggest a qualified design rule: share the learning of judgment until there is enough data to justify a split, and place domain-specific adaptation in an audited release boundary.

## Metadata
- **Published**: 2026-07-30T10:29:22Z
- **Authors**: Weining Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27984v1)