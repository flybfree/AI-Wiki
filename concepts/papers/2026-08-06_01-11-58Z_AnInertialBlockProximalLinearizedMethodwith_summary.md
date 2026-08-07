# Summary: 2026-08-06_01-11-58Z_AnInertialBlockProximalLinearizedMethodwithAdaptiv.md
Saved: 2026-08-06 21:54
Source: 2026-08-06_01-11-58Z_AnInertialBlockProximalLinearizedMethodwithAdaptiv.md
Model: None

---

## Summary  
The paper tackles a broad class of multiblock nonconvex and nonsmooth optimization problems that arise in applications such as pre‑earthquake anomaly analysis and machine learning. To address this challenging class, the authors introduce an inertial block proximal linearized method with two‑phase adaptive momentum (IBPL⁺‑TP). Their contribution is a novel algorithmic framework that combines inertia, block proximal linearization, and an adaptive two‑phase momentum strategy to achieve monotonic objective improvement, global convergence to a critical point, and provable convergence rates. The method also decouples the extrapolation parameters of two distinct points, allowing them to evolve independently of other algorithmic variables.

## Key Contributions  
- [Finding 1] A two‑phase adaptive momentum strategy is proposed that effectively updates the extrapolation parameters during optimization, improving step selection without external constraints.  
- [Finding 2] The method employs two different extrapolation points to accelerate convergence, leveraging inertial information to guide the search direction.  
- [Finding 3] Extrapolation parameters are independent and unconstrained by other algorithmic variables, providing greater flexibility for multiblock problems.

## Methodology  
The authors formulate a multiblock nonsmooth problem as a sum of block‑wise objectives, each equipped with proximal operators that handle ℓ₀ constraints. Using an inertial block proximal linearization, they replace the non‑smooth proximal step with a linearized approximation that incorporates momentum. The adaptive two‑phase momentum updates the extrapolation parameters at each phase, allowing one point to be used for early acceleration and another for later refinement. This decoupled approach yields a simple update rule that preserves monotonicity while enabling global convergence.

## Results  
Theoretically, the algorithm guarantees that the objective function is non‑increasing over iterations, converges globally to a critical point of the problem, and achieves a linear convergence rate of O(1/k). Empirically, on two benchmark machine‑learning tasks—sparse nonnegative matrix factorization with ℓ₀ constraints and sparse nonnegative CP decomposition with ℓ₀ constraints—the method outperforms several state‑of‑the‑art approaches in both convergence speed and final solution quality. The experiments confirm the theoretical guarantees and highlight the practical advantage of the decoupled extrapolation parameters.

## Significance  
By providing a unified, monotonic, and globally convergent algorithm for a wide class of nonsmooth multiblock problems, this work bridges theory and practice. The adaptive momentum framework reduces reliance on problem‑specific tuning while delivering faster convergence than existing inertial or proximal methods. This is especially valuable in high‑dimensional machine learning where ℓ₀ constraints are common.

## Related Concepts  
- Proximal operator (block‑wise)  
- Inertial optimization  
- Adaptive momentum  
- Extrapolation points  
- Nonconvex nonsmooth optimization  
- ℓ₀ constraint handling  
- Multiblock decomposition
