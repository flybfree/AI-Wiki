---
title: Evolving Self-tuning Benchmarks for Long-Horizon Tool Use
published: 2026-10-19T21:22:08Z
authors: Hyunji Alex Nam, Michael Dennis, Natasha Jaques, Minsuk Chang
url: http://arxiv.org/abs/2610.27307v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evolving Self-tuning Benchmarks for Long-Horizon Tool Use

## Abstract
For AI assistants to move beyond simple chat interfaces and reliably assist users with applications like Gmail, Venmo, and Slack, we need to improve their tool-use capabilities. However, existing tool use benchmarks are still limited and difficult to scale because they rely on human supervision or are too domain-specific. To make data generation scalable, we propose, TURTLE (**T**ool **U**se **R**elated **T**asks with **L**ong-Horizon **E**volution), an Unsupervised Environment Design (UED) approach to evolve existing tasks using a proposer, a solver, and a feedback generator large language model agents. The proposer is rewarded for difficult yet solvable tasks based on the solver's empirical performance, and the feedback generator summarizes the solver's execution traces for the proposer to exploit. TURTLE produces evolving, self-tuning test suites adaptable to different environment requirements, from supporting user simulators and dense document retrieval to interacting across multiple apps. Empirical results on AppWorld, $τ$-Bench, and AutomationBench using Gemma 4 31B-it show that the evolved tasks target the desired difficulty range (e.g., a 165\% increase in the percentage of hard tasks on AppWorld), increase task diversity (in terms of reasoning and simultaneous tool interactions), and elicit a broader range of failure modes than the original tasks.

## Metadata
- **Published**: 2026-10-19T21:22:08Z
- **Authors**: Hyunji Alex Nam, Michael Dennis, Natasha Jaques, Minsuk Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27307v1)