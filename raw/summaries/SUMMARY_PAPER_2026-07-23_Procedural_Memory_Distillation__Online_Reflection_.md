---
title: Procedural Memory Distillation: Online Reflection for Self-Improving Language Models
url: http://arxiv.org/abs/2607.01480v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-01_21-20-57Z_ProceduralMemoryDistillation_OnlineReflectionforSe.md
generated_at: 2026-07-23 23:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Procedural Memory Distillation (PMD) to capture cross‑episode signals from reinforcement learning with verifiable rewards and turn them into a procedural memory that is distilled into the model’s weights. By continuously updating this memory during training, PMD enables the policy to internalize recurring strategies and failure patterns without relying on external supervision at inference time.

## Key Takeaways
- The memory stores raw trajectories, self‑reflected strategies and higher‑level behavioral patterns extracted online from rollouts.
- The memory is distilled into the policy’s weights during training, allowing a memory‑free model to run at inference.
- Freezing either the memory or the policy reduces performance by more than 10% on SCIKNOWEVAL domains.

## Context
Current self‑distillation methods such as SDPO rely on episode‑level verification signals that are discarded after each rollout, missing the rich procedural knowledge that persists across episodes. This work addresses the gap by preserving and reusing this information within the model itself.

## Implications
PMD demonstrates that procedural memory can boost large language models’ reasoning abilities without adding inference overhead. Practitioners can adopt this co‑evolution framework to improve robustness in dynamic environments where consistent strategies are valuable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.01480v1)
