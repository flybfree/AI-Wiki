---
title: Dion3: Full-Stack Orthogonal Updates
url: http://arxiv.org/abs/2608.11612v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_03-42-40Z_Dion3_Full_StackOrthogonalUpdates.md
generated_at: 2026-08-13 08:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Dion3, a revised version of the Muon optimizer that targets the cubic-time Newton-Schulz orthogonalization step and its communication overhead when weights are sharded. By reducing FLOPs, accelerating kernels via symmetry exploitation, and applying megabatching, Dion3 cuts optimizer step time up to sixfold while matching or improving loss performance. The authors also propose selecting only a fraction of momentum matrix rows for orthogonalization, further boosting speed.

## Key Takeaways
- The Gram Newton-Schulz algorithm reduces the FLOP cost of orthogonalization compared to Muon’s cubic-time approach.
- CuteDSL kernels exploit symmetry to accelerate the orthogonalization step.
- Megabatching strategy minimizes communication overhead when weights are sharded across devices.
- Selecting a fraction of momentum matrix rows for orthogonalization yields additional speed gains and better performance than previous compressed versions.

## Context
In distributed deep learning, optimizer choice directly impacts training efficiency due to communication bottlenecks. Traditional full‑matrix orthogonalizations become prohibitive as model size grows, limiting scalability on large models or multi‑GPU setups. This paper addresses that limitation by rethinking the orthogonalization step at multiple layers of the stack.

## Implications
Dion3 enables faster optimizer steps without sacrificing convergence quality, making it suitable for large‑scale training where every millisecond counts. Practitioners can replace Muon with Dion3 via a drop‑in package, reducing hardware costs and accelerating model iteration cycles across cloud and on‑premise environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11612v1)
