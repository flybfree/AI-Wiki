---
title: Refusal-Gated Decoding: Preserving Refusal Behavior Under High-Temperature Sampling
url: http://arxiv.org/abs/2607.20791v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_23-33-51Z_Refusal_GatedDecoding_PreservingRefusalBehaviorUnd.md
generated_at: 2026-07-23 22:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how high‑temperature sampling affects the refusal behavior of large language models and introduces a sequential decoding method that retains greedy refusals while allowing higher entropy outputs. Experiments on three benchmark datasets show that the proposed approach preserves 91–99 % of the original refusal responses without adding significant latency.

## Key Takeaways
- The study demonstrates that high‑temperature sampling can erode model guardrails, leading to a measurable drop in refusal rates when entropy is increased.  
- Our sequential decoding technique restores most of these refusals by selectively preserving greedy tokens at critical points while allowing the rest of the generation to remain stochastic.  
- The method achieves minimal latency overhead, making it practical for real‑time applications that require both diversity and safety.

## Context
High‑temperature sampling is widely used to boost output variety but often compromises model safety features such as refusal responses. Maintaining these guardrails under stochastic decoding remains an open challenge in responsible AI deployment.

## Implications
For developers integrating LLMs into user‑facing systems, this work provides a lightweight way to keep harmful prompts blocked while still generating diverse answers. It supports safer and more engaging applications without sacrificing performance or safety.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20791v1)
