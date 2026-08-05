---
title: Crayotter: Learning Long-Horizon Video Editing Agents via Group-Relative Preference Backpropagation
url: http://arxiv.org/abs/2608.02694v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_10-41-25Z_Crayotter_LearningLong_HorizonVideoEditingAgentsvi.md
generated_at: 2026-08-05 01:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents Crayotter, a long‑horizon video editing agent that learns from subjective feedback by converting ordinal preferences into zero‑sum advantages using Group‑Relative Preference Backpropagation (GRPB). The method improves both the agent’s editing behavior and the final rendered products compared to several baselines.

## Key Takeaways
- GRPB transforms same‑task rankings into bounded credit over semantic editing segments, allowing the model to allocate learning signals without direct influence from current judgments.  
- A lagged allocator and guarded transmission prevent unreliable estimates from shaping the same rollout group, ensuring stable training across long horizons.  
- The 9B Crayotter model outperforms proprietary systems on AgenticVBench, demonstrating that preference‑based learning can be applied to subjective, delayed outcomes.

## Context
Long‑horizon video editing agents face a challenge: feedback arrives only after many interdependent decisions and is inherently subjective, making global scalar objectives ambiguous. This work addresses the need for task‑specific, ordinal preferences that can be efficiently backpropagated across long sequences without destabilizing learning dynamics.

## Implications
The approach offers practitioners a practical way to train agents on complex, multi‑step creative tasks where outcomes are not easily quantifiable. By focusing on relative preferences within each rollout group, Crayotter could inspire future systems that learn from user feedback in domains such as video production and interactive media.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02694v1)
