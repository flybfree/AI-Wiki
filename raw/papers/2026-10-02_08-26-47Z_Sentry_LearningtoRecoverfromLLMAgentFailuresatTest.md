---
title: Sentry: Learning to Recover from LLM Agent Failures at Test Time
published: 2026-10-02T08:26:47Z
authors: Changxiu Ji, Amy Lu, Qizheng Zhang, Kunle Olukotun
url: http://arxiv.org/abs/2610.02994v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sentry: Learning to Recover from LLM Agent Failures at Test Time

## Abstract
LLM agents often fail mid-task due to invalid tool calls, repeated actions, or poorly grounded reasoning, and learning from these failures is a path to reliability. We find that how failure knowledge reaches the agent matters as much as what it contains. Failure lessons are conditional: kept in the agent's context, they misfire when their failure is absent, and removing them from an evolving playbook improves performance. Runtime interventions, in contrast, act only when a failure occurs but do not learn from their repairs. We argue that failure knowledge is conditional knowledge and should be conditionally exposed, and instantiate this principle in Sentry, a failure-management layer that runs alongside the agent. When Sentry detects a failure, it retrieves matching lessons from an external playbook to guide recovery, verifies without access to task rewards whether the agent recovered, and stores a new lesson only if it did; the full playbook never enters the agent's context. Across multiple agentic benchmarks, Sentry outperforms the strongest runtime-intervention baseline on every benchmark, by 37\% on average, and the strongest context-evolution baseline by 39\% on the two benchmarks where both are evaluated; combining Sentry with context evolution yields further gains. Learned lessons transfer to held-out tasks, and controlled experiments show that exposing the full playbook to the agent lowers performance even when relevant lessons remain available on demand.

## Metadata
- **Published**: 2026-10-02T08:26:47Z
- **Authors**: Changxiu Ji, Amy Lu, Qizheng Zhang, Kunle Olukotun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02994v1)