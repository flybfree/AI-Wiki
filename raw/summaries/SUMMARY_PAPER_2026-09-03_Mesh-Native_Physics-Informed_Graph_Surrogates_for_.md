---
title: Mesh-Native Physics-Informed Graph Surrogates for TCAD-in-the-Loop Design Space Exploration
url: http://arxiv.org/abs/2609.02988v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-02_15-15-29Z_Mesh_NativePhysics_InformedGraphSurrogatesforTCAD_.md
generated_at: 2026-09-03 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a physics‑informed graph attention network that runs directly on tetrahedral mesh nodes of drift‑diffusion TCAD simulations, predicting electrostatic potential and quasi‑Fermi levels. Training uses a data loss combined with finite‑volume current continuity residuals to embed carrier transport physics. The surrogate enables fast per‑design inference and an active‑learning loop that selects the most informative designs for full simulation.

## Key Takeaways
- A mesh‑native GAT predicts electrostatic potential and electron/hole quasi‑Fermi levels at each node, preserving physical unknowns instead of mapping fixed parameters to scalars.
- Training incorporates finite‑volume current continuity residuals, embedding drift‑diffusion physics into the learning objective and reducing per‑field RMSE to sub‑volt accuracy on Sentaurus benchmarks.
- The active‑learning loop uses deep ensemble uncertainty to screen candidate designs quickly, achieving inference under a second per device even for large multi‑fin arrays.

## Context
This work advances AI surrogates beyond static mapping by operating on the underlying mesh graph, allowing size generalization across different FinFET geometries. It demonstrates that physics‑aware neural networks can replace expensive TCAD sweeps in design exploration pipelines.

## Implications
Designers can explore Pareto fronts for large device arrays without prohibitive simulation times, accelerating innovation cycles. Practitioners gain a tool to embed carrier transport constraints directly into AI‑driven optimization workflows, reducing reliance on costly high‑fidelity simulations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02988v1)
