---
title: A Framework for Designing Reward Functions: From Objectives to Features to Human-Aligned Reward Functions
published: 2026-08-12T17:46:00Z
authors: Di Yang Shi, W. Bradley Knox
url: http://arxiv.org/abs/2608.12302v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Framework for Designing Reward Functions: From Objectives to Features to Human-Aligned Reward Functions

## Abstract
We present a formal process to enable non-experts to instantiate and iterate on human-aligned reward functions, i.e. reward functions that adhere to a given preference ordering over trajectories. Given a task described in natural language, our process produces a linear reward function in three steps: distill the task's objectives into a set of fundamental objectives and derive measurable outcome variables that capture those fundamental objectives, select a causally representative subset of outcome variables as the reward terms, and fit weights to those reward terms via preference elicitation. Our contributions describe the first step and formalize the latter two steps. The first is a guided workflow for deriving outcome variables. The second is a reduction of reward term selection to minimum-cost partial cover on a causal DAG, solved in polynomial time via max-flow. The third is a geometric framing of weight fitting as a convex feasibility problem iteratively narrowed by preference queries, solved by existing separation oracle methods. To the best of our knowledge, this is the first reward-design method that maintains a deterministically conflict-free feasible weight region, narrowed to a desired tolerance via a separation oracle with O(n log κ) preference queries.

## Metadata
- **Published**: 2026-08-12T17:46:00Z
- **Authors**: Di Yang Shi, W. Bradley Knox
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12302v1)