---
title: QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides
url: http://arxiv.org/abs/2607.15810v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-17_10-21-27Z_QUADS_StabilizingNVFP4ReinforcementLearningforMoEv.md
generated_at: 2026-07-23 23:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the instability of using NVFP4 precision in reinforcement learning for Mixture-of-Experts models by showing that activation errors dominate over weight quantization issues. The proposed QUADS framework aligns quantization errors across both training and rollout sides, enabling BF16‑level accuracy and higher throughput than FP8.

## Key Takeaways
- Activation error is the primary cause of NVFP4 RL instability, as weights can be synchronized via a shared path while activations are recomputed online with coarse E2M1 grid errors.  
- QUADS introduces asymmetric quantization‑aware training that fake‑quantizes weights and keeps activations unquantized to improve alignment.  
- On the rollout side, residual activation compensation corrects high‑error channels without breaking native W4A4 GEMMs, yielding ~16% higher throughput than FP8.

## Context
Mixture‑of‑Experts models benefit from low‑precision inference but suffer from rollout bottlenecks that limit scalability. Recent advances like NVFP4 aim to combine fine‑grained scaling with high‑throughput GEMMs, yet practical deployment remains limited by numerical drift during RL training.

## Implications
QUADS demonstrates that precise error alignment can match BF16 performance while boosting throughput, offering a template for future low‑precision RL pipelines. Practitioners can adopt this approach to accelerate MoE model rollouts without sacrificing accuracy or stability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.15810v1)
