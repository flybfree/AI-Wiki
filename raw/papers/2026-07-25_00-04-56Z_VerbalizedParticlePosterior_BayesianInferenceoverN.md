---
title: Verbalized Particle Posterior: Bayesian Inference over Natural Language Hypotheses
published: 2026-07-25T00:04:56Z
authors: Yan Zhang, Shikan Lian, Shibo Li
url: http://arxiv.org/abs/2607.22961v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Verbalized Particle Posterior: Bayesian Inference over Natural Language Hypotheses

## Abstract
Verbalized Machine Learning (VML) parameterizes a model as a natural-language prompt that an LLM evaluates as f(x; theta). The framework is interpretable, but it commits to a single hypothesis with no measure of uncertainty, and that hypothesis varies substantially across optimization runs on the same data. We propose the Verbalized Particle Posterior (VPP), which treats verbalized learning as a Bayesian inference problem: maintain a population of natural-language hypotheses as particles, update them with Metropolis-Hastings (VPP-MH) or Sequential Monte Carlo (VPP-SMC), and predict by Bayesian model averaging. Both algorithms treat the LLM as a black box, requiring no access to logits or gradients. A distinctive consequence follows. In classical Bayesian learning, model selection sits outside the posterior; in VPP both model structure and parameters share a single language space, and the posterior ranges over both. We evaluate VPP on regression, classification, and rule-discovery benchmarks. It improves over a single VML run on every benchmark and matches or exceeds an oracle-best ensemble of independent VML runs on most, while eliminating the catastrophic single-run failures that VML occasionally produces. Because each particle is a human-readable hypothesis, the posterior is itself something a reader can inspect, seeing in plain text which explanations the data supported and which it ruled out.

## Metadata
- **Published**: 2026-07-25T00:04:56Z
- **Authors**: Yan Zhang, Shikan Lian, Shibo Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22961v1)