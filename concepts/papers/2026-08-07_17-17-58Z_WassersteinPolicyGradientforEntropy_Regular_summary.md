# Summary: 2026-08-07_17-17-58Z_WassersteinPolicyGradientforEntropy_RegularizedLin.md
Saved: 2026-08-09 23:12
Source: 2026-08-07_17-17-58Z_WassersteinPolicyGradientforEntropy_RegularizedLin.md
Model: None

---

## Summary  
The paper proposes a Wasserstein policy gradient (WPG) method for solving entropy‑regularized discounted linear‑quadratic (LQ) control problems, demonstrating that the WPG update reduces to a finite‑dimensional ordinary differential equation whose solution is the optimal feedback gain and action covariance. By employing a Bellman verification argument, the authors show that the unrestricted LQ problem admits a linear‑Gaussian policy and that the statewise Wasserstein gradient is tangent to this class of policies. The resulting ODE is proven globally well‑posed and converges exponentially from any admissible initialization, with the convergence exponent approaching a positive limit as the entropy temperature shrinks, free from pathological exponential decay terms. This work thus provides a theoretically grounded, analytically tractable alternative to standard policy gradient approaches for LQ control.

## Key Contributions  
- [Finding 1] The Wasserstein policy gradient is shown to be tangent to the linear‑Gaussian optimal policy class of unrestricted discounted LQ control via Bellman verification.  
- [Finding 2] The WPG update reduces exactly to a finite‑dimensional ODE for the feedback gain and action covariance, enabling closed‑form analysis.  
- [Finding 3] The ODE is globally well‑posed with exponential convergence from any admissible initialization, and its exponent converges to a positive limit as entropy temperature → 0 without introducing extra \(\exp(-c/τ)\) terms.

## Methodology  
The authors start by formulating the discounted LQ cost functional with an entropy regularization term that penalizes action variance. They then define the state‑conditional Wasserstein gradient of the expected cost, which involves transporting the optimal action law in the action space. Using a Bellman equation, they verify that this gradient is orthogonal to any feasible policy change and thus tangent to the linear‑Gaussian solution manifold. The resulting gradient dynamics are expressed as an ODE: \(\dot{g}=f(g)\) where \(g\) contains the feedback gain and covariance. Analytical solvability and stability properties of this ODE are proved, establishing convergence guarantees.

## Results  
Theoretically, the authors demonstrate that for any fixed LQ problem the WPG exponent \(\alpha\) satisfies \(\lim_{\tau\to0}\alpha = \alpha_* > 0\). Numerical simulations on a set of benchmark linear‑quadratic systems confirm exponential policy updates with rates matching the analytical limit. The convergence is independent of initialization, and the method avoids the usual \(\exp(-c/τ)\) decay that can arise in entropy‑regularized settings.

## Significance  
By replacing stochastic gradient descent with a deterministic ODE derived from Wasserstein transport, this work offers a theoretically rigorous, faster‑converging algorithm for LQ control. It bridges classical optimal‑control theory and modern reinforcement learning, providing a scalable framework that can be extended to more complex state‑action spaces while preserving convergence guarantees.

## Related Concepts  
- Wasserstein policy gradient (WPG) – uses action‑space transport to compute gradients.  
- Entropy regularization – penalizes action variance to encourage exploration.  
- Linear‑quadratic control – a class of optimal control problems with quadratic cost and linear dynamics.  
- Bellman verification – a technique proving that a candidate policy satisfies the Bellman optimality condition.  
- Exponential convergence – rapid rate at which a sequence approaches its limit, often characterized by an exponent.
