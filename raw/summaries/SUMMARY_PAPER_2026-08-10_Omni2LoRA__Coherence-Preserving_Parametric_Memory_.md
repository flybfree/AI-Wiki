---
title: Omni2LoRA: Coherence-Preserving Parametric Memory for Efficient Omni Language Models
url: http://arxiv.org/abs/2608.09227v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_07-49-10Z_Omni2LoRA_Coherence_PreservingParametricMemoryforE.md
generated_at: 2026-08-10 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents Omni2LoRA, a two‑stage framework that compresses multimodal memory into a fixed‑budget LoRA adapter while preserving audio‑visual coherence. The method achieves a 30 % rank budget and outperforms several token‑compression baselines on four audio‑visual question‑answering benchmarks.

## Key Takeaways
- It encodes the full multimodal context into a full‑rank LoRA adapter in a single forward pass, bypassing the token bottleneck.  
- A discrete rank allocation policy via Group Relative Policy Optimization (GRPO) allocates sub‑linear rank to synergistic cross‑modal anchors rather than isolated visual features.  
- The approach yields an 8–12 % accuracy improvement over strong baselines and reduces Time‑to‑First‑Token by up to 12×, with query latency under 0.5 s after a few queries.

## Context
Long joint token sequences severely limit the performance of omnimodal language models because inference scales linearly with sequence length. Conventional token‑compression techniques often sacrifice temporal cross‑modal anchors needed for coherent reasoning, making them unsuitable for long‑range tasks.

## Implications
Omni2LoRA provides a reusable parametric memory that can be applied across many OLM queries without recomputing large context representations. This reduces latency dramatically and enables scalable deployment of multimodal systems in real‑time applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09227v1)
