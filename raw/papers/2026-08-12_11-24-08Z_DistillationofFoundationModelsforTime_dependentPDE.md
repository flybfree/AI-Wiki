---
title: Distillation of Foundation Models for Time-dependent PDEs
published: 2026-08-12T11:24:08Z
authors: Daniel Musekamp, Boshra Ariguib, Andrei Manolache, Mathias Niepert
url: http://arxiv.org/abs/2608.11937v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distillation of Foundation Models for Time-dependent PDEs

## Abstract
Foundation models for time-dependent partial differential equations (PDEs) are trained on large and diverse collections of physical systems and can generalize effectively to new downstream tasks. After fine-tuning on only a few trajectories from a target domain, they can achieve strong accuracy in low-data regimes. However, these models are typically large and computationally intensive, limiting their usefulness as fast surrogates for numerical solvers. We propose Teacher Rollout Extension (TREX), a knowledge distillation framework that transfers the predictive capability of a pretrained foundation model into a compact and efficient student. Starting from a fine-tuned teacher, TREX augments limited downstream data by generating long synthetic trajectories through teacher rollouts, optionally with periodic noise injection. This procedure samples from the teacher-induced rollout distribution without requiring explicit knowledge of the initial-condition distribution, while exposing the student to long-horizon states and local recovery behavior around states encountered during autoregressive prediction. The student can further incorporate task-specific inductive biases, such as equivariance, that the teacher does not necessarily enforce. We evaluate TREX on multiple PDE benchmarks. The resulting students can match or surpass the teacher's accuracy while reducing the number of parameters by several orders of magnitude and achieving more than an order-of-magnitude speedup in inference.

## Metadata
- **Published**: 2026-08-12T11:24:08Z
- **Authors**: Daniel Musekamp, Boshra Ariguib, Andrei Manolache, Mathias Niepert
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11937v1)