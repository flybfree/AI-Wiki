---
title: Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs
url: http://arxiv.org/abs/2610.23707v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_16-30-38Z_ToolRecommendationforMulti_StepAgents_FindingEvery.md
generated_at: 2026-10-18 22:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents Tool Recommendation, a deployed system designed to solve the critical problem of tool discovery for multi-step agent tasks, where the sheer number of available tools (approximately 8,200 on the studied platform) exceeds any model's context window. The system provides agents with all necessary tools through a fixed three-tool interface operating at the gateway between agent and tools, and demonstrates substantial improvements in retrieval accuracy, token efficiency, and cost reduction compared to lexical baselines like BM25 and fixed tool lists.

## Key Takeaways
- Tool Recommendation places every tool a query needs in the top ten results 57% more often than BM25, a lexical ranking method commonly offered by commercial tool search systems, and compares favorably with published retrieval systems up to nine times its size, demonstrating that a compact deployed system can outperform much larger research baselines on the ToolRet benchmark.
- In paired multi-step workflows, the system's first recommendation covered every required tool in 93% of Codex sessions, indicating near-complete coverage of tool requirements without iterative searching, which is critical because a single missing tool causes the entire multi-step task to fail.
- Against a fixed list of 100 tools, Tool Recommendation reduced input tokens by 17% with Codex and 40% with Claude Code, and cut total billing in all 14 runs by up to 40%, with no degradation in task completion rates, showing that smarter tool provisioning directly translates to lower operational costs without sacrificing agent performance.

## Context
As agentic AI systems increasingly rely on Model Context Protocol (MCP) servers and tool-use frameworks, the challenge of scaling tool access has become a bottleneck: platforms host thousands of tools whose combined definitions overflow any model's context window, and traditional approaches expose only a small fixed subset to agents. This paper addresses the gap between the theoretical need for comprehensive tool access and the practical constraints of context windows, token budgets, and user consent management, positioning itself at the intersection of retrieval-augmented generation, agent orchestration, and enterprise API governance.

## Implications
For practitioners building production agent systems, this work demonstrates that a gateway-level tool recommendation layer can replace static tool lists, reducing both operational costs and failure modes caused by missing tools, which is especially relevant for enterprises managing thousands of internal APIs under user-specific consent and credential constraints. For the broader field, the results challenge the assumption that larger retrieval models are necessary for effective tool discovery, suggesting that well-designed deployed systems with fixed interfaces can achieve competitive or superior performance while remaining practical to integrate into existing agent architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23707v1)
