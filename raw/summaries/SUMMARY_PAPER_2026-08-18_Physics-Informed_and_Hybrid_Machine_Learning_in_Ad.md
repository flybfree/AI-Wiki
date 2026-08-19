---
title: Physics-Informed and Hybrid Machine Learning in Additive Manufacturing: Application to Fused Filament Fabrication
url: http://arxiv.org/abs/2608.17246v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_01-02-59Z_Physics_InformedandHybridMachineLearninginAdditive.md
generated_at: 2026-08-18 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates physics-informed hybrid machine learning approaches to predict bond quality and porosity in fused filament fabrication parts using deep neural networks. It evaluates eight combinations of three strategies that embed physical constraints, use simulation outputs as inputs, or pre-train with physics models. The results demonstrate improved accuracy even with limited experimental data.  

## Key Takeaways  
- Incorporating physics constraints directly into the loss function ensures the DNN's predictions align with known physical laws governing bond formation and porosity.  
- Feeding simulation outputs such as temperature profiles or stress fields as additional inputs to the DNN allows the network to leverage multi-physics FFF simulations for richer feature representation.  
- Pre-training a DNN using physics model input-output pairs before fine‑tuning on experimental data accelerates convergence and reduces overfitting when data are scarce.  

## Context  
This work addresses a growing need in additive manufacturing where reliable material property predictions can reduce waste and improve part performance. By integrating domain knowledge into deep learning, the study exemplifies how physics‑aware AI can close the gap between simulation and experiment, supporting more sustainable production pipelines.  

## Implications  
For industry practitioners, these methods enable faster design iterations by providing accurate porosity forecasts that directly influence mechanical strength. The approach also offers a template for other manufacturing processes where physical constraints are critical, fostering trust in data‑driven predictions without extensive empirical testing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17246v1)
