---
title: When Instruction Files Go Stale: Documentation Debt and Hidden Cost in Coding Agents
url: http://arxiv.org/abs/2611.09802v1
type: paper-summary
date: 2026-11-09
source_paper: 2026-11-06_17-54-01Z_WhenInstructionFilesGoStale_DocumentationDebtandHi.md
generated_at: 2026-11-09 21:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how stale repository instruction files (such as AGENTS.md and CLAUDE.md) create a form of documentation debt that silently increases the operational cost of LLM-based coding agents. Through a controlled experiment involving 22 maintenance tasks and 732 agent trajectories across two models, the authors demonstrate that agents follow outdated guidance when it appears relevant, incurring measurable extra tool calls, yet task-success evaluations fail to capture this hidden cost.

## Key Takeaways
- Agents actively follow stale instructions when they are topically relevant to the task at hand, even when correct information is available elsewhere in the repository. This means documentation debt is not merely a passive artifact but an active behavioral influence on agent decision-making, making it functionally equivalent to technical debt with compounding interest paid in every subsequent session.
- On the stale test command scenario, Claude Sonnet 5.5 required approximately two additional tool calls per run—roughly one-third more operations than when the corrected command was provided. However, for the other two stale instruction types (a code location and a component-adding procedure), no statistically detectable performance difference was observed, suggesting the impact of documentation debt is highly context-dependent and task-type-sensitive.
- Although agents generally recovered from immediate failures caused by stale guidance, none of them repaired the underlying instruction file itself. Correcting the instructions eliminated operations on obsolete paths, while removing them entirely prevented most such operations, indicating that proactive maintenance or removal of stale files is more effective than relying on agent self-correction.

## Context
This work sits at the intersection of software engineering, AI agent evaluation, and technical debt research. As coding agents like Claude Code, Cursor, and GitHub Copilot become standard tools in software development, their behavior is heavily shaped by repository-level configuration files that are read at the start of every session. The paper extends the well-established concept of documentation debt from human software engineering into the domain of autonomous agents, where the "interest" on that debt is paid in computational resources, tool calls, and potential errors rather than in developer time.

## Implications
For practitioners deploying coding agents in production, this research underscores that maintaining instruction files is not a cosmetic housekeeping task but a direct lever on agent efficiency and reliability; stale files silently inflate operational costs and can mislead agents even when correct information exists in the codebase. For the broader AI research community, the findings argue that evaluation frameworks must go beyond binary task-success metrics and instead measure intermediate behaviors such as tool-call counts, path selections, and recovery patterns to expose the hidden costs of documentation debt before they accumulate across thousands of agent sessions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.09802v1)
