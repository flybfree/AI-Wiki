---
title: Time Without Timesteps: Simulating Coupled Dynamical Systems via Self-Consistency
url: http://arxiv.org/abs/2609.03358v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_04-32-23Z_TimeWithoutTimesteps_SimulatingCoupledDynamicalSys.md
generated_at: 2026-09-03 22:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a self‑consistency framework for simulating coupled dynamical systems by training neural surrogates that map full inputs to complete outputs, eliminating the need for step‑by‑step integration. The method reduces computational depth to a few Newton iterations and shows that gradient computation becomes independent of solver steps. Experiments on van der Pol oscillators and Hodgkin‑Huxley networks demonstrate convergence up to a spectral radius boundary beyond which unrolled backpropagation fails.

## Key Takeaways
- Neural surrogates replace explicit time marching, producing full output trajectories from a single input trajectory and initial condition.  
- The simulation is solved as a fixed‑point problem where the number of Newton iterations (4–10) corresponds to solver depth rather than the integrator’s 1500 steps.  
- Gradient computation is linearized via GMRES, giving memory‑independent performance and an error below 0.04% even near divergence.

## Context
The work aligns with efforts to replace traditional ODE solvers in AI research with differentiable models that can be optimized end‑to‑end. By decoupling time resolution from computational depth, it enables scalable training of complex coupled dynamics without sacrificing gradient fidelity.

## Implications
This approach could accelerate the development of biologically realistic simulations and large‑scale physics‑informed neural networks where traditional solvers become bottlenecks. Practitioners may adopt self‑consistency methods to reduce memory usage and improve convergence robustness in real‑time applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03358v1)
