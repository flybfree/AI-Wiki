---
title: ReTrace: Rejected-Trajectory Conditioning for Speculative Decoding
url: http://arxiv.org/abs/2608.29748v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_12-20-54Z_ReTrace_Rejected_TrajectoryConditioningforSpeculat.md
generated_at: 2026-08-31 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ReTrace, a method for speculative decoding that conditions draft blocks on the rejected suffix from previous rounds rather than generating fresh placeholders. By preserving hidden representations of rejected tokens and fusing them with target‑aware correction signals, ReTrace improves both acceptance length and decoding speed without extra model passes.

## Key Takeaways
- Rejected positions in a rejected suffix can still carry useful semantic information that should be retained for the next draft block.
- The method aligns these hidden representations with the upcoming draft using gated residual fusion, allowing the draft model to incorporate them into its input embeddings.
- ReTrace maintains lossless speculative decoding by leaving verification unchanged and avoiding additional forward passes.

## Context
Speculative decoding seeks to accelerate language generation by generating multiple candidate tokens in parallel and verifying them against a larger target model. Traditional approaches discard rejected suffixes, limiting progress after the first failure. This paper addresses that limitation by treating rejection as a signal rather than an error, echoing techniques from conditional diffusion.

## Implications
ReTrace demonstrates that marginal improvements in draft generation can be amplified when feedback is properly conditioned across rounds, offering a pathway to faster and more accurate decoding for large models like Qwen3. Practitioners may integrate ReTrace with existing drafting enhancements to achieve further gains without redesigning the verification pipeline.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29748v1)
