# Summary: 2026-07-22_19-17-11Z_End_to_EndLearningofSafeOptimalFeedbackControlinHi.md
Saved: 2026-07-24 02:12
Source: 2026-07-22_19-17-11Z_End_to_EndLearningofSafeOptimalFeedbackControlinHi.md
Model: None

---

## Summary  
The paper proposes an end‑to‑end learning framework for high‑dimensional semi‑global feedback control that enforces hard safety constraints via Control Barrier Functions (CBFs). It overcomes the computational and differentiation bottlenecks of quadratic‑program based safety filters by embedding them within a Jacobian‑Free Backpropagation (JFB) layer using operator splitting, thereby enabling scalable training up to 1200 state dimensions. The contribution is both theoretical—justifying the method with nonsmooth analysis—and empirical—demonstrating effectiveness on multi‑agent problems.

## Key Contributions  
- Introduces a scalable end‑to‑end training method for high‑dimensional CBF‑based safety filters using Jacobian‑Free Backpropagation.  
- Provides theoretical justification through nonsmooth analysis, guaranteeing that hard safety guarantees are preserved during training.  
- Demonstrates empirical success on high‑dimensional (up to 1200 state, 400 control) multi‑agent nonlinear control tasks.

## Methodology  
The authors combine operator splitting with JFB to embed the quadratic‑program based CBF safety filter as an optimization layer inside a policy network. Training alternates between updating the neural policy and solving the QP that detects CBF violations; JFB computes gradients of the QP objective w.r.t. the neural parameters without forming explicit Jacobians, allowing gradient flow through the barrier constraints.

## Results  
Experiments show that the proposed method achieves near‑optimal feedback control performance while maintaining safety over state dimensions up to 1200 and control dimensions up to 400 in simulated multi‑agent environments. Theoretical analysis confirms that the nonsmooth analysis preserves the semi‑global property of CBFs, guaranteeing safety under all training dynamics.

## Significance  
This work bridges high‑dimensional control with rigorous safety constraints, enabling practical deployment of safe optimal controllers where prior methods are infeasible due to computational limits.

## Related Concepts  
Control Barrier Functions (CBFs), Jacobian‑Free Backpropagation (JFB), operator splitting, quadratic programming, nonsmooth analysis, semi‑global stability, high‑dimensional control, end‑to‑end learning.
