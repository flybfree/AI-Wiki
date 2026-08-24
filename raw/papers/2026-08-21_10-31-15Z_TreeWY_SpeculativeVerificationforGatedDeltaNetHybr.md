---
title: TreeWY: Speculative Verification for Gated DeltaNet Hybrids
published: 2026-08-21T10:31:15Z
authors: Sneha Murthy Ghantasala
url: http://arxiv.org/abs/2608.20961v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TreeWY: Speculative Verification for Gated DeltaNet Hybrids

## Abstract
Modern open models are hybrids: most layers are linear-attention (Gated DeltaNet, GDN) layers carrying a small fixed-size recurrent state instead of a growing key-value (KV) cache. This makes ordinary decoding memory-efficient, but hurts speculative decoding. To verify a batch of draft tokens and then roll back the rejected ones, today's systems snapshot the full recurrent state at every draft position for GDN layers, and those snapshots cannot be shared across branches of a draft tree, so a wide, high-acceptance tree becomes memory-infeasible. We remove the snapshots. Using a tree-structured WY transform of the gated delta rule, we compute every draft node's output with a single triangular solve and reconstruct only the one accepted state on commit, storing a small pseudo-value matrix instead of per-node states; the derivation depends only on the gated delta rule, not on any other architectural detail. In serving benchmarks on two scales of one hybrid model family (Qwen3.5 35B and 397B) this cuts speculative recurrent-state memory and KV-cache pressure at identical acceptance length, turning the freed HBM into higher throughput and much lower time-to-first-token (TTFT) wherever memory binds, and costing a few percent where it does not. For tree width the same memory buys affordability: a wider, higher-acceptance draft becomes possible, though not yet a throughput win.

## Metadata
- **Published**: 2026-08-21T10:31:15Z
- **Authors**: Sneha Murthy Ghantasala
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20961v1)