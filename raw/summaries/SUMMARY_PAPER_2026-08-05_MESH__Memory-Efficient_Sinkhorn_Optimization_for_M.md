---
title: MESH: Memory-Efficient Sinkhorn Optimization for Mixture-of-Experts Training
url: http://arxiv.org/abs/2608.04407v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_03-23-31Z_MESH_Memory_EfficientSinkhornOptimizationforMixtur.md
generated_at: 2026-08-05 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why memory‑efficient optimizers such as Sinkhorn gradient descent fail in Mixture‑of‑Experts (MoE) training and proposes a hidden‑momentum variant called MESH that restores performance while cutting optimizer state. Experiments on an 110 M‑parameter nanowhale MoE show that the hybrid reduces memory from 0.883 GB to 0.331 GB but worsens loss, and MESH brings it back down with only a small overhead.

## Key Takeaways
- The SAGE/Sinkhorn hybrid cuts optimizer state from 0.883 GB to 0.331 GB yet the evaluation loss rises to 3.8265 compared with AdamW’s 3.58–3.64 across seeds.
- Routed MoE expert matrices are the primary failure point because their gradients are conditional, temporally varying, and not compatible with stateless Sinkhorn normalization.
- MESH introduces a hidden‑momentum signal via a gradient‑buffer lifecycle, providing temporal first‑moment information without storing full optimizer state.

## Context
MoE models scale to billions of parameters but require massive memory for optimizer states, limiting deployment. Efficient training methods are essential to keep large models feasible on limited hardware, yet standard optimizers often degrade performance in MoE settings due to the non‑stationary nature of expert gradients.

## Implications
Reducing GPU memory and allocation can lower training costs and enable larger model deployments without sacrificing quality. Practitioners can adopt MESH or similar hidden‑momentum techniques to achieve memory savings while maintaining near‑AdamW performance, supporting broader adoption of MoE in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04407v1)
