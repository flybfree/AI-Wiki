---
title: Subtract or Replay? Exact Deletion from Language-Model Memory
url: http://arxiv.org/abs/2607.27539v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_00-17-05Z_SubtractorReplay_ExactDeletionfromLanguage_ModelMe.md
generated_at: 2026-07-30 20:16
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates how to perform exact deletion from persistent language‑model memory and finds that subtraction works for addressable records while replay is required for entangled writes. Experiments on Gemma 3 and Kimi show negligible impact at 1B parameters but higher cost at larger scales, confirming that exact deletion depends on the memory’s representation.

## Key Takeaways  
- The study shows algebraic decrement can remove a record with median KL 5.4×10⁻¹⁵ over 31 support‑token deletions and only +2% perplexity relative to fine‑tune at a 1B model.  
- At 4B and 12B parameters, certificate ordering persists but utility cost rises to 11.2% and 44.3%, indicating deletion becomes less efficient with larger memory sizes.  
- In Kimi Linear hybrid models, additive writes allow fixed decrement while the delta rule makes up to 49% of a record’s contribution suffix‑dependent, revealing that exact deletion is a property of representation.

## Context  
The work tackles a core challenge in persistent language modeling: enabling exact updates without catastrophic forgetting. By analyzing how memory stores records and their interactions with recurrent states, it contributes to the design of memory‑efficient architectures and verification of deletion guarantees.

## Implications  
For practitioners, this clarifies when subtraction is preferable versus replay, guiding implementation choices for memory systems. Industry adoption could benefit from lightweight models that retain exact deletions while keeping scaling costs manageable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27539v1)
