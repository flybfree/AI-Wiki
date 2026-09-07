---
title: $τ^τ$-Bench: An Environment for End-To-End, Realistic Agent Construction
published: 2026-09-04T01:23:47Z
authors: Quan Shi, Keshav Dhandhania, Karthik Narasimhan, Victor Barres
url: http://arxiv.org/abs/2609.04611v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# $τ^τ$-Bench: An Environment for End-To-End, Realistic Agent Construction

## Abstract
LLM agents are rapidly becoming production software, deployed to handle customer service, adjudicate disputes, and operate internal systems. Notably, the work of building them is increasingly handed to coding agents, yet existing benchmarks say little about whether an AI system can deliver one under the conditions of a real client engagement. We introduce $τ^τ$-bench (pronounced hyper-tau-bench), a benchmark that makes agent construction the task. A developer agent is given the records a business actually keeps, a client who holds requirements, a production API that operations must run through, a codebase to inherit, and limits on serving cost and models: the same starting point a real engagement provides. From these it must deliver a complete customer-service agent, scored by deploying that agent against held-out simulated users. Across 53 tasks spanning four domains, the strongest configuration, Claude Opus 5 under Claude Code, passes just 23.9% of evaluation simulations. Meanwhile, an expert-authored reference ceiling scores 82.2%. The failures mirror ones human agent developers see: models issue shallow queries in place of deep comprehension of the records, communicate almost nothing to the client, and experiment too little with agent architecture and serving spend, shipping the first design that runs. We aim for $τ^τ$-bench to turn the work of cooperative agent building into a measurable target for coding agents.

## Metadata
- **Published**: 2026-09-04T01:23:47Z
- **Authors**: Quan Shi, Keshav Dhandhania, Karthik Narasimhan, Victor Barres
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04611v1)