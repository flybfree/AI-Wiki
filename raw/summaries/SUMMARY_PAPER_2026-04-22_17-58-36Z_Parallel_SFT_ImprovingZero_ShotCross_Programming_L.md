---

title: "Summary: Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL"
url: http://arxiv.org/abs/2604.20835v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-04-22_17-58-36Z_Parallel_SFT_ImprovingZero_ShotCross_Programming_L.md
generated_at: "2026-06-11 10:25"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-04-22 17-58-36Z Parallel Sft Improvingzero Shotcross Programming L


## Summary
The paper introduces Parallel-SFT, a method that mixes functionally equivalent code written in different programming languages to improve zero-shot cross-programming-language transfer for code reinforcement learning. Experiments show that applying this SFT initialization before RL yields better performance on unseen languages compared with training directly from scratch. The model’s latent space becomes more functionality‑centric, clustering similar programs together.

## Key Takeaways
- Parallel-SFT mixes parallel programs across languages to create a richer data mixture that supports transfer.
- Without such initialization, RL can degrade or fail to improve performance on target languages.
- The resulting latent representation is more function‑focused, aligning equivalent code representations.

## Context
Current large language models excel in high‑resource languages but struggle with low‑resource ones due to scarce training examples. This work addresses the gap by leveraging universal programming concepts across languages, a direction explored in few recent studies on cross‑domain transfer.

## Implications
Practitioners can adopt Parallel-SFT to fine‑tune code models for broader language support without extensive data collection. The approach may enable more reliable deployment of AI assistants that generate code in multiple dialects.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2604.20835v1)
