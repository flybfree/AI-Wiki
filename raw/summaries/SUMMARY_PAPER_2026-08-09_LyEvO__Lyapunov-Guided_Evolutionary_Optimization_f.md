---
title: LyEvO: Lyapunov-Guided Evolutionary Optimization for Safe and Robust Sim-to-Real Policy Learning
url: http://arxiv.org/abs/2608.06481v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-06_18-19-33Z_LyEvO_Lyapunov_GuidedEvolutionaryOptimizationforSa.md
generated_at: 2026-08-09 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LyEvO, a physics‑grounded framework that merges constrained evolutionary optimization with statistical model checking and Lyapunov stability analysis to train safe and robust sim‑to‑real policies. Experiments on Cartpole and 3D Quadrotor show that the method yields controllers that remain stable in simulation while achieving reliable performance when transferred to real hardware.

## Key Takeaways
- LyEvO computes an initial candidate stability region using Lyapunov analysis, providing a principled starting point for optimization.
- The framework iteratively refines this region by generating operational scenarios drawn from the current region and verifying them statistically through SMC‑based model checking.
- Deployment readiness is assessed by expanding or contracting the stability region based on verification outcomes, offering a practical criterion for real‑world deployment.

## Context
Sim‑to‑real transfer remains challenging because policies that perform well in simulation often degrade when faced with physical uncertainties. Existing methods either rely solely on offline validation or lack systematic integration of system dynamics into optimization loops. LyEvO addresses these gaps by embedding Lyapunov theory directly into the evolutionary process, thus aligning theoretical stability with empirical verification.

## Implications
For robotics and autonomous systems, LyEvO provides a reproducible pipeline that reduces risk during deployment by continuously monitoring safety margins. Practitioners can leverage this approach to accelerate development cycles while ensuring that simulated policies are robust enough for real‑world operation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06481v1)
