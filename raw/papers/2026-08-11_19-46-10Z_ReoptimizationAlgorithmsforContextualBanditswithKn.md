---
title: Reoptimization Algorithms for Contextual Bandits with Knapsack Constraints
published: 2026-08-11T19:46:10Z
authors: Zhen Xu
url: http://arxiv.org/abs/2608.11383v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reoptimization Algorithms for Contextual Bandits with Knapsack Constraints

## Abstract
We study new algorithms for Contextual Bandits with Knapsack. In these problems, there are finitely many types of customers, products, and resources. Each product is made from a fixed combination of resources, and resources have finite capacity. A decision maker must assign each arriving customer one out of a set of multiple possible products. Every assignment of a customer to a product will generate a random reward, which equals an unknown linear function of customer and product features, plus a noise term. The objective is to jointly learn the mean reward function, and to make online assignments to minimize the expected revenue loss relative to an optimal policy that knows the reward function. We propose a natural and simple extension of the Upper-Confidence-Bound (UCB) family of algorithms and apply re-optimization techniques. We show that by taking advantage of re-optimization, our algorithm achieves an average regret of $O(\frac{(\ln T)^3}{T})$ where $T$ is the horizon length. Our bound significantly reduces the $O(\frac{1}{\sqrt{T}})$ bound in the literature for closely related dynamic-pricing problems that are based on re-optimization.

## Metadata
- **Published**: 2026-08-11T19:46:10Z
- **Authors**: Zhen Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11383v1)