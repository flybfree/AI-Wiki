---
title: Correlation flow governs learning at criticality
url: http://arxiv.org/abs/2608.08350v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-08_22-18-10Z_Correlationflowgovernslearningatcriticality.md
generated_at: 2026-08-11 13:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper establishes a theoretical link between correlation propagation and the Neural Tangent Kernel, showing that learning dynamics in infinitely wide deep networks are governed by a single critical point where the end‑to‑end Jacobian vanishes. At this point the NTK is exactly proportional to the output correlation at infinite depth, revealing an unexpected equivalence between information flow and learning. The authors also demonstrate how orthogonal initialisation suppresses finite‑size corrections that dominate under Gaussian initialisation.

## Key Takeaways
- Correlation propagation to infinite depth occurs only at a specific critical point in the weight‑bias variance plane where the end‑to‑end Jacobian algebraically vanishes with depth.  
- At this critical point the NTK becomes exactly proportional to the output correlation, indicating that learning is directly tied to how information spreads across layers.  
- Orthogonal initialisation eliminates leading finite‑size corrections present under Gaussian initialisation, clarifying their distinct roles in controlling asymptotic dynamics.

## Context
Deep neural networks are often approximated as infinitely wide and infinitely deep, a regime where the Neural Tangent Kernel (NTK) governs learning. Understanding how information propagates through such networks is crucial for interpreting training behavior and designing effective architectures. This work bridges random matrix theory with mean‑field analysis to uncover hidden relationships in this limit.

## Implications
The findings suggest that orthogonal initialisation can be strategically used to achieve smoother convergence by minimizing finite‑size effects at the critical point. Practitioners may leverage these insights to design initialization schemes that enhance stability and performance, especially for very deep or wide models where asymptotic behavior dominates training dynamics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08350v1)
