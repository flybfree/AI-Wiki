---
title: Explore Separately, Adopt Selectively: Execution-Guided Tool Use over Large Tool Libraries
published: 2026-10-15T21:56:10Z
authors: Anna Mazhar, Seiji Maekawa, Nikita Bhutani
url: http://arxiv.org/abs/2610.22688v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Explore Separately, Adopt Selectively: Execution-Guided Tool Use over Large Tool Libraries

## Abstract
Large language model agents must discover relevant tools from large libraries, e.g., thousands of tools, as new needs arise during task execution. When several candidates could satisfy the same need, execution may be required to identify the relevant one. Investigating candidates in a shared trajectory can leave alternatives unexplored or allow failed attempts to influence subsequent reasoning. To address this, we present BRIA (BRanch-Inspect-Adopt), a simple yet effective agent that temporarily isolates candidate investigations in separate branches. Each branch retrieves and executes tools to investigate its candidate; a task agent inspects the resulting execution evidence and adopts only useful results into its continuing trajectory. BRIA retrieves additional tools as new capability needs arise during task execution. We evaluate BRIA on PlanBench-XL and MCP-Atlas using a shared pool of 1897 tools, three language models, and static and adaptive retrieval baselines. Across all settings, BRIA matches or exceeds the strongest retrieval baseline. On MCP-Atlas, it achieves an average claim score of 89.77, compared with 75.40 for MCP-Zero, a gain of 14.37 percentage points. BRIA also lies on the Pareto frontier for task performance and input-token cost.

## Metadata
- **Published**: 2026-10-15T21:56:10Z
- **Authors**: Anna Mazhar, Seiji Maekawa, Nikita Bhutani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.22688v1)