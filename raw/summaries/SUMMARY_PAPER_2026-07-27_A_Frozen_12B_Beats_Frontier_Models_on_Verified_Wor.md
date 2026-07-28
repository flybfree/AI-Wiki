---
title: A Frozen 12B Beats Frontier Models on Verified Work: 100% Accuracy, 0 Tokens, Bit-Exact, Forever
url: http://arxiv.org/abs/2607.23806v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_19-08-33Z_AFrozen12BBeatsFrontierModelsonVerifiedWork_100_Ac.md
generated_at: 2026-07-27 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a system that keeps a language model frozen while storing verified solutions in persistent memory, achieving zero‑generation‑token answers for solved problem families. Across 180 fresh instances from four architectures and vendors the method scores perfect accuracy with deterministic output. The approach decouples capability from parameter scaling and demonstrates a reusable, low‑cost answer store.

## Key Takeaways
- The frozen model can retrieve and return exact answers at zero generation tokens per query, using a persistent memory that stores verified solutions without consulting an answer key.
- Memory selection takes only 1.4 microseconds and full reuse completes in 6–23 ms on a single GPU, consuming about 36 mWh, showing near‑instantaneous retrieval with minimal energy cost.
- On a store of 4,500 items the system achieves 94.3% correct similarity retrieval, indicating that exact addressing eliminates errors and the memory acts as a working context comparable to large token windows.

## Context
Traditional language models rely on generating new tokens for each query, which is compute‑intensive and non‑deterministic. This work proposes an alternative where verification precedes storage, turning solved problems into reusable assets that avoid repeated inference.

## Implications
For industry this means APIs could deliver instant answers without incurring per‑query generation costs, reducing latency and energy use. Practitioners can build systems that reuse verified knowledge across many queries, creating a cost‑effective alternative to frontier models that must generate fresh responses each time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23806v1)
