---
title: Learning to Act While Waiting: RL Finetuning of Generalist Robot Policies Under Inference Latency
url: http://arxiv.org/abs/2608.23831v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_21-19-50Z_LearningtoActWhileWaiting_RLFinetuningofGeneralist.md
generated_at: 2026-08-25 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ARLI, a latency‑aware framework that lets reinforcement learning improve generalist robot policies even when the policy’s inference is delayed. By interleaving action generation with execution and using state augmentations that include committed actions and mid‑inference observations, it restores near‑Markovian dynamics so standard RL can continue to learn. Experiments on simulated and real manipulation tasks show ARLI matches or exceeds performance of baseline methods under delay.

## Key Takeaways
- The framework interleaves action generation with execution to hide inference latency, preventing pauses that break the Markov assumption.
- State augmentations incorporate committed actions and mid‑inference observations to restore near‑Markovian structure during delayed inference.
- ARLI enables effective finetuning under inference delays where standard RL fails entirely, matching or exceeding performance in idealized no‑latency settings.

## Context
Modern generalist robot policies rely on large models with high inference latency, which can degrade learning stability. Traditional RL assumes instantaneous action feedback, making it incompatible with real‑world deployment constraints. This work bridges that gap by designing a low‑latency policy design that maintains reactivity within the inference window.

## Implications
The results show that RL finetuning is not limited by model size or latency when proper mechanisms are applied. Practitioners can deploy generalist policies in real robots without sacrificing learning efficiency, fostering safer and more reliable autonomous manipulation systems across industry and research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23831v1)
