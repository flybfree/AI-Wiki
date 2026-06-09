# Summary: 2026-04-24_17-46-55Z_Relaxation_InformedTrainingofNeuralNetworkSurrogat.md
Saved: 2026-05-07 22:29
Source: 2026-04-24_17-46-55Z_Relaxation_InformedTrainingofNeuralNetworkSurrogat.md
Model: None

---

## Summary
ReLU neural networks trained as surrogate models can be embedded exactly in mixed-integer linear programs (MILPs), enabling global optimization over the learned function. The tractability of the resulting MILP depends on structural properties of the network, i.e., the number of binary variables in associated formulations and the tightness of the continuous LP relaxation. These properties are determined during training, yet standard training objectives (prediction loss with classical weight regularization) offer no mechanism to directly control them.

## Key Takeaways
- ReLU neural networks trained as surrogate models can be embedded exactly in mixed-integer linear programs (MILPs), enabling global optimization over the learned function.
- The tractability of the resulting MILP depends on structural properties of the network, i.e., the number of binary variables in associated formulations and the tightness of the continuous LP relaxation.
- These properties are determined during training, yet standard training objectives (prediction loss with classical weight regularization) offer no mechanism to directly control them.

## Context
ReLU neural networks trained as surrogate models can be embedded exactly in mixed-integer linear programs (MILPs), enabling global optimization over the learned function.

## Implications
Experiments on non-convex benchmark functions and a two-stage stochastic programming problem with quantile neural network surrogates demonstrate that the proposed regularizers can reduce MILP solve times by up to four orders of magnitude relative to an unregularized baseline, while maintaining competitive surrogate model accuracy.

## Original Reference
- Title: Relaxation-Informed Training of Neural Network Surrogate Models
- Authors: Calvin Tsay
- Published: 2026-04-24T17:46:55Z
- URL: http://arxiv.org/abs/2604.22746v1
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-04-24_17-46-55Z_Relaxation_InformedTrainingofNeuralNetworkSurrogat.md

[[2026-04-24_17-46-55Z_Relaxation_InformedTrainingofNeuralNetworkSurrogat.md]]