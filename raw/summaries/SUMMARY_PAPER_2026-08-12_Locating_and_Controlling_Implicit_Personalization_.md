---
title: Locating and Controlling Implicit Personalization in Large Language Models
url: http://arxiv.org/abs/2608.11735v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_07-18-31Z_LocatingandControllingImplicitPersonalizationinLar.md
generated_at: 2026-08-12 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how large language models implicitly personalize their outputs based on demographic cues that users never explicitly state and links this behavior to specific internal activation signals. Experiments across five LLMs reveal strong correlations between these hidden activations and recommendation changes, with a maximum correlation of r=0.87.

## Key Takeaways
- A localized internal activation signal correlates with recommendation changes across five LLMs, reaching r=0.87.
- When multiple cues appear together, their combined internal signals do not linearly add up in output.
- Removing the internal signal for a single cue can suppress its influence more effectively than prompting.

## Context
This work reveals that personalization emerges from hidden activations rather than surface prompts, challenging assumptions about model behavior and highlighting the need for deeper mechanistic understanding. It underscores that LLMs may encode demographic information in their representations even without explicit user input.

## Implications
Understanding these signals could enable developers to mitigate unwanted bias while preserving performance, offering a pathway toward transparent and controllable AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11735v1)
