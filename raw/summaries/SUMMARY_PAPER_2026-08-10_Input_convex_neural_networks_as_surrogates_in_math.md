---
title: Input convex neural networks as surrogates in mathematical optimisation
url: http://arxiv.org/abs/2608.09707v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_15-11-22Z_Inputconvexneuralnetworksassurrogatesinmathematica.md
generated_at: 2026-08-10 22:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes input convex neural networks (ICNNs) as surrogates for mathematical optimisation problems, arguing they outperform conventional feedforward ReLU networks when the target function is approximately convex or concave. The authors demonstrate that ICNNs provide a tighter linear programming relaxation and enable an exact epigraph‑based reformulation under certain conditions, leading to faster branch‑and‑bound solutions.

## Key Takeaways
- ICNNs yield a tighter LP relaxation than FNNs with no integrality gap in favourable instances.  
- The convex architecture allows an LP‑based epigraph formulation that is exact when valid and otherwise bounded by the concave envelope.  
- A branch‑and‑bound algorithm that branches on input variables directly improves solve time and scalability.

## Context
Neural network approximations are widely used to replace expensive subproblems in optimisation, yet most methods rely on piecewise‑linear FNNs that require costly MIP formulations. This work highlights a structural advantage of convex neural architectures within the AI‑driven optimisation landscape.

## Implications
Practitioners can adopt ICNN surrogates as the default choice when convexity is plausible, gaining both accuracy and computational efficiency. The method supports scalable solutions across domains such as humanitarian logistics, oil well routing, and wine blending.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09707v1)
