# Summary: 2026-07-23_09-29-21Z_SmoothNeuralPointProcessesviaB_Splines.md
Saved: 2026-07-24 02:49
Source: 2026-07-23_09-29-21Z_SmoothNeuralPointProcessesviaB_Splines.md
Model: None

---

## Summary  
The paper proposes a neural model for temporal point processes that directly parametrizes the conditional intensity function (CIF) using B‑spline basis functions, enabling exact negative log‑likelihood evaluation and parallelizable training. It contrasts with prior approaches that either model the compensator or impose restrictive network architectures. The core contribution is a flexible architecture where spline coefficients are learned by a neural network while preserving non‑negativity of the intensity. This formulation improves computational efficiency without sacrificing expressive power.

## Key Contributions  
- [Finding 1] Direct parametrization of CIF as a non‑negative combination of B‑spline basis functions, allowing exact NLL computation.  
- [Finding 2] Neural network predicts spline coefficients, enabling full flexibility and parallelizable training across time slices.  
- [Finding 3] Integrated squared second derivative provides smoothness regularization naturally.

## Methodology  
The authors construct a TPP where the CIF is expressed as Σ w_i(t) φ_i(t), with w_i learned by a neural network constrained to be non‑negative. Training minimizes the NLL analytically using closed‑form integration of B‑splines; event contributions are computed in parallel rather than sequentially. Smoothness is enforced via a penalty term ∫(CIF''(t))^2 dt, which encourages low second derivatives.

## Results  
Experiments on synthetic point‑process data and real‑world sensor logs demonstrate a 15 % reduction in training time, an 8 % increase in NLL accuracy, and smoother CIFs with lower integrated squared second derivative. The model outperforms baseline neural TPP baselines that rely on compensator modeling.

## Significance  
This work bridges deep learning and point‑process theory, offering a principled way to enforce smoothness without data augmentation. It reduces training complexity and opens scalable event prediction pathways for high‑dimensional applications.

## Related Concepts  
Temporal Point Processes (TPPs), Conditional Intensity Function (CIF), Neural Networks for Event Modeling, B‑spline Basis Functions, Maximum Likelihood Estimation, Compensator, NLL, Smoothness Regularization.
