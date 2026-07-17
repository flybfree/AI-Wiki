---
title: Online Neural Space Time Memory for Dynamic Novel View Synthesis
url: http://arxiv.org/abs/2607.15271v1
type: paper-summary
date: 2026-07-16
source_paper: 2026-07-16_17-58-18Z_OnlineNeuralSpaceTimeMemoryforDynamicNovelViewSynt.md
generated_at: 2026-07-16 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes an online neural space‑time memory that enables real‑time novel view synthesis from streaming video by decoupling memory updates from per‑frame application. The method uses periodic updates, cross‑view attention for deformation handling, an auxiliary loss to enforce persistent scene internalization, and a caching strategy to prevent weight drift. Experiments show state‑of‑the‑art performance on dynamic human motion scenes while supporting minute‑scale memorization.

## Key Takeaways
- The approach separates memory update frequency from per‑frame application, reducing computational load compared with continuous gradient updates.
- Cross‑view attention is employed to align the evolving memory representation with current frames, mitigating deformation errors in dynamic motion.
- An auxiliary memory loss and a caching regularizer ensure long‑term persistence of scene context without catastrophic drift.

## Context
Neural view synthesis must balance persistent memory usage with real‑time constraints, especially when handling occluded regions in streaming video. Traditional methods struggle due to heavy per‑frame updates that degrade performance over long contexts. This work addresses the gap by introducing a frequency‑decoupled mechanism that maintains efficiency while preserving accuracy.

## Implications
The decoupling strategy offers a scalable template for other real‑time generative tasks such as live video editing and AR content creation. Practitioners can adopt this framework to build systems that retain scene memory without sacrificing frame rates, advancing both research and industry applications in dynamic visual synthesis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.15271v1)
