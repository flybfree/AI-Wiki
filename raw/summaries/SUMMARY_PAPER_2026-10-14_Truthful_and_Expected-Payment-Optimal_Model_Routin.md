---
title: Truthful and Expected-Payment-Optimal Model Routing in Graph-Based Agentic Workflows
url: http://arxiv.org/abs/2610.19316v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_23-59-09Z_TruthfulandExpected_Payment_OptimalModelRoutinginG.md
generated_at: 2026-10-14 21:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper addresses the problem of routing tasks across multiple LLM providers within graph-based agentic workflows, where switching providers incurs context-reprocessing costs while keeping dependent tasks on the same provider enables context reuse. The authors formulate this as a single-parameter procurement auction and propose STAR (Strategy-proof Topology-aware Agent Routing), a mechanism that minimizes virtual-cost-weighted graph workloads while guaranteeing truthful cost reporting from providers and minimizing the user's expected total payment under independent cost distributions.

## Key Takeaways
- Graph-based agentic workflows couple routing decisions across tasks because dependent tasks benefit from context reuse when assigned to the same provider, while switching providers requires reprocessing accumulated context. This topology-aware coupling means that naive per-task routing is suboptimal, and the allocation mechanism must account for the structure of the task graph, including fan-out and transferred payload sizes.
- STAR is designed as a strategy-proof mechanism: its allocation rule and payment scheme, computed by integrating workload over possible cost reports, make truthful reporting a dominant strategy for each provider regardless of what other providers report. This ensures that each truthful provider's execution cost is fully covered, eliminating the incentive for providers to strategically misreport their private real-time unit costs.
- Under independent cost distributions and non-decreasing virtual costs, STAR additionally minimizes the user's expected total payment. The synthetic experiments disentangle two distinct benefits: topology awareness reduces execution costs (growing with fan-out and transferred payload), while virtual-cost optimization reduces payment costs (increasing gradually along prior-shape heterogeneity). A paired sensitivity study confirms that payment savings degrade with prior misspecification but strategy-proofness is preserved throughout.

## Context
As agentic systems increasingly orchestrate multi-step workflows across heterogeneous LLM providers, the economics of task assignment become a central design concern. Existing routing literature often treats each task independently or assumes providers report costs honestly, ignoring both the structural coupling introduced by dependency graphs and the strategic behavior of providers who hold private cost information. This paper bridges mechanism design and agentic workflow engineering by treating provider selection as a procurement auction whose allocation must respect graph topology, a perspective largely absent from prior routing heuristics.

## Implications
For practitioners deploying multi-provider agentic pipelines, STAR provides a principled alternative to ad-hoc routing rules by simultaneously reducing execution costs through topology-aware allocation and reducing payment costs through virtual-cost optimization, while guaranteeing that providers have no incentive to inflate their quoted prices. For the broader AI systems community, the work demonstrates that mechanism-design tools from auction theory can be adapted to the structured, graph-constrained settings of modern agentic workflows, opening a research direction where incentive compatibility and computational efficiency must be co-designed rather than treated as separate concerns.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19316v1)
