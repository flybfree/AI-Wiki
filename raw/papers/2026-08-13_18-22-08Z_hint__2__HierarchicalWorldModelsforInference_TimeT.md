---
title: hint$^2$: Hierarchical World Models for Inference-Time Temporal Logic Guidance
published: 2026-08-13T18:22:08Z
authors: Moritz Zoellner, Anastasios Manganaris, Ahmed H. Qureshi, Rohan Paleja
url: http://arxiv.org/abs/2608.13678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# hint$^2$: Hierarchical World Models for Inference-Time Temporal Logic Guidance

## Abstract
A central goal of robot learning is to enable robots to execute rich instructions specified at runtime. Large-scale language-conditioned policies have made substantial progress toward this goal, yet still struggle with temporal structure and safety constraints. Linear Temporal Logic (LTL) provides a powerful language to express complex, non-Markovian instructions. However, guiding learned manipulation policies toward LTL satisfaction remains challenging because modern policies generate short-horizon action chunks and replan in closed loop, while almost all LTL specifications are evaluated over long-horizon trajectories. In this paper, we introduce hint$^2$, a method for guiding short-horizon policies toward satisfying complex LTL specifications at inference time using hierarchical world models. Our key idea is to derive two separate guidance objectives using each world model's abstraction level. A high-level model predicts future action-induced transitions in task-relevant atomic propositions to guide progress through the LTL automaton, while a low-level dynamics model predicts immediate state evolution for accurate local safety guidance. Our results show that hint$^2$ overcomes the limitations of current LTL-guided diffusion methods, outperforms existing inference-time steering methods in CALVIN, and successfully completes instructions with complex liveness and safety constraints more elegantly than language-conditioned alternatives. Finally, we demonstrate that hint$^2$ can handle complex instructions on a real UR5e manipulator.

## Metadata
- **Published**: 2026-08-13T18:22:08Z
- **Authors**: Moritz Zoellner, Anastasios Manganaris, Ahmed H. Qureshi, Rohan Paleja
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13678v1)