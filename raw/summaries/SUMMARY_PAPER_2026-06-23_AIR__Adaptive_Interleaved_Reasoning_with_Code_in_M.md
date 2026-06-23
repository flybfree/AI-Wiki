---
title: AIR: Adaptive Interleaved Reasoning with Code in MLLMs
url: http://arxiv.org/abs/2606.23678v1
type: paper-summary
date: 2026-06-23
source_paper: 2026-06-22_17-58-54Z_AIR_AdaptiveInterleavedReasoningwithCodeinMLLMs.md
generated_at: 2026-06-23 00:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AIR, an adaptive interleaved reasoning framework that augments multimodal large language models with code to solve complex numerical tasks. After reinforcement learning training using a group‑constrained reward function, the model shows a 6.1 percentage point gain in accuracy and a success rate above 95% on tool‑use benchmarks.

## Key Takeaways
- A two‑stage cold‑start data construction pipeline enables systematic generation of code‑augmented numerical computation datasets.
- Data filtering strategies applied to the RL dataset improve relevance and reduce noise, leading to more effective training.
- An adaptive tool‑invocation strategy based on a group‑constrained reward function guides interleaved reasoning trajectories toward higher performance.

## Context
Current MLLM research often limits interactive capabilities to visual perception tasks, leaving numerical computation underutilized. This work bridges that gap by integrating code execution into the reasoning loop, aligning with trends toward multimodal and tool‑aware AI systems.

## Implications
For practitioners, AIR provides a scalable method to enhance model robustness on computational challenges without extensive fine‑tuning. In industry, such improvements could translate to smarter assistants capable of handling real‑world calculations seamlessly.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.23678v1)
