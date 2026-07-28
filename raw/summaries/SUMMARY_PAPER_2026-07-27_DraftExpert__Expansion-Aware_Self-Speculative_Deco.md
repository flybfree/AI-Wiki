---
title: DraftExpert: Expansion-Aware Self-Speculative Decoding for End-Device MoE Inference
url: http://arxiv.org/abs/2607.24434v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_13-44-42Z_DraftExpert_Expansion_AwareSelf_SpeculativeDecodin.md
generated_at: 2026-07-27 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
DraftExpert introduces an expansion‑aware self‑speculative decoding framework for MoE models that are offloaded to edge accelerators. By training lightweight draft experts per layer, it balances accuracy gains with minimal extra loading overhead. On DeepSeek‑V2‑Lite and Moonlight‑16B‑A3B across CPU‑GPU and Flash‑NPU setups, DraftExpert boosts decode throughput by 1.45× on average while achieving draft acceptance rates of 84–87% and prefetch hit rates of 86–88%.

## Key Takeaways
- DraftExpert trains a lightweight accelerator‑resident draft expert per layer using residual, logit/token, and router‑agreement signals to improve accuracy without heavy computation.  
- The framework maintains a fixed‑footprint drafter composed of shared experts plus top‑1 and draft‑expert tokens, truncating confidence‑based expansion when needed.  
- Inference results show an average 1.45× increase in decode throughput, draft acceptance rising to 84–87%, and prefetch hit rates reaching 86–88%.

## Context
MoE models promise efficient inference by activating only a subset of experts per token, yet their routed weights often exceed accelerator memory limits. Edge deployment demands techniques that minimize latency while keeping model size manageable, making self‑speculative decoding especially valuable for single‑user settings.

## Implications
This work demonstrates that expanding the draft expert set can be done with minimal overhead, directly addressing a key bottleneck in edge AI. Practitioners can adopt DraftExpert to accelerate MoE inference on mobile and embedded devices without sacrificing performance or memory constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24434v1)
