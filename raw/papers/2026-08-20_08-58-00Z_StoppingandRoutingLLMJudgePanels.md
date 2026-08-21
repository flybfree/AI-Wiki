---
title: Stopping and Routing LLM Judge Panels
published: 2026-08-20T08:58:00Z
authors: Bin Zhu, Yi Xie, Yanghui Rao
url: http://arxiv.org/abs/2608.19802v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stopping and Routing LLM Judge Panels

## Abstract
LLM evaluation pipelines often have many candidate judges: general LLM-as-a-judge prompts, reward models, safety classifiers, confidence variants, and task-specific verifiers. The deployment question is not only which judge is best, but which judges should be called, on which examples, and when panel construction should stop. We formulate judge-panel design as a role-conditioned allocation problem. From a small labeled audit set, declared slices, and judge costs, the method estimates target-relative roles: copies add no conditional information, complements improve the global panel, and specialists help only on slices. These roles induce a policy: drop copies, add complements globally, route specialists conditionally, and stop when validation gain falls below a threshold. Across reasoning, code, safety, preference, reward-model, summarization, and math audits, the method is compared with single judges, flat panels, matched diversity heuristics, full-call stacking, reliability juries, and frugal cascades. The result is a regime map for judge calls: route specialists on deployable slices, stop in saturated verifier regimes, keep broad ensembles when their risk benefit is worth the cost, and ignore conditional copies. The output is a reusable, auditable call plan for the next evaluation batch.

## Metadata
- **Published**: 2026-08-20T08:58:00Z
- **Authors**: Bin Zhu, Yi Xie, Yanghui Rao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19802v1)