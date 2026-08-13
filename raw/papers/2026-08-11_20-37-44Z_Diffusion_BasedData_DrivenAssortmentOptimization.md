---
title: Diffusion-Based Data-Driven Assortment Optimization
published: 2026-08-11T20:37:44Z
authors: Junyi Liao, Xiaohui Jiang, Zhengwei Tong, Ethan X. Fang, Vahid Tarokh
url: http://arxiv.org/abs/2608.11419v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diffusion-Based Data-Driven Assortment Optimization

## Abstract
Assortment optimization is a fundamental problem in revenue management, typically addressed using parametric choice models such as the multinomial logit (MNL) and its variants. While these models enable tractable formulations, their performance is sensitive to model misspecification and often struggles to capture complex customer behavior. In this paper, we propose a model-agnostic framework for assortment optimization based on guided discrete diffusion. We represent assortments as binary vectors and perform stochastic search via a learned reverse diffusion process, avoiding explicit combinatorial enumeration. To incorporate decision objectives, we introduce a reward-guided mechanism that biases local transitions using estimates of expected revenue. This allows the method to effectively balance exploration and exploitation during generation. Empirically, we show that the proposed approach consistently identifies high-quality assortments and remains robust under model misspecification, often recovering near-optimal solutions in high-dimensional settings. Moreover, the generative nature of diffusion enables the production of diverse high-performing assortments, offering flexibility beyond a single deterministic solution. These results highlight the potential of generative modeling as a scalable and robust paradigm for combinatorial optimization in data-driven decision-making.

## Metadata
- **Published**: 2026-08-11T20:37:44Z
- **Authors**: Junyi Liao, Xiaohui Jiang, Zhengwei Tong, Ethan X. Fang, Vahid Tarokh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11419v1)