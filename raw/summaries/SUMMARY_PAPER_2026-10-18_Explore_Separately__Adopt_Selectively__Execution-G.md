---
title: Explore Separately, Adopt Selectively: Execution-Guided Tool Use over Large Tool Libraries
url: http://arxiv.org/abs/2610.22688v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-15_21-56-10Z_ExploreSeparately_AdoptSelectively_Execution_Guide.md
generated_at: 2026-10-18 20:38
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces BRIA (BRanch-Inspect-Adopt), an agent architecture designed to help large language model agents discover and select relevant tools from large tool libraries containing thousands of tools. The core innovation is isolating candidate tool investigations into separate execution branches, allowing a task agent to inspect execution evidence from each branch and selectively adopt only the results that prove useful. Evaluated on PlanBench-XL and MCP-Atlas with 1897 tools across three language models, BRIA consistently matches or exceeds the strongest retrieval baselines, achieving a 14.37 percentage point improvement in claim score on MCP-Atlas.

## Key Takeaways
- BRIA addresses a critical failure mode in tool-augmented agents: when multiple candidate tools could satisfy the same task need, investigating them in a shared trajectory leaves alternatives unexplored and allows failed attempts to contaminate subsequent reasoning. By temporarily isolating each candidate investigation into its own branch, BRIA ensures thorough exploration without cross-contamination of reasoning.
- The architecture follows a three-phase cycle: Branch (retrieve and execute tools for each candidate in isolation), Inspect (the task agent evaluates execution evidence from each branch), and Adopt (only useful results are incorporated into the continuing trajectory). This execution-guided selection is more reliable than purely retrieval-based ranking, as it grounds tool selection in actual execution outcomes rather than semantic similarity scores.
- BRIA demonstrates superior performance on both static and adaptive retrieval baselines across all tested settings, achieving an average claim score of 89.77 versus 75.40 for MCP-Zero on MCP-Atlas. Importantly, it also lies on the Pareto frontier for task performance versus input-token cost, meaning it achieves better results without proportionally increasing computational overhead.

## Context
As tool-augmented agents scale to handle thousands of available tools through frameworks like MCP (Model Context Protocol), the tool selection problem becomes a bottleneck for agent reliability. Current approaches rely heavily on retrieval ranking to pick tools before execution, but this fails when semantic similarity does not correlate with functional correctness. BRIA represents a shift from retrieval-first to execution-guided tool adoption, acknowledging that the only reliable way to determine whether a tool satisfies a task need is to actually run it. This positions the work at the intersection of agent planning, tool-use reasoning, and multi-branch exploration strategies.

## Implications
For practitioners building production agent systems with large tool inventories, BRIA offers a practical architecture that improves reliability without requiring model retraining or complex orchestration infrastructure. The execution-guided selection paradigm suggests that future agent frameworks should treat tool discovery as an iterative, evidence-driven process rather than a one-shot retrieval problem. For the broader field, the Pareto-optimal performance on both accuracy and token cost demonstrates that careful architectural design can outperform brute-force retrieval scaling, which is significant for deploying agents in cost-constrained environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22688v1)
