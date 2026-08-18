---
title: Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning
url: http://arxiv.org/abs/2608.15065v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_06-32-15Z_FunnelofThoughts_EfficientTest_TimeScalingviaEarly.md
generated_at: 2026-08-17 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Funnel of Thoughts (FoT), an inference‑time technique that retains the full 32‑trajectory voted accuracy while cutting attention FLOPs by half and lowering overall model cost by 28.8 %. By detecting unproductive trajectories through hesitation markers such as “Wait”, “Actually” and “perhaps”, FoT prunes these paths before completion, achieving a 56.1 % reduction in online generation attention and a 37.6 % wall‑time saving without any extra model inference.

## Key Takeaways
- Funnel of Thoughts halves the attention FLOPs and reduces full‑model inference cost by 28.8 % across 115 K reasoning trajectories, preserving the accuracy achieved through majority voting.
- The method identifies unproductive trajectories using a training‑free lexical signal that captures repeated hesitation markers, allowing pruning without retraining or fine‑tuning.
- Online generation attention drops to 43.9 % of original levels (a 56.1 % reduction) and wall time is cut by 37.6 %, all while the final answer remains correct.

## Context
Large Reasoning Models generate diverse answers, making multi‑sample voting a standard but expensive approach for reliable deployment. Existing solutions cannot scale to the massive inference budgets required for modern LLMs, creating a gap between accuracy and computational efficiency that FoT addresses with a training‑free pruning strategy.

## Implications
For practitioners, FoT enables scalable deployment of reasoning models without retraining, lowering compute costs and latency in real‑time applications. For industry, it offers a practical path to meet AI services’ cost constraints while maintaining high answer reliability across diverse tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15065v1)
