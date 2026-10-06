---
title: AgentPrivArena: Evaluating and Auditing Real-world AI Agent Privacy
published: 2026-10-05T14:55:53Z
authors: Shouju Wang, Haopeng Zhang
url: http://arxiv.org/abs/2610.06454v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentPrivArena: Evaluating and Auditing Real-world AI Agent Privacy

## Abstract
The rapid advancement of LLM agents has enabled systems to autonomously perform complex tasks through external tools, but their growing access to personal data introduces significant privacy risks. Existing benchmarks primarily evaluate LLM agent privacy through simulated trajectories and outcome-based metrics, limiting their ability to capture privacy risks arising during multi-step agent execution. In this work, we introduce AgentPrivArena, a framework for evaluating privacy risks in realistic LLM agent workflows. AgentPrivArena integrates authentic MCP tools and self-hosted services within a reproducible execution environment. We further propose trajectory-level privacy metrics that quantify unnecessary information access beyond final response leakage. Building on this framework, we introduce AgentPrivAudit, a runtime auditing approach for monitoring privacy violations during agent execution. Extensive experiments on state-of-the-art LLM agents reveal substantial privacy risks overlooked by existing evaluation paradigms, highlighting the importance of trajectory-level auditing for trustworthy agent deployment.

## Metadata
- **Published**: 2026-10-05T14:55:53Z
- **Authors**: Shouju Wang, Haopeng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06454v1)