---
title: Graph-Operator World Models for Morphology-Parameter Generalization in Continuous Control
url: http://arxiv.org/abs/2608.20936v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_10-01-46Z_Graph_OperatorWorldModelsforMorphology_ParameterGe.md
generated_at: 2026-08-23 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Graph-Operator World Models (GraphOp‑WM), a structured representation for continuous control that separates morphology‑independent dynamics from morphology‑specific operators. By modeling robot bodies as an attributed graph and factorizing transitions, the approach enables reuse of static components while adapting to changes in link lengths, masses, damping, and actuation. Experiments on Hopper, Walker2d, and HalfCheetah demonstrate improved generalization across unseen parameter splits.

## Key Takeaways
- The model uses a graph‑based representation where bodies are nodes and kinematic relations are edges, allowing static dynamics to be expressed as a local basis.
- Transitions are factorized into a morphology‑independent basis and a morphology‑conditioned structured operator that handles interpolation, extrapolation, and held‑out compositions of parameters.
- The operator combines node‑local modulation, kinematic‑tree coupling, and a low‑rank global correction to ensure static dependence is carried by the pathway.

## Context
Continuous control world models often fail when physical parameters vary across robot families, limiting their applicability. This work addresses that limitation by providing a principled separation of static and dynamic components within a unified graph framework.

## Implications
For researchers, GraphOp‑WM offers a template for designing adaptable controllers that can handle diverse morphologies without retraining from scratch. Practitioners in robotics and industry can leverage this to create more robust autonomous systems that operate across different articulated platforms with minimal overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20936v1)
