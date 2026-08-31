---
title: VICT: Verifier-Instrumented Credit Tracing for Long-Horizon LLM Agent Reinforcement Learning
url: http://arxiv.org/abs/2608.28128v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_09-43-54Z_VICT_Verifier_InstrumentedCreditTracingforLong_Hor.md
generated_at: 2026-08-30 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces VICT, a training‑time interface that links verifier atoms to actions via dependency‑valid proof edges, enabling fine‑grained credit assignment without altering the terminal reward. Experiments on ALFWorld and WebShop show VICT yields substantial gains over outcome‑only training and matches recent fine‑grained methods while preserving original rewards.

## Key Takeaways
- VICT redistributes group‑relative advantage only along verifier‑valid proof edges, moving credit assignment to the verifier side.  
- The method abstains when evidence is incomplete or ambiguous, leaving the terminal reward unchanged.  
- Ablations demonstrate that dense atom rewards, final‑commit credit, temporal proximity, and sparsity alone cannot explain VICT’s performance.

## Context
Fine‑grained credit assignment remains a bottleneck for long‑horizon LLM agents because standard scalar rewards ignore task structure. This work advances the field by treating verifier internals as explicit signals, offering a principled way to trace credit without extra inference components.

## Implications
Practitioners can adopt VICT to refine reinforcement learning loops in complex environments where partial evidence is available, reducing reliance on costly rollout‑side tricks and enabling more stable training.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28128v1)
