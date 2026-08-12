---
title: Correlation flow governs learning at criticality
url: http://arxiv.org/abs/2608.08350v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-08_22-18-10Z_Correlationflowgovernslearningatcriticality.md
generated_at: 2026-08-11 22:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how the correlation structure of weights influences learning in deep neural networks and shows that learning is governed by a critical point where information propagation aligns with the Neural Tangent Kernel. It demonstrates that only at this specific variance balance does the end‑to‑end Jacobian vanish, making the NTK proportional to output correlation. The results also reveal how orthogonal initialization suppresses finite‑size errors compared with Gaussian initialization.

## Key Takeaways
- Correlation propagation to infinite depth is possible only at a single critical point in the weight‑bias variance plane.
- At this critical point the end‑to‑end Jacobian vanishes algebraically with depth, leading to an NTK that is exactly proportional to the output correlation.
- Orthogonal initialisation suppresses the leading finite‑size corrections present under Gaussian initialisation.

## Context
Deep neural networks often assume infinite width and depth, where learning can be described by the Neural Tangent Kernel. Understanding how initialization affects this kernel is crucial for designing training procedures that avoid pathological behavior. This work bridges random matrix theory with mean‑field analysis to uncover the underlying physics of learning at criticality.

## Implications
For practitioners, recognizing the critical variance regime allows intentional use of orthogonal initialisation to achieve more stable and accurate convergence. In industry, this insight can guide regularization strategies and reduce overfitting in large models without sacrificing performance. The theoretical link between information flow and learning dynamics may inspire new architectures that harness correlation propagation for efficient training.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08350v1)
