---
title: EGI-BENCH: An Enterprise General Intelligence Benchmark Suite
published: 2026-10-19T20:02:07Z
authors: Zhiwei Liu, Zhujun Lan, Jielin Qiu, Zixiang Chen, Liangwei Yang, Ming Zhu, Akshara Prabhakar, Wenting Zhao, John Emmons, Jason Wu, Shafiq Rayhan Joty, Junnan Li, Shelby Heinecke, Silvio Savarese, Huan Wang
url: http://arxiv.org/abs/2610.27234v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EGI-BENCH: An Enterprise General Intelligence Benchmark Suite

## Abstract
Enterprise adoption of LLMs in agentic workflows is gated by evaluations that span a wide arc of abilities: CRM operations, heterogeneous-document retrieval, personal data understanding, multi-turn planning, tool use, function calling, long-horizon research, and long-context software engineering. These evaluations live today in separate repositories with divergent runners, dependencies, and scoring conventions, which makes cross-benchmark comparison difficult and obscures what a single aggregate number actually represents. We release EGI-BENCH, a unified LLM agent benchmark suite that consolidates eight enterprise facing agent benchmarks (CRMARENA, HERB, PERSONABENCH, USERBENCH, MCP-UNIVERSE, MCPEVAL, BENCHFORCE, LOCOBENCH) behind a single command-line interface with two runtime-budgeted execution modes. On top of the suite we define the Enterprise General Intelligence (EGI) Score, a six-dimensional framework (M1-M6) whose buckets are populated by fine-grained sub-metrics routed from each benchmark rather than by benchmark-level averages. We describe the suite, the sub-metric routing, and the quick/deep budgets, and report results for fourteen frontier and cost-efficient LLMs spanning the GPT, Claude, and Gemini families under quick mode. Top-line EGI ranges from 39.6 (GPT-4o mini) to 65.6 (gpt-5.5), and no single model dominates every capability axis: gpt-5.5 leads task outcome, planning, and retrieval grounding; Claude Sonnet 4.5 leads tool actioning and safety/abstention; and Claude Haiku 4.5 leads engineering quality. Code is available at https://github.com/SalesforceAIResearch/egi-bench.

## Metadata
- **Published**: 2026-10-19T20:02:07Z
- **Authors**: Zhiwei Liu, Zhujun Lan, Jielin Qiu, Zixiang Chen, Liangwei Yang, Ming Zhu, Akshara Prabhakar, Wenting Zhao, John Emmons, Jason Wu, Shafiq Rayhan Joty, Junnan Li, Shelby Heinecke, Silvio Savarese, Huan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27234v1)