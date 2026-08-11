---
title: Online Learning of Scale Parameters in Score-Driven Filters
published: 2026-08-10T07:43:38Z
authors: Fabrizio Lillo, Giulia Livieri, Gianluca Palmari
url: http://arxiv.org/abs/2608.09218v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Online Learning of Scale Parameters in Score-Driven Filters

## Abstract
Score-driven filters multiply a scaled log-likelihood score by a gain that controls the update magnitude. We treat this gain as a decision variable and study its online learning. Conditional on the current state, observation, score, and scaling rule, each admissible gain induces a reachable next state and a one-step-ahead predictive density: scalar gains govern distance along a line, while diagonal gains govern coordinatewise transmission. Gain selection is therefore a conditional predictive decision problem with a Kullback-Leibler objective. For a scalar unscaled gain, the negative raw product of consecutive scores is the stochastic gradient of this loss; positive aGAS scaling only rescales the effective step. Monotone differentiable gain links induce mirror-descent geometries on bounded gain domains, while persistence yields a Bregman pull towards a reference gain. Under convexity, compactness, and regularity conditions, we establish dynamic-regret bounds for projected and discounted mirror updates relative to time-varying, current-information comparators. Simulations illustrate the roles of scaling, link geometry, persistence, and coordinatewise transmission rates. An out-of-sample panel of equity-index volatilities shows that the bounded mirror gain generally matches or outperforms a constant gain while avoiding the extreme spikes of a nominally unbounded exponential link, with the strongest improvements observed in multi-crisis markets.

## Metadata
- **Published**: 2026-08-10T07:43:38Z
- **Authors**: Fabrizio Lillo, Giulia Livieri, Gianluca Palmari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09218v1)