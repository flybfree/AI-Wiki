---
title: Learning Unsteady Aneurysm Hemodynamics with Physics-Informed DeepONets
url: http://arxiv.org/abs/2608.13629v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_09-08-24Z_LearningUnsteadyAneurysmHemodynamicswithPhysics_In.md
generated_at: 2026-08-16 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The authors introduce a modified multi‑input multi‑output physics‑informed deep operator network (M3PI‑DeepONet) that predicts unsteady three‑dimensional velocity and pressure fields in an idealized abdominal aortic aneurysm geometry. The model achieves low error rates while drastically reducing computational time compared with conventional CFD.

## Key Takeaways
- The architecture fuses latent representations from multiple input branches before trunk injection, enabling a coordinate basis that adapts to several physical constraints simultaneously.
- Training relies on physics‑informed residuals derived from the three‑dimensional Navier‑Stokes equations, using only 0.3 % of labeled internal data together with branch conditioning signals.
- The network predicts velocity and pressure fields with average relative L2 errors below 4 % and 5 %, respectively, and provides a 36× speedup in retained‑cycle inference once conditioned inputs are available.

## Context
This work extends the use of physics‑informed deep learning beyond static flow predictions to unsteady three‑dimensional cardiovascular flows, addressing a longstanding gap between computational accuracy and real‑time applicability. By integrating Navier‑Stokes constraints directly into the loss function, the approach demonstrates that deep operators can respect fluid dynamics while remaining compact.

## Implications
For clinicians, the rapid inference capability could enable bedside monitoring of aneurysm hemodynamics without full CFD runs, supporting early intervention decisions. The method also offers a template for other complex 3D biomedical simulations where physics and data must co‑evolve.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13629v1)
