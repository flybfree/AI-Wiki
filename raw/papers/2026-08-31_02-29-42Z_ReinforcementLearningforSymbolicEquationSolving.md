---
title: Reinforcement Learning for Symbolic Equation Solving
published: 2026-08-31T02:29:42Z
authors: Kevin P O Keeffe
url: http://arxiv.org/abs/2608.30162v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reinforcement Learning for Symbolic Equation Solving

## Abstract
We present a reinforcement-learning agent that solves symbolic equations step by step, covering both nonlinear closed equations (radicals, exponentials, trigonometric) and a controlled class of restricted-open families requiring a change of variables (CoV) such as completing the square. We cast algebra as an MDP with a dynamic action space and a tree-structured policy (TreeMLP). The main policy learns from reward alone with no supervised solution traces; the CoV substitution comes from a supervised generator interchangeable with a CAS call. On closed equations the agent matches the prior best on CommonCore (0.93 greedy vs. ConPoLe's 0.925) under a single policy. On four hand-designed restricted-open families (quadratic, cubic, quartic, exponential) it reaches 0.79 beam / 0.67 greedy, exceeding the strongest non-learned search (A-star, 0.64). Learned CoV timing has content only on the exponential family, the one requiring a nested CoV, where a natural rule solves none of the held-out equations while the policy solves 75% from reward alone. At 10x scale a sharp seed-level bimodality emerges; a UCB learning-progress curriculum shows a non-significant positive trend toward mitigating it. We do not claim general open-equation solving: every open-equation result is confined to these four controlled families.

## Metadata
- **Published**: 2026-08-31T02:29:42Z
- **Authors**: Kevin P O Keeffe
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30162v1)