---
title: AT-AT: Automatic Tool Optimization from Agent Traces
published: 2026-10-26T01:18:17Z
authors: Maya Ravichandran, Pragya Tripathi, Dharamendra Kumar, Adith Swaminathan, Nathan Kallus
url: http://arxiv.org/abs/2610.34679v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AT-AT: Automatic Tool Optimization from Agent Traces

## Abstract
Efforts to improve LLM-based agents typically focus on modifying the agent itself, yet success also depends on the environment in which an agent acts. Tools mediate this interaction: a tool's description shapes how an agent calls it, and its implementation determines the results and errors the agent receives afterwards. Many tools, such as APIs and MCP servers, are shared by many agents and maintained by providers who cannot change those agents. We introduce AT-AT (Automatic Tool Optimization from Agent Traces), an agentic tool optimizer that improves a shared toolset offline from historical agent executions while holding the agents fixed. A lightweight coding agent reads agent trajectories and their evaluation results, and selectively edits tool descriptions and, when permitted, implementations. On $τ^2$-bench-verified, AT-AT achieves the highest task completion rates in the Airline and Telecom domains at lower cost than strong prompt- and tool-optimizer baselines, and its Telecom gain is statistically significant under paired permutation tests. Optimizing the tools within a coding agent harness also improves held-out performance on TerminalBench-2 and TBLite. When applied to three production MCP servers at a large enterprise, AT-AT lowered cost or tool error rates on every server and increased held-out task passes on one. By turning accumulated execution traces into updates to shared tool environments, AT-AT provides a path toward continual improvement of agent systems through environment-side learning.

## Metadata
- **Published**: 2026-10-26T01:18:17Z
- **Authors**: Maya Ravichandran, Pragya Tripathi, Dharamendra Kumar, Adith Swaminathan, Nathan Kallus
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34679v1)