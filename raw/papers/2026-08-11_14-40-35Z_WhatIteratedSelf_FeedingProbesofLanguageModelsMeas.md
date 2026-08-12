---
title: What Iterated Self-Feeding Probes of Language Models Measure, and a test that separates the construction from the model
published: 2026-08-11T14:40:35Z
authors: Nicolás Vera Zúñiga
url: http://arxiv.org/abs/2608.10986v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Iterated Self-Feeding Probes of Language Models Measure, and a test that separates the construction from the model

## Abstract
A growing class of methods probes a language model by feeding it its own output: self-consistency, iterated refinement, agentic loops. We ask what such a probe measures, in a construction chosen to make the question sharp: a ring of token cells resampled in place by the model's own windowed conditional p_r(x_i | x_{i+-r}). The substrate is Glauber dynamics on token sequences and is not new; what we change is the coupling. Advancing two rings that differ in one token under common random numbers makes undamaged copies diverge by exactly zero, so damage spreading becomes measurable where a maximal coupling gives mixing times instead. The answer is that it measures two different things at once, in readings that look alike. Some quantities are fixed by the construction: the damage light cone is kinematic, and the radius scaling of the token-space Lyapunov exponent lambda_ca(r) is model-invariant across 19 models and two scale ladders spanning 70x. Others genuinely track the model: lambda_ca crosses zero at a reproducible point in training, and the attractor share ranks models consistently however the lattice is built. Left undistinguished, the first kind is readily mistaken for the second -- we did so ourselves for four months, and report a phase transition we measured to three decimal places that belongs to the probe rather than to any language model. We give the test that separates them: hold the construction fixed and vary the model, or hold the model fixed and vary the construction, and see which readings move. We validate the instrument by reproduction first, recovering a Domany-Kinzel damage field bit-exactly against an independent prediction, and we report the estimator failures that this discipline caught -- four retracted verdicts, each on a quantity that looked like a measurement. The methodology ships as a package.

## Metadata
- **Published**: 2026-08-11T14:40:35Z
- **Authors**: Nicolás Vera Zúñiga
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10986v1)