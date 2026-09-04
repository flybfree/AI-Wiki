---
title: TRACE: Spatiotemporal Contact Memory Graph Network Simulator for Granular Dynamics
url: http://arxiv.org/abs/2609.02991v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-02_15-30-41Z_TRACE_SpatiotemporalContactMemoryGraphNetworkSimul.md
generated_at: 2026-09-03 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TRACE, a graph‑network simulator for granular dynamics that stores inter‑granular contact history directly on edges rather than in node features or memory. By using attention‑based message passing and a gated recurrent unit to update edge memory, the model predicts normal and tangential forces while respecting Coulomb friction and internal force balance. Experiments show TRACE reduces long‑rollout position error by 31‑62% and final‑deposit error by 58‑89% compared with existing simulators, achieving speedups of 12.2× in 2D and 8.9× in 3D over the material point method.

## Key Takeaways
- TRACE stores interaction history on contact edges using a persistent memory updated by attention and GRU, enabling accurate force prediction across rearrangements.
- The model’s physics‑structured decoder enforces Coulomb friction limits and equal‑and‑opposite internal forces, producing stable long‑horizon rollouts with minimal interpenetration.
- TRACE outperforms GNS and NMGNS in both 2D and 3D benchmarks, delivering up to 62% lower position error and 89% lower deposit error while using fewer parameters.

## Context
In AI research on simulation, graph‑based simulators aim to capture complex physical interactions efficiently. TRACE advances this by integrating temporal contact memory directly into the edge structure, moving beyond node‑level representations that lose granular detail during particle rearrangements.

## Implications
This work provides a more faithful and computationally efficient alternative for industries relying on granular material modeling, such as geotechnical engineering and manufacturing. Practitioners can leverage TRACE to generate realistic long‑term simulations with reduced error and faster computation, supporting better design decisions in structural analysis and process optimization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02991v1)
