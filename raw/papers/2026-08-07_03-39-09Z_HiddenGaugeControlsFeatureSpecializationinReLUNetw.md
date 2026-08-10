---
title: Hidden Gauge Controls Feature Specialization in ReLU Networks
published: 2026-08-07T03:39:09Z
authors: Tongxi Wang
url: http://arxiv.org/abs/2608.06766v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hidden Gauge Controls Feature Specialization in ReLU Networks

## Abstract
Training changes a network's predictions while allocating task-relevant structure across its internal units. In an overparameterized ReLU network, several neurons can begin with exactly the same functional role, yet one may acquire a teacher feature while the others become redundant. We call the identity of that neuron feature ownership and ask whether it can be controlled by a parameter choice invisible to the initial predictor. In a tractable Gaussian teacher--student model, we fix the complete initial function and vary only a positive-homogeneous scaling gauge. Opposite gauges produce distinct feature trajectories and a sharp $Θ(D^2)$ separation in specialization time that no global change of clock can explain. Among any fixed number of initially duplicate students, assigning the favorable gauge to one neuron deterministically selects it as the owner and drives the remaining functional contribution to zero. An exact reaction--transport decomposition attributes the effect to different mobilities for changing a feature's coefficient and direction. We prove global selection and functional pruning, extend finite-time selection to visible perturbations and small-step full-batch gradient descent, and verify the predicted loss, alignment, pruning, and dissipation trajectories in population and finite-sample training. The initial predictor therefore determines neither when the feature is learned nor which neuron learns it.

## Metadata
- **Published**: 2026-08-07T03:39:09Z
- **Authors**: Tongxi Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06766v1)