---
title: Auditing Agent Actions through Query-Conditioned Attribution
published: 2026-09-27T15:37:05Z
authors: Yifan Liu, Praveen Venkateswaran, Abdulhamid Adebayo, Dong Wang
url: http://arxiv.org/abs/2609.33676v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditing Agent Actions through Query-Conditioned Attribution

## Abstract
LLM agents increasingly take consequential actions through interactions with users, policies, and external tools. Auditing these agents requires automated attribution of realized actions to their historical basis. However, existing attribution formulations do not provide question-specific traces for diverse auditing objectives. Additionally, when access to the acting model is limited (e.g., in API-only deployments), applicable methods commonly rely on costly input perturbations or external LLM analysis of complete trajectories. We therefore formulate $\textit{query-conditioned agent action attribution}, a new task that takes a natural-language auditing query as input and recovers the source and ordered intermediate evidence for the query-specified aspect of an action. We instantiate this task with $A^3Bench$, a benchmark comprising 1,396 auditing queries across policy basis, parameter provenance, failure propagation, and unsafe-behavior tracing. To enable efficient, query-specific attribution, we use small open-weight models as attribution proposers that combine query-conditioned gradient saliency with query-semantic relevance to rank history units. Our proposer consistently achieves stronger source and evidence rankings at lower inference cost than open-weight baselines, improving source MRR by up to 40.9\% and evidence MAP by 42.1\% with only two forward passes and one backward pass. Controlled evaluations confirm that our proposer improves attribution specificity by adapting its rankings to fine-grained changes in the auditing query. Building on a proposer ensemble, our end-to-end system surpasses the strongest frontier-model baseline in source accuracy (64.5\% vs.\ 60.4\%) while reducing empirical deployment latency by 29.9\% relative to the fastest frontier API baseline. Code and data will be released after the initial review period following final validation and cleanup.

## Metadata
- **Published**: 2026-09-27T15:37:05Z
- **Authors**: Yifan Liu, Praveen Venkateswaran, Abdulhamid Adebayo, Dong Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33676v1)