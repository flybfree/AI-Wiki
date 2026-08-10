---
title: CEDAR: Agent-Orchestrated Tree Search for Goal-Directed Optimization of Complex Systems
published: 2026-08-07T06:54:58Z
authors: Yingtao Tian
url: http://arxiv.org/abs/2608.06871v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CEDAR: Agent-Orchestrated Tree Search for Goal-Directed Optimization of Complex Systems

## Abstract
Complex systems, core objects of study in artificial life, model diverse phenomena through nonlinear, feedback-driven interactions that produce emergent behavior, with applications from population dynamics and biology to economic policy and strategic decision-making. Yet the difficulty of predicting how feedback structure gives rise to emergent behavior, a central open problem in artificial life, makes goal-directed design exceptionally challenging. In established practice, system structures are written in specialized modeling languages such as DYNAMO or STELLA, compounding the challenge with labor-intensive workflows that limit adoption and hinder timely decision-making. To address these challenges, we introduce CEDAR, an autonomous method that uses Large Language Model (LLM) agents to discover complex systems satisfying user-specified behavioral goals. Our key innovation is an LLM-driven Monte Carlo Tree Search (MCTS) deeply coupled with complex systems: at each iteration, an LLM Judge evaluates emergent behavior against specified goals and an LLM Editor proposes improved variants, with the Judge acting as a fitness function and the Editor as a variation operator, akin to a generate-and-evaluate loop in evolutionary computation. We represent complex systems as a restricted, runnable subset of Python with domain-specific primitives, letting LLMs modify system dynamics directly. CEDAR formalizes this as an MCTS variant with an LLM-parameterized transition kernel and value function, enabling goal-directed discovery of complex system behaviors while preserving solution diversity, and its LLM-based interpretability reveals how structural changes drive emergent behavior. CEDAR reduces human effort while enabling capabilities difficult to achieve with existing approaches, facilitating broader adoption of complex systems across domains.

## Metadata
- **Published**: 2026-08-07T06:54:58Z
- **Authors**: Yingtao Tian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06871v1)