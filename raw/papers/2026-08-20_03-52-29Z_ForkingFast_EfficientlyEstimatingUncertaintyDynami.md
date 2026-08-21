---
title: Forking Fast: Efficiently Estimating Uncertainty Dynamics in Text Generation
published: 2026-08-20T03:52:29Z
authors: Eric Bigelow, Amir Zur, Satchel Grant, Tal Haklay, Can Rager, Owen Lewis, Thomas McGrath, Jack Merullo, Ekdeep Singh Lubana, Atticus Geiger
url: http://arxiv.org/abs/2608.19611v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Forking Fast: Efficiently Estimating Uncertainty Dynamics in Text Generation

## Abstract
LLM reasoning is stochastic, and so understanding a model requires grappling with the distribution of reasoning chains that it might produce for a given question, i.e., its uncertainty. Resampling-based analyses characterize this distribution, revealing which steps of a rollout determine how the model arrives at its answer. However, a major limitation of these approaches is that resampling text sequences at every token or sentence in a reasoning chain is very costly. Our work strives to make resampling analysis more computationally efficient, while also shedding light on an important scientific question: what is the right statistical model for explaining uncertainty dynamics in text generation? We show that when resampling many reasoning chains, uncertainty dynamics converge to stable patterns, and noise is largely an artifact of sampling rather than an LLM's sensitivity to each individual token or reasoning step. We develop a statistical model for smoothing noisy low-sample rollout data to better approximate high-sample data, allowing us to significantly cut sampling costs.

## Metadata
- **Published**: 2026-08-20T03:52:29Z
- **Authors**: Eric Bigelow, Amir Zur, Satchel Grant, Tal Haklay, Can Rager, Owen Lewis, Thomas McGrath, Jack Merullo, Ekdeep Singh Lubana, Atticus Geiger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19611v1)