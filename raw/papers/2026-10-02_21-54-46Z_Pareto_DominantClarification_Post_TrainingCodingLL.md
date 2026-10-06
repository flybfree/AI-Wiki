---
title: Pareto-Dominant Clarification: Post-Training Coding LLMs via PPO-Lagrangian Budget Constraints
published: 2026-10-02T21:54:46Z
authors: Abhinav Rajput, Acey Vogelstein
url: http://arxiv.org/abs/2610.04089v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pareto-Dominant Clarification: Post-Training Coding LLMs via PPO-Lagrangian Budget Constraints

## Abstract
Coding agents operating under ambiguous instructions or user prompts must decide whether to ask clarifying questions or attempt a solution directly. While clarification from the user may improve the correctness of the agent's solution, each back-and-forth interaction incurs user and system costs, forming an explicit accuracy vs. efficiency tradeoff. Existing works study clarification behavior but do not train policies under enforceable clarification budgets; penalty-based approaches typically require separate coefficient tuning swept across all clarification budget levels. We formulate clarification as a Constrained Markov Decision Process (CMDP) and post-train Qwen2.5-Coder-7B-Instruct with PPO-Lagrangian to optimize coding accuracy, subject to an expected question-budget constraint. Evaluated on HumanEvalComm with a GPT-4o-mini oracle simulator, the resulting policies reveal that untuned clarification behavior is Pareto-inefficient: budget-constrained policies can simultaneously achieve higher accuracy and lower clarification rates than the baseline model. Across budget levels, we observe a log-shaped Pareto frontier with diminishing returns to additional clarification. Gains arise not from simply asking more questions overall, but from improved question targeting and better code generation under ambiguity. Without explicit supervision, trained policies learn to allocate clarification budget non-uniformly, asking more frequently on tougher (multi-degradation) tasks. These results suggest that unconstrained interactive LLM systems may systematically use clarification inefficiently.

## Metadata
- **Published**: 2026-10-02T21:54:46Z
- **Authors**: Abhinav Rajput, Acey Vogelstein
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04089v1)