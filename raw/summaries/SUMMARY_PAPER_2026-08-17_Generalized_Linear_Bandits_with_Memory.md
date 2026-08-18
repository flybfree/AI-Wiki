---
title: Generalized Linear Bandits with Memory
url: http://arxiv.org/abs/2608.15848v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_16-39-09Z_GeneralizedLinearBanditswithMemory.md
generated_at: 2026-08-17 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses generalized linear bandits with memory, a setting where rewards depend on recent actions via a finite‑length history matrix. It improves upon the existing \(\tilde{O}(T^{3/4})\) regret bound by providing a refined analysis that yields a \(\tilde{O}(\sqrt{T})\) rate for linear models and extends it to nonlinear generalizations. The proposed block‑wise algorithm using shrunken confidence bounds achieves a unified regret expression independent of link‑function curvature.

## Key Takeaways
- The previous \(\tilde{O}(T^{3/4})\) bound is loose; the authors recover a \(\tilde{O}(\sqrt{T})\) regret rate through tighter analysis.
- Their algorithm works for both linear and generalized linear models, handling memory effects and nonlinear rewards simultaneously.
- The resulting regret term \(\tilde{O}\left(\sqrt{mT} + d\sqrt{T} + \sqrtκ\, d^{2} m^{1/4} T^{1/4} + κd^{2} \right)\) shows that the leading order is \(\sqrt{T}\) regardless of curvature.

## Context
Bandits with memory introduce non‑stationary dynamics where each episode’s reward depends on a window of past actions, complicating standard analysis. Generalized linear models allow flexible link functions but often suffer from higher regret due to nonlinearity and memory constraints. This work bridges those gaps by delivering an algorithmic framework that respects both aspects.

## Implications
For practitioners, this means more reliable performance in online decision‑making tasks where historical context matters, such as personalized recommendation or adaptive control. The \(\sqrt{T}\) bound offers a practical advantage over cubic‑root rates, enabling faster convergence and lower computational overhead in real‑world deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15848v1)
