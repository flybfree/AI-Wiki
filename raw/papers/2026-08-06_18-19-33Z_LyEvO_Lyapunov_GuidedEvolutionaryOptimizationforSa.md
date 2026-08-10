---
title: LyEvO: Lyapunov-Guided Evolutionary Optimization for Safe and Robust Sim-to-Real Policy Learning
published: 2026-08-06T18:19:33Z
authors: Riccardo Curcio, Hongpeng Cao, Marco Caccamo
url: http://arxiv.org/abs/2608.06481v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LyEvO: Lyapunov-Guided Evolutionary Optimization for Safe and Robust Sim-to-Real Policy Learning

## Abstract
Training controllers that are safe and robust in simulation, and systematically assessing their readiness for real-world deployment, remain key challenges in sim-to-real transfer. To address this, we propose LyEvO, a physics-grounded framework that combines constrained Evolutionary Optimization and Statistical Model Checking (SMC)-based verification with Lyapunov-based stability analysis. Leveraging prior knowledge of the system dynamics, LyEvO uses Lyapunov analysis to compute an initial candidate stability region. An iterative loop then uses operational scenarios drawn from this region to jointly optimize and statistically verify a policy, and subsequently expands the region's boundaries based on the verification outcome. This integrated procedure provides a practical criterion for assessing deployment readiness. We evaluate LyEvO on Cartpole and 3D Quadrotor benchmarks through extensive simulations and targeted real-world experiments, demonstrating safe and robust sim-to-real transfer.

## Metadata
- **Published**: 2026-08-06T18:19:33Z
- **Authors**: Riccardo Curcio, Hongpeng Cao, Marco Caccamo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06481v1)