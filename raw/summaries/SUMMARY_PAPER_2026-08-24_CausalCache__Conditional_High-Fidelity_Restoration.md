---
title: CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents
url: http://arxiv.org/abs/2608.22577v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_20-04-21Z_CausalCache_ConditionalHigh_FidelityRestorationfor.md
generated_at: 2026-08-24 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CausalCache to improve long-horizon GUI agents by reallocating a limited visual-context budget across the entire interaction trace, preserving high-fidelity images of distant events when they are more valuable than recent ones. Experiments show that restoring history at high fidelity yields measurable gains in success points on benchmark tasks without harming performance.

## Key Takeaways
- CausalCache reallocates the same $B$ promotional slots over the full trace instead of only recent events, evicting a recent image when a distant event has higher conditional marginal utility.
- The history-gated key/value (HGKV) adapter modifies only restored history-image tokens and is bypassed with no history image, enabling exact control.
- On OSWorld-Verified, restoring distant high-fidelity images adds about 13 success points over summary-only memory, while same-budget recent allocations remain indistinguishable.

## Context
Long-horizon GUI agents face a trade-off between cheap textual summaries and limited high‑fidelity visual context. This work addresses the challenge of allocating scarce visual resources across long interaction histories to maximize task performance.

## Implications
By providing a principled method for prioritizing which events receive high‑fidelity restoration, CausalCache can be applied to any GUI agent that must balance memory constraints with visual fidelity, potentially improving user experience and system efficiency in real‑world applications. The approach also offers a template for budget‑aware memory management across heterogeneous tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22577v1)
