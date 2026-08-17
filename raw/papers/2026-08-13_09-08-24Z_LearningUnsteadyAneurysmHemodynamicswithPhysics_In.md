---
title: Learning Unsteady Aneurysm Hemodynamics with Physics-Informed DeepONets
published: 2026-08-13T09:08:24Z
authors: Oscar L. Cruz-Gonzalez, Valérie Deplano, Badih Ghattas
url: http://arxiv.org/abs/2608.13629v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Unsteady Aneurysm Hemodynamics with Physics-Informed DeepONets

## Abstract
Clinically actionable, patient-specific hemodynamic assessment, specifically wall shear stress, vortex structure and pressure distributions, is critical for determining risky or unfavorable evolution in Abdominal Aortic Aneurysms (AAA). While Physics-Informed Deep Operator Networks (PI-DeepONets) show promising results in complementing established 5 tools such as Computational Fluid Dynamics (CFD), a persistent architectural challenge remains for complex 3D flows. In this direction, we propose a Modified Multi-Input Multi-Output PI-DeepONets (M3PI-DeepONet) designed for predicting unsteady flows in an idealized AAA geometry. Central to our model is the Aggregated Injection strategy, where latent representations from multiple input branches are fused prior to trunk injection, allowing the coordinate basis to adapt to multiple physical constraints. To the best of our knowledge, this is the first architecture to combine the layer-wise gating mechanism with a multi-branch operator-network topology, yielding an input-adaptive trunk basis. Additionally, we integrate the 3D Navier-Stokes equations as governing physical laws, so the model is trained based on physics-informed residuals, initial and boundary conditions, and only 0.3% of the labeled internal data together with the selected branch-conditioning signals. The M3PI-DeepONet simultaneously predicts unsteady 3D flow velocity and pressure fields with an average relative L2 velocity error below 4% and pressure error around 5% while achieving a conservative retained-cycle inference speedup of approximately 36x compared to reference CFD simulations once the branch inputs used for conditioning are available. This work advances the application of deep learning in cardiovascular disease modeling, marking step toward real-time, non-invasive clinical diagnostics.

## Metadata
- **Published**: 2026-08-13T09:08:24Z
- **Authors**: Oscar L. Cruz-Gonzalez, Valérie Deplano, Badih Ghattas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13629v1)