---
title: MS-Eval: Benchmarking Sub-Agent Delegation and Orchestration in MCP-Intensive Working Scenarios
published: 2026-10-16T03:13:30Z
authors: Bowen Ding, Qixin Wang, Lexing Ruan, Weiyi Lu, Qiwei Ge, Ruishan Fang, Tao Lin
url: http://arxiv.org/abs/2610.22869v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MS-Eval: Benchmarking Sub-Agent Delegation and Orchestration in MCP-Intensive Working Scenarios

## Abstract
LLM agents are increasingly integrated into real-world works, yet they must handle diverse domain-specific tools and complex multi-sub-task problems that sequential tool invocation resolves inefficiently and with severe context bloat. The Main-Agent Delegation and Sub-Agent Execution (MAD-SAE) paradigm addresses these issues by delegating sub-tasks to specialized sub-agents for parallel execution in isolated contexts, but its delegation and orchestration quality remains unquantified. We introduce MS-Eval, a unified evaluation kit comprising an MCP-intensive benchmark, a controlled execution harness, tailored delegation and orchestration metrics, and the MSQ index for comprehensive assessment. Evaluating four MAD-SAE variants and eight frontier models reveals that (1) sub-agent specialization (Spec) is the best practical practice; (2) open-source models are largely competitive with few exceptions; and (3) MAD-SAE generally raises cost with contingent payoff, benefiting most open-source models in both performance and efficiency while leaving closed-source models with higher cost and degraded performance. Our case study further traces these gains to better single-agent solutions, effective context offloading, and genuine sub-task parallelism, whereas unnecessary or redundant delegation turns the same cost into pure overhead. Codes: https://github.com/LINs-lab/MS-Eval

## Metadata
- **Published**: 2026-10-16T03:13:30Z
- **Authors**: Bowen Ding, Qixin Wang, Lexing Ruan, Weiyi Lu, Qiwei Ge, Ruishan Fang, Tao Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.22869v1)