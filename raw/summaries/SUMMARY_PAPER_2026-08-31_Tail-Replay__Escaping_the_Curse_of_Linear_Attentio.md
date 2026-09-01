---
title: Tail-Replay: Escaping the Curse of Linear Attention in Prefix Caching for Hybrid LLMs
url: http://arxiv.org/abs/2608.30310v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_06-27-07Z_Tail_Replay_EscapingtheCurseofLinearAttentioninPre.md
generated_at: 2026-08-31 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Tail‑Replay, a caching scheme for hybrid large language models that interleaves full‑attention and linear‑attention layers. By leveraging the lossy compression property of gated delta networks, it enables unconstrained token‑level reuse without storing recurrent checkpoints, achieving near full‑prefill quality with only a small replay budget.

## Key Takeaways
- Tail‑Replay caches only the full‑attention key‑value pairs and reconstructs linear‑attention states by replaying a short recent suffix of the matched prefix.  
- The reuse boundary is set by shared tokens rather than checkpointed recurrent states, allowing flexible token alignment.  
- On benchmark models, a 5–10 % replay budget retains 92.8–99.9 % of full‑prefill quality while delivering up to 14.3× speedup at 32K prefix length.

## Context
Hybrid LLMs combine high‑capacity full attention with efficient linear attention to handle long contexts, but their caching mechanisms are limited by the need for checkpointed recurrent states. Tail‑Replay addresses this mismatch by exploiting the inherent compression of gated delta networks, reducing reliance on stored checkpoints and enabling more flexible prefix reuse.

## Implications
The approach lowers serving costs for hybrid models, making them viable for real‑time applications with long contexts. Practitioners can adopt Tail‑Replay to balance quality and efficiency without sacrificing token‑level flexibility in caching strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30310v1)
