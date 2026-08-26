---
title: Adaptive Influence Graphs for Failure Attribution in Multi-Agent Systems
published: 2026-08-25T10:18:19Z
authors: Yarden Bakish, Amir Dudai, Roy Ganz, Oren Nuriel, Elad Ben Avraham, Mor Shpigel Nacson, Ron Litman
url: http://arxiv.org/abs/2608.24361v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Influence Graphs for Failure Attribution in Multi-Agent Systems

## Abstract
Multi-agent LLM systems are increasingly deployed in real-world applications, where failures can be costly and difficult to localize. Despite growing efforts to automate failure attribution, diagnosing failed runs still largely relies on human engineers. Yet engineers rarely debug complex systems by reading raw logs end to end. Instead, observability tools organize traces around components, actions, and dependencies to support targeted navigation. We hypothesize that modern LLMs can benefit from the same paradigm. To test this hypothesis, we introduce Adaptive Influence Graphs (AIGs), a two-stage agentic framework that first transforms a failed trace into a structured graph and then navigates it to identify the critical error. Across multiple models, we show that richer trace representations consistently improve failure attribution, with adaptive graph construction and agent-directed traversal yielding the strongest results. AIGs establish a new state of the art on Who&When, the standard benchmark for multi-agent failure attribution. This affirms our hypothesis that attribution depends not only on the diagnosing model, but also on how the trace is represented and explored.

## Metadata
- **Published**: 2026-08-25T10:18:19Z
- **Authors**: Yarden Bakish, Amir Dudai, Roy Ganz, Oren Nuriel, Elad Ben Avraham, Mor Shpigel Nacson, Ron Litman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24361v1)