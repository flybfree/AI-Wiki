---
title: Flow Map Learning via Nongradient Vector Flow
published: 2026-07-29T02:17:27Z
authors: Mark Goldstein, Anshuk Uppal, Raghav Singhal, Aahlad Puli, Rajesh Ranganath
url: http://arxiv.org/abs/2607.26398v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Flow Map Learning via Nongradient Vector Flow

## Abstract
Diffusion and flow-based models benefit from simple regression losses, but inference incurs significant overhead because sampling requires integration. Consistency models address this by directly learning the flow maps along the ODE trajectory, opening a design space between one-step and many-step approaches. However, existing methods face computational challenges such as requiring model inverses or backpropagation through iterated model calls, and do not always prove that the desired ODE flow map is a solution to the loss. We introduce SGFlow, an approach for learning flow maps that bypasses explicit invertibility constraints and expensive differentiation through model iteration. SGFlow trains a model to compute both the ODE solutions and the implied velocity from scratch by following non-conservative dynamics with a stationary point at the desired flow map. On the CIFAR image benchmark, no single method attains the best FID at every step count: SGFlow attains the best FID at 10 sampling steps and remains competitive with flow matching, Meanflow, and Lagrangian map matching at other step counts, while being the only one with a proven stationary-point guarantee for its stopgrad-based dynamics.

## Metadata
- **Published**: 2026-07-29T02:17:27Z
- **Authors**: Mark Goldstein, Anshuk Uppal, Raghav Singhal, Aahlad Puli, Rajesh Ranganath
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26398v1)