---
title: LLM within MCP Matters: Measuring Inefficient Resource Utilization Driven by LLMs
published: 2026-08-09T04:17:12Z
authors: Minhan Cho, Soyoung Park, Kihyeon Jeong, Byeongkyu Jeon, Daejin Choi, Jinyoung Han
url: http://arxiv.org/abs/2608.08467v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM within MCP Matters: Measuring Inefficient Resource Utilization Driven by LLMs

## Abstract
The Model Context Protocol (MCP) standardizes how servers expose data and tools to Large Language Models (LLMs). A common server design embeds frequently used reference data, such as identifier lookup tables, directly in the server instructions: the system-prompt text a server hands to the host application. When a query concerns an entry of the embedded table, the model can act on it immediately instead of re-discovering the same information through a search tool. We test whether client LLMs actually consume such instruction-embedded data, reporting a 54,000-trial study across 24 LLMs (9 Claude, 6 Gemini, 9 GPT) on a production legal-information MCP server. A diagnostic condition that removes the competing search tool shows that failures are dominated by behavioral preference rather than missing capability. With search unavailable, 23 of 24 models read the embedded data reliably (hit ratio at least 98%); with a search tool merely present, 9 models drop below 15%. A 2^3 factorial analysis of three instruction-level interventions reveals strong interaction effects: combining all three restores at least 86% for 20 of 24 models, but individual interventions can backfire for specific model families. Per-server prompt engineering is therefore a workaround rather than a fix; we argue that MCP host applications should provide an explicit mechanism that places server instructions ahead of tool selection in the client LLM's deliberation.

## Metadata
- **Published**: 2026-08-09T04:17:12Z
- **Authors**: Minhan Cho, Soyoung Park, Kihyeon Jeong, Byeongkyu Jeon, Daejin Choi, Jinyoung Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08467v1)