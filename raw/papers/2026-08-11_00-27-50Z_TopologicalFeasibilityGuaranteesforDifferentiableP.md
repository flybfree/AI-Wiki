---
title: Topological Feasibility Guarantees for Differentiable Predictive Control
published: 2026-08-11T00:27:50Z
authors: Guangyu Wu, Ján Drgoňa
url: http://arxiv.org/abs/2608.10332v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Topological Feasibility Guarantees for Differentiable Predictive Control

## Abstract
Differentiable predictive control (DPC), a self-supervised learning approach for approximating explicit model predictive control (MPC) policies, offers significant computational advantages over online optimization-based MPC. However, feasibility guarantees, a core requirement for safe control, are currently provided either probabilistically or via online safety filters. The lack of rigorous feasibility guarantees for offline policy optimization remains an open problem. This paper establishes deterministic feasibility guarantees for DPC using a novel topological analysis of the induced reachable safe set, without requiring online safety filters. By exploiting the inherent model-based nature of DPC, in which differentiable system dynamics are embedded directly into the computational graph, we analyze the properties of the learned control policies and the corresponding system states from topological and geometric perspectives. Inspired by our theoretical analysis, we propose a novel self-supervised offline policy learning strategy that utilizes a proxy loss with Control Barrier Functions (CBFs). Crucially, these properties not only significantly improve policy training but also enable the derivation of strict, deterministic feasibility guarantees from a finite number of training samples. Extensive closed-loop simulations validate our theoretical findings, demonstrating that the empirical constraint violations monotonically decrease to zero as the training sample size increases. Ultimately, this work illustrates that DPC policy optimization yields formal safety certificates that are structurally unattainable with conventional black-box methods, e.g., reinforcement learning (RL) or supervised learning-based approximate MPC, thereby providing a new perspective on feasibility guarantees in learning-based control.

## Metadata
- **Published**: 2026-08-11T00:27:50Z
- **Authors**: Guangyu Wu, Ján Drgoňa
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10332v1)