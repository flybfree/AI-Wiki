---
title: The Menu Is an Execution Prior: State-Path Tool Menus for Online Agents
url: http://arxiv.org/abs/2609.09395v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-08_19-46-08Z_TheMenuIsanExecutionPrior_State_PathToolMenusforOn.md
generated_at: 2026-09-09 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces the State‑Path Tool Menu, a tool menu that encodes an execution prior for online agents by linking tools to a pre‑computed state path. Experiments on ToolBench show the menu raises online success from 0.737 to 0.898 and outperforms several baselines without altering the underlying agent.

## Key Takeaways
- The State‑Path tool menu selects a short ordered subset of tools that form a viable route from the current request state to the desired outcome, ensuring prerequisite tools are highlighted before consumers.  
- Its encoder encodes which tools can run from the current state, how their outputs satisfy later inputs, and recurring order patterns in training paths, while a retriever covers executable entries, missing‑input producers, and the final action.  
- The framework maintains success gains across different executor families despite varying model capacities.

## Context
Online agents struggle with large tool libraries where relevance ranking may hide essential intermediate steps. Current approaches treat tools as independent, leading to incomplete or delayed execution chains that reduce task completion rates.

## Implications
The State‑Path menu offers a scalable way to improve agent performance without modifying the core language model, encouraging industry adoption of more robust tool selection mechanisms in real‑world deployment systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09395v1)
