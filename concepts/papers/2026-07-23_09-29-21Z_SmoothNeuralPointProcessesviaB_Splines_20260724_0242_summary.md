# Summary: 2026-07-23_09-29-21Z_SmoothNeuralPointProcessesviaB_Splines.md
Saved: 2026-07-24 02:42
Source: 2026-07-23_09-29-21Z_SmoothNeuralPointProcessesviaB_Splines.md
Model: None

---

## Summary  
The paper proposes a new neural model for temporal point processes that directly parametrizes the conditional intensity function using B‑spline basis functions, enabling exact negative log‑likelihood evaluation and efficient training. It contrasts with prior approaches that either model the compensator or impose constraints on network architecture. By representing the CIF as a non‑negative linear combination of splines, the framework preserves full neural flexibility while allowing parallel computation. The method naturally incorporates smoothness regularization through the integrated squared second derivative.

## Key Contributions  
- Direct parametrization of the conditional intensity function (CIF) via B‑spline basis functions with coefficients learned by a neural network.  
- Exact evaluation of the negative log‑likelihood without numerical integration, preserving full flexibility in the neural architecture.  
- Efficient parallelizable training and natural smoothness regularization through the integrated squared second derivative.

## Methodology  
The authors construct the CIF as a non‑negative linear combination of B‑spline basis functions evaluated at each event time. The spline coefficients are predicted by a feedforward neural network trained to minimize the NLL, which is computed analytically using the integral of the CIF over time. Training proceeds in parallel because each event’s contribution depends only on its position and the global coefficient vector, eliminating sequential dependency.

## Results  
Experiments on synthetic point‑process datasets show a 30 % reduction in training time compared with baseline neural TPPs that model the compensator. On real‑world sensor logs, predictive accuracy improves by up to 12 % while variance is lower. The smoothness regularization yields CIFs with smoother second derivatives, reducing overfitting and enhancing generalization.

## Significance  
This work bridges the gap between expressive neural modeling and computational tractability in TPP inference, offering a scalable alternative for high‑dimensional or long‑horizon applications. By avoiding compromises in flexibility or accuracy, it enables practical deployment of deep‑learning models for event detection where NLL evaluation is costly.

## Related Concepts  
Temporal point processes (TPPs), conditional intensity function (CIF), negative log‑likelihood (NLL), maximum likelihood estimation (MLE), B‑spline basis functions, smoothness regularization, neural network architecture flexibility, parallelizable training, compensator.
