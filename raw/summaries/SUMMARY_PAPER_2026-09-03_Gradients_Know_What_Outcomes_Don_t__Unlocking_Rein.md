---
title: Gradients Know What Outcomes Don't: Unlocking Reinforcement Learning for LLM Reasoning with Gradient-Aligned Rewards
url: http://arxiv.org/abs/2609.03342v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_04-00-28Z_GradientsKnowWhatOutcomesDon_t_UnlockingReinforcem.md
generated_at: 2026-09-03 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Gradient-Aligned Reward (GAR), a dense reward that leverages the model’s own gradient to align with expert reasoning trajectories. It extracts a compact gradient vector from each rollout using truncated backpropagation through the output projection layer and measures its cosine similarity to an expert‑anchor gradient. This approach yields a reasoning‑aware reward with less than 9 % wall‑clock overhead compared with binary outcome rewards. The authors prove that the cosine can be decomposed into prediction‑error and activation‑pattern factors, clarifying what the alignment signal actually captures.

## Key Takeaways
- GAR replaces binary RLVR rewards with a dense gradient similarity reward that is computed on‑the‑fly without offline annotation.
- The reward’s cosine similarity decomposes multiplicatively into a prediction error term and an activation pattern term, revealing its dual nature.
- Experiments show GAR consistently outperforms GRPO and other baselines on competition math benchmarks and transfers to GPQA Diamond and MMLU‑Pro.

## Context
Current reinforcement learning for chain‑of‑thought prompting relies heavily on binary or expensive dense rewards that ignore existing expert solutions. This work demonstrates a lightweight, gradient‑based alternative that can be integrated directly into training loops of large language models.

## Implications
The method enables more nuanced reward shaping without costly annotation pipelines, encouraging industry adoption of RL for LLM reasoning. Practitioners can expect improved performance on diverse benchmarks with minimal added computational cost, accelerating research and deployment cycles.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03342v1)
