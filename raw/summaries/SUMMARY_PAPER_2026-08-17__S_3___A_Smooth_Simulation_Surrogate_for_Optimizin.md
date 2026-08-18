---
title: $S^3$: A Smooth Simulation Surrogate for Optimizing Discrete Abstractions of Dynamical Systems
url: http://arxiv.org/abs/2608.15920v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_20-31-04Z_S_3__ASmoothSimulationSurrogateforOptimizingDiscre.md
generated_at: 2026-08-17 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces S^3, a smooth simulation surrogate that approximates the reverse simulation metric used to measure conservatism in abstraction-based modeling of black‑box controllers. By coupling S^3 with Taylor model based reachability, it enables gradient optimization of abstraction parameters while guaranteeing soundness. Experiments on three case studies demonstrate strong correlation with the original metric, faster computation, and effective reduction of conservatism.

## Key Takeaways
- The surrogate S^3 provides a differentiable objective that closely mirrors the reverse simulation metric, allowing precise measurement of conservatism in abstract models.
- Integration with Taylor model based reachability ensures that any optimization performed via gradient descent preserves soundness by construction.
- Empirical results show that S^3 reduces abstraction conservatism significantly while maintaining computational speed compared to traditional methods.

## Context
In safety‑critical AI where black‑box neural networks control physical systems, abstraction models are essential for analysis but often suffer from excessive nondeterministic behavior. Existing tools rely on reverse simulation which is computationally heavy and not amenable to gradient optimization. The need for a lightweight, differentiable surrogate that balances soundness and efficiency remains unmet.

## Implications
Practitioners can now use S^3 to iteratively refine abstract models without sacrificing safety guarantees, accelerating development cycles in autonomous robotics and aerospace systems. This approach bridges the gap between rigorous theoretical analysis and practical optimization, fostering trustworthy AI deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15920v1)
