---
title: MCPGen: Benchmarking LLMs on Executable MCPWorkflow Development
published: 2026-09-20T22:57:06Z
authors: Yingxuan Yang, Jiaqi Liu, Lirui Guan, Jiaye Gao, Weiwen Liu, Weinan Zhang, Ying Wen
url: http://arxiv.org/abs/2609.23925v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MCPGen: Benchmarking LLMs on Executable MCPWorkflow Development

## Abstract
We study whether LLMs can produce executable workflow artifacts that remain consistent across graph structure, tool implementation, schema bindings, and runtime wiring. In this setting, correctness depends on cross-layer consistency: a workflow may be structurally plausible, yet still fail because tool implementations, schema bindings, or runtime execution do not align. Existing benchmarks largely evaluate these capabilities in isolation or rely on trajectory-level proxies, leaving open whether generated workflow artifacts execute end-to-end. We introduce \textbf{MCPGen}, an executable benchmark for Model Context Protocol (MCP) workflow development. MCPGen contains 100 self-contained MCP projects across 16 application domains and evaluates three diagnostic tasks: workflow reconstruction, tool creation, and backward-compatible workflow extension. We evaluate 11 representative LLMs in a single-turn foundation-model setting, assessing generated artifacts through static analysis, unit and integration tests, and process-isolated end-to-end execution. Models reach 88.5\% on workflow reconstruction, but no model exceeds 57\% end-to-end execution success. Per-tool unit-test pass rates reach 63.8\%, while project-level integration success does not exceed 45\%, suggesting that integration remains a major bottleneck even when isolated tool tests pass.

## Metadata
- **Published**: 2026-09-20T22:57:06Z
- **Authors**: Yingxuan Yang, Jiaqi Liu, Lirui Guan, Jiaye Gao, Weiwen Liu, Weinan Zhang, Ying Wen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23925v1)