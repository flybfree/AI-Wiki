# Summary: 2026-08-03_04-45-52Z_BeckmannTransportModels_FromAutonomousFlowstoOne_S.md
Saved: 2026-08-04 00:29
Source: 2026-08-03_04-45-52Z_BeckmannTransportModels_FromAutonomousFlowstoOne_S.md
Model: None

---

## Summary  
The paper introduces autonomous flow models that solve Beckmann's transportation problem by mapping between distributions supported on lower‑dimensional manifolds. These flows are time‑independent, yielding a one‑step generative map that is the exact solution of a conservation equation. By learning this map directly from data we obtain a unifying framework that recovers known models such as Poisson flow and quadratic regression loss. The approach corrects inconsistencies in existing methods and demonstrates strong performance on ImageNet 256×256.

## Key Contributions  
- [Finding 1] Autonomous flows provide exact one‑step mappings between distributions when the target is singular.  
- [Finding 2] The associated map solves a simple conservation equation, enabling direct learning from samples.  
- [Finding 3] The framework unifies Poisson flow and quadratic regression loss within Beckmann’s transport problem.

## Methodology  
The authors construct time‑independent velocity fields that satisfy the divergence condition of an autonomous flow. They enforce the flux constraint of Beckmann’s problem by requiring the Jacobian to preserve measure, then derive a one‑step map as the unique solution of the resulting PDE. Learning is performed via maximum likelihood or regression on a quadratic loss.

## Results  
Experiments show that the learned maps reproduce high‑quality images on ImageNet 256×256 with PSNR and FID comparable to state‑of‑the‑art generators. Theoretical analysis confirms exactness of the map under the singular support assumption.

## Significance  
This work bridges deep generative modeling and optimal transport, offering a principled way to generate data on manifolds without complex autoregressive steps. It provides a loss that is both differentiable and physically meaningful, potentially simplifying training.

## Related Concepts  
- Autonomous flow (time‑independent velocity field)  
- One‑step generative map  
- Beckmann transportation problem  
- Poisson flow model  
- Quadratic regression loss
