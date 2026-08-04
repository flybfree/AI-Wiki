---
title: From Chains to Trees: Parent-Conditioned Drafting for Semi-Autoregressive Speculative Decoding
url: http://arxiv.org/abs/2608.02123v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_12-15-26Z_FromChainstoTrees_Parent_ConditionedDraftingforSem.md
generated_at: 2026-08-03 23:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Parent-Conditioned Drafting Tree (PCTree) to improve speculative decoding for semi-autoregressive models. It keeps the one-pass parallel backbone of DSpark while allowing multiple parent-consistent continuations by using a lightweight Markov head to score child nodes in a tree structure. Experiments show speedup gains ranging from 3% to 29.5% across Qwen3 variants and benchmarks.

## Key Takeaways
- The conditional structure of the draft can be leveraged to generate multiple parallel children without retraining or extra backbone passes, preserving the original one-pass inference.
- PCTree allocates a fixed verification budget per parent, selecting the most probable path while still exploring alternatives, which avoids early mismatch invalidation of suffixes.
- The method achieves up to 29.5% speedup over autoregressive decoding on Qwen3-14B with a modest draft block size, demonstrating practical inference-only improvements.

## Context
Speculative decoding aims to reduce latency by drafting large token blocks and verifying only the final output, but current implementations treat drafts as linear chains limiting parallelism. This paper addresses that limitation by converting the chain into a tree while maintaining the efficiency of the original backbone.

## Implications
For practitioners, PCTree offers a simple inference-only upgrade that can be applied to existing semi-autoregressive models without architectural changes. It may become a standard technique for deploying faster LLM responses in production systems where latency is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02123v1)
