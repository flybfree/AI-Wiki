---
title: ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models
url: http://arxiv.org/abs/2608.14022v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_07-13-34Z_ForgeWM_ProgressiveCausalTrainingforFew_StepAction.md
generated_at: 2026-08-16 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents ForgeWM, a progressive framework that converts bidirectional action‑conditioned video generators into low‑latency few‑step world models for interactive gaming. By combining domain adaptation, teacher‑forced causal training, and on‑policy distribution matching with a bidirectional teacher, the method achieves steady‑state performance at denoising budgets of one to four steps while maintaining high imaging quality.

## Key Takeaways
- The framework uses progressive budget specialization so that students trained for 1, 2, or 4 steps can be deployed without sacrificing quality.  
- A dual‑path protocol lets a one‑step student re‑noise and refine its draft during gameplay while preserving latency constraints.  
- On Minecraft data the system outperforms prior models in imaging quality, motion‑profile alignment, action accuracy, and mouse‑control fidelity.

## Context
Interactive video world models must generate short clips that match real‑time player inputs without noticeable lag. Existing causal distillation techniques focus on offline synthesis, leaving interactive latency and control fidelity unresolved. ForgeWM addresses these gaps by integrating domain‑specific adaptation into the training pipeline.

## Implications
The results suggest a practical path for deploying controllable few‑step video generation in real‑world games where both speed and precision are critical. Practitioners can adopt the four‑stage recipe to create budget‑sensitive models that balance quality with low latency, opening new possibilities for immersive AI‑driven gameplay experiences.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14022v1)
