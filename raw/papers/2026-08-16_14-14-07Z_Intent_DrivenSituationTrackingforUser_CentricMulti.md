---
title: Intent-Driven Situation Tracking for User-Centric Multi-Turn Agents
published: 2026-08-16T14:14:07Z
authors: Meiling Tao, Yiling Tao, Peng Wang
url: http://arxiv.org/abs/2608.15755v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Intent-Driven Situation Tracking for User-Centric Multi-Turn Agents

## Abstract
User-centric multi-turn agents must act on an evolving task situation shaped by changing user intents, accumulated tool-grounded facts, missing information, and execution constraints. Existing context-management methods improve the use of past interaction history, but rarely maintain an explicit situation state that separates grounded facts from task-state judgments. As a result, agents often need to infer fine-grained attributes, task dependencies, and constraint satisfaction implicitly from dialogue traces. We propose Intent-Driven Situation States (IDSS), a training-free framework that maintains an explicit situation state alongside the dialogue. IDSS parses tool returns into provenance-aware entities and attributes, tracks user intents, required variables, constraints, and execution status, and propagates new facts to task constraints to update action executability. This allows agents to avoid infeasible actions, advance dependent goals, and reuse relevant information without repeatedly searching raw history. Experiments on three interactive benchmarks across eight LLMs show that IDSS improves task completion, preference elicitation, and interaction efficiency, with clear gains on tasks involving multi-entity coordination, evolving user constraints, and constraint-aware replanning. Ablations and error analyses show that these improvements come from the interaction between fact persistence, intent-centered state tracking, and constraint modeling. These results suggest that explicit situation tracking offers an effective alternative to history-centric context management for reliable user-centric multi-turn agents.

## Metadata
- **Published**: 2026-08-16T14:14:07Z
- **Authors**: Meiling Tao, Yiling Tao, Peng Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15755v1)