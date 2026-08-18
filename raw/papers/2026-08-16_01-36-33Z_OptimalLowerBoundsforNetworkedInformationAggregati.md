---
title: Optimal Lower Bounds for Networked Information Aggregation
published: 2026-08-16T01:36:33Z
authors: Ambar Pal
url: http://arxiv.org/abs/2608.15472v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Optimal Lower Bounds for Networked Information Aggregation

## Abstract
The problem of networked information aggregation, studied in Kearns et al. (2026), involves a group of learners situated on the vertices of a directed acyclic graph $G$, each learning a linear predictor $\widehat Y$ for a fixed random variable $Y$ given access to a local feature, as well as the predictors learnt by its parents. Learning proceeds iteratively, with learners ordered according to a topological sort of $G$. The main quantity of interest is the error incurred by the current learner, constrained to this flow of information, with respect to the best linear predictor using all the features seen so far. When the studied error is the MSE, i.e., $\mathbb{E} (\widehat Y - Y)^2$, Kearns et al. (2026) show that the error is at most $O(1/\sqrt{D})$ along a path of length $D$. They also obtain a hard instance where the MSE is lower bounded by $Ω(1/D)$, leaving the correct order open. In this work, we resolve this central open problem, and obtain a family of worst case problem instances with a MSE lower bound of $Ω(1/\sqrt{D})$.   By exploiting invariances in the structure of the learnt predictors, our analysis generalizes to all convex loss functions $\ell(\widehat Y, Y)$ satisfying regularity conditions which include strong convexity in a ball around the origin, and that the ideal predictor minimizing the population loss is positively correlated with the label. We show that networked information aggregation on a gaussian instance in our worst case family incurs an $\ell$-error lower bounded by $Ω(1/\sqrt{D})$ with respect to this ideal predictor. We demonstrate that a variety of common losses satisfy these regularity conditions. In particular, the logistic loss satisfies them, and hence our analysis also closes the gap between the upper and lower bounds in Bateni et al. (2026).

## Metadata
- **Published**: 2026-08-16T01:36:33Z
- **Authors**: Ambar Pal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15472v1)