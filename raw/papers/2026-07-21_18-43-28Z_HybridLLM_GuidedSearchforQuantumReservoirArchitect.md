---
title: Hybrid LLM-Guided Search for Quantum Reservoir Architecture Design
published: 2026-07-21T18:43:28Z
authors: Krishna Bhatia, Gautami Sanjay Naik
url: http://arxiv.org/abs/2607.19506v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hybrid LLM-Guided Search for Quantum Reservoir Architecture Design

## Abstract
Quantum reservoir computing (QRC) uses fixed quantum dynamics as a high-dimensional temporal feature map and trains only a lightweight classical readout. QRC is attractive for near-term quantum machine learning, but its performance depends strongly on architecture choices such as input encoding, reservoir depth, entanglement topology, measurement features, state-reset policy, feature construction, and readout regularization. We introduce \method, a simulator-based benchmark that formulates QRC design as constrained black-box architecture search and evaluates whether large language models can act as proposal controllers for this search problem. The benchmark compares five policies under identical evaluation budgets: random search, evolutionary search, Bayesian/TPE optimization, a feedback-based LLM agent, and \hybrid, which combines LLM proposals with memory, mutation, crossover, duplicate avoidance, and exploration. On NARMA10, Mackey-Glass forecasting, and temporal parity, \hybrid{} is the most consistent policy: it ranks first on NARMA10 and temporal parity and second on Mackey-Glass, narrowly behind evolutionary search. Under a 25-evaluation budget and three seeds, \hybrid{} improves over random search on all tasks, including a 23.6\% relative reduction in Mackey-Glass error. The results do not show that LLMs are universal QRC optimizers; rather, they show that generative models can be useful high-level controllers when embedded inside validated, reproducible hybrid search loops.

## Metadata
- **Published**: 2026-07-21T18:43:28Z
- **Authors**: Krishna Bhatia, Gautami Sanjay Naik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19506v1)