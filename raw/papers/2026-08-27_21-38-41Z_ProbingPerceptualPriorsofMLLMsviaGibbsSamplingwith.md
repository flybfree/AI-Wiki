---
title: Probing Perceptual Priors of MLLMs via Gibbs Sampling with Interpretable Generative Controls
published: 2026-08-27T21:38:41Z
authors: Manuel Cherep, Pattie Maes, Nikhil Singh
url: http://arxiv.org/abs/2608.27727v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Probing Perceptual Priors of MLLMs via Gibbs Sampling with Interpretable Generative Controls

## Abstract
A model's behavior on a task is jointly determined by the input it receives and the prior it brings in, i.e. the distribution over stimuli it implicitly expects. Interpretability research has traditionally studied models by holding inputs fixed and examining model responses either mechanistically, probing how internal structure represents inputs, or behaviorally, measuring how variation in inputs leads to variation in outputs. Neither reconstructs the prior distribution itself, since internal structure shows what a model can represent, not what it expects, and any fixed stimulus set leaves most of the possible input space unseen. In particular, such an input space in real-world settings, such as images seen by VLMs, is extremely high-dimensional and diverse. These priors thus remain a poorly understood component of models that nonetheless influence real-world behavior. We propose a method to sample from models' perceptual prior distributions directly, by steering a generative model to produce stimuli along controllable axes and running Gibbs sampling over that space with the model under study as the judge. We apply this to a variety of categories and target variables (such as trustworthiness in faces and cheapness in art images) and recover both canonical biases and surprising novel priors invisible to direct prompting, warranting further investigation of their downstream effects.

## Metadata
- **Published**: 2026-08-27T21:38:41Z
- **Authors**: Manuel Cherep, Pattie Maes, Nikhil Singh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27727v1)