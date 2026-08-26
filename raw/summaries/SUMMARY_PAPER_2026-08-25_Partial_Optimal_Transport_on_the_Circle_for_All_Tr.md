---
title: Partial Optimal Transport on the Circle for All Transported Masses in O(N log N)
url: http://arxiv.org/abs/2608.23910v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_23-32-24Z_PartialOptimalTransportontheCircleforAllTransporte.md
generated_at: 2026-08-25 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PAWC, a new algorithm that computes the full profile of partial optimal transport on a circle in O(N log N) time and O(N) memory. It eliminates the quadratic factor present in existing methods by preserving line structure through a free‑gap invariant, allowing all cardinality costs to be obtained simultaneously with a single optimal gap.

## Key Takeaways
- PAWC returns all K+1 cost values for partial optimal transport on the circle without re‑running the line algorithm per support gap.  
- The algorithm maintains a global circulation that corresponds to an optimized cut, providing a free‑gap invariant that guarantees each local update remains valid.  
- Empirically, PAWC achieves 0.56 ms processing at N=4096 versus 1.5 s for a single transported fraction from general solvers.

## Context
Partial optimal transport is widely used in AI to handle outliers and occlusion by leaving part of the mass unmatched. On periodic data such as angles or directions, the problem naturally maps to a circle where global circulation offers a more efficient solution than treating it linearly. This work bridges the gap between linear PAWL performance and circular geometry.

## Implications
For practitioners dealing with angular measurements, this algorithm reduces computational cost dramatically, enabling real‑time applications in computer vision and signal processing. The ability to retrieve the full profile instantly improves robustness against noisy or occluded data, offering a scalable alternative to costly exact optimal transport solvers.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23910v1)
