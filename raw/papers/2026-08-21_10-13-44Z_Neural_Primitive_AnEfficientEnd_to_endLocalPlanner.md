---
title: Neural-Primitive: An Efficient End-to-end Local Planner with Primitive-based Imitation Learning for Autonomous Flight
published: 2026-08-21T10:13:44Z
authors: Zhitao Liu, Guangtong Xu, Zihan Wang, Jialiang Hou, Chao Xu, Fei Gao
url: http://arxiv.org/abs/2608.20948v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neural-Primitive: An Efficient End-to-end Local Planner with Primitive-based Imitation Learning for Autonomous Flight

## Abstract
Autonomous flight in unknown cluttered environments is hindered by the computation-quality-memory trilemma of onboard trajectory generation. In this paper, we propose an efficient end-to-end local planner via imitation learning. A lightweight offline-primitive-based dataset collection framework is designed to produce safe and high-quality trajectory primitives in non-convex environments. A compact neural network directly maps sensory inputs to polynomial coefficients that inherently encode higher-order dynamical information. The learned policy generates smooth, empirically collision-free and dynamically feasible trajectories in real time without back-end solving. It achieves ultra-fast computation (below 1ms on a standard desktop and average 3.68ms during onboard flight), while maintaining low onboard memory requirements (less than 1.5MiB). Extensive simulation benchmarks demonstrate superiority in both planning latency and target-reaching progress quality. Zero-shot deployment in real-world experiments further validates the robust sim-to-real transfer capability of the proposed method.

## Metadata
- **Published**: 2026-08-21T10:13:44Z
- **Authors**: Zhitao Liu, Guangtong Xu, Zihan Wang, Jialiang Hou, Chao Xu, Fei Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20948v1)