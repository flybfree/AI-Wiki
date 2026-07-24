---
title: Barzilai-Borwein Fails Superlinear Convergence on an Open Set of Quadratics for Every Dimension $n\geq 4$
url: http://arxiv.org/abs/2607.21579v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_17-56-05Z_Barzilai_BorweinFailsSuperlinearConvergenceonanOpe.md
generated_at: 2026-07-23 22:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper disproves the conjecture that the Barzilai‑Borwein (BB) method achieves root‑superlinear convergence for almost every strictly convex quadratic problem in dimensions four and higher. It constructs a nonempty open set of such problems where BB1 converges but cannot converge superlinearly, showing that the objective gap is bounded by squared geometric rates while the gradient and error norms are only geometrically bounded.

## Key Takeaways
- For every finite dimension n≥4 there exists a positive‑measure family of strictly convex quadratic problems and initial points for which the long Barzilai‑Borwein method converges but fails to converge root‑superlinearly.  
- The gradient norm, error energy norm, and objective gap are all bounded below by geometric sequences with the same rates, indicating that superlinear convergence is impossible.  
- This result relies on a computer‑assisted proof of a nonresonant attracting seven‑cycle in dimension four.

## Context
Understanding the exact convergence properties of popular optimization algorithms is crucial for AI practitioners who rely on these methods to solve large‑scale quadratic models such as logistic regression and support vector machines. The failure of superlinear guarantees undermines claims of near‑optimal performance that are often assumed without rigorous justification, highlighting a gap between theoretical optimism and practical behavior.

## Implications
For researchers developing robust optimization algorithms, this work underscores the need for careful analysis beyond simple convergence rates to assess algorithmic stability in high dimensions. Practitioners should treat BB as a reliable linear‑rate method rather than one that may promise faster convergence without additional safeguards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21579v1)
