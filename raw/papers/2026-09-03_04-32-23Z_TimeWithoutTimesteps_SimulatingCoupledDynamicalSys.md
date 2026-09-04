---
title: Time Without Timesteps: Simulating Coupled Dynamical Systems via Self-Consistency
published: 2026-09-03T04:32:23Z
authors: Liyu Zerihun, Mark Shinyoung Lee
url: http://arxiv.org/abs/2609.03358v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Time Without Timesteps: Simulating Coupled Dynamical Systems via Self-Consistency

## Abstract
Numerical simulation of dynamical systems is usually organized as a causal march through time: each state is computed from the previous one. We explore a different formulation for coupled systems. For each subsystem type we train a neural surrogate mapping a full driving trajectory and initial condition directly to a full output trajectory; following classical waveform relaxation, coupled systems are assembled by enforcing self-consistency among these trajectories: simulation becomes a fixed-point problem over complete trajectories rather than a stepwise rollout. On coupled van der Pol oscillators and Hodgkin-Huxley neuron networks, sequential depth becomes the number of solver iterations: 4-10 Newton iterations where the reference integrator takes 1500 steps. The gradient likewise loses its time recursion: it becomes a linear system solved by GMRES at memory independent of solver depth. A single scalar measured from the learned operator, the spectral radius of its Jacobian, predicts in advance where the coupled solve will converge; past that boundary, unrolled backpropagation diverges and a Neumann adjoint fails, while the implicit gradient remains correct to 0.04%. We report where the approach succeeds and where surrogate error degrades it.

## Metadata
- **Published**: 2026-09-03T04:32:23Z
- **Authors**: Liyu Zerihun, Mark Shinyoung Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03358v1)