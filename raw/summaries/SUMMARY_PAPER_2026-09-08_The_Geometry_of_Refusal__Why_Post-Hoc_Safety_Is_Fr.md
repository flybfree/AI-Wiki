---
title: The Geometry of Refusal: Why Post-Hoc Safety Is Fragile and Pretraining-Time Safety Persists
url: http://arxiv.org/abs/2609.06934v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_02-08-19Z_TheGeometryofRefusal_WhyPost_HocSafetyIsFragileand.md
generated_at: 2026-09-08 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper explains why post‑hoc safety methods such as reinforcement learning from human feedback (RLHF) and direct preference optimization (DPO) are fragile, showing that small benign fine‑tuning can restore the behaviors they were meant to suppress. It finds that safety updates lie in a thin orthogonal subspace of capability loss, making them easy to mask rather than eliminate.

## Key Takeaways
- Post‑hoc safety updates are nearly orthogonal to the directions that define model capabilities, so they create a refusal gate that sits on top of intact abilities.
- A kernel‑immobility lemma shows that such an update can only suppress, not erase, a capability; benign fine‑tuning (about 100 steps) restores the suppressed behavior in models like Qwen‑2.5‑7B and Llama‑3‑8B‑Instruct.
- The safety signal persists across pretraining because it is introduced early, with a sharp transition around 6 billion tokens, leading to consistent refusal rates that survive attacks.

## Context
Large language model alignment relies heavily on post‑hoc fine‑tuning, yet recent attacks repeatedly reopen the vulnerabilities. Understanding whether this fragility stems from timing or from how safety is embedded in pretraining helps researchers design more robust systems.

## Implications
For practitioners, embedding safety during pretraining could yield stronger defenses that survive fine‑tuning attacks without sacrificing performance. This insight may guide industry efforts to prioritize early alignment over later post‑hoc adjustments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.06934v1)
