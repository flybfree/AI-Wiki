---
title: Computing with Agentic Oracles
published: 2026-08-02T19:50:15Z
authors: Jie Wang
url: http://arxiv.org/abs/2608.01464v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Computing with Agentic Oracles

## Abstract
This paper extends the stochastic-oracle model of AI-augmented computing to include agentic oracles. Unlike a stationary stochastic oracle, which responds to the same query according to a fixed response distribution across calls, an agentic oracle can pursue a goal autonomously and may access an environment containing task-relevant resources. These capabilities affect both response distributions and token costs beyond what is visible at the query-response interface. We develop a framework for analyzing token costs in Stochastic-Oracle Turing Machines (SOTMs) that compute with agentic oracles. Each call has an \emph{orchestration token cost}, visible to the caller at the query-response interface, and an \emph{agentic token cost}, incurred by internal operations not exposed to the caller. We show that an SOTM computing with an agentic oracle that can retain intermediate state can have token-cost advantages over SOTMs using stationary stochastic oracles when solving the same task at the same quality level, both with and without environment access. We also investigate goal-loss risk, including how internal dispatch ordering can reduce exposure to irreversible actions. We provide a goal-loss avoidance criterion, derive progress--retry--goal-loss formulas, establish goal-depth lower bounds on token complexity, characterize token complexity when the probability of goal loss is zero, and show that goal-loss risk can impose an upper bound on the achievable quality of a task involving environment updates.

## Metadata
- **Published**: 2026-08-02T19:50:15Z
- **Authors**: Jie Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01464v1)