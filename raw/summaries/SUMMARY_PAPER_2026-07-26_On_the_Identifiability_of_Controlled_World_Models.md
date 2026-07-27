---
title: On the Identifiability of Controlled World Models
url: http://arxiv.org/abs/2607.22430v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_15-49-12Z_OntheIdentifiabilityofControlledWorldModels.md
generated_at: 2026-07-26 20:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a joint identifiability theory for Joint‑Embedding Predictive Architectures when the latent state is Gaussian and the behavior policy is state‑dependent. It shows that under two conditions—spectral separation of the predictable signal and non‑degenerate conditional action variation—the JEPA objective identifies both the latent state and the controlled transition up to an orthogonal transformation. The work also provides quantitative bounds for representation and transition identifiability when optimization is approximate.

## Key Takeaways
- Spectral separation of the predictable signal governs representation identifiability, meaning that if the signal can be uniquely separated in frequency space, the latent state can be recovered from observations.
- Non‑degenerate conditional action variation ensures that each action direction has a distinct effect on the transition, preventing confounding between state and dynamics.
- The cost of limited action coverage is quantified by a counterfactual-to-on‑policy error ratio equal to the inverse of the transition‑identifiability margin.

## Context
This research addresses a core challenge in reinforcement learning: ensuring that learned world models can reliably predict both states and dynamics under realistic, nonlinear observation maps. Accurate identifiability is essential for stable planning and safe exploration, especially when actions are limited or behavior policies are complex. The theoretical framework bridges statistical learning theory with practical model‑based control.

## Implications
For practitioners, the paper clarifies when a learned world model can be trusted to recover hidden states and dynamics without additional assumptions, guiding design of action spaces and observation pipelines. It also highlights the need for sufficient action diversity to avoid costly errors in counterfactual predictions, informing both research priorities and deployment strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22430v1)
