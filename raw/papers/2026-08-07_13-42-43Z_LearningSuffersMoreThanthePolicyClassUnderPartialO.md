---
title: Learning Suffers More Than the Policy Class Under Partial Observability: A Closed-Form Analysis
published: 2026-08-07T13:42:43Z
authors: Idil Gözel
url: http://arxiv.org/abs/2608.07228v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Suffers More Than the Policy Class Under Partial Observability: A Closed-Form Analysis

## Abstract
When a reinforcement learning agent cannot observe the full state, we usually blame its policies: it cannot see enough to represent a good one. We show that in a solvable case the bigger problem lies elsewhere. Even when a good policy is available and the agent's value function is expressive enough to describe it exactly, learning still ends up somewhere far worse.   We study a partially observed linear-quadratic problem in which a standard actor-critic learner can be solved in closed form. At our default setting the best policy the agent can represent is already close to optimal, costing 10.4% more than the ideal controller that observes everything. Learning does not find it. The algorithm instead comes to rest at a policy that is 35% worse than the best one available to it, and we can say exactly where and why.   The cause is a bias in what the critic learns rather than a limit on what the actor can express. Because the agent cannot attribute what it sees to the part of the state it cannot observe, the critic misreads that unexplained variation as sharp curvature in its own value estimates, and the actor follows that error away from the optimum. We derive closed-form expressions for the resulting policy, for its cost, and for the one design choice that removes the problem, which is how far the learner looks ahead before trusting its own value estimates. Deep reinforcement learning experiments follow these predictions closely. Notably, giving the agent memory of past observations does not help, while changing how far it looks ahead does.

## Metadata
- **Published**: 2026-08-07T13:42:43Z
- **Authors**: Idil Gözel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07228v1)