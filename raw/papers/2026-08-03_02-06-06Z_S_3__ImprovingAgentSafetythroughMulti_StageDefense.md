---
title: $S^3$: Improving Agent Safety through Multi-Stage Defense
published: 2026-08-03T02:06:06Z
authors: Zibo Xiao, Haoyu Wang, Jun Sun
url: http://arxiv.org/abs/2608.02683v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# $S^3$: Improving Agent Safety through Multi-Stage Defense

## Abstract
Large Language Model (LLM) agents rely on multi-stage agentic workflows, with stages such as memory, planning, and tool execution, to accomplish complex tasks. However, risks may emerge at different stages, propagate across steps, and become difficult to detect and mitigate. Existing safety methods protect only isolated stages and are difficult to integrate, leaving agents without comprehensive protection throughout the workflow. To address these limitations, we introduce Stage-Specific Safety Skills, a unified abstraction that represents heterogeneous safety designs as reusable and composable components with explicit stage semantics. We further develop an automated transformation pipeline that converts existing safety designs into reusable safety skills and establish a community-driven safety skill library. Building on this abstraction, we propose $S^3$, a multi-stage defense framework in which a guard agent orchestrates stage-specific safety skills for risk detection and mitigation throughout the agentic workflow. We also construct the Multi-Stage Risk Benchmark (MSRB) to evaluate representative risks across workflow stages. Experimental results show that $S^3$ consistently outperforms representative state-of-the-art baselines in both safety effectiveness and utility preservation. These results demonstrate the potential of stage-specific safety skills as a scalable and composable foundation for building resilient and trustworthy agent systems.

## Metadata
- **Published**: 2026-08-03T02:06:06Z
- **Authors**: Zibo Xiao, Haoyu Wang, Jun Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02683v1)