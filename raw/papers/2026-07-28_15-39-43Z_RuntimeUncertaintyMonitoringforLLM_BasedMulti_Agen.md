---
title: Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks
published: 2026-07-28T15:39:43Z
authors: Bart Custers, Koorosh Aslansefat
url: http://arxiv.org/abs/2607.25877v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks

## Abstract
This paper investigates how multi-agent systems (MAS)-based on large language models (LLMs) can support actuarial risk modelling, with a particular focus on uncertainty quantification. Actuarial workflows represent a high-stakes decision-support setting where unreliable outputs may lead to incorrect risk assessment, unfair pricing, and regulatory non-compliance. To address uncertainty introduced by the probabilistic nature of LLMs and dependencies between agents, a multi-agent framework is proposed in which specialised agents perform data preparation, modelling, review, and explanation tasks under a central hub. The main contribution is a novel approach to uncertainty propagation using token-level log-probabilities and a Bayesian Network. Importantly, log probabilities are not treated as direct probabilities of correctness or task success. Instead, length-normalised log-probability summaries are transformed into calibrated task-level confidence estimates before incorporation into the Bayesian Network. Results show that the framework reproduces baseline actuarial performance while providing additional insight into workflow stability and runtime uncertainty propagation.

## Metadata
- **Published**: 2026-07-28T15:39:43Z
- **Authors**: Bart Custers, Koorosh Aslansefat
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25877v1)