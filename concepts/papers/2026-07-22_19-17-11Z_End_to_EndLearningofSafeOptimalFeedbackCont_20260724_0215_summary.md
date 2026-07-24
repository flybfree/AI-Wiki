# Summary: 2026-07-22_19-17-11Z_End_to_EndLearningofSafeOptimalFeedbackControlinHi.md
Saved: 2026-07-24 02:15
Source: 2026-07-22_19-17-11Z_End_to_EndLearningofSafeOptimalFeedbackControlinHi.md
Model: None

---

## Summary  
The paper addresses the challenge of learning high‑dimensional semi‑global feedback controllers that satisfy hard safety constraints enforced by control barrier functions (CBFs) in an end‑to‑end manner, overcoming the computational and differentiation bottlenecks that have limited prior approaches to low‑dimensional systems. It introduces a scalable training framework that embeds a quadratic‑program based safety filter as an optimization layer while preserving hard guarantees, enabling training of policies with state dimensions up to 1200 and control dimensions up to 400.

## Key Contributions  
- [Finding 1] A theoretically justified end‑to‑end training framework that embeds a quadratic‑program safety filter using CBFs without sacrificing hard safety guarantees.  
- [Finding 2] Operator splitting combined with Jacobian‑Free Backpropagation (JFB) to achieve scalable gradient computation in high‑dimensional settings.  
- [Finding 3] Demonstrated effectiveness on multi‑agent nonlinear control problems with state and control dimensions up to 1200 and 400, respectively.

## Methodology  
The authors adopt operator splitting where the policy network is divided into a forward dynamics predictor and a safety filter that solves a quadratic program for each trajectory segment. Jacobian‑Free Backpropagation approximates the Jacobian of the quadratic‑program objective using finite differences, allowing gradient flow through the barrier layer without explicit Jacobian computation, thus preserving the nonsmooth optimization’s stability.

## Results  
Experiments on simulated high‑dimensional multi‑agent systems show that the proposed method converges to policies satisfying safety constraints with near‑optimal performance, outperforming baseline methods that limit dimensions. Theoretical analysis confirms that the nonsmooth optimization remains well‑conditioned and gradients are stable under JFB, providing a solid foundation for practical deployment.

## Significance  
This work bridges the gap between safe control and deep reinforcement learning in high‑dimensional real‑world scenarios, enabling practical deployment of semi‑global policies where safety is critical without sacrificing scalability. It demonstrates that end‑to‑end training can be made feasible for systems far beyond the 16‑state limit of earlier approaches.

## Related Concepts  
Control Barrier Functions (CBFs), Jacobian‑Free Backpropagation (JFB), operator splitting, quadratic programming, semi‑global stability, end‑to‑end training, high‑dimensional control.
