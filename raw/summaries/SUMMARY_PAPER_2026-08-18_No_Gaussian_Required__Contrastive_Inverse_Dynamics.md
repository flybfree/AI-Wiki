---
title: No Gaussian Required: Contrastive Inverse Dynamics for JEPA World Models
url: http://arxiv.org/abs/2608.17542v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_09-03-35Z_NoGaussianRequired_ContrastiveInverseDynamicsforJE.md
generated_at: 2026-08-18 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Action-Contrastive Masked Transition Modeling (AC-MTM) as a contrastive inverse dynamics method that replaces the Gaussian regularizer in Joint-Embedding Predictive Architectures. It trains an action discrimination head to enforce non‑collapsed latent transitions, achieving performance comparable to SIGReg while removing reliance on target networks or stop‑gradient tricks.

## Key Takeaways
- AC-MTM adds a training‑only inverse‑dynamics head that uses Action‑NCE to make each latent transition identify the correct action among others, providing anti‑collapse pressure without a Gaussian prior.  
- The model discards the inverse branch at test time, leaving forward encoding and planning unchanged from LeWM.  
- On OGBench Visual Scene, AC-MTM reaches 80 % success versus 58 % for SIGReg, improving by 20–24 points across seeds.

## Context
Current world‑model architectures struggle with latent collapse, requiring auxiliary regularizers that impose unrealistic Gaussian assumptions. This work shows that contrastive inverse dynamics can supply a distribution‑free signal, aligning with trends toward self‑supervised and task‑agnostic training pipelines in AI research.

## Implications
Practitioners can adopt AC-MTM to stabilize world models without costly pretraining or reconstruction objectives, lowering development costs for robotics and game agents. The approach also clarifies action‑space and observability requirements, guiding future design of compact, reliable perception systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17542v1)
