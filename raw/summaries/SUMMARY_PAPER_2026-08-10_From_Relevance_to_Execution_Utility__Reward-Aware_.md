---
title: From Relevance to Execution Utility: Reward-Aware Dynamic Execution Gating for Skill-Based LLM Agents
url: http://arxiv.org/abs/2608.09168v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_06-28-25Z_FromRelevancetoExecutionUtility_Reward_AwareDynami.md
generated_at: 2026-08-10 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces RADEG, a lightweight decision layer that predicts the execution utility of a query‑bundle pair before launching an expensive rollout. By learning a low‑cost surrogate model, it reduces unnecessary agent executions while preserving most verifier reward. Experiments on 288 held‑out rollouts show RADEG outperforms relevance‑based and random gating across various execution budgets.

## Key Takeaways
- RADEG learns a low‑cost surrogate model that predicts the execution utility of a query‑bundle pair before launching an expensive rollout, enabling early filtering.
- It uses locally perturbed same‑query rollouts to isolate bundle composition effects on verifier reward, providing informative supervision while controlling task difficulty.
- Deployment updates only a warm‑started logistic head as new feedback arrives, allowing inexpensive adaptation without retraining the retriever or agent.

## Context
In the rapidly expanding field of skill‑based LLM agents, efficient execution gating is a bottleneck because retrieving plausible bundles does not guarantee worthwhile outcomes. Current relevance‑driven methods either incur high compute or ignore utility, limiting scalability and practical deployment.

## Implications
For practitioners, RADEG offers an inexpensive way to adapt the execute/skip boundary as new task feedback arrives, enabling continuous improvement without retraining core components. This makes large‑scale deployment of skill‑augmented agents more feasible and cost‑effective.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09168v1)
