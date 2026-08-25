---
title: ReWorld: An Interactive World Model with Long-Horizon Memory
url: http://arxiv.org/abs/2608.23565v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_17-59-05Z_ReWorld_AnInteractiveWorldModelwithLong_HorizonMem.md
generated_at: 2026-08-24 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ReWorld, an interactive world model that separates short‑term control from long‑term memory during training while enforcing a fixed budget at inference. By using mixed per‑head attention windows and random chunk dropping, the model can attend to recent actions for precise control yet retain the entire history for rich recall. Evaluation shows superior control fidelity (11.95° rotation error) and camera‑motion consistency among six benchmark models.

## Key Takeaways
- Mixed per-head attention confines most heads to recent past while a few global heads span full history, balancing short‑term responsiveness with long‑term memory.
- Random chunk dropping creates sparse but in‑distribution histories, allowing the model to regenerate starting views even after sliding windows evict evidence.
- A fixed 12‑chunk KV cache backed by pose‑indexed landmarks enables real‑time streaming of eight video sources across photorealistic, game, and stylized worlds.

## Context
ReWorld addresses a core tension in interactive AI: the need for immediate action following while preserving an unbounded memory of visited locations. This separation is crucial because full attention over long sequences is computationally prohibitive, yet it limits control precision. The work demonstrates that a bounded cache can still support high‑fidelity interaction without sacrificing recall.

## Implications
For game developers and AR/VR engineers, ReWorld offers a scalable architecture that can run real‑time interactive worlds with consistent motion across diverse visual styles. Practitioners can adopt the LoRA‑based distillation to compress training resources while maintaining performance, enabling deployment on edge hardware.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23565v1)
