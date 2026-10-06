---
title: DUET: Co-Evolving Solver and Grader Agents
published: 2026-10-02T21:51:26Z
authors: Fengyu Gao, Sourav Pal, Austin Z. Henley, Arjun Radhakrishna, Gustavo Soares
url: http://arxiv.org/abs/2610.04087v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DUET: Co-Evolving Solver and Grader Agents

## Abstract
Agentic workflows are increasingly used across domains such as technology, finance, and enterprise operations. As these agents become more widely deployed, continually improving them becomes increasingly important. This raises an immediate challenge: How should the agent evolve? This evolution requires effective evaluation that can assess outcomes and provide useful feedback for optimization. As the agent evolves, its behaviors and failure modes may also change, making a fixed evaluator increasingly inadequate. Another fundamental question: How should we evaluate an evolving agent? These two challenges are inherently coupled; changes in agent behavior can expose limitations of the current evaluator, while a stronger evaluator provides more informative feedback for improving the agent. Motivated by this interaction, we introduce DUET, a framework that jointly optimizes a solver agent and a grader agent to improve both. DUET iteratively selects training tasks, executes them with the solver, evaluates the resulting outcomes with the grader, and uses a tool-using update module to revise the solver and the grader, alternating between the two across rounds. By updating the grader within the optimization loop, DUET turns evaluation from a fixed source of feedback into a first-class optimization objective that adapts alongside the solver. Experiments across four agent benchmarks show that DUET improves both solver and grader performance and consistently outperforms baselines that optimize the solver with a fixed grader.

## Metadata
- **Published**: 2026-10-02T21:51:26Z
- **Authors**: Fengyu Gao, Sourav Pal, Austin Z. Henley, Arjun Radhakrishna, Gustavo Soares
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04087v1)