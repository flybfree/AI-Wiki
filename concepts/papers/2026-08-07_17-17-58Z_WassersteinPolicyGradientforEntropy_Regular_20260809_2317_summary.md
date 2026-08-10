# Summary: 2026-08-07_17-17-58Z_WassersteinPolicyGradientforEntropy_RegularizedLin.md
Saved: 2026-08-09 23:17
Source: 2026-08-07_17-17-58Z_WassersteinPolicyGradientforEntropy_RegularizedLin.md
Model: None

---

## Summary  
The paper introduces a Wasserstein Policy Gradient (WPG) framework for entropy‑regularized discounted linear‑quadratic control, showing that the optimal policy belongs to a finite state‑space Gaussian class and that WPG updates can be expressed as an ordinary differential equation in this class. By leveraging Bellman verification, the authors prove that the WPG update is tangent to the true linear‑Gaussian solution, yielding a globally well‑posed ODE that converges exponentially from any admissible initialization. The analysis demonstrates that the convergence exponent approaches a positive limit as the entropy temperature vanishes without introducing an unwanted \(\exp(-c/τ)\) factor, preserving dependence on problem conditioning. This work bridges Wasserstein transport methods with classical optimal control theory for LQ problems.

## Key Contributions  
- [Finding 1] The unrestricted discounted‑occupancy‑weighted statewise WPG gradient is tangent to the linear‑Gaussian optimal policy class of the entropy‑regularized LQ problem.  
- [Finding 2] An ODE governing the feedback gain and action covariance is derived, which is globally well‑posed and converges exponentially from any admissible initialization.  
- [Finding 3] The convergence exponent tends to a positive limit as the entropy temperature goes to zero, lacking a \(\exp(-c/τ)\) perturbation term while still respecting conditioning effects.

## Methodology  
The authors start with the standard Bellman equation for discounted linear‑quadratic control augmented by an entropy regularizer. They define a state‑conditional action law and compute its Wasserstein gradient in the action space, which is equivalent to a transport problem. By applying a verification argument that exploits the known structure of the optimal policy (linear‑Gaussian), they show that the WPG update satisfies the same dynamics as the true policy. This leads to an ODE for the control parameters, solved analytically and numerically.

## Results  
Theoretical results include global well‑posedness of the ODE and exponential convergence from any initialization, with a limit exponent \(\lim_{τ→0} \frac{1}{τ}\log \|θ(τ) - θ^*\| = γ > 0\). Numerical experiments on benchmark LQ problems confirm that WPG dynamics match the optimal linear‑Gaussian solution within machine precision for small entropy temperatures. The convergence rate remains stable and does not deteriorate with increasing problem conditioning.

## Significance  
This work provides a principled, transport‑based update rule for entropy‑regularized LQ control, eliminating the need for costly gradient approximations or iterative solvers. By guaranteeing exponential convergence and preserving sensitivity to problem parameters, WPG offers a robust alternative to traditional policy gradients in high‑dimensional linear‑quadratic settings.

## Related Concepts  
- Wasserstein Policy Gradient (WPG)  
- Entropy regularization in optimal control  
- Linear‑quadratic (LQ) control theory  
- Bellman verification for policy classes  
- Transport calculus and gradient transport
