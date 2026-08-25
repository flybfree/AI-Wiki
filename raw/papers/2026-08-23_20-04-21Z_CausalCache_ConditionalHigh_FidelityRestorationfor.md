---
title: CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents
published: 2026-08-23T20:04:21Z
authors: Jiaxuan Luo, Zhanfeng Liao, Jiayao Teng, Yuan Wang, Haojian Huang
url: http://arxiv.org/abs/2608.22577v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents

## Abstract
Long-horizon GUI agents can retain a complete interaction trace cheaply as textual action records, but expose only a few past events to the policy in high-fidelity pixels. We formulate this as conditional fidelity restoration: each event persists in summary-only form and is linked to an archived screenshot, while an active visual-context budget $B$ limits how many events may be promoted to summary-plus-image form. Recent-$B$ spends every slot on the latest events. CausalCache instead reallocates the same $B$ promotions over the complete trace, evicting a recent image only when a distant event has higher conditional marginal utility. Its history-gated key/value (HGKV) adapter modifies only restored history-image tokens and is exactly bypassed with no history image. Matched-budget replacement groups and per-arm-anchored difference-in-differences supervision make uniform history amplification worth zero; a budget-aware selector then chooses which summarized events to restore. On desktop, the frozen policy shows no reliable preference for a task-relevant archived screenshot over the recent frame it would displace; HGKV learns exactly that selectivity inside a pre-specified drift envelope. On OSWorld-Verified, restoring history to high fidelity is worth about $13$ success points over summary-only memory, while same-budget allocations remain indistinguishable. Zero-shot on a cross-application mobile benchmark, CausalCache significantly improves overall success over the same-budget recent allocation ($+3.7$ points on the full roster), and the gain concentrates where it should: $+8.6$ points on the memory-critical split fixed by benchmark metadata at construction, no detectable effect on matched controls, and a significant split-by-method interaction.

## Metadata
- **Published**: 2026-08-23T20:04:21Z
- **Authors**: Jiaxuan Luo, Zhanfeng Liao, Jiayao Teng, Yuan Wang, Haojian Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22577v1)