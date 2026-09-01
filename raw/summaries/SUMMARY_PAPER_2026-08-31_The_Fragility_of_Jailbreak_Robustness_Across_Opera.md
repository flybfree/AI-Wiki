---
title: The Fragility of Jailbreak Robustness Across Operational States
url: http://arxiv.org/abs/2608.30748v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_13-14-47Z_TheFragilityofJailbreakRobustnessAcrossOperational.md
generated_at: 2026-08-31 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how jailbreak robustness varies when the operational state of a language model is altered, showing that simple prompt changes can raise attack success rates dramatically. Across seven aligned models and three attacks, they find ASR can increase by up to 56 percentage points due to non‑vanilla states.

## Key Takeaways
- Changing an ordinary system prompt not intended for safety can cause a large jump in jailbreak success rates, from 2% to 58%, even when the attack is unchanged.  
- The variation is linked to differences in hidden representations along a refusal-related axis, indicating that model internal states mediate these outcomes.  
- A single vanilla‑state evaluation does not fully capture robustness; robust assessments must consider how performance changes across operational contexts.

## Context
The study highlights a gap between standard safety evaluations and real‑world usage where prompts are often modified. This discrepancy can lead to overconfidence in reported ASR scores, which are typically measured under a single configuration.

## Implications
For practitioners, this means that reliability metrics must be re‑evaluated across different operational states to avoid misleading risk assessments. The field should adopt multi‑state robustness testing to better understand model behavior under varied user interactions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30748v1)
