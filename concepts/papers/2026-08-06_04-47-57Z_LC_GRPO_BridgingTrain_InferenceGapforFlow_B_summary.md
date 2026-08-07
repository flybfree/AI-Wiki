# Summary: 2026-08-06_04-47-57Z_LC_GRPO_BridgingTrain_InferenceGapforFlow_BasedGRP.md
Saved: 2026-08-06 22:05
Source: 2026-08-06_04-47-57Z_LC_GRPO_BridgingTrain_InferenceGapforFlow_BasedGRP.md
Model: None

---

## Summary  
Flow‑based generative models rely on deterministic ordinary differential equation (ODE) sampling, while online reinforcement learning requires stochastic rollouts; this mismatch can degrade performance. LC‑GRPO bridges the gap by adding a Langevin correction to an ODE Euler step, recovering the score directly from flow velocity and yielding an isotropic Gaussian transition. The correction reduces the finite‑step error of imperfect ODE discretization and makes the training distribution more aligned with inference. This approach narrows the train‑inference gap without sacrificing sample efficiency or generation quality.

## Key Contributions  
- [Finding 1] A theoretical analysis shows that one Langevin correction step reduces the Wasserstein error of an imperfect ODE Euler step under suitable conditions.  
- [Finding 2] Empirical experiments on SD3.5‑Medium, FLUX.1‑Dev, and HunyuanVideo demonstrate that LC‑GRPO improves reward optimization across text‑to‑image and text‑to‑video tasks while preserving generation quality.  
- [Finding 3] The proposed transition is more accurate than the standard Euler–Maruyama discretization of the reverse SDE at matched randomness levels.

## Methodology  
The authors construct LC‑GRPO by first performing an inference‑aligned ODE Euler step, then applying a stochastic Langevin correction that targets the marginal distribution at the resulting timestep. The score is obtained directly from the flow velocity, eliminating the need for an additional score model, and the transition remains an isotropic Gaussian with a tractable likelihood suitable for policy optimization.

## Results  
Experiments consistently show higher rewards than baseline Euler–Maruyama methods, generation quality remains comparable to or better than standard approaches, and the gap between stochastic training rollouts and deterministic test‑time ODE inference is substantially narrowed. Theoretical bounds support these empirical gains.

## Significance  
LC‑GRPO resolves a fundamental mismatch in flow‑based reinforcement learning, enabling more reliable exploration and optimization without compromising sample efficiency or generation fidelity. This work advances the practical deployment of flow models in RL settings.

## Related Concepts  
Flow models, Langevin dynamics, Langevin correction, Euler–Maruyama discretization, Wasserstein distance, Gradient‑Proportional Policy Optimization (GRPO), stochastic differential equations, ODE sampling, isotropic Gaussian transitions.
