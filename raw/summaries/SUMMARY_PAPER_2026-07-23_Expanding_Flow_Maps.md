---
title: Expanding Flow Maps
url: http://arxiv.org/abs/2607.21585v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_17-57-38Z_ExpandingFlowMaps.md
generated_at: 2026-07-23 23:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Expanding Generative Flows (EFlows) and their distilled version, Expanding Flow Maps (EFMs), which enable generative models to handle variable output dimensions by augmenting the state with conditional noise. EFMs factor the map between any two timesteps into an expand operator that adds new coordinates or tokens and a transport map that moves along an interpolant. The framework works for both continuous and discrete spaces, including the simplex.

## Key Takeaways
- EFlows define flows between distributions of increasing dimensionality using an expanding interpolant that augments state with conditional noise.
- EFMs decompose this map into two learnable operations: an expand operator that adds new coordinates or tokens and a transport map that pushes the expanded state forward, allowing composition to generate a single joint map.
- The approach generalizes existing fixed-canvas flows by treating them as special cases where the expand operator is identity.

## Context
This work addresses a longstanding limitation of flow-based generative models that restrict outputs to fixed dimensions or sequence lengths. By making output size a learnable, controllable degree of freedom, EFlows and EFMs open new possibilities for variable-size graph generation and dynamic sequencing.

## Implications
For practitioners, the framework reduces computational complexity by using few-step compositions while preserving flexibility. It could be applied in image synthesis where resolution varies or in language models that generate sequences of differing lengths.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21585v1)
