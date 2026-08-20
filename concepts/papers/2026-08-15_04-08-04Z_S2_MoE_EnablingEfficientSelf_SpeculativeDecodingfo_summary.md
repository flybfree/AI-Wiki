---
title: "S2-MoE: Enabling Efficient Self-Speculative Decoding for Mixture-of-Experts on Edge Devices"
type: paper-summary
source_paper: "2026-08-15_04-08-04Z_S2_MoE_EnablingEfficientSelf_SpeculativeDecodingfo.md"
---
# Summary: S2-MoE

**Original paper:** [arXiv: 2608.15018](http://arxiv.org/abs/2608.15018v1)

## Summary
S2-MoE combines mixture-of-experts inference with self-speculative decoding through routing-aware expansion, expert reuse, and shared draft-target context. On llama.cpp it reports up to 5.3× speedup, with 2.0× average speedup, over standard autoregressive decoding across tested models.

## Why it matters
Edge deployment depends on memory movement and bandwidth as much as raw compute. Routing-aware speculation is a practical way to make large sparse models more usable on constrained devices.
