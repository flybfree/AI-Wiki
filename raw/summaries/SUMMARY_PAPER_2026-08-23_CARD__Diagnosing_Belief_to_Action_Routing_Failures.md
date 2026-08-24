---
title: CARD: Diagnosing Belief to Action Routing Failures in Vision Language Models
url: http://arxiv.org/abs/2608.20763v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_05-53-48Z_CARD_DiagnosingBelieftoActionRoutingFailuresinVisi.md
generated_at: 2026-08-23 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CARD, a diagnostic method that steers activations along one axis while measuring responses on another to reveal whether vision-language models use belief representations for action prediction. Experiments on open-weight VLMs show a critical routing failure where beliefs are not incorporated into next actions, leaving partner information unused.

## Key Takeaways
- CARD reveals that belief representations remain disconnected from downstream action predictions in current VLMs.
- The study demonstrates that valuable partner state information is ignored during decision making.
- This gap persists across multiple open-weight models on the Relay Chain benchmark.

## Context
Vision-language models aim to integrate visual and textual knowledge, yet their internal mental-state representations often do not influence real‑world behavior. Understanding how these representations are utilized is essential for building truly interactive agents.

## Implications
If belief information is not routed into actions, systems may appear competent but act suboptimally in cooperative settings. Addressing this routing failure could lead to more reliable and trustworthy AI assistants that respect partner intentions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20763v1)
