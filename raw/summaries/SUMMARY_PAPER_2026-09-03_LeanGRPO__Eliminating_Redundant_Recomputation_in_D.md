---
title: LeanGRPO: Eliminating Redundant Recomputation in Diffusion RL
url: http://arxiv.org/abs/2609.03528v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_08-24-56Z_LeanGRPO_EliminatingRedundantRecomputationinDiffus.md
generated_at: 2026-09-03 22:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LeanGRPO, a method that eliminates redundant recomputation in diffusion reinforcement learning by restructuring data‑parallel layouts and offering two training schedules: one that retains computation graphs during rollout (LeanGRPO‑Retain) and another that uses provisional gradients with delayed correction (LeanGRPO‑Reweight). Experiments on FlowGRPO/DanceGRPO with FLUX.1‑dev and Wan show up to 1.83× speedup while keeping the original optimization objective unchanged.

## Key Takeaways
- LeanGRPO‑Retain tracks gradients during rollout, reusing saved activations for backward passes, thus removing the need to recompute selected timesteps.
- LeanGRPO‑Reweight computes provisional gradients with advantage estimates and later corrects them after trajectory completion, avoiding full recomputation.
- The two schedules are tuned for different model scales and input sizes, delivering significant speed gains without sacrificing performance.

## Context
Diffusion reinforcement learning methods such as DanceGRPO and FlowGRPO rely on repeated gradient tracking of selected timesteps, which is computationally expensive. Redundant recomputation limits the efficiency of these approaches, especially when rollout and policy update share the same backend. This work addresses that inefficiency by rethinking how computation graphs are managed.

## Implications
LeanGRPO provides a practical framework for faster diffusion RL training, reducing memory pressure and inference time. Practitioners can adopt either schedule based on their model size, leading to more scalable and efficient generative AI pipelines. The approach may inspire similar reuse strategies in other gradient‑intensive reinforcement learning settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03528v1)
