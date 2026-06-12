---
title: Reinforcement Learning for Neural Model Editing
published: 2026-06-11T15:16:42Z
authors: Shaivi Malik
url: http://arxiv.org/abs/2606.13461v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reinforcement Learning for Neural Model Editing

## Abstract
Editing pretrained neural networks requires specialized algorithms tailored to specific objectives. Designing such algorithms is often time-consuming and demands significant effort. We present an exploratory framework that formulates neural model editing as a reinforcement learning problem, where agents modify models using reward feedback. We introduce two environments: MaskWorld, where agents scale weights multiplicatively, and ShiftWorld, where agents apply additive weight updates. The reward function combines a utility-preservation objective with a task-specific editing objective, enabling agents to learn targeted modifications while maintaining overall model performance. We evaluate the framework on bias mitigation in text classification and machine unlearning in image classification, both of which traditionally rely on specialized algorithms. Our results show that the learned policies reduce forget set accuracy to nearly 0% while preserving over 90% retain set accuracy on the unlearning task. In the bias mitigation setting, the learned policies improve bias-related performance by more than 5% while maintaining general classification utility. Our findings show that neural model editing can be cast as a reinforcement learning problem, allowing editing policies to be learned from reward feedback rather than manually engineered for each task.

## Metadata
- **Published**: 2026-06-11T15:16:42Z
- **Authors**: Shaivi Malik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.13461v1)