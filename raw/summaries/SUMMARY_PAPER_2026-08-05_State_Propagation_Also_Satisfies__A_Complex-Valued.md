---
title: State Propagation Also Satisfies: A Complex-Valued State-Space Model for Deterministic State Tracking
url: http://arxiv.org/abs/2608.03425v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_10-16-24Z_StatePropagationAlsoSatisfies_AComplex_ValuedState.md
generated_at: 2026-08-05 01:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a minimal recurrent architecture called Complex State Propagator that tracks deterministic state across layers using complex-valued vectors and input-dependent rotations. It demonstrates that state propagation alone can achieve perfect accuracy on tasks like parity checking and modular counting without attention mechanisms. The model uses block-level skip connections, complex normalization, and SiLU activation at sequence boundaries to prevent degradation.

## Key Takeaways
- State propagation alone is sufficient for deterministic tracking tasks, eliminating the need for attention or output projections.
- Complex-valued hidden states are updated via input-dependent rotations in the complex domain, preserving information flow across layers.
- The combination of block-level skip connections, element-wise complex normalization, and SiLU activation at boundaries ensures stable deep learning without gradient vanishing.

## Context
Deterministic state tracking tasks such as parity checking and modular counting require exact logical computation rather than probabilistic modeling. Traditional transformer-based models overfit these problems by introducing unnecessary complexity. This work shows that a lightweight recurrent model can match high performance, highlighting the efficiency of focused architectures for specific computational domains.

## Implications
The findings suggest that researchers should consider minimal architectures when attention is not essential, reducing computational cost and latency in real-time applications. Practitioners may adopt CSP as a template for designing efficient stateful systems in robotics or embedded AI where precision matters more than flexibility.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03425v1)
