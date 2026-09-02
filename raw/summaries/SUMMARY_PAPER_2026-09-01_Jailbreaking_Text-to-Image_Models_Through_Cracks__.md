---
title: Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate
url: http://arxiv.org/abs/2609.01168v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_12-45-27Z_JailbreakingText_to_ImageModelsThroughCracks_Navig.md
generated_at: 2026-09-01 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a unified geometric framework called Detection Surface to analyze how heterogeneous safety filters interact in text-to-image models and proposes CRACK, a multi‑agent debate system that adapts jailbreak searches by exploring, diagnosing, and arbitrating across filter layers. Experiments show CRACK reaches up to 99.63 % attack success under composite defenses while using fewer queries than prior methods.

## Key Takeaways
- The Detection Surface reveals that successful evasion occurs in a sparse non‑convex region where bypassing one filter can trigger another, indicating complex cross‑layer conflicts.  
- CRACK’s three agents—Attack, Defense, and Judge—iteratively generate prompt mutations and layer‑specific feedback to refine strategies guided by reward signals.  
- The framework achieves higher success rates than methods that treat the entire safety pipeline as a single aggregate filter.

## Context
Current text‑to‑image safety systems rely on layered filters that can produce contradictory outputs, creating blind spots for adversarial attacks. Existing jailbreak research often optimizes against isolated components or queries the whole system, limiting insight into which constraints are truly active.

## Implications
Understanding these conflict zones helps designers build more robust and transparent safety pipelines. Practitioners can leverage CRACK’s adaptive debate to reduce query costs while maintaining effective content moderation in generative AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01168v1)
