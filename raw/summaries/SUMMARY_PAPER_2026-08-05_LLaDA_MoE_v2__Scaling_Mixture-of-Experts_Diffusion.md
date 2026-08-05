---
title: LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models
url: http://arxiv.org/abs/2608.03457v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_10-53-02Z_LLaDAMoEv2_ScalingMixture_of_ExpertsDiffusionLangu.md
generated_at: 2026-08-05 01:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the scaling behavior of Mixture-of-Experts diffusion language models (MoE dLLMs), contrasting their optimization trends with those of autoregressive models. The authors train a 30B‑parameter MoE dLM called LLaDA MoE v2 on 23.5 T tokens and show it rivals Qwen3 despite using fewer pretraining tokens, establishing practical scaling laws for MoE diffusion architectures.

## Key Takeaways
- Optimal batch size grows faster with compute than learning rate decay, indicating that larger batches are more beneficial early in training.
- IsoFLOP analysis shows a data‑side tilt: the token budget allocated to the model increases faster than the activated computation, suggesting data becomes the limiting factor at scale.
- Larger expert pools are preferred for bigger models while keeping moderate granularity effective; the fraction of capacity assigned to shared experts remains stable across scales.

## Context
Diffusion language models provide a non‑autoregressive alternative that can be combined with MoE to reduce cost per token. Understanding how hyperparameters and architecture scale is crucial as industry pushes toward massive, efficient LLMs, yet prior research focused mainly on autoregressive scaling laws.

## Implications
These findings guide engineers in designing MoE dLLMs that maximize compute efficiency and performance, especially for resource‑constrained deployments where token budget and expert allocation matter. Practitioners can leverage the observed trends to balance model size, activation rates, and data usage, accelerating development toward cost‑effective large language systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03457v1)
