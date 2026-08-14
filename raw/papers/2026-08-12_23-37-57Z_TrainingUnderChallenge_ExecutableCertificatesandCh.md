---
title: Training Under Challenge: Executable Certificates and Challenge-Closed Optimality for Neural Networks
published: 2026-08-12T23:37:57Z
authors: Farhang Yeganegi, Arian Eamaz, Mojtaba Soltanalian
url: http://arxiv.org/abs/2608.12655v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training Under Challenge: Executable Certificates and Challenge-Closed Optimality for Neural Networks

## Abstract
A flat training curve does not reveal whether a neural network has reached a global optimum, is locally trapped, is representation-limited, or is mismatched to its trainer. We introduce Training Under Challenge, an executable-certificate framework in which predeclared, architecture-valid procedures construct complete alternatives in the same certified class and reevaluate the same objective. Any lower-valued candidate is a replayable witness that lower-bounds the checkpoint's empirical global-optimality gap. Passing a finite suite is only suite-relative; global-gap conclusions require a separately justified coverage mechanism. We define a resource-indexed challenge-power modulus that characterizes the largest gap compatible with passage. For squared loss, current block-decrease operators make coverage checkable and yield uniform and realized-residual bounds. We prove the converse frontier: without coverage, a first-order ReLU trainer can reach infinitely many exact conditional head optima while converging to a non-global point. On a channel-gated ResNet-18 distillation problem with known optimum, eight internal challenges cover all 240 audited output directions, and realized-residual bounds lie within factors of 1.74--3.02 of the true gap. Paired predictive certificates separate decoder under-use from representation insufficiency, while quantized-denoising studies demonstrate diagnosis, repair, and current-state recertification.

## Metadata
- **Published**: 2026-08-12T23:37:57Z
- **Authors**: Farhang Yeganegi, Arian Eamaz, Mojtaba Soltanalian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12655v1)