---
title: The Menu Is an Execution Prior: State-Path Tool Menus for Online Agents
published: 2026-09-08T19:46:08Z
authors: Bo Yan, Weikai Lin, Song Wang
url: http://arxiv.org/abs/2609.09395v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Menu Is an Execution Prior: State-Path Tool Menus for Online Agents

## Abstract
Language models act through tools, yet practical agents face libraries containing thousands of interfaces. We introduce the tool menu as the short, ordered subset of available tools shown to an agent before execution. The agent can call only tools in this menu. Multi-step tasks require the final action and the prerequisite tools that create its inputs in a usable order. Current constructors rank tools by request relevance, which can surface the final action while omitting or delaying less obvious producers. We introduce the state path, a pre-execution route from the observable request state to the desired outcome, and propose State-Path Tool Menu to learn it. Our framework treats the menu as an execution prior over these routes. Its encoder represents which tools can run from the current state, how their outputs satisfy later inputs, and which orders recur in training paths. A retriever covers an executable entry, the missing-input producers, and the final action. A reranker then places producers before consumers. On ToolBench, our menu raises online success from 0.737 to 0.898 and outperforms retrieval, reranking, generation, and routing baselines without changing the agent. The State-Path menu also covers more complete chains with 32 tools than the official list covers with 128, and its success gain persists across executor families with different model capacities. Our code is at https://github.com/Met2348/State-Path.

## Metadata
- **Published**: 2026-09-08T19:46:08Z
- **Authors**: Bo Yan, Weikai Lin, Song Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09395v1)