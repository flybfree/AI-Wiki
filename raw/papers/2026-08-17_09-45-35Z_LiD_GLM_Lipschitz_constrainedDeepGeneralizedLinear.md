---
title: LiD-GLM: Lipschitz-constrained Deep Generalized Linear Models
published: 2026-08-17T09:45:35Z
authors: Tom Splittgerber, Niklas Koenen, Marvin N. Wright, Werner Brannath
url: http://arxiv.org/abs/2608.16340v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LiD-GLM: Lipschitz-constrained Deep Generalized Linear Models

## Abstract
The combination of traditional statistical models and neural network (NN) components into semi-structured hybrid models is an intriguing approach to construct models that, ideally, combine traditional interpretability with the unprecedented flexibility of NNs. In order to preserve interpretability, it is usually necessary to restrict the NN components to prevent them from dominating the model. However, existing methods that enforce structural constraints on their NN components severely limit their models' flexibility; in contrast, methods that only enforce weak, indirect constraints lose meaningful interpretability. The method we propose therefore leverages invertible residual neural networks (i-ResNets) to equip generalized linear models with both nonlinear parameter estimation and a flexible correction of their distributional assumptions while always retaining stochastic monotonicity of the modeled distribution in the (formerly linear) predictor. The i-ResNets correspond to a controlled deviation from identity and by constraining their Lipschitz constant one can rigorously limit and quantify how far the hybrid model deviates from its traditional counterpart. This enables a user-specifiable compromise between flexibility and interpretability without limiting the structure of nonlinear and interaction effects that can be learned. Furthermore, we develop specific inherent interpretation techniques for our model and enforce model identifiability through an adapted post-hoc orthogonalization.

## Metadata
- **Published**: 2026-08-17T09:45:35Z
- **Authors**: Tom Splittgerber, Niklas Koenen, Marvin N. Wright, Werner Brannath
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16340v1)