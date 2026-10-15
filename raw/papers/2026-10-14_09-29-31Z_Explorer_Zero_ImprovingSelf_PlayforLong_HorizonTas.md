---
title: Explorer-Zero: Improving Self-Play for Long-Horizon Tasks with Decomposable Verifiable Rewards
published: 2026-10-14T09:29:31Z
authors: Tianyu Liu, Davide Belli, Bence Major, Arash Behboodi, Tribhuvanesh Orekondy
url: http://arxiv.org/abs/2610.19868v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Explorer-Zero: Improving Self-Play for Long-Horizon Tasks with Decomposable Verifiable Rewards

## Abstract
Training LLM agents on long-horizon interactive tasks with reinforcement learning typically relies on human-annotated tasks and reliable verification, both expensive to construct for stateful environments. Self-play offers an alternative, but must generate achievable, compositional tasks and provide feedback beyond binary outcomes. We propose Explorer-Zero, a self-play framework that jointly generates tasks and fine-grained, verifiable rewards through environment interaction. A learned proposer explores the environment, constructs tasks, and records intermediate and final states as verification targets. These checkpoints reward partial completion, while alternating proposer--solver training adapts the generated curriculum. We show theoretically that subtask rewards reduce collapse among unsuccessful rollouts when they complete different numbers of subtasks. Without human-annotated training tasks, Explorer-Zero outperforms the evaluated self-play baselines across ALFWorld, ScienceWorld, and AppWorld; on AppWorld, our 30B agent reaches 59.67% task success, approaching 62.65% for RL on human-annotated tasks. Further analyses support task-relevant composition and benefits on complex tasks, while self-play initialization improves subsequent human-data RL across all three benchmarks.

## Metadata
- **Published**: 2026-10-14T09:29:31Z
- **Authors**: Tianyu Liu, Davide Belli, Bence Major, Arash Behboodi, Tribhuvanesh Orekondy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19868v1)