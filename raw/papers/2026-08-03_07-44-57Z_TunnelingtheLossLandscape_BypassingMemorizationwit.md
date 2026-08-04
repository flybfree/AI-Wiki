---
title: Tunneling the Loss Landscape: Bypassing Memorization with Monte Carlo Parameter Swapping
published: 2026-08-03T07:44:57Z
authors: Lai Shun Chan, Xiaotian Zhang, Yue Shang, Ge Zhang, Entao Yang
url: http://arxiv.org/abs/2608.01833v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tunneling the Loss Landscape: Bypassing Memorization with Monte Carlo Parameter Swapping

## Abstract
Grokking is a striking phenomenon in neural network training, where a model can undergo a prolonged period of pure memorization before abrupt generalization. While previous works have attempted to interpret it through classical machine learning mechanisms like weight norm, recent research draws an analogy from statistical physics, framing grokking as a form of computational glass relaxation. This theory defines the initial memorization as a result of `fast cooling' where the training loss is reduced so quickly that a glass state is formed, followed by a `slow relaxation' towards final generalization. Although providing a unifying framework for representative grokking theories, this perspective has remained largely at the theoretical on macroscopic level without direct empirical validation on training dynamics. Here we introduce a three-component framework to directly characterize the training dynamics via parameter mobility (PM), and two representative measurements from glassy dynamics: replica correlation (RC) and fractal dimension (FD). We demonstrate that standard optimization presents clear signatures of glass dynamics and inherently traps the grokking network in a kinetic arrested memorization state with a collapsed mobility, strong history dependence, and channel-like motions. This quantitative agreement motivates us to introduce State-Aware Monte Carlo Parameter Swapping (SAM-Swap), an optimization plug-in that can accelerate generalization, inspired by swap Monte Carlo algorithm widely used in glass dynamics. Comparing SAM-Swap, weight decay, and Gaussian gradient noise, we find that accelerated generalization is consistently associated with random exploration in the parameter space, similar to diffusion in physics.

## Metadata
- **Published**: 2026-08-03T07:44:57Z
- **Authors**: Lai Shun Chan, Xiaotian Zhang, Yue Shang, Ge Zhang, Entao Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01833v1)