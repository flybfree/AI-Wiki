---
title: Decentralized Online Riemannian Optimization for Strongly Geodesically Convex Functions
url: http://arxiv.org/abs/2607.20316v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_16-03-43Z_DecentralizedOnlineRiemannianOptimizationforStrong.md
generated_at: 2026-07-23 23:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses decentralized online optimization of strongly geodesically convex losses on Riemannian manifolds with bounded sectional curvature. It establishes O(log T) static regret bounds that match the minimax-optimal rate for Euclidean strong convexity, extending centralized results to networked settings. The analysis includes a general network error bound for time-varying step sizes and new strong subconvexity arguments.

## Key Takeaways
- Strong g-convexity improves centralized regret from O(sqrt(T)) to O(log T) but decentralized methods have not yet achieved this rate.
- A general network-error analysis is introduced that accommodates decaying step sizes, resolving incompatibility with fixed-step assumptions.
- The same O(log T) static regret bound holds for the two-point bandit feedback setting using strong subconvexity of smoothed losses.

## Context
Online optimization on curved spaces remains a bottleneck in federated learning where participants cannot share gradients directly. Achieving optimal rates under network constraints is essential for privacy-preserving and scalable AI systems. This work bridges theory gaps between Riemannian convex analysis and decentralized algorithm design.

## Implications
Practitioners can deploy stronger regret guarantees without sacrificing step size adaptivity, enabling better performance in large-scale distributed learning. The results provide theoretical justification for using strongly geodesically convex losses such as those arising from manifold-based embeddings, encouraging more efficient model training across heterogeneous devices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20316v1)
