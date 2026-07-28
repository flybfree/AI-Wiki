---
title: Two-Timescale Hierarchical Reinforcement Learning for Resilient Operations
published: 2026-07-26T03:08:43Z
authors: Young Hyun Cho, Franz Stoll, Will Wei Sun, Guang Lin, Stephan Biller
url: http://arxiv.org/abs/2607.23434v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Two-Timescale Hierarchical Reinforcement Learning for Resilient Operations

## Abstract
Unexpected shocks recur in global operations, requiring decision rules that adapt as market and operating conditions change. Many operational systems also have hierarchical structures in which long-term and short-term decisions pursue a shared objective. We study how hierarchical reinforcement learning can strengthen resilience by adapting these interdependent rules jointly. We develop a two-timescale hierarchical reinforcement learning framework that adapts long-term and short-term policies at their respective time scales. Because the policies are interdependent, we synchronize their updates and prove, to our knowledge, the first convergence guarantees for coupled two-timescale learning. Over $T$ periods, our policies' average gap from an optimal policy pair is $O(T^{-1/2})$, improving to $O(\log T/T)$ when poor decisions produce clearer profit losses. In a used-car case study, inventory replenishment is the long-term decision and customer-arrival pricing the short-term decision. Relative to the strongest partially adaptive benchmark, the framework increases mean profit by $9.2\%$ under joint demand-supply shocks and by $11.8\%$ under a prolonged shock scenario, while maintaining a more stable profit trajectory over time. Short-term adaptation addresses routine seasonality and one-sided disruptions by responding immediately to changing conditions. Under joint demand-supply shocks, however, it is insufficient alone; long-term adaptation is also needed to create favorable conditions for short-term decisions. Joint adaptation thus yields higher and more stable profits through disruption and recovery. Because many organizations already use hierarchical planning, the framework strengthens operational resilience without altering existing decision structures.

## Metadata
- **Published**: 2026-07-26T03:08:43Z
- **Authors**: Young Hyun Cho, Franz Stoll, Will Wei Sun, Guang Lin, Stephan Biller
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23434v1)