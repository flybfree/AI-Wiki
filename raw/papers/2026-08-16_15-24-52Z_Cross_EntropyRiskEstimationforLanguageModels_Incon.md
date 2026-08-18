---
title: Cross-Entropy Risk Estimation for Language Models: Inconsistency Must Be Dense, and the Holdout Method Is No Exception
published: 2026-08-16T15:24:52Z
authors: Hanti Lin
url: http://arxiv.org/abs/2608.15798v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Entropy Risk Estimation for Language Models: Inconsistency Must Be Dense, and the Holdout Method Is No Exception

## Abstract
Language models are compared by their held-out per-token cross-entropy risk---the quantity scaling laws are fitted to. We show that it cannot be consistently estimated. Consistency, or convergence to the estimand, is defined relative to a \emph{possible state of the world}: a pair consisting of a data-generating distribution and a model we turn out to train. Quantifying over models as well as data-generating mechanisms is essential, because what decides whether a model's risk is estimable is a tail property of the distribution its weights induce, which no sample reveals. The per-token cross-entropy risk is hard to estimate because of a topological fact: among the possible states, finite risk and infinite risk each lie arbitrarily close to every instance of the other. Consequently no estimator---not merely the holdout average---is consistent at every state at which the risk is defined. Worse, inconsistent estimation persists under both bounding the expected sequence length and restricting to full-support models; and in that restricted setting the states at which inconsistency occurs are even dense. Two interesting ways out are identified, and neither is free. Way out 1: using a bounded context window, we can floor a model's next-token probabilities, making its risk finite exactly when the data-generating distribution has finite expected sequence length---a new, statistical rationale for a choice that was made on computational grounds, though the assumption it substitutes is itself beyond the reach of any test. Way out 2: reporting the risk only when it falls below a threshold fixed in advance restores consistency, at no cost to what model selection actually requires---but we need to recognize that the goal of estimation is revised.

## Metadata
- **Published**: 2026-08-16T15:24:52Z
- **Authors**: Hanti Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15798v1)