---
title: A Mean-Field Framework for Inference-Time Distributional Control of Diffusion Models
published: 2026-08-09T15:41:01Z
authors: Samuel Howard, Nikolas Nüsken
url: http://arxiv.org/abs/2608.08770v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Mean-Field Framework for Inference-Time Distributional Control of Diffusion Models

## Abstract
Diffusion models are increasingly used as controllable samplers, whose generations can be steered at inference time according to a chosen reward function. While such rewards are typically defined on individual samples, for many applications it is desirable to steer according to distribution-level rewards, for example to calibrate with population-level information or to encourage diversity. In both cases, simply incorporating the reward gradient into the dynamics, while often effective, comes with few theoretical guarantees on the sampled distribution. For pointwise rewards, recent work has therefore sought to develop a principled framework for targeting a prescribed tilted distribution using particle reweighting. However, an analogous theoretically-grounded approach for distributional rewards is currently lacking. In this work, we formulate inference-time distributional control as targeting a tilted measure under a mean-field framework, and derive a weighted interacting particle scheme to target it in a principled manner. Our framework recovers pointwise-reward steering as a special case, while providing a theoretical foundation for existing batch-level steering methods. Empirically, we verify that the procedure correctly targets the prescribed distribution in tractable low-dimensional settings, and investigate its behaviour in higher-dimensional protein conformation tasks.

## Metadata
- **Published**: 2026-08-09T15:41:01Z
- **Authors**: Samuel Howard, Nikolas Nüsken
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08770v1)