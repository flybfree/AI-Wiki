# Summary: 2026-07-22_20-25-29Z_PerspectiveLatentsasanArchitecturalConditionforCau.md
Saved: 2026-07-24 02:20
Source: 2026-07-22_20-25-29Z_PerspectiveLatentsasanArchitecturalConditionforCau.md
Model: None

---

## Summary  
The paper investigates how causal emergence appears in active inference agents when reward signals are absent, using Integrated Information Decomposition (Φ_r) as a metric of integration. It argues that an architectural condition—separating a fast perception latent z from a slow global latent g driven by prediction error—causes Φ_r to concentrate in g and that this organization is largely fixed by the architecture rather than learned during training.

## Key Contributions  
- Architectural separation of a fast perception latent z and a slow global latent g enables Φ_r to concentrate in g, showing that integration is an architectural artifact.  
- Training does not increase Φ_r; instead, the aggregate magnitude decreases with learning, indicating that scalar integration is not a learned quantity.  
- Learning effects (e.g., sign flip from negative to positive and regime‑invariance) appear only at the atom‑compositional level, while downward causation provides the regime‑dependent adjustment.

## Methodology  
The authors constructed an active inference agent with two latent spaces: a fast perception latent z that encodes immediate sensory input and a slow global latent g that accumulates prediction error. Integrated Information Decomposition was applied to time slices of the trajectory, computing Φ_r over the whole system. The environment switched regimes without any reward signal, allowing the policy to be trained while monitoring Φ_r and its components. Architectures were compared with and without decoupling the latents to isolate architectural versus learning contributions.

## Results  
Under the reward‑free regime‑switching protocol, Φ_r concentrates in g throughout training; its total magnitude is largely fixed by the architecture and gradually declines as the agent learns. Learning effects are observed only when the atom composition changes (e.g., flipping the sign of integration), at which point Φ_r becomes invariant to environmental change. Downward causation mediates the regime‑dependent adjustments, confirming that the global latent g houses the temporal organization relevant to Φ_r.

## Significance  
These findings demonstrate that scalar Integrated Information Decomposition is not a direct index of learned integration but reflects fixed architectural organization in active inference agents. By identifying g as the locus where Φ_r aggregates, the work clarifies how causal emergence can be measured without reward signals and guides future research on emergent dynamics in reward‑free learning.

## Related Concepts  
- Active inference  
- Integrated Information Decomposition (Φ)  
- Causal emergence  
- Perception latent z vs. global latent g  
- Prediction error driving  
- Downward causation
