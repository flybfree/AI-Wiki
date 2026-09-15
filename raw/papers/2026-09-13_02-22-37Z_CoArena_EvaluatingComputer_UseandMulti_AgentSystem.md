---
title: CoArena: Evaluating Computer-Use and Multi-Agent Systems in Real Time
published: 2026-09-13T02:22:37Z
authors: Nitish Kovuru, Prateek Jannu
url: http://arxiv.org/abs/2609.14239v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoArena: Evaluating Computer-Use and Multi-Agent Systems in Real Time

## Abstract
Static benchmarks for computer-use agents fix a task set at release and score every system against it once. That makes them reproducible, and it lets them drift from what they should measure: a fixed task set ages, leaks into training corpora, and cannot follow how people actually use agents from week to week. CoArena measures use directly. Real users submit tasks; two systems, each a single model or a multi-agent pipeline behind the same tool interface, execute the same task concurrently in identical sandboxed desktops; users judge the two outcomes without knowing which system produced them; and a public leaderboard is refit from those judgments. The central contribution is a formal account of what makes such an evaluation real-time. We define real-time as five measurable properties, each with an equation and a worked example: continuous task arrival, live concurrent execution, online rating updates, freshness with contamination resistance, and bounded feedback latency from a failed run to a reusable training environment. The rating methodology follows in full: the Bradley-Terry pairwise model, its likelihood with weighted observations and ties, the penalized maximum-likelihood estimator, and the streaming update applied when a single vote arrives (a stochastic-gradient step on the same likelihood, recovering Elo). It gives confidence intervals from the observed information and a cluster-robust sandwich, rank bands from a parametric bootstrap, the rule by which a new system enters the board, and the convergence rate of the estimate. Vote quality is treated with inter-judge agreement statistics, redundant judging, and explicit handling of ties and abstentions. A five-system example with 211 votes is carried from the vote matrix to ratings, intervals, and rank bands. Every number is derived from stated inputs or labeled illustrative; none is a measurement of a deployed system.

## Metadata
- **Published**: 2026-09-13T02:22:37Z
- **Authors**: Nitish Kovuru, Prateek Jannu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14239v1)