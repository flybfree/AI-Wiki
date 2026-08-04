---
title: Recursive Gaussian Processes and the Bayesian Brain
url: http://arxiv.org/abs/2608.00503v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_07-53-51Z_RecursiveGaussianProcessesandtheBayesianBrain.md
generated_at: 2026-08-03 23:43
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Recursive Gaussian Processes (RGPs) as a formal link between predictive coding and Bayesian inference in deep neural networks. By using a single Gaussian process indexed by layer and input, RGPs avoid representational collapse while enabling learnable cross‑layer dependencies through the precision‑weighted term \(r_{1g}\). The authors show that RGP components—shared GP, spike‑and‑slab variable selection, and MCMC dynamics—map onto cortical microcircuitry, providing a neurobiological substrate for hierarchical Bayesian computation.

## Key Takeaways
- RGPs replace deep Gaussian processes with a single indexed process \(g(t,\cdot)\) that prevents representational collapse while allowing cross‑layer precision weighting via \(r_{1g}\).  
- The framework intrinsically implements hierarchical Bayesian inference, uncertainty propagation, and prediction error weighting, which are mapped onto shared GP, spike‑and‑slab selection, and MCMC dynamics.  
- This mapping aligns RGP inference with the free energy principle, showing that variational free energy minimization corresponds to neuronal microcircuit activity.

## Context
Predictive coding has long been a theoretical model for cortical computation but lacks scalable implementations that respect both Bayesian exactness and neurobiological constraints. Deep Gaussian processes suffer from representational collapse, limiting their applicability to hierarchical tasks. RGPs offer a bridge by preserving probabilistic structure while enabling biologically plausible dynamics.

## Implications
For AI researchers, RGPs provide a principled tool to design deep models that align with Bayesian principles and neural circuit constraints. For neuroscience, the model offers testable predictions about laminar‑specific dynamics and spectral asymmetries between feedforward and feedback processing, potentially informing both theory and experimental design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00503v1)
