---
title: Groundhog Bit-Flip Attack: Seeding Infinite Generation Loops in Mixture-of-Experts LLMs through Bit Flips
url: http://arxiv.org/abs/2608.25276v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_01-23-01Z_GroundhogBit_FlipAttack_SeedingInfiniteGenerationL.md
generated_at: 2026-08-26 20:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a bit‑flip attack called Groundhog Bit‑Flip Attack that targets Mixture‑of‑Experts LLMs by flipping routing‑layer bits to extend decoding token usage while preserving semantic meaning. Experiments show that manually deactivating fewer than four experts inflates output length by 5912% across conversational, reasoning and agentic tasks, causing most test samples to reach the maximum token limit.

## Key Takeaways
- The attack exploits the correlation between specific expert activations and end‑of‑sequence tokens, allowing bit flips to trigger indefinite generation.
- Manual deactivation of fewer than four experts causes average output inflation of 5912%, with most test samples reaching maximum token length.
- Semantic fidelity is largely preserved despite the massive increase in token usage.

## Context
Mixture‑of‑experts models are widely used for scalable LLMs, but their routing mechanisms create hidden vulnerabilities that can be exploited without retraining. This work demonstrates that lightweight bit flips can bypass these defenses and cause availability issues.

## Implications
The findings warn developers of MoE‑based systems about potential denial‑of‑service attacks that could degrade user experience or incur high costs. Mitigating such bit‑flip vulnerabilities is essential for reliable deployment in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25276v1)
